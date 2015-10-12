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
"""
################# GLOBAL IMPORTS ####################
import sys
import os
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


def add_git_repo_to_tower(
        log,
        pathToProjectRoot):
    """create and execute the command to add git repo to tower

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToProjectRoot`` -- path to project

    **Return:**
        - None

    **Todo**
    """
    log.info('starting the ``add_git_repo_to_tower`` function')

    from subprocess import Popen, PIPE, STDOUT
    cmd = """gittower "%(pathToProjectRoot)s" """ % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    log.info('completed the ``add_git_repo_to_tower`` function')
    return None

if __name__ == '__main__':
    main()
