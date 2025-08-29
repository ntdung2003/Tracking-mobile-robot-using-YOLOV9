import cv2
import os

# Đọc video
video_path = r'D:\Mobile_Robot\YOLOv9_Object_Tracking\data_ext\Camo Recording 2024-07-30 16-27-20.mp4'
cap = cv2.VideoCapture(video_path)

# Tạo thư mục để lưu các frame
output_folder = r'D:\Mobile_Robot\YOLOv9_Object_Tracking\data_ext\Camo Recording 2024-07-30 16-27-20\frames'
os.makedirs(output_folder, exist_ok=True)

# Lấy thông tin về video
fps = cap.get(cv2.CAP_PROP_FPS)  # Tỷ lệ khung hình (frame rate)
frame_interval = int(fps * 1)

# Đọc và lưu các frame
frame_number = 0
saved_frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Lưu frame nếu nó nằm trong khoảng thời gian yêu cầu
    if frame_number % frame_interval == 0:
        frame_filename = os.path.join(output_folder, f'frame_{saved_frame_number:04d}.png')
        cv2.imwrite(frame_filename, frame)
        saved_frame_number += 1

    frame_number += 1

cap.release()
print(f'Đã lưu {saved_frame_number} frame vào thư mục {output_folder}.')
