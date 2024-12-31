import json
import boto3
import pymysql
import csv
import os

# RDS 설정 (환경 변수에서 가져오기)
rds_host = os.environ['RDS_HOST']
db_username = os.environ['DB_USERNAME']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
db_table = os.environ['DB_TABLE']

# S3 클라이언트 생성
s3 = boto3.client('s3')

# Lambda 핸들러 함수
def lambda_handler(event, context):
    try:
        # 전달된 이벤트 로그 출력
        print("Received event:", json.dumps(event))
        
        # 'Records' 키 확인
        if 'Records' not in event:
            raise KeyError("'Records' 키가 이벤트 데이터에 없습니다.")
        
        # S3 이벤트 처리
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        print(f"Bucket: {bucket}, Key: {key}")

    except KeyError as e:
        print(f"KeyError: {e}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"Invalid event format: {str(e)}")
        }
    except Exception as e:
        print(f"Unhandled exception: {e}")
        raise e
        
    # S3에서 파일 다운로드
    download_path = f'/tmp/{key.split("/")[-1]}'
    s3.download_file(bucket, key, download_path)
    
    print(f"Downloading file from S3 bucket '{bucket}', key '{key}'")

    try:
        # MySQL 연결 설정
        connection = pymysql.connect(
            host=rds_host,
            user=db_username,
            password=db_password,
            database=db_name
        )
        print("MySQL 연결 성공")
    except Exception as e:
        print(f"MySQL 연결 실패: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Database connection error: {str(e)}")
        }
    
    try:
        with connection.cursor() as cursor:
            # CSV 파일 읽기
            with open(download_path, 'r') as file:
                csv_reader = csv.reader(file)
                # 첫 번째 행에 헤더가 있다면 다음 줄로 넘어가기
                next(csv_reader)
                for row in csv_reader:
                    # 각 행을 RDS 테이블에 삽입
                    sql = f"""
                    INSERT INTO {db_table} (user_id, ip, req_type, content_name, search_text, timestamp) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(sql, (int(row[0]), row[1], row[2], row[3], row[4], row[5]))
            connection.commit()
            print("데이터 삽입 완료")
    except Exception as e:
        print(f"RDS 데이터 삽입 중 오류 발생: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error inserting into RDS: {str(e)}")
        }
    finally:
        connection.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Data stored successfully in RDS!')
    }
