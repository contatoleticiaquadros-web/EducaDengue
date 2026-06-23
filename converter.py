import tensorflow as tf
model = tf.keras.models.load_model("modelo/keras_model.h5", compile=False)
model.save("modelo/keras_model.keras")
