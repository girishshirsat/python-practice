import numpy as np
import cv2
import matplotlib.pyplot as plt

arr=np.array([1,2,3,4])
print(arr[0:])

#arr1=np.array([[1,2,3,4],12])
#print(arr1)
print("============================================")
arr1=np.array([[1,2,3,4],[12,2,8,9]])
#print(arr1)
print("============================================")
arr1=np.array([[1,2,3,5],[12,2,8,9]])
print(arr1)
print("============================================")

a=cv2.imread('download.jpeg',0)
cv2.imshow(a)