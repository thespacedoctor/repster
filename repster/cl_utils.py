#!/usr/bin/env python
# encoding: utf-8
"""
cl_utils.py
===========
:Summary:
    Command-line utils for repster

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

Usage:
    repster -i
    repster create -l <location> -d <pathToHostDirectory> -n <projectName>
    repster create -b -l <location> -d <pathToHostDirectory> -n <projectName> 
    repster hook -l <location> -n <projectName> -w <domainName>

    -h, --help        show this help message
    -v, --version     show version
    -l, --location    github or bitbucket (gh or bb)
    -d, --directiory  path to the directory to host the local git repo
    -n, --name        name of the project
    -b, --branches    with master, dev and bug branches
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
from open_repo_in_sublime import open_repo_in_sublime
from add_git_repo_to_bitbucket import add_git_repo_to_bitbucket
from add_git_repo_to_github import add_git_repo_to_github
from add_git_repo_to_tower import add_git_repo_to_tower
from create_local_git_repo import create_local_git_repo
from create_project_folder import create_project_folder
from add_hook_to_bitbucket_repo import add_hook_to_bitbucket_repo
from add_hook_to_github_repo import add_hook_to_github_repo
from open_webhook_list_in_browser import open_webhook_list_in_browser
# from ..__init__ import *


def main(arguments=None):
    """
    The main function used when ``cl_utils.py`` is run as a single script from the cl, or when installed as a cl command
    """
    ########## IMPORTS ##########
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    su = setup_main_clutil(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING",
        options_first=False
    )
    arguments, settings, log, dbConn = su.setup()

    # unpack remaining cl arguments using `exec` to setup the variable names
    # automatically
    for arg, val in arguments.iteritems():
        if arg[0] == "-":
            varname = arg.replace("-", "") + "Flag"
        else:
            varname = arg.replace("<", "").replace(">", "")
        if isinstance(val, str) or isinstance(val, unicode):
            exec(varname + " = '%s'" % (val,))
        else:
            exec(varname + " = %s" % (val,))
        if arg == "--dbConn":
            dbConn = val
        log.debug('%s = %s' % (varname, val,))

    ## START LOGGING ##
    startTime = dcu.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE cl_utils.py AT %s' %
        (startTime,))

    if create and pathToHostDirectory and projectName:
        create_project_folder(
            log=log,
            pathToHostDirectory=pathToHostDirectory,
            projectName=projectName
        )

        pathToProjectRoot = """%(pathToHostDirectory)s/%(projectName)s""" % locals(
        )
        if not branchesFlag:
            create_local_git_repo(
                log=log,
                pathToProjectRoot=pathToProjectRoot,
                branches=False
            )
        else:
            create_local_git_repo(
                log=log,
                pathToProjectRoot=pathToProjectRoot,
                branches=True
            )

        if location == "bb" or location == "bitbucket":
            add_git_repo_to_bitbucket(
                log=log,
                pathToProject=pathToProjectRoot,
                pathToCredentials=False,
                private=True
            )
        elif location == "gh" or location == "github":
            add_git_repo_to_github(
                log=log,
                pathToProject=pathToProjectRoot,
                pathToCredentials=False
            )

        add_git_repo_to_tower(
            log=log,
            pathToProjectRoot=pathToProjectRoot
        )

        open_repo_in_sublime(
            log=log,
            pathToProjectRoot=pathToProjectRoot
        )

    if hook:
        if location == "bb" or location == "bitbucket":
            add_hook_to_bitbucket_repo(
                log,
                repoName=projectName,
                hookDomain=domainName,
                pathToCredentials=False
            )
        elif location == "gh" or location == "github":
            add_hook_to_github_repo(
                log,
                repoName=projectName,
                hookDomain=domainName,
                pathToCredentials=False
            )
        open_webhook_list_in_browser(
            log=log,
            location=location,
            projectName=projectName
        )

    if "dbConn" in locals() and dbConn:
        dbConn.commit()
        dbConn.close()
    ## FINISH LOGGING ##
    endTime = dcu.get_now_sql_datetime()
    runningTime = dcu.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE cl_utils.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return

###################################################################
# CLASSES                                                         #
###################################################################
# xt-class-module-worker-tmpx
# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xt-worker-def

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
