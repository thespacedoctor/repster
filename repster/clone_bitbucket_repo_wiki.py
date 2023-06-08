#!/usr/local/bin/python
# encoding: utf-8
"""
*Clone the wiki for a bitbucket repo*

:Author:
    David Young

:Date Created:
    December 8, 2014

.. todo::
    
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import readline
import glob
import yaml
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]

###################################################################
# CLASSES                                                         #
###################################################################


class clone_bitbucket_repo_wiki():

    """
    *The worker class for the clone_bitbucket_repo_wiki module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``projectName`` -- name of the project
        - ``pathToHostDirectory`` -- path to directory used to host the wiki
        - ``username`` -- github username
        - ``strapline`` -- strapline for the code repo
        - ``wiki`` -- wiki (False, same or seperate)
        - ``pathToCredentials`` -- path to yaml file containing  credentials

    .. todo::

    """
    # Initialisation

    def __init__(
            self,
            log,
            projectName,
            pathToHostDirectory,
            strapline,
            wiki,
            pathToCredentials
    ):
        self.log = log
        log.debug("instansiating a new 'clone_bitbucket_repo_wiki' object")
        self.projectName = projectName
        self.pathToHostDirectory = pathToHostDirectory
        self.wiki = wiki
        self.strapline = strapline
        self.pathToCredentials = pathToCredentials
        # xt-self-arg-tmpx

        # Initial Actions
        # Setup credentials
        stream = file(pathToCredentials, 'r')
        yamlContent = yaml.load(stream)
        stream.close()

        self.username = yamlContent["user"]
        self.password = yamlContent["password"]

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """
        *get the clone_bitbucket_repo_wiki object*

        **Return:**
            - ``wikiUrl, pathToWikiRoot`` -- the URL to bitbucket wiki, path to wiki repo on local machine

        .. todo::

        """
        self.log.debug('starting the ``get`` method')

        # If seperate wiki, create the bitbucket repo
        if self.wiki == "seperate":
            self.projectName = self.projectName + "_wiki"
            self._create_new_seperate_wiki()

        self._clone_the_wiki_repo()

        username = self.username
        projectName = self.projectName
        pathToHostDirectory = self.pathToHostDirectory
        if self.wiki == "seperate":
            wikiUrl = "https://bitbucket.org/%(username)s/%(projectName)s/wiki/" % locals(
            )
        else:
            wikiUrl = False
        pathToWikiRoot = "%(pathToHostDirectory)s/%(projectName)s.wiki" % locals()

        self.log.debug('completed the ``get`` method')
        return wikiUrl, pathToWikiRoot

    def _clone_the_wiki_repo(
            self):
        """
        *clone the wiki repo*

        **Return:**
            - None

        .. todo::

        """
        self.log.debug('starting the ``_clone_the_wiki_repo`` method')

        # create and execute the clone commmand
        username = self.username
        projectName = self.projectName
        pathToHostDirectory = self.pathToHostDirectory
        os.chdir(pathToHostDirectory)
        cmd = """git clone git@bitbucket.org:%(username)s/%(projectName)s.git/wiki %(projectName)s.wiki""" % locals(
        )
        from subprocess import Popen, PIPE, STDOUT
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
        output = p.communicate()[0]
        self.log.debug('output: %(output)s' % locals())

        self.log.debug('completed the ``_clone_the_wiki_repo`` method')
        return None

    def _create_new_seperate_wiki(
            self):
        """
        *generate the command to create a repo for a seperate wiki and then execute*

        **Return:**
            - None

        .. todo::

        """
        self.log.debug('starting the ``_create_new_seperate_wiki`` method')

        projectName = self.projectName
        strapline = self.strapline
        username = self.username
        password = self.password
        if strapline:
            strapline = "--data description='%(strapline)s'" % locals()
        private = "--data is_private='true'"
        from subprocess import Popen, PIPE, STDOUT
        cmd = """curl --user %(username)s:%(password)s  https://api.bitbucket.org/1.0/repositories/ --data name=%(projectName)s  %(private)s %(strapline)s --data has_wiki='true' """ % locals(
        )
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
        output = p.communicate()[0]
        self.log.debug('output: %(output)s' % locals())

        self.log.debug('completed the ``_create_new_seperate_wiki`` method')
        return None


if __name__ == '__main__':
    main()
