#!/usr/bin/env python
# encoding: utf-8
"""
create_local_git_repo.py
========================
:Summary:
    Create a local git repo

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
def create_local_git_repo(
        log,
        pathToProjectRoot,
        branches=False):
    """create a first instance of a git repo with all the neccessary files

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToProjectRoot`` -- path to the root of the project

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean create_local_git_repo function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.info('starting the ``create_local_git_repo`` function')
    ## TEST THE ARGUMENTS
    os.chdir(pathToProjectRoot)

    from subprocess import Popen, PIPE, STDOUT
    cmd = """git init && git add --all . && git commit -m "first commit" """ % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    if branches:
        cmd = """git branch bug && git branch dev""" % locals()
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
        output = p.communicate()[0]
        log.debug('output: %(output)s' % locals())

    ## VARIABLES ##
    log.info('completed the ``create_local_git_repo`` function')
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
