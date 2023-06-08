import os
import nose
import shutil
from repster import clone_github_repo_wiki
from repster.utKit import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_clone_github_repo_wiki(unittest.TestCase):

    def test_clone_github_repo_wiki_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["projectName"] = "sandwich"
        kwargs["pathToHostDirectory"] = "/Users/Dave/Desktop"
        kwargs["strapline"] = "nice seperate wiki mate"
        kwargs["wiki"] = "seperate"
        kwargs["pathToCredentials"] = "/Users/Dave/github_credentials.yaml"
        # xt-kwarg_key_and_value
        wiki = clone_github_repo_wiki(**kwargs)
        wiki.get()

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
