import pickle
import seaborn as sns
import pandas as pd # Import Pandas for data manipulation using dataframes
import numpy as np # Import Numpy for data statistical analysis
import matplotlib.pyplot as plt # Import matplotlib for data visualisation
import random


# The pickle module implements binary protocols for serializing and de-serializing a Python object structure.
with open("C:/Users/siddhk/Downloads/P74-Project-5/Project 5/traffic-signs-data/train.p", mode='rb') as training_data:
    train = pickle.load(training_data)
with open("C:/Users/siddhk/Downloads/P74-Project-5/Project 5/traffic-signs-data/valid.p", mode='rb') as validation_data:
    valid = pickle.load(validation_data)
with open("C:/Users/siddhk/Downloads/P74-Project-5/Project 5/traffic-signs-data/test.p", mode='rb') as testing_data:
    test = pickle.load(testing_data)


print(train['features'])