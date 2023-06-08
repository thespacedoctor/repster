#!/usr/bin/env python
# encoding: utf-8
"""
*Command-line utils for repster*

:Author:
    David Young

:Date Created:
    June 4, 2014

.. todo::
    

Usage:
    repster -i create
    repster create -l <location> -d <pathToHostDirectory> -n <projectName> -s <strapline> -y <pathToSettings> [-w <seperateOrSame>] [-r <repoName>]
    repster hook -l <location> -n <projectName> -u <domainName> -y <pathToSettings>

    -h, --help                             show this help message
    -v, --version                          show version
    -i, --interactive                      interactive mode
    -l, --location                         github or bitbucket (gh or bb)
    -d, --directiory                       path to the directory to host the local git repo
    -n, --name                             name of the project
    -s, --strapline                        description of project ("use quotes")
    -w, --wiki                             add a private or public wiki
    -u, --domainName                       the domain name
    -y, --yamlSettings                     path to the yaml settings file
    -r <repoName>, --repoName <repoName>   remote repo name if not the same as the local projectName
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
import webbrowser
import pickle
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times
from open_repo_in_sublime import open_repo_in_sublime
from add_git_repo_to_bitbucket import add_git_repo_to_bitbucket
from add_git_repo_to_github import add_git_repo_to_github
from add_git_repo_to_tower import add_git_repo_to_tower
from create_local_git_repo import create_local_git_repo
from create_project_folder import create_project_folder
from add_hook_to_bitbucket_repo import add_hook_to_bitbucket_repo
from add_hook_to_github_repo import add_hook_to_github_repo
from open_webhook_list_in_browser import open_webhook_list_in_browser
from clone_github_repo_wiki import clone_github_repo_wiki
from clone_bitbucket_repo_wiki import clone_bitbucket_repo_wiki

import readline
import glob

# for interactive commands ...


def tab_complete(text, state):
    return (glob.glob(text + '*') + [None])[state]


def main(arguments=None):
    """
    *The main function used when ``cl_utils.py`` is run as a single script from the cl, or when installed as a cl command*
    """
    su = tools(
        arguments=arguments,
        docString=__doc__,
        logLevel="WARNING",
        options_first=False
    )
    arguments, settings, log, dbConn = su.setup()

    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(tab_complete)

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
    startTime = times.get_now_sql_datetime()
    log.info(
        '--- STARTING TO RUN THE cl_utils.py AT %s' %
        (startTime,))

    privateFlag = True
    # set options interactively if user requests
    if interactiveFlag:

        if interactiveFlag == "create":
            create = True

        location = ""
        while location != "g" and location != "b":
            location = raw_input(
                "github or bitbucket [g/b]? \n  >  ")
        if location == "g":
            location = "github"
        else:
            location = "bitbucket"

        # load previous settings
        moduleDirectory = os.path.dirname(__file__) + "/resources"
        pathToPickleFile = "%(moduleDirectory)s/%(location)s.p" % locals()
        try:
            with open(pathToPickleFile):
                pass
            previousSettingsExist = True
        except:
            previousSettingsExist = False
        previousSettings = {}
        if previousSettingsExist:
            previousSettings = pickle.load(open(pathToPickleFile, "rb"))

        if "pathToHostDirectory" in previousSettings:
            default = previousSettings["pathToHostDirectory"]
            pathToHostDirectory = raw_input(
                "path to the host directory? (%(default)s)\n  >  " % locals())
            if not len(pathToHostDirectory):
                pathToHostDirectory = default
        else:
            pathToHostDirectory = raw_input(
                "path to the host directory?\n  >  " % locals())

        if "yamlSettingsFlag" in previousSettings:
            default = previousSettings["yamlSettingsFlag"]
            yamlSettingsFlag = raw_input(
                "path to the credentials file? (%(default)s)\n  >  " % locals())
            if not len(yamlSettingsFlag):
                yamlSettingsFlag = default
        else:
            yamlSettingsFlag = raw_input(
                "path to the credentials file?\n  >  " % locals())

        if "projectName" in previousSettings:
            default = previousSettings["projectName"]
            projectName = raw_input(
                "name of new git repo? (%(default)s)\n  >  " % locals())
            if not len(projectName):
                projectName = default
        else:
            projectName = raw_input(
                "name of new git repo?\n  >  " % locals())

        while privateFlag != "y" and privateFlag != "n":
            privateFlag = raw_input(
                "private repo [y/n]? \n  >  ")
        if privateFlag == "y":
            privateFlag = True
        else:
            privateFlag = False

        if "strapline" in previousSettings:
            default = previousSettings["strapline"]
            strapline = raw_input(
                "give a short description of the project (%(default)s)\n  >  " % locals())
            if not len(strapline):
                strapline = default
        else:
            strapline = raw_input(
                "give a short description of the project\n  >  " % locals())

        while wikiFlag != "y" and wikiFlag != "n":
            wikiFlag = raw_input(
                "add a wiki [y/n]? \n  >  ")
        if wikiFlag == "y":
            wiki = ""
            while wiki != "y" and wiki != "n":
                wiki = raw_input(
                    "do you want to make a seperate repo for wiki/issues [y/n]? \n  >  ")
            if wiki == "y":
                wiki = "seperate"
            else:
                wiki = "same"
        else:
            wiki = False

        # save the most recently used requests
        pickleMeObjects = [
            "pathToHostDirectory", "projectName", "strapline", "yamlSettingsFlag"]
        pickleMe = {}
        theseLocals = locals()
        for k in pickleMeObjects:
            pickleMe[k] = theseLocals[k]
        pickle.dump(pickleMe, open(pathToPickleFile, "wb"))

    else:
        if wikiFlag:
            wiki = seperateOrSame
        else:
            wiki = False

    # Create command ...
    if create and pathToHostDirectory and projectName:
        create_project_folder(
            log=log,
            pathToHostDirectory=pathToHostDirectory,
            wiki=wiki,
            projectName=projectName
        )

        pathToProjectRoot = """%(pathToHostDirectory)s/%(projectName)s""" % locals(
        )

        create_local_git_repo(
            log=log,
            pathToProjectRoot=pathToProjectRoot
        )

        wikiUrl = False
        if location == "bb" or location == "bitbucket":
            repoUrl = add_git_repo_to_bitbucket(
                log=log,
                pathToProject=pathToProjectRoot,
                strapline=strapline,
                pathToCredentials=pathToSettings,
                private=privateFlag,
                wiki=wiki
            )
            if wiki:
                thisWiki = clone_bitbucket_repo_wiki(
                    log=log,
                    projectName=projectName,
                    pathToHostDirectory=pathToHostDirectory,
                    strapline=strapline,
                    wiki=wiki,
                    pathToCredentials=pathToSettings
                )
                wikiUrl, pathToWikiRoot = thisWiki.get()
                add_git_repo_to_tower(
                    log=log,
                    pathToProjectRoot=pathToWikiRoot
                )
                if wikiUrl:
                    webbrowser.open_new_tab(wikiUrl)
        elif location == "gh" or location == "github":
            repoUrl = add_git_repo_to_github(
                log=log,
                pathToProject=pathToProjectRoot,
                strapline=strapline,
                private=privateFlag,
                pathToCredentials=yamlSettingsFlag,
                wiki=wiki,
                projectName=repoNameFlag
            )

            if wiki:
                thisWiki = clone_github_repo_wiki(
                    log=log,
                    projectName=projectName,
                    pathToHostDirectory=pathToHostDirectory,
                    strapline=strapline,
                    wiki=wiki,
                    pathToCredentials=yamlSettingsFlag
                )
                wikiUrl, pathToWikiRoot = thisWiki.get()
                add_git_repo_to_tower(
                    log=log,
                    pathToProjectRoot=pathToWikiRoot
                )
                if wikiUrl:
                    webbrowser.open_new_tab(wikiUrl)

        add_git_repo_to_tower(
            log=log,
            pathToProjectRoot=pathToProjectRoot
        )

        open_repo_in_sublime(
            log=log,
            pathToProjectRoot=pathToProjectRoot
        )

        ## open in webbrowser
        try:
            webbrowser.open_new_tab(repoUrl)
        except:
            pass

    # hook commands ...
    if hook:
        if location == "bb" or location == "bitbucket":
            add_hook_to_bitbucket_repo(
                log,
                repoName=projectName,
                hookDomain=domainName,
                pathToCredentials=yamlSettingsFlag
            )
        elif location == "gh" or location == "github":
            add_hook_to_github_repo(
                log,
                repoName=projectName,
                hookDomain=domainName,
                pathToCredentials=yamlSettingsFlag
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
    endTime = times.get_now_sql_datetime()
    runningTime = times.calculate_time_difference(startTime, endTime)
    log.info(
        '-- FINISHED ATTEMPT TO RUN THE cl_utils.py AT %s (RUNTIME: %s) --' %
        (endTime, runningTime, ))

    return


if __name__ == '__main__':
    main()
