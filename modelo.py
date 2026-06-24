import os
import numpy as np
import tensorflow as tf
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "modelo", "keras_model.h5")
LABELS_PATH = os.path.join(BASE_DIR, "modelo", "labels.txt")

model = tf.keras.models.load_model(MODEL_PATH, compile=False)

with open(LABELS_PATH, "r", encoding="utf-8") as f:
    labels = [linha.strip() for linha in f.readlines()]

def prever(img):
    imagem = Image.fromarray(img)
    imagem = imagem.resize((224, 224))
    imagem = np.asarray(imagem)
    imagem = (imagem.astype(np.float32) / 127.5) - 1
    imagem = np.expand_dims(imagem, axis=0)
    previsao = model.predict(imagem, verbose=0)
    indice = np.argmax(previsao)
    classe = labels[indice]
    confianca = float(previsao[0][indice])
    return classe, confianca
