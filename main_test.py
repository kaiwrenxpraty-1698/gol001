'''
Functional test to test the main script
adding article to be read: https://www.digitalocean.com/community/tutorials/how-to-use-unittest-to-write-a-test-case-for-a-function-in-python
'''
import unittest
import sys
import io

from main import initiate_program, start_application

def main_test():
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    initiate_program()
    sys.stdout = sys.__stdout__
    print('Captured', capturedOutput.getvalue())

if __name__ == "__main__":
    main_test()


