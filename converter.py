import tensorflow as tf

model = tf.keras.models.load_model("modelo/model.savedmodel")
model.save("modelo/keras_model.h5")
