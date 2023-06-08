import os
import nose
import shutil
from .. import add_hook_to_github_repo
from repster.utKit import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_add_hook_to_github_repo(unittest.TestCase):

    def test_add_hook_to_github_repo_function(self):
        # xt-kwargs
        kwargs = {}
        kwargs["log"] = log
        kwargs[
            "repoName"] = "dryxPython" % globals()
        kwargs["pathToCredentials"] = False
        kwargs["hookDomain"] = "thespacedoctor.co.uk"
        # xt-kwarg_key_and_value
        add_hook_to_github_repo.add_hook_to_github_repo(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
