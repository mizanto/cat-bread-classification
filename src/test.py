import requests

url = 'https://z181ex0uw6.execute-api.eu-central-1.amazonaws.com/prod/predict'

body = {
    'url': 'https://www.katdootje.nl/wp-content/uploads/Orange-Maine-Coon.webp'
}

result = requests.post(url, json=body).json()
print(result)
