import os
import nose
import shutil
from .. import create_project_folder
from .. import create_local_git_repo
from .. import add_git_repo_to_github
from gitflow.utKit import utKit

## SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_add_git_repo_to_github():

    def test_add_git_repo_to_github_function(self):
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
        kwargs["branches"] = True
        create_local_git_repo.create_local_git_repo(**kwargs)

        kwargs = {}
        kwargs["log"] = log
        kwargs[
            "pathToProject"] = "%(pathToOutputDir)s/testProjectName" % globals()
        kwargs["pathToCredentials"] = False
        # xt-kwarg_key_and_value
        add_git_repo_to_github.add_git_repo_to_github(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
