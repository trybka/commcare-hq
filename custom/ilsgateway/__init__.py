from custom.ilsgateway.tanzania.reports.alerts import AlertReport
from custom.ilsgateway.tanzania.reports.dashboard_report import DashboardReport

CUSTOM_REPORTS = (
    ('Custom reports', (
        DashboardReport,
        AlertReport,
    )),
)

# For QA purposes it should be set to true.
TEST = True
