#!/usr/bin/env python3

"""
config.py
Configuration document.
Contain variables for global access and easier debugging.
"""

__author__  = "David Kristoffersen"
__email__   = "david.alta2010@gmail.com"

"""
User variables: Can be modified
"""

# Disables call tree print
print_tree = 1
# Determines if the call tree print should print unicode characters
print_unicode = 1
# Overwrite standard print
print_polymorph = 1

# Printing colors
col_green = "\x1b[38;2;50;160;50m"
col_yellow = "\x1b[38;2;255;204;51m"
col_brown = "\x1b[38;2;160;82;45m"
col_blue = "\x1b[38;2;50;150;250m"
col_red = "\x1b[38;2;220;55;22m"
col_bold = "\x1b[1m"
col_faint = "\x1b[2m"
col_reset = "\x1b[m"

"""
Module variables: Can not be modified
"""

# Used to check if entering a function or not
type_enter = 0
type_mid = 1
type_exit = 2

# Unicode box drawings
enter_str = "┌"
mid_str = "│"
connect_str = "├"
exit_str = "└"

# Padding attributes
padd_str = "─"
padd_width = 2
padd_len = 40
