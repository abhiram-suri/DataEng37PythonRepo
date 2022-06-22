import boto3
from pprint import pprint

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# bucket_list = s3_client.list_buckets()
# # pprint(bucket_list, sort_dicts=False)
#
# for bucket in bucket_list['Buckets']:
#     print(bucket['Name'])

bucket_name = 'data-eng-resources'
paginator = s3_client.get_paginator('list_objects_v2')
bucket_contents = paginator.paginate(Bucket=bucket_name)
#
# pprint(bucket_contents, sort_dicts=False)
for bucket in bucket_contents:
    for b in bucket['Contents']:
        print(b['Key'])



