import cv2
import numpy as np
from camera_props import *
# def undistort_frame(frame, camera_matrix, dist_coeffs):
#     h, w = frame.shape[:2]
#     new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (w, h), 1, (w, h))
#     undistorted_frame = cv2.undistort(frame, camera_matrix, dist_coeffs, None, new_camera_matrix)
#     x, y, w, h = roi
#     undistorted_frame = undistorted_frame[y:y+h, x:x+w]
#     return undistorted_frame
#
# # Загрузка параметров калибровки камеры
# camera_matrix = camera_matrix
# dist_coeffs = distortion_coefficient
#
# cap = cv2.VideoCapture("rtsp://root:pass@192.168.0.94/mjpeg")  # Используйте свой источник видеопотока, если это не камера
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     undistorted_frame = undistort_frame(frame, camera_matrix, dist_coeffs)
#
#     cv2.imshow('Original', frame)
#     cv2.imshow('Undistorted', undistorted_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

cap = cv2.VideoCapture("rtsp://root:pass@192.168.0.94/mjpeg")

while cap.isOpened():
    ret, frame = cap.read()
    # cv.imshow('Webcam Distorted', frame)
    print("we are reading frames")

    # Grab Frames and attempt to undistort
    h, w = frame.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coefficient, (w, h), 1, (w, h))
    # undistort
    dst = cv2.undistort(frame, camera_matrix, distortion_coefficient, None, newcameramtx)
    print("Undistorting")

    # crop the image
    x, y, w, h = roi
    print("Cropped the image")

    dst = dst[y:y + h, x:x + w]
    cv2.imshow('UNDISTORTED', dst)

    # End loop when hit d
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break