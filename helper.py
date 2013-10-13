#!/usr/bin/python
#
# Nemo integration for Beyond Compare 3
#
# Installation for Linux Mint:
#  1) Copy kit to ~/.local/share/nemo/actions
#  2) chmod +x helper.py #this script)
#  3) ./helper.py  # one-time setup takes exactly 0 arguments

import os
import sys
import errno
import re

# Define path for nemo actions. 
# Otherwise, working directory would default to the current Nemo folder.
acts = os.path.expanduser('~/.local/share/nemo/actions')
act = os.path.join(acts, 'bc-half.nemo_action')
# Define paths for templates for actions.
act_lhs = os.path.join(acts, 'bc-lhs.na')
act_rhs = os.path.join(acts, 'bc-rhs.na')

# Define the path for holding the lhs state.
temp = os.path.expanduser('~/tmp/bcompare')
state = os.path.join(temp, 'state.txt')

# The nemo action must pass the helper script exactly one argument.
if len(sys.argv)==2:
	if len(sys.argv[1])>0:
		if os.path.exists(state):
			# Build and execute the BC command *after* cleaning up.
			rhs = sys.argv[1]
			f = open(state,'r')
			lhs = f.readline().strip()
			f.close
			os.unlink(state)
			os.unlink(act)
			os.symlink(act_lhs, act)
			os.execlp('bcompare', 'bcompare', lhs, rhs)

		else:
			# Stash lhs path.
			f = open(state, 'w')
			f.write(sys.argv[1])
			f.close
			# Rewrite the action for the rhs.
			# Be liberal in what we accept, and conservative in what we generate.
			lines = [line for line in open(act_lhs, 'r')]
			pat = r'^([\ \t])*Name([\ \t])*=.*'
			lines = [re.sub(pat,'Name=Compare to '+os.path.basename(sys.argv[1]), line) for line in lines]
			pat = r'^([\ \t])*Icon-Name([\ \t])*=.*'
			lines = [re.sub(pat,'Icon-Name=bcomparefull32', line) for line in lines]
			pat = r'^([\ \t])*Comment=([\ \t])*.*'
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