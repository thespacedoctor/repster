#!/usr/bin/env python
# encoding: utf-8
"""
*add a local git repo to github*

:Author:
    David Young

:Date Created:
    June 4, 2014

.. todo::
    
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import yaml
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


def add_git_repo_to_github(
        log,
        pathToProject,
        strapline,
        private=False,
        pathToCredentials=False,
        wiki=False):
    """
    *add git repo to github*

    **Key Arguments:**
        - ``log`` -- logger
        - ``strapline`` -- the short description of the project
        - ``pathToProject`` -- path to the project on local machine
        - ``private`` -- private repo?
        - ``pathToCredentials`` -- path to yaml file containing github credentials
        - ``wiki`` -- wiki [False, same or seperate]

    **Return:**
        - ``repoUrl`` -- url to the github repo

    .. todo::

    """
    log.info('starting the ``add_git_repo_to_github`` function')

    if wiki == "same" or wiki == True:
        sameRepoWiki = "true"
    else:
        sameRepoWiki = "false"

    if private:
        private = "true"
    else:
        private = "false"

    # move into local repo directory and test for a remote
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

    # generate and execute the command to create the new github repo
    if pathToProject[-1] == "/":
        pathToProject = pathToProject[:-1]
    projectName = os.path.basename(pathToProject)
    stream = file(pathToCredentials, 'r')
    yamlContent = yaml.load(stream)
    stream.close()
    strapline = strapline.replace("'", "\u0027").replace('"', '\\"')
    user = yamlContent["user"]
    token = yamlContent["token"]
    from subprocess import Popen, PIPE, STDOUT
    cmd = """curl -u "%(user)s:%(token)s" https://api.github.com/user/repos -d '{"name":"%(projectName)s", "private":%(private)s, "description":"%(strapline)s", "has_wiki":%(sameRepoWiki)s}'""" % locals(
    )
    print cmd
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    # add the github remote to the local git repo and push branches to github
    cmd = """git remote add origin git@github.com:%(user)s/%(projectName)s.git && git push -u origin --all && git push -u origin --tags""" % locals(
    )
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    repoUrl = "https://github.com/%(user)s/%(projectName)s" % locals()

    log.info('completed the ``add_git_repo_to_github`` function')
    return repoUrl

if __name__ == '__main__':
    main()
