'''
Last login of users

:maintainer:    Robert Booth <robert.booth@trebortech.com>
:maturity:      new
:depends:       lastlog command
:platform:      Linux


'''

# Import base libs
import logging
from __future__ import absolute_import

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
    users = __salt__['cmd.run'](cmd)

    return users 