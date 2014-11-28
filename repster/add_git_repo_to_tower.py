# !/usr/bin/env python
# encoding: utf-8
"""
add_git_repo_to_tower.py
========================
:Summary:
    add a local git project to tower

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
# LAST MODIFIED : June 4, 2014
# CREATED : June 4, 2014
# AUTHOR : DRYX
def add_git_repo_to_tower(
        log,
        pathToProjectRoot):
    """add git repo to tower

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean add_git_repo_to_tower function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``add_git_repo_to_tower`` function')

    from subprocess import Popen, PIPE, STDOUT
    cmd = """gittower %(pathToProjectRoot)s""" % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    log.info('completed the ``add_git_repo_to_tower`` function')
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
