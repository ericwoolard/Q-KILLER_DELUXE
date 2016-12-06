import praw
import os
import time
import datetime
import traceback

r = praw.Reddit(user_agent='r/subreddit ModQ counter script')

try:
    r.login('USERNAME', 'PASSWORD', disable_warning=True)
except:
    error_message = traceback.format_exc()
    now = str(datetime.datetime.now())
    print(now + ' - Error:\n' + error_message + '\n\n\n')
    time.sleep(300)

while True:
    try:
        subreddit = r.get_subreddit('SUBREDDIT')
        startTime = time.time()

        print('Gathering items in queue...')
        modQueue = subreddit.get_mod_queue()
        count = 0

        for item in modQueue:
            count += 1
        print('Total items in queue: ' + str(count))

        if count >= 15:
            print('Items in queue higher than 15! Alerting Slack.')
            message = '<!here> *Uhh..HELLO?? What are you doing?? THERE ARE {} THINGS IN MODQUEUE...GET TO WORK!*'.format(
                str(count))
            cmd = 'curl https://slack.com/api/chat.postMessage -X POST -d "channel=#CHANNELNAME" -d "text=' \
                  + message + '" -d "username=USERNAME" -d ' \
                              '"token=SLACK_TOKEN_HERE" -d ' \
                              '"icon_emoji=:ICON_NAME:"'
            os.system(cmd)

        elapsedTime = str(round(time.time() - startTime, 2))
        finish = 'Cycle completed in {}s. Waiting for next interval...'.format(elapsedTime)
        print(finish)
        time.sleep(180)
    except:
        error_message = traceback.format_exc()
        now = str(datetime.datetime.now())
        print(now + ' - Error:\n' + error_message + '\n\n\n')
        time.sleep(300)

