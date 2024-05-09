import Text_to_Speech
import Speech_to_Text
from multiprocessing import Process
import Summarization
import Image_to_Text
import Seen_explanation
from tkinter import *
#import sys
import Object_Detection
#while True:
#x = ""
t = Tk()
t.geometry("300x100")
def start():
    Text_to_Speech.start()
    x = Speech_to_Text.spch_to_txt()
    #qx = "scene explanation"
    #x = x.lower()
    #x = str(x)
    #print(len(x))
    #print(len("scene"))
    #x = "summary"
    while len(x):
        if x == "read text":
            Image_to_Text.img_to_text()
        elif x == "detect objects":
            Object_Detection.OD()
        elif x == "summary":
            #Summarization
            Summarization.summ()
            #print("Adfas")
        elif x == "scene explain":
            '''Process(target=Seen_explanation.se()).start()
            Process(target=Seen_explanation.se1()).start()'''
            Seen_explanation.se()
        else:
            Text_to_Speech.spk("Invalid input is given")
            Text_to_Speech.spk("Speak again")
            x = Speech_to_Text.spch_to_txt()
            #break
'''def end():
     Text_to_Speech.spk("Closing!")
     sys.exit()'''
b = Button(t, command = start, text = "Start")
#b1 = Button(t, command = end, text = "End")
b.pack(side=TOP)
#b1.pack(side=BOTTOM)
t.mainloop()

'''Text_to_Speech.start()
x = Speech_to_Text.spch_to_txt()
#x = "scene explanation"
#x = x.lower()
#x = str(x)
#print(len(x))
#print(len("scene"))
#x = "detect object"
while len(x):
    if x == "read text":
        Image_to_Text.img_to_text()
    elif x == "detect objects":
        Object_Detection.OD()
    elif x == "summarize":
        #Summarization
        print("Adfas")
    elif x == "scene explain":
        Seen_explanation.se()
    else:
        Text_to_Speech.spk("Invalid input is given")
        Text_to_Speech.spk("Speak again")
        x = Speech_to_Text.spch_to_txt()
        #break
'''