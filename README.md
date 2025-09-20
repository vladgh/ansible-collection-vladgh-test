# Ansible Collection - vladgh.test

A simple "Hello World" Ansible collection for testing and demonstration purposes.

## Description

This is a minimal Ansible collection that demonstrates the basic structure and components of an Ansible collection. It includes:

- A simple `hello_world` module that generates greeting messages
- A `hello_world` role that uses the module
- Example playbooks showing how to use both the module and role
- Basic unit tests

## Installation

You can install this collection using the `ansible-galaxy` command:

```bash
ansible-galaxy collection install vladgh.test
```

Or directly from the repository:

```bash
ansible-galaxy collection install git+https://github.com/vladgh/ansible-collection-vladgh-test.git
```

## Included Content

### Modules

- `vladgh.test.hello_world` - A simple module that generates greeting messages

### Roles

- `vladgh.test.hello_world` - A role that demonstrates using the hello_world module

## Usage

### Using the Module Directly

```yaml
- name: Say hello to the world
  vladgh.test.hello_world:
  register: result

- name: Display greeting
  debug:
    msg: "{{ result.greeting }}"

- name: Say hello to a specific person
  vladgh.test.hello_world:
    name: Alice
    message: Good morning
```

### Using the Role

```yaml
- name: Use hello_world role with defaults
  hosts: localhost
  roles:
    - vladgh.test.hello_world

- name: Use hello_world role with custom variables
  hosts: localhost
  vars:
    hello_world_name: "Ansible Users"
    hello_world_message: "Greetings"
  roles:
    - vladgh.test.hello_world
```

### Running Example Playbooks

```bash
# Run the module example playbook
ansible-playbook playbooks/hello_world.yml

# Run the role example playbook
ansible-playbook playbooks/hello_world_role.yml
```

## Module Parameters

### hello_world

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| name      | str  | No       | "World" | The name to greet |
| message   | str  | No       | "Hello" | Custom message to display |

## Role Variables

### hello_world

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| hello_world_name | str | "World" | The name to greet |
| hello_world_message | str | "Hello" | Custom message to display |

## Testing

Run the unit tests:

```bash
python -m pytest tests/unit/
```

Or run them directly:

```bash
python tests/unit/test_hello_world.py
```

## License

MIT

## Author Information

This collection was created by Vlad Ghinea.