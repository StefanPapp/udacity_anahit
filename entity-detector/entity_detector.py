import boto3
import json
import argparse
import os

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--text', help='text', required=True)

args = parser.parse_args()


comprehend = boto3.client(service_name='comprehend',
                          region_name=os.environ['AWS_REGION'],
                          aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                          aws_secret_access_key=os.environ['AWS_SECRET_KEY']
                          )

text = args.text

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectEntities\n')

# Create CloudWatchEvents client
cloudwatch_events = boto3.client('events')

# Put an event
response = cloudwatch_events.put_events(
    Entries=[
        {
            'Detail': json.dumps({'text': text }),
            'DetailType': 'entitySubmitted',
            'Resources': [
                'RESOURCE_ARN',
            ],
            'Source': 'detect_entity'
        }
    ]
)
print(response['Entries'])