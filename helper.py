#!/usr/bin/python
import os
import sys

# path for nemo actions; needed because working directory is otherwise the current nemo target
acts = os.path.expanduser('~/.local/share/nemo/actions')
act_lhs = os.path.join(acts, 'bc-lhs.na')
act_rhs = os.path.join(acts, 'bc-rhs.na')
act = os.path.join(acts, 'bc-half.nemo_action')

# path for holding the lhs state 
temp = os.path.expanduser('~/tmp/bcompare')
state = os.path.join(temp, 'state.txt')

# The nemo action must pass the helper script exactly one argument.

if not os.path.exists(temp):
	os.makedirs(temp)

if len(sys.argv)==2:
	if len(sys.argv[1])>0:
		if os.path.exists(state):
			# build and execute the command
			rhs = sys.argv[1]
			f = open(state,'r')
			lhs = f.readline().strip()
			f.close
			os.unlink(state)
			os.unlink(act)
			os.symlink(act_lhs, act)
			os.execlp('bcompare', 'bcompare', lhs, rhs)
		else:
			# stash lhs path
			f = open(state, 'w')
			f.write(sys.argv[1])
			f.close
			os.unlink(act)
			os.symlink(act_rhs, act)
