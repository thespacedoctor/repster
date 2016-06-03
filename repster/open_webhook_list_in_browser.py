#!/usr/bin/env python
# encoding: utf-8
"""
*Open the webhooks listing in bitbucket or github*

:Author:
    David Young

:Date Created:
    September 16, 2014

.. todo::
    
"""
################# GLOBAL IMPORTS ####################
import sys
import os
import webbrowser
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from fundamentals import tools, times


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
    """
    *open webhook list in browser*

    **Key Arguments:**
        - ``log`` -- logger
        - ``location`` -- bitbucket or github
        - ``projectName`` -- the name of the project

    **Return:**
        - None

    .. todo::

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
