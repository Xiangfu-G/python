import cv2
import numpy as np

d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imdecode(np.fromfile("F:/Python代码/PyQt/test_qr.png", dtype=np.uint8), 1))
print("text is:", val)
