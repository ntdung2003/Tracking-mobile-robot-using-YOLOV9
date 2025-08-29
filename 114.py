import cv2

# Function to capture the click event
points = []
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates (x, y): ({x}, {y})")
        points.append((x, y))

# Read and display the image
image_path = r'D:\Mobile_Robot\YOLOv9_Object_Tracking\output_image_1920x1080.jpg'
frame = cv2.imread(image_path)
#frame = cv2.resize(frame, (1280,720))
if frame is None:
    print("Error: Could not open image.")
    exit()

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', click_event)

while True:
    display_frame = frame.copy()
    for point in points:
        cv2.circle(display_frame, point, 2, (0, 255, 0), -1)

    
    # Vị trí gốc tọa độ bạn muốn vẽ
    #origin = (637, 358)  # Tọa độ gốc tọa độ
    origin = (958, 540)  # Tọa độ gốc tọa độ
    # Độ dài của các đường của dấu cộng
    line_length = 15
    # Màu sắc và độ dày của dấu cộng
    color = (0, 255, 0)  # Màu xanh lá cây
    thickness = 2
    # Vẽ đường ngang của dấu cộng
    cv2.line(display_frame, (origin[0] - line_length, origin[1]), (origin[0] + line_length, origin[1]), color, thickness)
    # Vẽ đường dọc của dấu cộng
    cv2.line(display_frame, (origin[0], origin[1] - line_length), (origin[0], origin[1] + line_length), color, thickness)
    
    cv2.imshow('Image', display_frame)
    cv2.imwrite('output_image_110.jpg', display_frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
