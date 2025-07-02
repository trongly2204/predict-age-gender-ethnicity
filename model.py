import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from deepface import DeepFace


def predict(image):
    image_np = np.array(image)

    try:
        demography = DeepFace.analyze(image_np, enforce_detection=False)[0]

        age = demography.get('age', 'N/A')

        # Extract the key with highest confidence if gender is a dict
        gender_raw = demography.get('gender', 'N/A')
        if isinstance(gender_raw, dict):
            gender = max(gender_raw, key=gender_raw.get)
        else:
            gender = gender_raw

        ethnicity = demography.get('dominant_race', 'N/A')

    except Exception as e:
        print("DeepFace failed:", str(e))
        age, gender, ethnicity = 'N/A', 'N/A', 'N/A'

    return age, gender, ethnicity
