
#importing the libraries
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPool2D
from keras.datasets import mnist
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt


#Load the data and split it into train and test 
(X_train, y_train), (X_test, y_test) = mnist.load_data()


#Get the image shape
print(X_train.shape)
print(X_test.shape)

