import tensorflow as tf
model = tf.keras.models.load_model("modelo/modelo.salvo")
model.save("modelo/model.keras")
