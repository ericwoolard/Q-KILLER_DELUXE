REQUIREMENTS
------------
1. curl
2. Python 3.5
3. PRAW
4. Slack API token for bot

How to use
----------
1. Place Q-Killer script in a new directory (~/qkiller/ will do)
2. Edit credentials on line 10 in qkiller.py
3. Edit subreddit on line 19
4. Adjust alert param number on lines 30-31 (optional)
5. Edit Slack API info lines 35-37
6. start the script with `nohup` by running `nohup python3 qkiller.py &` 

If you only have 1 version of python installed, just use `python` instead of `python3`

INFO
----------
This script was made for the /r/GlobalOffensive mod team, to alert us in Slack if the modqueue reaches 15 or more items.
Use `nohup` to run in the background and ignore the hangup signal. (See 'How to use' above)