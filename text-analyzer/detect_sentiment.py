import boto3
import json
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--text', help='text', required=True)

args = parser.parse_args()


comprehend = boto3.client(service_name='comprehend', region_name='eu-central-1')

text = args.text

print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectSentiment\n')