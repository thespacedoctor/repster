#!/usr/bin/env python
# encoding: utf-8
"""
*Open the project in sublime*

:Author:
    David Young

:Date Created:
    June 4, 2014

.. todo::
    
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : June 4, 2014
# CREATED : June 4, 2014
# AUTHOR : DRYX
def open_repo_in_sublime(
        log,
        pathToProjectRoot):
    """
    *create and execute command to open repo in sublime*

    **Key Arguments:**
        - ``log`` -- logger,
        - ``pathToProjectRoot`` -- the path to the root of the project

    **Return:**
        - None

    .. todo::

    """
    log.debug('starting the ``open_repo_in_sublime`` function')

    basePath = pathToProjectRoot
    for d in os.listdir(basePath):
        if os.path.isfile(os.path.join(basePath, d)):
            if "sublime-project" in d:
                projectPath = os.path.join(basePath, d)
                from subprocess import Popen, PIPE, STDOUT
                cmd = """open "%(projectPath)s" """ % locals()
                p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
                output = p.communicate()[0]
                log.debug('output: %(output)s' % locals())

    log.debug('completed the ``open_repo_in_sublime`` function')
    return None


if __name__ == '__main__':
    main()
