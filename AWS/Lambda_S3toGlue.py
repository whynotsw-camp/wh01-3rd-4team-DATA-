import json
import boto3
import base64

# AWS 클라이언트 설정
s3_client = boto3.client('s3')
glue_client = boto3.client('glue')

# Glue 크롤러 이름 (사전에 생성해 두어야 함)
CRAWLER_NAME = '<crawler_name>'

# Lambda 핸들러 함수
def lambda_handler(event, context):
    # 이벤트에서 S3 버킷 이름과 객체 키를 추출합니다.
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    print(f'New file {object_key} uploaded to bucket {bucket_name}')

    # Glue 크롤러 실행
    try:
        response = glue_client.start_crawler(Name=CRAWLER_NAME)
        print(f'Successfully started Glue crawler: s3Crawler')
    except glue_client.exceptions.CrawlerRunningException:
        print(f'Glue crawler s3Crawler is already running.')
    except Exception as e:
        print(f'Error starting Glue crawler: {str(e)}')
        raise

    return {
        'statusCode': 200,
        'body': json.dumps('Glue crawler started successfully')
    }
