#!/usr/bin/env python
# encoding: utf-8
"""
add_hook_to_github_repo.py
==========================
:Summary:
    Add a hook to github repo via cl

:Author:
    David Young

:Date Created:
    June 25, 2014

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
import yaml
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
## LAST MODIFIED : June 25, 2014
## CREATED : June 25, 2014
## AUTHOR : DRYX
def add_hook_to_github_repo(
        log,
        repoName,
        hookDomain,
        pathToCredentials=False):
    """add hook to github repo

    **Key Arguments:**
        - ``log`` -- logger

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean add_hook_to_github_repo function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    log.info('starting the ``add_hook_to_github_repo`` function')

    if not pathToCredentials:
        pathToCredentials = "/Users/Dave/github_credentials.yaml"

    stream = file(pathToCredentials, 'r')
    yamlContent = yaml.load(stream)
    stream.close()

    user = yamlContent["user"]
    token = yamlContent["token"]

    import urllib
    if "http://" not in hookDomain:
        hookDomain = "http://%(hookDomain)s" % locals()
    urlString = "%(hookDomain)s/assets/scripts/commonutils/update_git_repo.py?repoName=%(repoName)s" % locals()

    from subprocess import Popen, PIPE, STDOUT
    cmd = """curl -u "%(user)s:%(token)s" -v -H "Content-Type: application/json" -X POST -d '{"name": "web", "active": true, "events": ["push"], "config": {"url": "%(urlString)s", "content_type": "json"}}' https://api.github.com/repos/%(user)s/%(repoName)s/hooks""" % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())


    log.info('completed the ``add_hook_to_github_repo`` function')
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

