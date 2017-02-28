import praw
import os
import time
from datetime import datetime
import traceback
import requests


def setup():
    try:
        reddit = praw.Reddit(client_id='CLIENT_ID',
                             client_secret='CLIENT_SECRET',
                             password='PASSWORD',
                             user_agent='ModQ counter script by /u/zebradolphin5',
                             username='USERNAME')
        subreddit = reddit.subreddit('SUBREDDIT')
        getCount(subreddit)
    except:
        error_message = traceback.format_exc()
        now = str(datetime.now())
        print(now + ' - Error:\n' + error_message + '\n\n\n')
        time.sleep(300)
        setup()


def getCount(subreddit):
    while True:
        try:
            startTime = time.time()

            print('Gathering items in queue...')
            modQueue = subreddit.get_mod_queue()
            count = 0

            for item in modQueue:
                count += 1
            print('Total items in queue: ' + str(count))

            if count >= 15:
                alertTime = str(datetime.now())
                print(alertTime + 'Items in queue higher than 15! Alerting Slack.')
                message = '*Uhh..HELLO?? What are you doing?? THERE ARE {} THINGS IN MODQUEUE...GET TO WORK!* \n<http://www.reddit.com/r/mod/about/modqueue>'.format(str(count))
                body = {'text': '<!here> *Q-KILLER* \n{}'.format(message), 'channel': '#general', 'username': 'BOT', 'icon_emoji': ':middle_finger:'}
                r_headers = {'Content-type': 'application/json'}

                try:
                    r = requests.post('YOUR_WEBHOOK_URL', json=body, headers=r_headers)

                    if r.status_code != 200:
                        now = str(datetime.now())
                        print(now + ' - Error:\n' + 'Received HTTP Response other than 200' + '\n\n\n')

                except requests.exceptions.RequestException:
                    req_error = traceback.format_exc()
                    now = str(datetime.now())
                    print(now + ' - Error:\n' + req_error + '\n\n\n')

            elapsedTime = str(round(time.time() - startTime, 2))
            finish = 'Cycle completed in {}s. \nWaiting for next interval...'.format(elapsedTime)
            print(finish)
            time.sleep(180)
        except:
            error_message = traceback.format_exc()
            now = str(datetime.now())
            print(now + ' - Error:\n' + error_message + '\n\n\n')
            time.sleep(300)
            setup()


if __name__ == '__main__':
    setup()
