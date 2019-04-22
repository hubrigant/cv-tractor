import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Load a color image in grayscale
img = cv.imread('training/0692340_versatile-tractor-1150.jpeg', 0)

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)

