mint-beyond-compare
===================

Python glue to add Beyond Compare context menus to the Mint file browser

It's only right that the world's best file browser should support the world's best diff/merge tool! Unfortunately, as of this writing, Scooter (http://www.scootersoftware.com) has taken a binary approach to shell integration.  Fortunately, Scooter made Beyond Compare scriptable. This hack sets up and manages nemo action files to support both simultaneous and left-then-right selections. 

Yes, this repo probably should have been called nemo-beyond-compare. But go load Mint anyway. You'll be glad you did.

Installation
------------

 1. Clone the repo into ~/.local/share/nemo/actions

 2. chmod +x helper.py

 3. ./helper.py   # one-time setup

 4. Enjoy

Dependencies
------------
 Beyond Compare 3

 Python 2.x

 Nemo