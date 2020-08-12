import boto3
import json
import os
import time
import shutil

comprehend = boto3.client(service_name='comprehend',
                          region_name=os.environ['AWS_REGION'],
                          aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                          aws_secret_access_key=os.environ['AWS_SECRET_KEY']
                          )

while True:
    for file in os.listdir(os.environ['LANDING_ZONE']):
        if file.endswith("txt"):
            abs_path = os.path.join(os.environ['LANDING_ZONE'], file)
            file_handler = open(abs_path, "r+")
            text = file_handler.read()
            cloudwatch_events = boto3.client('events')
            response = cloudwatch_events.put_events(
            Entries=[
               {
                 'Detail': json.dumps({'text': text }),
                 'DetailType': 'sentimentsSubmitted',
                 'Resources': [
                     'RESOURCE_ARN',
                 ],
                 'Source': 'sentiments_detector'
               }
             ]
            )
            print(response['Entries'])
            result = json.dumps(comprehend.detect_sentiments(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
            shutil.move(abs_path, os.path.join(os.environ['COMPLETE_ZONE'], file))

            client = boto3.client('sns', region_name=os.environ['AWS_REGION'],
                                         aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                                         aws_secret_access_key=os.environ['AWS_SECRET_KEY'])
            response = client.publish(
                TargetArn=os.environ['ARN'],
                Message=json.dumps({'default': json.dumps(result)}),
                Subject='sentiments recognition',
                MessageStructure='json'
            )
            time.sleep(5)
