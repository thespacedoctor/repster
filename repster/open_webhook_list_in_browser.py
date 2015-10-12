#!/usr/bin/env python
# encoding: utf-8
"""
open_webhook_list_in_browser.py
===============================
:Summary:
    Open the webhooks listing in bitbucket or github

:Author:
    David Young

:Date Created:
    September 16, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import webbrowser
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : September 16, 2014
# CREATED : September 16, 2014
# AUTHOR : DRYX
def open_webhook_list_in_browser(
        log,
        location,
        projectName):
    """open webhook list in browser

    **Key Arguments:**
        - ``log`` -- logger
        - ``location`` -- bitbucket or github
        - ``projectName`` -- the name of the project

    **Return:**
        - None

    **Todo**
    """
    log.info('starting the ``open_webhook_list_in_browser`` function')

    # Open URL in a new tab, if a browser window is already open.
    if location == "bb" or location == "bitbucket":
        projectName = projectName.lower()
        url = "https://bitbucket.org/thespacedoctor/%(projectName)s/admin/hooks" % locals(
        )
        webbrowser.open_new_tab(url)

    if location == "gh" or location == "github":
        url = "https://github.com/thespacedoctor/%(projectName)s/settings/hooks" % locals(
        )
        webbrowser.open_new_tab(url)

    log.info('completed the ``open_webhook_list_in_browser`` function')
    return None


if __name__ == '__main__':
    main()
