REQUIREMENTS
------------
1. Slack Incoming Webhook Integration (https://api.slack.com/incoming-webhooks)
2. Python 3+
3. PRAW 4+
4. Reddit API Token & Secret for the script

How to use
----------
1. Place Q-Killer script in a new directory
2. Edit lines 11-15 with your credentials, and line 16 with your subreddit
3. Edit line 47 with your Slack incoming webhook URL 
4. *OPTIONAL*: Adjust alert parameter on line 39 (`if count >= 15:`). This decides how many things in queue it takes to trigger the alert
5. Start the script with `nohup` by running `nohup python3 qkiller.py &` (Linux)

If you only have 1 version of python installed, just use `python` instead of `python3` when starting the script.

INFO
----------
This script was made for the /r/GlobalOffensive mod team, to alert us in Slack if the modqueue reaches 15 or more items.
Use `nohup` to run in the background and ignore the hangup signal. (See 'How to use' above)

To obtain a client ID and client secret, login to the Reddit account that will be using the script, and go to preferences>apps.
Click on "Create a new app" (may say "Create another app") and select the 'Script' type. Name/description can be whatever. You can
leave the about URL blank, but you still must provide a redirect URI even though it's not needed for a script application. For 
that, you can just put `http://localhost/`. The string at the top left (underneath what should say personal use script) will be
your client_ID. Client secret should be obvious :P