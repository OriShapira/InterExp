import boto3
import AMT_Parameters as config

create_hits_in_live = True # false means sandbox
environments = {
        "live": {
            "endpoint": "https://mturk-requester.us-east-1.amazonaws.com",
            "preview": "https://www.mturk.com/mturk/preview",
            "manage": "https://requester.mturk.com/mturk/manageHITs"
        },
        "sandbox": {
            "endpoint": "https://mturk-requester-sandbox.us-east-1.amazonaws.com",
            "preview": "https://workersandbox.mturk.com/mturk/preview",
            "manage": "https://requestersandbox.mturk.com/mturk/manageHITs"
        },
}
mturk_environment = environments["live"] if create_hits_in_live else environments["sandbox"]


def send_message(mturkClient, workerIds, subject, message):
    try:
        response = mturkClient.notify_workers(
            Subject=subject,
            MessageText=message,
            WorkerIds=workerIds
        )
        print('Finished sending: ' + str(response))
    except Exception as e:
        print('Failed to send message:\n\t' + str(e))


# create a client with which to work on MTurk:
mturkClient = boto3.client(
    service_name='mturk',
    region_name='us-east-1',
    endpoint_url=mturk_environment['endpoint'],
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
)
# Test that you can connect to the API by checking your account balance
user_balance = mturkClient.get_account_balance()
# In Sandbox this always returns $10,000. In live, it will be your acutal balance.
print('Your account balance is {}'.format(user_balance['AvailableBalance']))

WORKER_IDS = []
SUBJECT = ''
MESSAGE = """"""
send_message(mturkClient, WORKER_IDS, SUBJECT, MESSAGE)
#print(MESSAGE)
print('DONE')