FROM public.ecr.aws/lambda/python:3.11

RUN pip install --upgrade pip
RUN pip install keras_image_helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp311-cp311-linux_x86_64.whl

COPY models/cats.tflite .
COPY src/lambda.py .

CMD ["lambda.lambda_handler"]