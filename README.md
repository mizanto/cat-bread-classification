# Cat Breed Classifier Project

### Problem Description
This project focuses on developing a machine learning model capable of classifying images of cats into distinct breeds. The aim is to create an accurate and reliable model that can analyze an image and predict the cat's breed from a predefined list. This model has practical applications in various fields, including animal welfare, pet care, and digital content creation. By leveraging advanced image processing and machine learning techniques, this project demonstrates the potential of AI in enhancing our understanding and interaction with domestic animals.

### Dataset
The dataset used for this project is the [Cat Breeds Dataset](https://www.kaggle.com/datasets/doctrinek/catbreedsrefined-7k) from Kaggle. 

### Preparation
1. Download folders with images from https://drive.google.com/drive/folders/1X1fpKq9ykybmHSm7Rh8vWxY3xlw9JKzc?usp=drive_link
2. Unzip folders from `dataset.zip`
3. Copy folders to `dataset/`

Now you should have the following structure:
```
dataset/
    original/
        ...
    cleaned/
        ...
    lite/
        ...
```

### Model
Models are to big to upload to GitHub. You can download it from https://drive.google.com/drive/folders/1lE-x7aqGtZucwp4xJPXLX6e2YlYKEszl?usp=drive_link

### Key Steps
* Data Exploration: Initial dataset analysis using Jupyter Notebook (exploration.ipynb).
* Model Preparation: Preparation of code for production deployment in Jupyter Notebook (prepare_to_prod.ipynb).
* Lambda Function: Deployment code (lambda.py) for AWS Lambda, using TensorFlow Lite for model inference.
* Testing: A script (test.py) to test the deployed model endpoint.
* Docker Image: Dockerfile for building the AWS Lambda compatible image.
* AWS Deployment: Setup of AWS Lambda function and API Gateway.

### Repository Structure
* `dataset/`: Dataset directories (original, cleaned, lite versions)
* `models/`: Saved model files
* `notebooks/`: Jupyter notebooks for exploration and preparation
* `src/`: Source code including the lambda function
* `dockerfile`: Instructions for Docker image creation
* `README.md`: Information and instructions about the project

### Building Docker Image

Build the Docker image using the command:
    
```bash
docker build -t cat-breed-classifier .
```

### Uploading to AWS ECR

1. Create Repository: In AWS ECR, create a new repository for the Docker image.
2. Authenticate Docker: Authenticate your Docker client to the Amazon ECR registry.
3. Tag Image: Tag your Docker image to match your repository.
```bash
docker tag cats-model [aws_account_id].dkr.ecr.[region].amazonaws.com/cats-model
```
4. Push Image: Push the Docker image to your newly created AWS ECR repository.
```bash
docker push [aws_account_id].dkr.ecr.[region].amazonaws.com/cats-model
```

This process builds a Docker image compatible with AWS Lambda, uploads it to AWS ECR, and makes it available for deployment.

### How to Test
You can test the deployed model endpoint using the following curl command:

```bash
curl -X POST https://z181ex0uw6.execute-api.eu-central-1.amazonaws.com/prod/predict \
    -H "Content-Type: application/json" \
    -d '{"url":"https://www.katdootje.nl/wp-content/uploads/Orange-Maine-Coon.webp"}'
```
This sends a POST request to the model endpoint with an image URL and returns the model's prediction.