import cv2
from PIL import Image
from dis_bg_remover import remove_background as rb 
model_path=r"yourmodelpath"
image_path=r"yourimagepath"

img, mask = rb(model_path,image_path)

cv2.imwrite('generated.png',img)
cv2.imwrite('mask.png',mask)