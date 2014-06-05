#!/usr/bin/env python
# encoding: utf-8
"""
create_project_folder.py
========================
:Summary:
    Create the project folder from template

:Author:
    David Young

:Date Created:
    June 4, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import shutil
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
# from ..__init__ import *

###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx
# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
## LAST MODIFIED : June 4, 2014
## CREATED : June 4, 2014
## AUTHOR : DRYX
def create_project_folder(
        log,
        pathToHostDirectory,
        projectName):
    """create project folder

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean create_project_folder function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``create_project_folder`` function')

    moduleDirectory = os.path.dirname(__file__)
    src = "%(moduleDirectory)s/resources/template_project" % locals()
    dst = "%(pathToHostDirectory)s/%(projectName)s" % locals()

    dst = dst.replace("//", "/")

    exists = os.path.exists(dst)
    if not exists:
        shutil.copytree(src, dst)
    else:
        basePath = src
        for d in os.listdir(basePath):
            if os.path.isfile(os.path.join(basePath, d)):
                exists = os.path.exists("%(dst)s/%(d)s" % locals())
                if not exists:
                    shutil.copyfile(os.path.join(basePath, d), "%(dst)s/%(d)s" % locals())
        

    pathToWriteFile = "%(dst)s/%(projectName)s.sublime-project" % locals()
    exists = os.path.exists(pathToWriteFile)
    if not exists:
        sublime_project_text = """{
  "folders": [{
      "path": "%(dst)s"
  }],
  "settings": {
      "python_test_runner": {
          "test_root": "%(dst)s",
          "test_delimeter": ":",
          "test_command": "/Library/Frameworks/Python.framework/Versions/2.7/bin/nosetests "
      }
  }
}
""" % locals()
        try:
            log.debug("attempting to open the file %s" % (pathToWriteFile,))
            writeFile = open(pathToWriteFile, 'w')
        except IOError, e:
            message = 'could not open the file %s' % (pathToWriteFile,)
            log.critical(message)
            raise IOError(message)
        writeFile.write(sublime_project_text)
        writeFile.close()

    log.info('completed the ``create_project_folder`` function')
    return None

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

############################################
# CODE TO BE DEPECIATED                    #
############################################

if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
