import os
from pymongo import MongoClient
import numpy as np
import cv2

sample = cv2.imread("C:/Users/GFG0298/Downloads/839314868452.bmp")
client = MongoClient("mongodb://localhost:27017")
db = client["aadharDB"]
finger_data = db["fingerDB"]
doc = {
    "finger": sample.tolist(),
    "Aadhar": "839314868452"
}
# print(type(sample))
finger_data.insert_one(doc)
# print(sample)
# print(np.array(doc["finger"]))
# data = finger_data.find({})
# i = 0
# for dat in data:
#     print(i)
#     i += 1
#     print(np.array((dat["finger"])))
