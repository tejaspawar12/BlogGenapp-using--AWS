import boto3
import botocore.config
import json
from datetime import datetime
import traceback

def blog_generate_using_bedrock(blogtopic: str) -> str:
    # ✅ Proper prompt format for LLaMA 3
    prompt = f"<s>[INST] Write a 200-word blog on the topic: {blogtopic} [/INST]"

    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.7,
        "top_p": 0.9
    }

    try:
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1",
                               config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3}))
        
        response = bedrock.invoke_model(
            body=json.dumps(body),
            modelId="meta.llama3-8b-instruct-v1:0",  # ✅ LLaMA 3 model
            contentType="application/json",
            accept="application/json"
        )

        response_content = response["body"].read()
        response_data = json.loads(response_content)
        print("✅ Raw response from model:", response_data)

        blog_details = response_data.get("generation", "")
        # ✅ Clean unwanted tokens
        blog_details = blog_details.replace("[/INST]", "").replace("<s>", "").strip()
        return blog_details

    except Exception as e:
        print("❌ Error generating blog:")
        traceback.print_exc()
        return ""

def save_blog_details_s3(s3_key, s3_bucket, generate_blog):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)
        print(f"✅ Blog saved to S3 → s3://{s3_bucket}/{s3_key}")
    except Exception as e:
        print("❌ Error saving blog to S3:")
        traceback.print_exc()

def lambda_handler(event, context):
    try:
        print("🚀 Lambda triggered")
        event = json.loads(event['body'])
        blogtopic = event['blog_topic']
        print(f"📝 Topic: {blogtopic}")

        generate_blog = blog_generate_using_bedrock(blogtopic=blogtopic)

        if generate_blog:
            current_time = datetime.now().strftime('%H%M%S')
            s3_key = f"blog-output/{current_time}.txt"
            s3_bucket = 'awsbedrockdemofirst'  # ✅ Update to your correct bucket
            save_blog_details_s3(s3_key, s3_bucket, generate_blog)
        else:
            print("⚠️ No blog was generated")

        return {
            'statusCode': 200,
            'body': json.dumps('Blog Generation is completed')
        }

    except Exception as e:
        print("❌ Lambda Handler Error:")
        traceback.print_exc()
        return {
            'statusCode': 500,
            'body': json.dumps('Internal Server Error')
        }
