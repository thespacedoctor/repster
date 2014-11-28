#!/usr/bin/env python
# encoding: utf-8
"""
open_repo_in_sublime.py
=======================
:Summary:
    Open the project in sublime

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
def open_repo_in_sublime(
        log,
        pathToProjectRoot):
    """open repo in sublime

    **Key Arguments:**
        - ``log`` -- logger,
        - ``pathToProjectRoot`` -- the path to the root of the project

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean open_repo_in_sublime function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``open_repo_in_sublime`` function')

    basePath = pathToProjectRoot
    for d in os.listdir(basePath):
        if os.path.isfile(os.path.join(basePath, d)):
            if "sublime-project" in d:
                projectPath = os.path.join(basePath, d)
                from subprocess import Popen, PIPE, STDOUT
                cmd = """open %(projectPath)s""" % locals()
                p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
                output = p.communicate()[0]
                log.debug('output: %(output)s' % locals())

    log.info('completed the ``open_repo_in_sublime`` function')
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
