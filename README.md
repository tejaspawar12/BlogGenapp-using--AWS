# BlogGenapp-using--AWS
# 📝 Serverless Blog Generator using AWS Bedrock, Lambda & S3

This project is a **serverless blog generation system** powered by **Amazon Bedrock**, which uses **LLMs (Meta Llama3 8B Instruct)** to dynamically generate 200-word blog posts on any topic.

The system is built using **AWS Lambda, Bedrock, S3, IAM, CloudWatch**, and **API Gateway**, with testing via **Postman**. It demonstrates the power of Generative AI integration within the AWS cloud ecosystem.

---

## 🚀 Tech Stack

- **Amazon Bedrock** – LLM inference (Llama3 8B Instruct)
- **AWS Lambda** – Serverless Python function to orchestrate the flow
- **Amazon S3** – Stores generated blog content as `.txt` files
- **Amazon API Gateway** – Exposes a RESTful endpoint to trigger blog generation
- **IAM Roles & Policies** – Granular permissions to enable secure access
- **Amazon CloudWatch** – Logs Lambda execution and debugging info
- **Postman** – Used for testing REST API

---

## 🛠️ Architecture Overview

```text
Client (Postman) → API Gateway → Lambda Function
                             ↓
                      Amazon Bedrock (LLM)
                             ↓
                  Generated Blog → Amazon S3
                             ↓
                      Logs → CloudWatch


# 📆 Features

- Accepts any blog topic via **POST** request
- Generates content using **LLM (Meta Llama3 via Bedrock)**
- Automatically stores generated blog in **Amazon S3**
- Logs the generation and storage process in **CloudWatch**
- **IAM-managed** secure access across all services

---



