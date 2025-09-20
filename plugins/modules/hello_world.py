#!/usr/bin/python

# Copyright: (c) 2024, Vlad Ghinea
# MIT License (see COPYING or https://opensource.org/licenses/MIT)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: hello_world

short_description: A simple Hello World module

version_added: "1.0.0"

description: This is a simple Hello World module that demonstrates basic Ansible module functionality.

options:
    name:
        description: The name to greet
        required: false
        type: str
        default: "World"
    message:
        description: Custom message to display
        required: false
        type: str
        default: "Hello"

author:
    - Vlad Ghinea (@vladgh)
'''

EXAMPLES = r'''
# Simple greeting
- name: Say hello to the world
  vladgh.test.hello_world:

# Greet a specific person
- name: Say hello to Alice
  vladgh.test.hello_world:
    name: Alice

# Custom message
- name: Say good morning
  vladgh.test.hello_world:
    name: Bob
    message: Good morning
'''

RETURN = r'''
greeting:
    description: The greeting message
    type: str
    returned: always
    sample: 'Hello, World!'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=False, default='World'),
        message=dict(type='str', required=False, default='Hello')
    )

    # seed the result dict in the object
    result = dict(
        changed=False,
        greeting=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is the normal case)
    name = module.params['name']
    message = module.params['message']
    greeting = f"{message}, {name}!"
    
    result['greeting'] = greeting
    result['changed'] = True

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()