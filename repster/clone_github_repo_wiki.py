#!/usr/local/bin/python
# encoding: utf-8
"""
*Clone a github wiki to a specific location on computer*

:Author:
    David Young

:Date Created:
    ggd

.. todo::
    
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import re
import readline
import glob
import yaml
from docopt import docopt
from mechanize import Browser
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]

###################################################################
# CLASSES                                                         #
###################################################################


class clone_github_repo_wiki():

    """
    *The worker class for the clone_github_repo_wiki module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``projectName`` -- name of the project
        - ``pathToHostDirectory`` -- path to directory used to host the wiki
        - ``username`` -- github username
        - ``strapline`` -- strapline for the code repo
        - ``wiki`` -- wiki [False, same or seperate]
        - ``pathToCredentials`` -- path to yaml file containing the github credentials

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
        log.debug("instansiating a new 'clone_github_repo_wiki' object")
        self.projectName = projectName
        self.pathToHostDirectory = pathToHostDirectory
        self.wiki = wiki
        self.strapline = strapline
        self.pathToCredentials = pathToCredentials
        # xt-self-arg-tmpx

        # Initial Actions
        # Import github credentials
        stream = file(self.pathToCredentials, 'r')
        yamlContent = yaml.load(stream)
        stream.close()

        self.username = yamlContent["user"]
        self.token = yamlContent["token"]
        self.password = yamlContent["password"]

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """
        *get the clone_github_repo_wiki object*

        **Return:**
            - ``wikiUrl, pathToWikiRoot`` -- the URL to github wiki, path to wiki repo on local machine

        .. todo::

        """
        self.log.debug('starting the ``get`` method')

        if self.wiki == "seperate":
            self.projectName = self.projectName + "_wiki"
            self._create_new_seperate_wiki()
        self._initiate_the_wiki()
        self._clone_the_wiki_repo()

        username = self.username
        projectName = self.projectName
        pathToHostDirectory = self.pathToHostDirectory
        if self.wiki == "seperate":
            wikiUrl = "https://github.com/%(username)s/%(projectName)s" % locals(
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

        # create the command to clone the github repo then execute
        username = self.username
        projectName = self.projectName
        pathToHostDirectory = self.pathToHostDirectory
        os.chdir(pathToHostDirectory)
        cmd = """git clone git@github.com:%(username)s/%(projectName)s.wiki.git""" % locals(
        )
        from subprocess import Popen, PIPE, STDOUT
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
        output = p.communicate()[0]
        self.log.debug('output: %(output)s' % locals())

        os.chdir("%(pathToHostDirectory)s/%(projectName)s.wiki" % locals(
        ))

        self.log.debug('completed the ``_clone_the_wiki_repo`` method')
        return None

    def _initiate_the_wiki(
            self):
        """
        *initiate the github wiki - not available in API so fill in form on github pages*

        **Return:**
            - None

        .. todo::

        """
        self.log.debug('starting the ``_initiate_the_wiki`` method')

        username = self.username
        projectName = self.projectName

        # sign into github
        br = Browser()
        br.set_handle_robots(False)
        br.open("https://github.com/login")
        br.select_form(nr=1)
        br.form['login'] = self.username
        br.form['password'] = self.password
        br.submit()

        # open wiki page for repo and create first page
        response = br.open(
            "https://github.com/%(username)s/%(projectName)s/wiki/_new" % locals())
        br.select_form("gollum-editor")
        response = br.submit()

        self.log.debug('completed the ``_initiate_the_wiki`` method')
        return None

    def _create_new_seperate_wiki(
            self):
        """
        *create new seperate wiki -  create and execute the command to create the wiki repo*

        **Return:**
            - None

        .. todo::

        """
        self.log.debug('starting the ``_create_new_seperate_wiki`` method')

        projectName = self.projectName
        strapline = self.strapline
        username = self.username
        token = self.token

        from subprocess import Popen, PIPE, STDOUT
        cmd = """curl -u "%(username)s:%(token)s" https://api.github.com/user/repos -d '{"name":"'%(projectName)s'", "private":true, "description":"%(strapline)s", "has_wiki":true}'""" % locals(
        )
        print cmd
        p = Popen(cmd, stdout=PIPE, stdin=PIPE, shell=True)
        output = p.communicate()[0]
        self.log.debug('output: %(output)s' % locals())

        self.log.debug('completed the ``_create_new_seperate_wiki`` method')
        return None


if __name__ == '__main__':
    main()
