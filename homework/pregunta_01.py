# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


import os
import zipfile
import pandas as pd


def pregunta_01():
    import os

    input_zip_path = "files/input.zip"
    extract_path = "files/input"
    output_path = "files/output"

    # Crear carpeta de salida si no existe
    os.makedirs(output_path, exist_ok=True)

    # Descomprimir input.zip
    with zipfile.ZipFile(input_zip_path, 'r') as zip_ref:
        zip_ref.extractall("files")

    def build_dataset(split):
        data = []
        base_path = os.path.join(extract_path, split)
        for sentiment in ["positive", "negative", "neutral"]:
            sentiment_path = os.path.join(base_path, sentiment)
            for filename in os.listdir(sentiment_path):
                file_path = os.path.join(sentiment_path, filename)
                with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                    phrase = f.read().strip()
                    data.append({"phrase": phrase, "target": sentiment})
        return pd.DataFrame(data)

    # Construir y guardar train_dataset
    train_df = build_dataset("train")
    train_df.to_csv(os.path.join(output_path, "train_dataset.csv"), index=False)

    # Construir y guardar test_dataset
    test_df = build_dataset("test")
    test_df.to_csv(os.path.join(output_path, "test_dataset.csv"), index=False)
