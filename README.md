mint-beyond-compare
===================

Python glue to add Beyond Compare context menus to the Mint file browser

It's only right that the world's best file browser should support the world's best diff/merge tool! 

This python hack sets up and manages nemo action files to support both simultaneous selection -- viz., compare these two objects -- and left-then-right selections -- viz., compare this object to that object -- for Nemo on Linux Mint.

Scooter (http://www.scootersoftware.com) has taken a binary approach to shell integration. That approach has the advantage of simplifying installation for multiple licensed users. Unfortunately, it doesn't always work.  And supporting a combinatoric beastiary of Linux OS and shell choices seems like a lot to ask of a presumably small company. Fortunately, Scooter made Beyond Compare scriptable. 

Yes, this repo probably should have been called nemo-beyond-compare. But go load Mint anyway. You'll be glad you did.

Installation
------------

 1. Clone the repo into ~/.local/share/nemo/actions

 2. chmod +x helper.py

 3. ./helper.py   # one-time setup

 4. Enjoy

Tested With...
--------------
 Beyond Compare 3

 Python 2.7

 Nemo 1.8.3

 Linux Mint 15 (Cinnamon on Olivia)