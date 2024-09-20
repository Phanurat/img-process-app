import cv2
import numpy as np
import image_processor  # โมดูลที่เราสร้าง

# โหลดภาพ
img = cv2.imread('input_image.jpg')  # เปลี่ยนชื่อไฟล์เป็นภาพที่คุณต้องการ

# ประมวลผลภาพ
gray_image = image_processor.apply_gray_scale(img)

# แสดงผล
cv2.imshow('Original Image', img)
cv2.imshow('Gray Image', gray_image)

# รอจนกว่าจะปิดหน้าต่าง
cv2.waitKey(0)
cv2.destroyAllWindows()
