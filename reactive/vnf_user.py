from charmhelpers.core.hookenv import (
    action_get,
    action_fail,
    action_set,
    status_set,
    log,
)

from charms.reactive import (
    clear_flag,
    set_flag,
    when,
    when_not,
)
import random


@when('sshproxy.configured')
@when_not('vnf-user.installed')
def install_vnf_user():
    set_flag('vnf-a.installed')
    status_set('active', 'Ready!')


@when('actions.add-user')
def action_add_user():
    """Run the touch command.

    Runs touch on vnf-a and vnf-b and returns the success or failure for each.
    """
    err = ''
    user_id = 0
    try:
        username = action_get('username')
        tariff = action_get('tariff')

        # If this were a functional VNF, it would add the username to its
        # database. For the purposes of demonstrating actions, this will return
        # a random number.
        user_id = random.randint(1, 100)

    except Exception as err:
        # This marks the action as having failed, so the ns charm knows not to
        # continue with the add_user operation.
        action_fail(str(err))
    else:
        # This will put the user_id in the action output, which will be read
        # by the ns charm. Multiple values could be returned here.
        action_set({'user-id': user_id})
    finally:
        clear_flag('actions.add-user')
