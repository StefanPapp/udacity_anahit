import boto3
import json
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--text', help='text', required=True)

args = parser.parse_args()


comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')

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
            'DetailType': 'sentimentSubmitted',
            'Resources': [
                'RESOURCE_ARN',
            ],
            'Source': 'detect_sentiment'
        }
    ]
)
print(response['Entries'])