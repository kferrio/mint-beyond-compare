#!/usr/bin/python
import os
import sys
import errno
import re

# path for nemo actions; needed because working directory is otherwise the current nemo target
acts = os.path.expanduser('~/.local/share/nemo/actions')
act = os.path.join(acts, 'bc-half.nemo_action')
act_lhs = os.path.join(acts, 'bc-lhs.na')
act_rhs = os.path.join(acts, 'bc-rhs.na')


# path for holding the lhs state 
temp = os.path.expanduser('~/tmp/bcompare')
state = os.path.join(temp, 'state.txt')

# The nemo action must pass the helper script exactly one argument.

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

			# rewrite the 
			lines = [line for line in open(act_lhs, 'r')]
			pat = r'^Name=.*'
			lines = [re.sub(pat,'Name=Compare to '+os.path.basename(sys.argv[1]), line) for line in lines]
			pat = r'^Icon-Name=.*'
			lines = [re.sub(pat,'Icon-Name=bcomparefull32', line) for line in lines]
			pat = r'^Comment=.*'
			lines = [re.sub(pat,'Comment=Select right side for comparison', line) for line in lines]
			f = open(act_rhs, 'w')
			for line in lines:
				f.write(line)
			f.close()

			os.unlink(act)
			os.symlink(act_rhs, act)
else:
	# called with no arguments => initialize
	if not os.path.exists(temp):
		os.makedirs(temp)
	if os.path.exists(state):
		os.unlink(state)

	try:
		os.symlink(act_lhs, act)
	except OSError, e:
		if errno.EEXIST == e.errno:
			try:
				os.unlink(act)
				os.symlink(act_lhs, act)
			except:
				print "Setup failed."