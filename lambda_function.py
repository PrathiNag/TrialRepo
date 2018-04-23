import boto3
dynamodb = boto3.client('dynamodb');


def lambda_handler(event, context):
    response= dynamodb.create_table(
    AttributeDefinitions=[{ 'AttributeName' : 'string', 'AttributeType' : 'S'}],
    TableName='string',
    KeySchema=[{'AttributeName' : 'string','KeyType' : 'HASH'}],
    ProvisionedThroughput={'ReadCapacityUnits':1, 'WriteCapacityUnits':2}
    );
    print(response);