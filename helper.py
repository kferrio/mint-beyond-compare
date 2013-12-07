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
act_link_l = os.path.join(acts, 'bc-half.nemo_action')
act_link_r = os.path.join(acts, 'bc-otherhalf.nemo_action')
# Define paths for templates for actions.
act_lhs = os.path.join(acts, 'bc-lhs.na')
act_rhs = os.path.join(acts, 'bc-rhs.na')

# Define the path for holding the lhs state.
temp = os.path.expanduser('~/tmp/bcompare')
state = os.path.join(temp, 'state.txt')

# The nemo action must pass the helper script exactly two arguments.
if len(sys.argv)==3:
	if sys.argv[1] == "-r":
		# right-hand file - launch BC if left-hand was already set
		if len(sys.argv[2])>0 and os.path.exists(state):
			# Build and execute the BC command *after* cleaning up.
			rhs = sys.argv[2]
			with open(state, 'r') as f:
				lhs = f.readline().strip()
			os.unlink(state)
			# Remove symlink so the rhs option will disappear
			os.unlink(act_link_r)
			os.execlp('bcompare', 'bcompare', lhs, rhs)
	elif sys.argv[1] == "-l":
		# left-hand file - stash the path and enable the other menu option
		if len(sys.argv[2])>0:
			# Stash lhs path.
			with open(state, 'w') as f:
				f.write(sys.argv[2])
			# Rewrite the action for the rhs.
			# Be liberal in what we accept, and conservative in what we generate.
			lines = [line for line in open(act_rhs, 'r')]
			pat = r'^([\ \t])*Name([\ \t])*=.*'
			lines = [re.sub(pat,'Name=Compare to '+os.path.basename(sys.argv[2]), line) for line in lines]
			with open(act_rhs, 'w') as f:
				for line in lines:
					f.write(line)
			# Create symlink so the rhs option will appear
			os.symlink(act_rhs, act_link_r)
else:
	# called with no arguments => initialize
	if not os.path.exists(temp):
		os.makedirs(temp)
	if os.path.exists(state):
		os.unlink(state)

	try:
		os.symlink(act_lhs, act_link_l)
	except OSError, e:
		if errno.EEXIST == e.errno:
			try:
				os.unlink(act_link_l)
				os.symlink(act_lhs, act_link_l)
			except:
				print "Setup failed."