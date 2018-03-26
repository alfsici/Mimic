#!usr/bin/env python

"""
This module contains basic configuration parameters for SimpleKRLProcessor.
"""

# Default program
DEFAULT_PROGRAM = \
    'DEF example()\n' \
    '  BAS(#INITMOV, 0)' \
    '  ; Go to start position\n' \
    '  PTP {{A1 0, A2 -90, A3 90, A4 0, A5 90, A6 0}}\n' \
    '  ; Perform the following instructions\n' \
    '{}\n' \
    '  ; Go to end position\n' \
    '  PTP {{A1 0, A2 -90, A3 90, A4 0, A5 90, A6 0}}\n' \
    'END\n'
