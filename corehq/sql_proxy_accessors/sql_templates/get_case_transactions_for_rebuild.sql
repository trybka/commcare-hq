DROP FUNCTION IF EXISTS get_case_transactions_for_rebuild(TEXT);

CREATE FUNCTION get_case_transactions_for_rebuild(case_id TEXT) RETURNS SETOF form_processor_casetransaction AS $$
    CLUSTER '{{ PL_PROXY_CLUSTER_NAME }}';
    RUN ON hash_string(case_id, 'siphash24');
$$ LANGUAGE plproxy;
