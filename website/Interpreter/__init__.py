__author__ = 'tclh123'

import os
package_path = os.path.abspath(os.path.dirname(__file__))
#print package_path
import sys
sys.path.insert(0, package_path)

import common
import lexer
import parser