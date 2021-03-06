#!/usr/bin/env python

import os
import sys
from path import path
from charmhelpers.contrib.ansible import AnsibleHooks

# Create the hooks helper, passing a list of hooks which will be
# handled by default by running all sections of the playbook
# tagged with the hook name.


def hook_names(here=path(__file__).parent):
    for name in (x.basename()
                 for x in here.files() if x.islink()):
        yield name


hooks = AnsibleHooks(playbook_path='playbooks/site.yaml',
                     default_hooks=list(hook_names()))

if not os.path.exists('/etc/ansible'):
    os.mkdir('/etc/ansible')
    # Work around some wonkyness with ansible
    with open('/etc/ansible/hosts', 'w') as f:
        f.write('localhost')


if __name__ == "__main__":
    hooks.execute(sys.argv)
