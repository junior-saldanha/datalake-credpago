import boto3
from datetime import datetime

sageclient = boto3.client('sagemaker', region_name='sa-east-1')
sagemaker_role='arn:aws:iam::127012818163:role/service-role/AmazonSageMaker-ExecutionRole-20210518T105032'

def handler(event, context):
    
    process_job_arn = sageclient.create_processing_job(
        ProcessingJobName= f"rais2020-extraction-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}",
        ProcessingOutputConfig={
            'Outputs': [
                {
                    'OutputName': 'rais',
                    'S3Output': {
                        'S3Uri': 's3://cp-datalake/dms/',
                        'LocalPath': '/opt/ml/processing/output/datalake',
                        'S3UploadMode': 'EndOfJob'
                    }
                },
            ]
        },
        ProcessingResources={
            'ClusterConfig': {
                'InstanceCount': 1,
                'InstanceType': 'ml.m5.xlarge',
                'VolumeSizeInGB': 50,

            }
        },
        AppSpecification={
            'ImageUri': '127012818163.dkr.ecr.sa-east-1.amazonaws.com/datalake:latest'
        },
        RoleArn=sagemaker_role
    )

    return {
        'statusCode': 200,
        'body': f"Started job {process_job_arn['ProcessingJobArn']}"
    }
