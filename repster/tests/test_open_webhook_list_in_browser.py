import os
import nose
import shutil
from repster import open_webhook_list_in_browser
from repster.utKit import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_open_webhook_list_in_browser(unittest.TestCase):

    def test_open_webhook_list_in_browser_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["location"] = "bb"
        kwargs["projectName"] = "pessto_marshall_engine"
        # xt-kwarg_key_and_value

        open_webhook_list_in_browser(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
