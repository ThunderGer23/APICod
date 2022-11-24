from tensorflow_hub import hub
import tensorflow_text as text
from tensorflow import keras

new_model = keras.models.load_model(
    ('Cod_Red.h5'),
    custome_objects = {'KerasLayer': hub.KerasLayer}
)

