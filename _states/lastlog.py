# -*- coding: utf-8 -*-
'''
Last login of users

:maintainer:    Robert Booth <robert.booth@trebortech.com>
:maturity:      new
:depends:       lastlog command
:platform:      Linux


'''
from __future__ import absolute_import

# Import base libs
import logging
from datetime import datetime, timedelta

log = logging.getLogger(__name__)


# Provide a name that you can call the module from
__virtualname__ = 'lastlog'


# Check to see if this module should load on the minion
def __virtual__():
    if __grains__.get('kernel') == 'Linux':
        return __virtualname__
    else:
        return (False, '')


def cleanup_users(name, olderthan=90):

    ret = {'name': name,
           'changes': {},
           'result': True,
           'comment': ''}

    changes = []

    userlogins = __salt__['lastlog.last_login']

    timeformat = '%a %b %d %H:%M:%S %z %Y'
    present = datetime.now

    for user in userlogins:
        username = user[0]
        lastlogin = user[1]

        flastlogin = datetime.datetime.strptime(lastlogin, timeformat)
        deltatime = present - flastlogin

        days = deltatime.timedelta().days()

        if days > olderthan:
            # remove user
            changes.append(username)

    ret['changes'] = changes

    return ret