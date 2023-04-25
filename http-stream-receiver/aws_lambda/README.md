## AWS Lambda receiver

This code is to serve the case when flespi http stream is pointed to AWS lambda, which parses JSON array and pushes messages to AWS SQS queue.

How to use it with [Python](python) code:
1. create a queue at AWS SQS
2. create AWS python lambda function
3. specify AWS SQS queue as destination for lambda function (this will assign appropriate policies to lambda)
4. use [python code](python/lambda_function). Replace SQS queue URL in the code 
5. make lambda funciton URL public
6. use function URL as URI at http stream configuration

This json can be used as lambda test:

`{"body": "[{\"device.id\":1,\"device.name\":\"Test AWS lambda to SQS\",\"ident\":\"123456789012345\",\"parameter\":\"test1\",\"timestamp\":1681069928},{\"device.id\":1,\"device.name\":\"Test AWS lambda to SQS\",\"ident\":\"123456789012345\",\"parameter\":\"test2\",\"timestamp\":1681069929}]"}
`