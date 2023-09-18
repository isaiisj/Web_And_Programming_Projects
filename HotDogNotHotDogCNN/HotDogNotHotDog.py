import numpy as np
import pandas as pd
import tensorflow as tf
import random
import matplotlib.pyplot as plt
from tensorflow.keras import datasets,layers,models
import tensorflow_datasets as tfds

ds,ds_info = tfds.load('food101',shuffle_files = True,as_supervised=True, with_info = True)
