import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread(r'D:\Mobile_Robot\YOLOv9_Object_Tracking\data_ext\frame_0.jpg')
#image = cv2.resize(image, (1280,720))
# Tạo cửa sổ hiển thị
cv2.imshow('Image', image)

pts1 = np.float32([[135, 63], [1800, 60], [1734, 1032], [207, 1041]])
#pts1 = np.float32([[90, 42], [1200, 40], [1156, 688], [138, 694]])

height, width = image.shape[:2]
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(image, matrix, (width, height))

# Hiển thị kết quả
cv2.imshow('Transformed Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu ảnh kết quả
cv2.imwrite('output_image_1920x1080.jpg', result)
