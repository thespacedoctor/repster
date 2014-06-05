#!/usr/bin/env python
# encoding: utf-8
"""
add_git_repo_to_github.py
============================
:Summary:
    add a local git repo to github

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
import yaml
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
def add_git_repo_to_github(
        log,
        pathToProject,
        pathToCredentials=False):
    """add git repo to github

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean add_git_repo_to_github function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``add_git_repo_to_github`` function')

    os.chdir(pathToProject)

    from subprocess import Popen, PIPE, STDOUT
    cmd = """git remote""" % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    if "origin" in output:
        basename = os.path.basename(pathToProject)
        log.error(
            'cound not add %(basename)s to github as it already has an "origin" remote' %
            locals())
        return

    if pathToProject[-1] == "/":
        pathToProject = pathToProject[:-1]

    projectName = os.path.basename(pathToProject)

    if not pathToCredentials:
        pathToCredentials = "/Users/Dave/github_credentials.yaml"

    stream = file(pathToCredentials, 'r')
    yamlContent = yaml.load(stream)
    stream.close()

    user = yamlContent["user"]
    token = yamlContent["token"]

    from subprocess import Popen, PIPE, STDOUT
    cmd = """curl -u "%(user)s:%(token)s" https://api.github.com/user/repos -d '{"name":"'%(projectName)s'"}'""" % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    cmd = """git remote add origin git@github.com:%(user)s/%(projectName)s.git && git push -u origin --all && git push -u origin --tags""" % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    log.info('completed the ``add_git_repo_to_github`` function')
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
