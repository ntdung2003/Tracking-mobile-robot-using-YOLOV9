import cv2
import os
import numpy as np
import yaml

# Đọc ma trận hiệu chỉnh từ file YAML
with open("calibration_matrix_26_9_2024_9h13.yaml", "r") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
camera_matrix = np.array(data['camera_matrix'])
dist_coeffs = np.array(data['dist_coeff'])

# Hàm hiệu chỉnh ảnh
def undistort(frame, camera_matrix, dist_coeffs):
    if camera_matrix is not None and dist_coeffs is not None:
        frame = cv2.resize(frame, (1280, 720))
        h, w = frame.shape[:2]
        new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (w, h), 1, (w, h))
        frame = cv2.undistort(frame, camera_matrix, dist_coeffs, None, new_camera_matrix)
        x, y, w, h = roi
        frame = frame[y:y+h, x:x+w]
        frame = cv2.resize(frame, (1280, 720))
    return frame

# Đọc ảnh bản đồ và hiệu chỉnh
map_image_path = r'D:\Mobile_Robot\YOLOv9_Object_Tracking\image_output_calib_28_9_2024_ROI.jpg'
map_image = cv2.imread(map_image_path)
map_image = cv2.convertScaleAbs(map_image, alpha=1, beta=-55)
#map_image = undistort(map_image, camera_matrix, dist_coeffs)

# Đọc dữ liệu từ file .txt
txt_file_path = r'D:\Mobile_Robot\YOLOv9_Object_Tracking\28_9_2024\exp17_28_9_2024\pixel.txt'
with open(txt_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split()
        
        # Đảm bảo rằng dòng có đủ 3 giá trị
        if len(parts) == 3:
            obj_id = int(parts[0])
            cx = float(parts[1])
            cy = float(parts[2])
            center_x = int(cx)
            center_y = int(cy)
            
            cv2.circle(map_image, (center_x, center_y), radius=1, color=(0, 0, 255), thickness=-1)
            """
            marker_type = cv2.MARKER_STAR  # cv2.MARKER_TILTED_CROSS, cv2.MARKER_STAR, cv2.MARKER_DIAMOND, vv.
            marker_size = 2
            cv2.drawMarker(map_image, (center_x, center_y), color=(0, 0, 255), markerType=marker_type, markerSize=marker_size, thickness=1)
            """
# Hiển thị và lưu ảnh kết quả
cv2.imshow('Map with Center Points', map_image)
#map_image = cv2.resize(map_image, (1920, 1080))
cv2.waitKey(0)
cv2.destroyAllWindows()

output_path = r'D:\Mobile_Robot\YOLOv9_Object_Tracking\data_ext\output_image_28_9_2024_15h04.png'
cv2.imwrite(output_path, map_image)
