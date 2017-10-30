REQUIREMENTS
------------
1. [PRAW 4+](https://praw.readthedocs.io/en/latest/index.html)
2. [SlackClient](https://github.com/slackapi/python-slackclient)

How to use
----------
1. Place Q-Killer script in a new directory
2. Place your Slack bots token on line 17 of `qkiller.py`
3. Fill out the info in `auth.json` (see ["Creating a Script Application](https://github.com/ericwoolard/Q-KILLER_DELUXE/blob/master/README.md#creating-a-script-application) below)
4. Edit the message to deliver and the channel name in `settings.json` *Note* - if you want to mention all active users, you must use `<!here>` instead of `@here`. Same applies for `@channel` mentions - use `<!channel>` instead.
5. *OPTIONAL*: Adjust alert parameter (`NUM_TO_ALERT`) on line 21. This decides how many reports must be in queue before an alert is triggered
6. Start the script with `nohup` by running `nohup python3 qkiller.py &` (Linux)

If you only have 1 version of python installed, just use `python` instead of `python3` when starting the script.

**WINDOWS** - To run this script on a windows server or desktop, you can use `pythonw` to run it in the background.

INFO
----------
This script was made by /u/zebradolphin5 for the /r/GlobalOffensive mod team, to alert us in Slack if the modqueue reaches 15 or more items.
Use `nohup` to run in the background and ignore the hangup signal. (See 'How to use' above)

Creating A Script Application
----------
To obtain a client ID and client secret, login to the Reddit account that will be using the script, and go to preferences>apps.
Click on "Create a new app" (may say "Create another app") and SELECT THE 'Script' TYPE (not 'web' or 'installed'. Name/description 
can be whatever. You can leave the about URL blank, but you still must provide a redirect URI even though it's not needed for a 
script application. For that, you can just put `http://localhost/`. The string at the top left (underneath what should say personal 
use script) will be your client_ID. Client secret is listed next to the 'Secret' field. 