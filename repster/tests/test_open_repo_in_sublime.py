import os
import nose
import shutil
from .. import create_project_folder
from .. import create_local_git_repo
from .. import open_repo_in_sublime
from repster.utKit import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_open_repo_in_sublime(unittest.TestCase):

    def test_open_repo_in_sublime_function(self):
        try:
            shutil.rmtree("%(pathToOutputDir)s/testProjectName" % globals())
        except:
            pass

        kwargs = {}
        kwargs["log"] = log
        kwargs["pathToHostDirectory"] = pathToOutputDir
        kwargs["projectName"] = "testProjectName"
        create_project_folder.create_project_folder(**kwargs)

        kwargs = {}
        kwargs["log"] = log
        kwargs[
            "pathToProjectRoot"] = "%(pathToOutputDir)s/testProjectName" % globals()
        create_local_git_repo.create_local_git_repo(**kwargs)

        kwargs = {}
        kwargs["log"] = log
        kwargs[
            "pathToProjectRoot"] = "%(pathToOutputDir)s/testProjectName" % globals()
        open_repo_in_sublime.open_repo_in_sublime(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
