# System imports
import io
import json
import os
import requests
import time
import traceback
from datetime import datetime
# Third party imports
import praw
import prawcore
from slackclient import SlackClient


# Create our instance of SlackClient so we can send messages to slack 
# when our conditions to do so are met
slack_bot = SlackClient('SLACK_TOKEN_HERE')

# This sets the number of reports in modqueue at which a Slack alert
# will be triggered. You may change this to any number you like.
NUM_TO_ALERT = 15


def setup():
    # Open our auth.json file storing our login and OAuth credentials,
    # and store it in a variable for use in this script
    with io.open('auth.json', 'r') as f:
        auth = json.load(f)
        try:
            # Create our Reddit instance for authentication
            r = praw.Reddit(client_id=auth['client_id'],
                            client_secret=auth['client_secret'],
                            username=auth['username'],
                            password=auth['password'],
                            user_agent=auth['user_agent'])

            subreddit = r.subreddit(auth['subreddit'])
            getCount(subreddit)
        except prawcore.exceptions.OAuthException as e:
            print('Prawcore OAuthException - Could not authenticate!\t {}'.format(e.description))
        except:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(now + ' - Error:\n' + error_message + '\n\n\n')
            time.sleep(300)
            setup()


def getCount(subreddit):
    while True:
        try:
            modQueue = subreddit.mod.modqueue()
            count = 0

            # Determine how many reports are currently in mod-queue
            for item in modQueue:
                count += 1
            print('Total items in queue: {} -- {}'.format(str(count), datetime.now()))

            if count >= NUM_TO_ALERT:
                alert_time = str(datetime.now())
                print('{} - Items in queue higher than {}! Alerting Slack.'.format(alert_time, NUM_TO_ALERT))

                with io.open('settings.json', 'r') as f:
                    settings = json.load(f)
                    message = settings['message'].format(str(count))
                    r_headers = {'Content-type': 'application/json'}

                    try:
                        slack_bot.api_call("chat.postMessage", 
                                            channel=settings['channel'], 
                                            text=message, 
                                            as_user=True)
                    except:
                        req_error = traceback.format_exc()
                        now = str(datetime.now())
                        print(now + ' - Error:\n' + req_error + '\n\n\n')

            time.sleep(180)
        except:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(now + ' - Error:\n' + error_message + '\n\n\n')
            time.sleep(300)
            setup()


if __name__ == '__main__':
    setup()


