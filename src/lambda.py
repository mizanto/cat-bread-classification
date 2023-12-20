import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor('xception', target_size=(150, 150))

interpreter = tflite.Interpreter(model_path='cats.tflite')
interpreter.allocate_tensors()

index_input = interpreter.get_input_details()[0]['index']
index_output = interpreter.get_output_details()[0]['index']

classes = [
    'Abyssinian',
    'American Curl',
    'Bengal',
    'British Shorthair',
    'Maine Coon',
    'Norwegian Forest',
    'Persian',
    'Russian Blue',
    'Siamese',
    'Sphynx'
]


def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(index_input, X)
    interpreter.invoke()
    pred_lite = interpreter.get_tensor(index_output)

    float_pred = pred_lite[0].tolist()

    return dict(zip(classes, float_pred))


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result
