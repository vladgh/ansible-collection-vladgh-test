#!/usr/bin/env python

import os
import sys
import unittest
from unittest.mock import patch, MagicMock

# Add the plugins/modules directory to the path so we can import our module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../plugins/modules'))

from hello_world import run_module


class TestHelloWorldModule(unittest.TestCase):
    
    @patch('hello_world.AnsibleModule')
    def test_default_greeting(self, mock_ansible_module):
        # Mock the AnsibleModule
        mock_module = MagicMock()
        mock_module.params = {'name': 'World', 'message': 'Hello'}
        mock_module.check_mode = False
        mock_ansible_module.return_value = mock_module
        
        # Run the module
        run_module()
        
        # Check that exit_json was called with the expected result
        expected_result = {
            'changed': True,
            'greeting': 'Hello, World!'
        }
        mock_module.exit_json.assert_called_once_with(**expected_result)
    
    @patch('hello_world.AnsibleModule')
    def test_custom_greeting(self, mock_ansible_module):
        # Mock the AnsibleModule
        mock_module = MagicMock()
        mock_module.params = {'name': 'Alice', 'message': 'Good morning'}
        mock_module.check_mode = False
        mock_ansible_module.return_value = mock_module
        
        # Run the module
        run_module()
        
        # Check that exit_json was called with the expected result
        expected_result = {
            'changed': True,
            'greeting': 'Good morning, Alice!'
        }
        mock_module.exit_json.assert_called_once_with(**expected_result)
    
    @patch('hello_world.AnsibleModule')
    def test_check_mode(self, mock_ansible_module):
        # Mock the AnsibleModule in check mode
        mock_module = MagicMock()
        mock_module.params = {'name': 'World', 'message': 'Hello'}
        mock_module.check_mode = True
        mock_ansible_module.return_value = mock_module
        
        # Run the module
        run_module()
        
        # Check that exit_json was called with no changes
        expected_result = {
            'changed': False,
            'greeting': ''
        }
        mock_module.exit_json.assert_called_once_with(**expected_result)


if __name__ == '__main__':
    unittest.main()