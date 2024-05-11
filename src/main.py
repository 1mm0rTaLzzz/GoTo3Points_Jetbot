import cv2
from cv2 import aruco
from calibration.camera_props import *

cap = cv2.VideoCapture("rtsp://root:pass@192.168.0.94/mjpeg")

dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()
detector = aruco.ArucoDetector(dictionary, parameters)
tvec_id4 = np.array([0, 0, 0])
tvec_id1 = np.array([0, 0, 0])
rvec_id5 = np.array([0, 0, 0])
rvec_id1 = np.array([0, 0, 0])
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    corners, ids, rejectedImgPoints = detector.detectMarkers(gray)

    counter = 0
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
    if corners:
        for c in corners:
            if ids[counter] == 7:
                rvec, tvec, _ = aruco.estimatePoseSingleMarkers(c, 0.1, camera_matrix, distortion_coefficient)
                frame = cv2.drawFrameAxes(frame_markers, camera_matrix, distortion_coefficient, rvec, tvec, 0.1, 2)
                tvec_id5 = tvec
                rvec_id5 = rvec
            if ids[counter] == 1:
                rvec, tvec, _ = aruco.estimatePoseSingleMarkers(c, 0.1, camera_matrix, distortion_coefficient)
                frame = cv2.drawFrameAxes(frame_markers, camera_matrix, distortion_coefficient, rvec, tvec, 0.1, 2)
                tvec_id1 = tvec
                rvec_id1 = rvec
            counter += 1
    if not ret:
        break
    print('id5', tvec_id5, rvec_id5 * 180 / np.pi)
    print('id1', tvec_id1, rvec_id1 * 180 / np.pi)
    # if np.abs(rvec_id5[0][0][0] - rvec_id1[0][0][0]) < 1 and np.abs(rvec_id5[0][0][1] - rvec_id1[0][0][1]) < 1:
    #     print('match')
    # distance = ((tvec_id4[0][0][0] - tvec_id0[0][0][0]) ** 2 + (tvec_id4[0][0][1] - tvec_id0[0][0][1]) ** 2) ** 0.5
    # print(distance)
    cv2.imshow('Video Stream', frame)

    # Для остановки воспроизведения нажмите клавишу "q"Po
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
