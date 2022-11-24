import tensorflow_hub as hub
import tensorflow_text as text
from tensorflow import keras

new_model = keras.models.load_model(
    ('Cod_Red.h5'),
    custom_objects = {'KerasLayer': hub.KerasLayer}
)

