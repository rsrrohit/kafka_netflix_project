from kafka import KafkaConsumer
import json
import boto3
consumer = KafkaConsumer('netflix_data')

#dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
dynamodb = boto3.resource('dynamodb')
for message in consumer:
    #print(message.value)
    dataPoint = json.loads(message.value)
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    response = table.put_item(Item=dataPoint)
    print("Response from dynamodb: ", response)
