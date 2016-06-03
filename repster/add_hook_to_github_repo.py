#!/usr/bin/env python
# encoding: utf-8
"""
*Add a hook to github repo via cl*

:Author:
    David Young

:Date Created:
    June 25, 2014

.. todo::
    
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
import yaml
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times

###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : June 25, 2014
# CREATED : June 25, 2014
# AUTHOR : DRYX


def add_hook_to_github_repo(
        log,
        repoName,
        hookDomain,
        pathToCredentials=False):
    """
    *add hook to github repo*

    **Key Arguments:**
        - ``log`` -- logger
        - ``repoName`` -- the name of the repo to add hook to
        - ``hookDomain`` -- the domain of the service to add the hook
        - ``pathToCredentials`` -- path to yaml file containing bitbucket credentials

    **Return:**
        - None

    .. todo::

    """
    log.info('starting the ``add_hook_to_github_repo`` function')

    # create and execute the command to add the hook to bitbucket
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
    cmd = """curl -u "%(user)s:%(token)s" -v -H "Content-Type: application/json" -X POST -d '{"name": "web", "active": true, "events": ["push"], "config": {"url": "%(urlString)s", "content_type": "json"}}' https://api.github.com/repos/%(user)s/%(repoName)s/hooks""" % locals(
    )
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    log.info('completed the ``add_hook_to_github_repo`` function')
    return None


if __name__ == '__main__':
    main()
