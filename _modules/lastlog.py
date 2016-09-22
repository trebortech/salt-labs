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


# Impoort salt libs
from salt import utils

# Import supporting libs


log = logging.getLogger(__name__)


# Provide a name that you can call the module from
__virtualname__ = 'lastlog'


# Check to see if this module should load on the minion
def __virtual__():
    if __grains__.get('kernel') == 'Linux':
        return __virtualname__
    else:
        return (False, '')



def never_logged_in():

    cmd = "lastlog | grep Never | awk '{print $1}'"
    users = __salt__['cmd.shell'](cmd)

    return users

def last_login():

    cmd = "lastlog | grep -v Never"
    users = __salt__['cmd.shell'](cmd)

    userlist = users.split('\n')

    logins = []
    for user in userlist:
        username = user[0:18].strip()
        date = user[43:].strip()

        if username != 'Username':
            logins.append([username ,date])

    return logins
