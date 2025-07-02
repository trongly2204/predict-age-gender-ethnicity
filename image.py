import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def import_image(image_name):
    image = Image.open(image_name)
    return image