#!/usr/bin/env python
# encoding: utf-8
"""
*Create a local git repo*

:Author:
    David Young

:Date Created:
    June 4, 2014

.. todo::
    
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import shutil
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
def create_local_git_repo(
        log,
        pathToProjectRoot,
        branches=False):
    """
    *create a first instance of a git repo with all the neccessary files*

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToProjectRoot`` -- path to the root of the project
        - ``branches`` -- create dev and bug branches?

    **Return:**
        - None

    .. todo::

    """
    log.info('starting the ``create_local_git_repo`` function')

    # create the local repo
    os.chdir(pathToProjectRoot)
    from subprocess import Popen, PIPE, STDOUT
    cmd = """git init && git add --all . && git commit -m "first commit" """ % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    # add branches if required
    if branches:
        cmd = """git branch bug && git branch dev""" % locals()
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
        output = p.communicate()[0]
        log.debug('output: %(output)s' % locals())

    log.info('completed the ``create_local_git_repo`` function')
    return None


if __name__ == '__main__':
    main()
