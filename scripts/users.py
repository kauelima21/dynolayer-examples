import boto3


table_name = 'users'
key_schema = [
    {
        'AttributeName': 'id',
        'KeyType': 'HASH'
    },
]


attribute_definitions = [
    {
        'AttributeName': 'id',
        'AttributeType': 'S'
    },
]


provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}


dynamodb = boto3.client('dynamodb', region_name='sa-east-1', endpoint_url='http://localhost:8000')


response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=attribute_definitions,
    ProvisionedThroughput=provisioned_throughput,
)


table_description = dynamodb.describe_table(TableName=table_name)
print("Status da criação da tabela:", table_description['Table']['TableStatus'])
