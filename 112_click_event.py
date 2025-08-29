import cv2
import yaml
import numpy as np

with open("calibration_matrix_26_9_2024_9h13.yaml", "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

camera_matrix = np.array(data['camera_matrix'])
dist_coeffs = np.array(data['dist_coeff'])
def undistort(frame, camera_matrix, dist_coeffs):
    if camera_matrix is not None and dist_coeffs is not None:
        #frame = cv2.resize(frame, (1920,1080))
        h, w = frame.shape[:2]
        new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (w, h), 1, (w, h))
        frame = cv2.undistort(frame, camera_matrix, dist_coeffs, None, new_camera_matrix)
        x, y, w, h = roi
        frame = frame[y:y+h, x:x+w]
        frame = cv2.resize(frame, (1280,720))
    return frame

points = []
def normalize_coordinates(x, y, width, height):
    return x / width, y / height

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        h, w = params['height'], params['width']
        norm_x, norm_y = normalize_coordinates(x, y, w, h)
        print(f"Coordinates (x, y): ({x}, {y})")
        #print(f"Coordinates (x, y): ({x}, {y}) -> Normalized: ({norm_x:.4f}, {norm_y:.4f})")
        points.append((x, y))


cv2.namedWindow('Video')
video_path = r'D:\Mobile_Robot\YOLOv9_Object_Tracking\data_ext\Camo Recording 2024-07-30 16-27-20.mp4'
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = undistort(frame, camera_matrix, dist_coeffs)
    #h, w = frame.shape[:2]
    #frame = cv2.resize(frame, (1280,720))

    h, w = frame.shape[:2]
    for point in points:
        cv2.circle(frame, point, 1, (0,0,255), -1)

    cv2.imshow('Video', frame)
    cv2.setMouseCallback('Video', click_event, {'width': w, 'height': h})

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
