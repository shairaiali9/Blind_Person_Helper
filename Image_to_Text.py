import cv2 
import pytesseract
import Text_to_Speech #Khud k banaya huya
def img_to_text():
    Text_to_Speech.spk("Capturing")
    cam = cv2.VideoCapture(0)
    _, frame = cam.read()
    #img = cv2.imread(frame)
    img = frame
    # Adding custom options
    '''custom_config = r'--oem 3 --psm 6'
    x = pytesseract.image_to_string(img, config=custom_config)'''

    #custom_config = r'--oem 3 --psm 6'
    x = pytesseract.image_to_string(img)
    Text_to_Speech.read_text(x)
    print(x)