import os
import cv2
import cv2 as cv
import imutils
import numpy as np
from imutils.object_detection import non_max_suppression

directory = 'C:\\Users\\Jakub\\Desktop\\pythonProject\\static'

input_dir = 'NoRecognition'
output_dir = 'Recognition'

def HOGpersonDetector(img_name: str):
    image = cv.imread(img_name)
    image = imutils.resize(image, width=min(800, image.shape[1]))

    hog = cv.HOGDescriptor()
    hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

    (regions, weights) = hog.detectMultiScale(image,
                                              winStride=(8, 8),
                                              padding=(16, 16),
                                              scale=1.05)

    regions = np.array([[x, y, x + w, y + h] for (x, y, w, h) in regions])
    pick = non_max_suppression(regions, probs=None, overlapThresh=0.8)

    people_at_photo = 0

    for (xA, yA, xB, yB) in pick:
        cv.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
        people_at_photo += 1

    cv.putText(image, "People at photo: " + str(people_at_photo), (30, 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    cv.imshow("Result", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv2.imwrite