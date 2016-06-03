#!/usr/bin/env python
# encoding: utf-8
"""
*add a local git repo to bitbucket*

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
def add_git_repo_to_bitbucket(
        log,
        pathToProject,
        strapline=False,
        pathToCredentials=False,
        private=True,
        wiki=False):
    """
    *add git repo to bitbucket*

    **Key Arguments:**
        - ``log`` -- logger
        - ``pathToProject`` -- path to the project directory on the local machine
        - ``strapline`` -- project description
        - ``pathToCredentials`` -- path to yaml file containing bitbucket credentials
        - ``private`` -- is repo to be set to private?
        - ``wiki`` -- wiki [False, same or seperate]


    **Return:**
        - ``repoUrl`` - the bitbucket url to the repo

    .. todo::

    """
    log.info('starting the ``add_git_repo_to_bitbucket`` function')

    # test remote of local repo
    os.chdir(pathToProject)
    from subprocess import Popen, PIPE, STDOUT
    cmd = """git remote""" % locals()
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())
    if "origin" in output:
        basename = os.path.basename(pathToProject)
        log.error(
            'cound not add %(basename)s to bitbucket as it already has an "origin" remote' %
            locals())
        return

    # create and execute the command to start a new repo on bitbucket
    if pathToProject[-1] == "/":
        pathToProject = pathToProject[:-1]
    projectName = os.path.basename(pathToProject)
    stream = file(pathToCredentials, 'r')
    yamlContent = yaml.load(stream)
    stream.close()
    user = yamlContent["user"]
    password = yamlContent["password"]
    if private:
        private = "--data is_private='true'"
    else:
        private = ""
    if strapline:
        strapline = "--data description='%(strapline)s'" % locals()
    else:
        strapline = ""
    if wiki == "same":
        has_wiki = "--data has_wiki='true'"
    else:
        has_wiki = ""
    from subprocess import Popen, PIPE, STDOUT
    ueprojectName = projectName.replace(" ", "-").lower()

    cmd = """curl --user %(user)s:%(password)s  https://api.bitbucket.org/1.0/repositories/ --data name=%(ueprojectName)s %(private)s %(strapline)s %(has_wiki)s --data has_issues='true' """ % locals(
    )
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    # add remote repo to local repo and push branches to bitbucket
    cmd = """git remote add origin git@bitbucket.org:%(user)s/%(ueprojectName)s.git && git push -u origin --all && git push -u origin --tags""" % locals(
    )
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
    output = p.communicate()[0]
    log.debug('output: %(output)s' % locals())

    repoUrl = "https://bitbucket.org/%(user)s/%(ueprojectName)s" % locals()

    log.info('completed the ``add_git_repo_to_bitbucket`` function')
    return repoUrl

if __name__ == '__main__':
    main()
