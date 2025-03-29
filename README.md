# 📝 Serverless Blog Generator using AWS Bedrock, Lambda & S3

This project is a **serverless blog generation system** powered by **Amazon Bedrock**, specifically utilizing the **Meta Llama3 8B Instruct LLM**, to dynamically generate 200-word blog posts based on provided topics.

The solution integrates various AWS services such as **AWS Lambda, Bedrock, Amazon S3, IAM, Amazon CloudWatch**, and **API Gateway**, with testing facilitated via **Postman**. It demonstrates practical implementation of Generative AI within the AWS ecosystem.

---

## 🚀 Tech Stack

- **Amazon Bedrock**: LLM inference using Meta Llama3 8B Instruct model.
- **AWS Lambda**: Serverless Python function orchestrating workflow.
- **Amazon S3**: Persistent storage of generated blog content.
- **AWS API Gateway**: REST API trigger endpoint.
- **IAM (Identity and Access Management)**: Secure, granular permission management.
- **Amazon CloudWatch**: Real-time logging and monitoring.
- **Postman**: API testing tool.

---

## 🛠️ Architecture Overview

```
Client (Postman) → API Gateway → Lambda Function
                             ↓
                      Amazon Bedrock (LLM)
                             ↓
                  Generated Blog → Amazon S3
                             ↓
                      Logs → CloudWatch
```

---

## 📆 Features

- Accepts any blog topic via POST request.
- Generates content using LLM (Meta Llama3 via Bedrock).
- Automatically stores generated blog content in Amazon S3.
- Logs all operations in CloudWatch.
- Secure access managed via IAM.

---

## 🔄 How It Works

### 1. Invoke API via Postman

**Request:**

- Method: **POST**
- URL: `https://<your-api-gateway-url>/dev/blog-generation`
- Headers:
  ```
  Content-Type: application/json
  ```
- Body:
  ```json
  {
    "blog_topic": "The impact of AI in finance"
  }
  ```

### 2. Lambda Workflow

- Parses blog topic from request.
- Sends structured prompt to the Bedrock model.
- Receives and processes the generated output.
- Saves output to:
  ```
  s3://<your-bucket>/blog-output/<timestamp>.txt
  ```
- Logs each step to Amazon CloudWatch.

---

## 🧐 Model Used

- **Model ID:** `meta.llama3-8b-instruct-v1:0`
- **Provider:** Meta via Amazon Bedrock
- **Prompt Template:**
  ```
  <s>[INST] Write a 200-word blog on the topic: {topic} [/INST]
  ```

---

## 🔐 IAM Policy Notes

Attach the following IAM policy to your Lambda role for required access:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "s3:PutObject"
      ],
      "Resource": "*"
    }
  ]
}
```

> ✅ **Security Best Practice**: Restrict resources using specific ARNs.

---

## 📂 Sample Output

**Example S3 Path:**
```
s3://awsbedrockdemofirst/blog-output/201522.txt
```

**Sample Blog Content:**
```
The impact of AI in finance is rapidly transforming how institutions make decisions...
```

---

## 📊 Monitoring

All Lambda invocations and related errors are logged to **Amazon CloudWatch Logs**, facilitating easy debugging and performance monitoring.

---

## ✅ Setup Instructions

Follow these steps to set up the project in your AWS account:

1. Clone this repository.
2. Deploy the Lambda function with an appropriate IAM role.
3. Create an Amazon S3 bucket (e.g., `awsbedrockdemofirst`).
4. Enable Bedrock model access (`meta.llama3-8b-instruct-v1:0`).
5. Configure API Gateway to trigger your Lambda function.
6. Test the system using Postman as shown above.

---

## 📌 Useful Links

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)
- [API Gateway Documentation](https://docs.aws.amazon.com/apigateway/)
- [IAM Permissions Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Postman](https://www.postman.com/)

---

## 👋 About

This project was developed as part of **Ud StudyAide's initiative** to explore Generative AI using AWS Bedrock and serverless cloud infrastructure.

**Author:** Tejas Pawar  
**Program:** M.S. Data Science, University of Delaware  
[Connect with me on LinkedIn](https://www.linkedin.com) *(Add your profile link)*

⭐ **Feel free to star this repository or provide feedback!**
