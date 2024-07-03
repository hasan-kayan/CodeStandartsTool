# Check if the function has a test cass
import os
import sys
import re

def check_test(func_name):
    test_file = os.path.join(os.getcwd(), 'tests', 'test_{}.py'.format(func_name))
    if not os.path.exists(test_file):
        print('Test file for function {} not found'.format(func_name))
        sys.exit(1)
    with open(test_file, 'r') as f:
        content = f.read()
        if 'def test_{}('.format(func_name) not in content:
            print('Test case for function {} not found'.format(func_name))
            sys.exit(1)