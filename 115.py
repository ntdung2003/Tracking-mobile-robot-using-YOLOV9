import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread(r'D:\Mobile_Robot\YOLOv9_Object_Tracking\data_ext\image\WIN_20240711_15_31_07_Pro.jpg')


# Tạo cửa sổ hiển thị
cv2.imshow('Image', image)

# Danh sách lưu trữ các điểm góc
points = []

# Hàm callback để lấy các điểm góc từ chuột
def get_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(image, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow('Image', image)

cv2.setMouseCallback('Image', get_points)

# Chờ người dùng chọn đủ 4 điểm
while len(points) < 4:
    cv2.waitKey(1)

cv2.destroyAllWindows()

# Chuyển đổi các điểm thành dạng numpy array
pts1 = np.float32(points)

# Xác định vị trí mới của các điểm đó (một hình chữ nhật chuẩn)
# Kích thước của hình chữ nhật mới sẽ bằng kích thước của ảnh gốc
height, width = image.shape[:2]
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

# Tính toán ma trận biến đổi phối cảnh
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Áp dụng biến đổi phối cảnh
result = cv2.warpPerspective(image, matrix, (width, height))

# Hiển thị kết quả
cv2.imshow('Transformed Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu ảnh kết quả
cv2.imwrite('output_image.jpg', result)