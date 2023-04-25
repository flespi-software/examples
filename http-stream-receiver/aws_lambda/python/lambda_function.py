import json
import boto3

# Initialize SQS client
sqs = boto3.client('sqs')

# Get URL of SQS queue
queue_url = '<YOUR-QUEUE-URL-HERE>' # example: 'https://sqs.<AWS-REGION>.amazonaws.com/<ACCOUNT-ID>/<QUEUE-NAME>'

def lambda_handler(event, context):
    try:
        # Parse JSON payload from API Gateway event
        messages = json.loads(event['body'])

        # Split the messages into batches of up to 10 messages each
        message_batches = [messages[i:i+10] for i in range(0, len(messages), 10)]

        # Send each batch of messages to the SQS queue
        for batch in message_batches:
            # Create a list of message entries for the batch
            message_entries = []
            for i, message in enumerate(batch):
                message_entry = {
                    'Id': str(i),
                    'MessageBody': json.dumps(message)
                }
                message_entries.append(message_entry)
            # Send the batch of messages to the SQS queue
            response = sqs.send_message_batch(
                QueueUrl=queue_url,
                Entries=message_entries
            )

        # Return success response to API Gateway
        return {'statusCode': 200}
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e), 'body': event})
        }
