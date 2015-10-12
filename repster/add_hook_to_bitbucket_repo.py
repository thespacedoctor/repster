#!/usr/bin/env python
# encoding: utf-8
"""
add_hook_to_bitbucket_repo.py
=============================
:Summary:
    Add a hook to an existing bitbucket repo

:Author:
    David Young

:Date Created:
    June 25, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from subprocess import Popen, PIPE, STDOUT
from docopt import docopt
import yaml
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : June 25, 2014
# CREATED : June 25, 2014
# AUTHOR : DRYX
def add_hook_to_bitbucket_repo(
        log,
        repoName,
        hookDomain,
        pathToCredentials=False):
    """add hook to bitbucket repo

    **Key Arguments:**
        - ``log`` -- logger
        - ``repoName`` -- the name of the repo to add hook to
        - ``hookDomain`` -- the domain of the service to add the hook
        - ``pathToCredentials`` -- path to yaml file containing github credentials

    **Return:**
        - None

    **Todo**
    """
    log.info('starting the ``add_hook_to_bitbucket_repo`` function')

    # create the command to add the hook to the repo
    stream = file(pathToCredentials, 'r')
    yamlContent = yaml.load(stream)
    stream.close()
    user = yamlContent["user"]
    password = yamlContent["password"]
    repoNameLower = repoName.lower()
    import urllib
    if "http://" not in hookDomain:
        hookDomain = "http://%(hookDomain)s" % locals()
    urlString = "%(hookDomain)s/assets/scripts/commonutils/update_git_repo.py?repoName=%(repoName)s" % locals()

    # make sure hook doesn't exist already
    cmd = """curl --user %(user)s:%(password)s --request GET https://api.bitbucket.org/1.0/repositories/%(user)s/%(repoNameLower)s/services/ --data "type=POST" """ % locals(
    )
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    if urlString in output:
        log.warning('bitbucket hook already exists %(urlString)s' % locals())
        return

    urlString = urllib.quote(hookDomain)
    cmd = """curl --user %(user)s:%(password)s  https://api.bitbucket.org/1.0/repositories/%(user)s/%(repoNameLower)s/services/ --data "type=POST&URL=%(urlString)s/assets/scripts/commonutils/update_git_repo.py?repoName=%(repoName)s" """ % locals(
    )
    print cmd

    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    log.info('completed the ``add_hook_to_bitbucket_repo`` function')
    return None

if __name__ == '__main__':
    main()
