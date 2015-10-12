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
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import shutil
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : June 4, 2014
# CREATED : June 4, 2014
# AUTHOR : DRYX
def create_project_folder(
        log,
        pathToHostDirectory,
        projectName,
        wiki):
    """create project folder

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToHostDirectory`` -- path to directory used to host the wiki
        - ``projectName`` -- name of the project
        - ``wiki`` -- wiki [False, same or seperate]

    **Return:**
        - None

    **Todo**
    """
    log.info('starting the ``create_project_folder`` function')

    # copy template folder to project path
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
                    shutil.copyfile(os.path.join(basePath, d),
                                    "%(dst)s/%(d)s" % locals())

    # create the sublime project file for the project
    pathToWriteFile = "%(dst)s/%(projectName)s.sublime-project" % locals()
    theseFolders = """ { "path": "%(dst)s" } """ % locals()
    if wiki:
        wikiName = ""
        if wiki == "seperate":
            wikiName = projectName + "_wiki"
        else:
            wikiName = projectName
        wikiName = wikiName + ".wiki"
        wikiDst = "%(pathToHostDirectory)s/%(wikiName)s" % locals()
        wikiDst = wikiDst.replace("//", "/")
        theseFolders = """ %(theseFolders)s,
        { "path": "%(wikiDst)s" } """ % locals()

    exists = os.path.exists(pathToWriteFile)
    if not exists:
        sublime_project_text = """{
  "folders": [%(theseFolders)s],
  "settings": {
      "python_test":{
          "command": "/Users/Dave/.virtualenvs/%(projectName)s/bin/nosetests",
          "working_dir": "/Users/Dave/git_repos/%(projectName)s/%(projectName)s",
          "color_scheme": "dark"
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


if __name__ == '__main__':
    main()
