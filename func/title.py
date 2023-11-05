import os
import ctypes
import sys

def setTitle(_str):
    system = os.name
    if system == 'nt':
        #if its windows
        ctypes.windll.kernel32.SetConsoleTitleW(f"Widow 1.0.0 @ Menu")
    elif system == 'posix':
        #if its linux
        sys.stdout.write(f"Widow 1.0.0 @ Menu")
    else:
        #if its something else or some err happend for some reason, we do nothing
        pass