from __future__ import absolute_import
from __future__ import unicode_literals

from memoized import memoized

from corehq.apps.userreports.models import DataSourceActionLog
from dimagi.utils.logging import notify_exception
from corehq.util.test_utils import unit_testing_only


class IndicatorAdapter(object):

    def __init__(self, config):
        self.config = config

    @memoized
    def get_table(self):
        raise NotImplementedError

    def rebuild_table(self, initiated_by=None, source=None):
        raise NotImplementedError

    def drop_table(self):
        raise NotImplementedError

    @unit_testing_only
    def clear_table(self):
        raise NotImplementedError

    def get_query_object(self):
        raise NotImplementedError

    def best_effort_save(self, doc, eval_context=None):
        """
        Does a best-effort save of the document. Will fail silently if the save is not successful.

        For certain known, expected errors this will do no additional logging.
        For unexpected errors it will log them.
        """
        try:
            indicator_rows = self.get_all_values(doc, eval_context)
        except Exception as e:
            self.handle_exception(doc, e)
        else:
            self._best_effort_save_rows(indicator_rows, doc)

    def _best_effort_save_rows(self, rows, doc):
        """
        Like save rows, but should catch errors and log them
        """
        raise NotImplementedError

    def handle_exception(self, doc, exception):
        from corehq.util.cache_utils import is_rate_limited
        ex_clss = exception.__class__
        key = '{domain}.{table}.{ex_mod}.{ex_name}'.format(
            domain=self.config.domain,
            table=self.config.table_id,
            ex_mod=ex_clss.__module__,
            ex_name=ex_clss.__name__
        )
        if not is_rate_limited(key):
            notify_exception(
                None,
                'unexpected error saving UCR doc',
                details={
                    'domain': self.config.domain,
                    'doc_id': doc.get('_id', '<unknown>'),
                    'table': '{} ({})'.format(self.config.display_name, self.config._id)
                }
            )

    def save(self, doc, eval_context=None):
        """
        Saves the document. Should bubble up known errors.
        """
        indicator_rows = self.get_all_values(doc, eval_context)
        self.save_rows(indicator_rows)

    def bulk_save(self, docs):
        """
        Evalutes UCR rows for given docs and saves the result in bulk.
        """
        raise NotImplementedError

    def get_all_values(self, doc, eval_context=None):
        "Gets all the values from a document to save"
        return self.config.get_all_values(doc, eval_context)

    def bulk_delete(self, doc_ids):
        for _id in doc_ids:
            self.delete({'_id': _id})

    def delete(self, doc):
        raise NotImplementedError

    @property
    def run_asynchronous(self):
        return self.config.asynchronous

    def log_action(self, initiated_by, source, skip=False):
        if skip:
            return

        kwargs = {
            'domain': self.config.domain,
            'indicator_config_id': self.config.get_id,
            'action': DataSourceActionLog.REBUILD,
            'initiated_by': initiated_by,
            'source': source,
        }
        try:
            DataSourceActionLog.objects.create(**kwargs)
        except Exception:
            notify_exception(None, "Error saving UCR action log", details=kwargs)
