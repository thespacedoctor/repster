import os
import nose
import shutil
from .. import create_project_folder
from repster.utKit import utKit

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# xnose-class-to-test-main-command-line-function-of-module


class test_create_project_folder(unittest.TestCase):
    try:
        shutil.rmtree("%(pathToOutputDir)s/testProjectName" % globals())
    except:
        pass

    def test_create_project_folder_function(self):
        kwargs = {}
        kwargs["log"] = log
        kwargs["pathToHostDirectory"] = pathToOutputDir
        kwargs["projectName"] = "testProjectName"
        create_project_folder.create_project_folder(**kwargs)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
