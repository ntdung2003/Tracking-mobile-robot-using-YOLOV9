import cv2
import numpy as np

def draw_grid(image, grid_size, origin):
    """
    Vẽ lưới lên bức ảnh với gốc tọa độ tại vị trí bất kỳ.
    
    :param image: Ảnh gốc
    :param grid_size: Kích thước ô lưới (grid_size x grid_size)
    :param origin: Tọa độ gốc (x, y)
    """
    height, width, _ = image.shape
    origin_x, origin_y = origin
    
    # Vẽ các đường thẳng ngang
    for y in range(origin_y, height, 60):
        cv2.line(image, (0, y), (width, y), (255, 0, 111), 1)
    for y in range(origin_y, 0, -60):
        cv2.line(image, (0, y), (width, y), (255, 0, 111), 1)
    
    # Vẽ các đường thẳng dọc
    for x in range(origin_x, width, grid_size):
        cv2.line(image, (x, 0), (x, height), (255, 0, 111), 1)
    for x in range(origin_x, 0, -grid_size):
        cv2.line(image, (x, 0), (x, height), (255, 0, 111), 1)
    
    return image

# Đọc ảnh từ file
image = cv2.imread(r'D:\Mobile_Robot\YOLOv9_Object_Tracking\image_11111.jpg')
image = cv2.resize(image, (1280,720))

# Kích thước ô lưới
grid_size = 60

# Tọa độ gốc (x, y)
origin = (630, 374)

# Vẽ lưới lên ảnh với gốc tọa độ mới
image_with_grid = draw_grid(image, grid_size, origin)

# Hiển thị ảnh
cv2.imshow('Image with Grid', image_with_grid)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu ảnh với lưới
cv2.imwrite(r'D:\Mobile_Robot\YOLOv9_Object_Tracking\data_ext\output_image_26_9_24_10h22.jpg', image_with_grid)
