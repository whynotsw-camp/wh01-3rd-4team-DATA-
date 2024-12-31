import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col
from pyspark.sql.functions import date_format

# Glue Context 초기화
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Glue DB에서 테이블 로드
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="<GlueDB_name>",  # Glue DB 이름
    table_name="<Glue_table_name>"    # Glue 테이블 이름
)

# DynamicFrame을 DataFrame으로 변환
df = datasource.toDF()

# 데이터 변환 (테이블 스키마에 맞게 처리)
transformed_df = df \
    .withColumn("ip", col("ip")) \
    .withColumn("user_id", col("user_id")) \
    .withColumn("req_type", col("req_type")) \
    .withColumn("content_name", col("content_name")) \
    .withColumn("search_text", col("search_text")) \
    .withColumn("timestamp", date_format(col("timestamp"), "yyyyMMddHHmmss")) \

# 순서 정렬
ordered_df = transformed_df.select(
    "user_id",
    "ip", 
    "req_type", 
    "content_name", 
    "search_text", 
    "timestamp"
)

# DataFrame을 DynamicFrame으로 변환
dynamic_frame = DynamicFrame.fromDF(ordered_df, glueContext, "ordered_data")

# S3로 데이터 저장
glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="s3",
    connection_options={
        "path": "<S3 저장 경로>",  # S3 저장 경로
        "partitionKeys": []  # 파티션 키가 필요하면 설정
    },
    format="csv"  # 저장할 포맷
)

job.commit()
