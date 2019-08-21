#!/usr/bin/python

import lldb
import commands
import optparse
import shlex

def skip_ptrace(frame, bp_loc, internal_dict):
    # interpreter = lldb.debugger.GetCommandInterpreter()
    # returnObject = lldb.SBCommandReturnObject()
    # interpreter.HandleCommand('register write pc \`$lr\`', returnObject)
    # # interpreter.HandleCommand('breakpoint delete -N bp_ptrace', returnObject)
    # interpreter.HandleCommand('c', returnObject)
    addr_lr = frame.FindRegister('lr')
    print(addr_lr)
    frame.SetPC(int(addr_lr.GetValue(), 16))
    lldb.debugger.HandleCommand('c')

def aadbg(debugger, command, result, internal_dict):
    interpreter = lldb.debugger.GetCommandInterpreter()
    returnObject = lldb.SBCommandReturnObject()
    interpreter.HandleCommand('breakpoint set -n ptrace -N bp_ptrace', returnObject)
    interpreter.HandleCommand('breakpoint command add --python-function aadebug.skip_ptrace', returnObject)
    # interpreter.HandleCommand('c', returnObject)

# And the initialization code to add your commands 
def __lldb_init_module(debugger, internal_dict):
    print('before add customized function')
    debugger.HandleCommand('command script add aadbg -f aadebug.aadbg')
    print('The "aadbg" python command has been installed and is ready for use.')
    print('Use this command to import: command script import ~/github/lldb_scripts/aadebug.py')
    