
# Summary

Serverless Cloud Document Reader is a Django application that is deployed in AWS Lambda 

The linked repo contains a set of samples in different programming languages showing how to create a simple client application using API V1 for processing image with the specified parameters and exporting the result.

For the code created, Find the [Repository](https://www.ocrsdk.com/documentation/api-reference/process-image-method/) in my [Github](https://www.ocrsdk.com/documentation/) account.


## Features

- Text recognition
  - full-page and zonal OCR (printed text) for 200+ languages
  - ICR (hand-printed text)
- Document conversion
  - convert image/PDF to searchable PDF, PDF/A and Microsoft Word, Excel, PowerPoint
- Data extraction
  - Receipt recognition
  - Barcode recognition 
  - Business card recognition
  - ID recognition (MRZ)

## Quick start guide

# AWS configuration

1. [Register](https://portal.aws.amazon.com/billing/signup#/start) for an AWS account,AWS Accounts Include 12 Months of Free Tier Access.
2. [Download](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html) and setup the AWS cli.
3. Create an IAM User withe the [required](https://www.codingforentrepreneurs.com/blog/aws-iam-user-role-policies-zappa-serverless-python) policies for the lambda function.
3. Login to your AWS account through the cli.


# Azure configuration
Create an account in Microsoft Azure Cloud Platform
1. [Register](https://azure.microsoft.com/auth/signin/?loginProvider=Microsoft&redirectUri=%2Fen-in%2Ffree%2F) an account in Microsoft Azure Cloud Platform.
2. [Create](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.CognitiveServices%2Faccounts)a Cognitive Services resource.
3. Make note of the Api Key and the endpoints which are located under "Keys and Endpoint"-> 

# Setting up a Virtual Environment

Zappa requires a Virtual Evironment to package the required python libraries into the S3 storage. to set up your virtual environment run the following commands.

```
mkdir venv
cd venv
virtualenv env
source env/bin/activate
pip install django zappa

```
# Djagno Configuration
Download the Django application from my GitHub repository [here.]()

# Zappa Configuration

1.Make sure your virtual environment is active and run

```
Zappa init
```
you should get this message:
```
███████╗ █████╗ ██████╗ ██████╗  █████╗
╚══███╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
  ███╔╝ ███████║██████╔╝██████╔╝███████║
 ███╔╝  ██╔══██║██╔═══╝ ██╔═══╝ ██╔══██║
███████╗██║  ██║██║     ██║     ██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝
Welcome to Zappa!
Zappa is a system for running server-less Python web applications on AWS Lambda and AWS API Gateway.
This `init` command will help you create and configure your new Zappa deployment.
Let's get started!
Your Zappa configuration can support multiple production stages, like 'dev', 'staging', and 'production'.
What do you want to call this environment (default 'dev'):
```
 Zappa asks you to define which env you want to configure, as it’s able to handle multiple envs. stick with the default ‘dev’.




## License
This project was developed by Steve Jefferson and is released under the MIT License.


