#!/usr/local/bin/python
import sys
import boto3
import os

s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
#        print(bucket.name)

if len(sys.argv) < 2:
    raise ValueError('You must pass in a filename to upload')


bucket="cs-training-data"
path=sys.argv[1]
filename=os.path.basename(path)

print 'Uploading to S3: ' + path

data = open(path, 'rb')
s3.Bucket(bucket).put_object(Key=filename, Body=data)
