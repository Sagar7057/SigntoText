from PIL import Image, ImageTk
import tkinter as tk
import cv2
import os
import numpy as np
from keras.models import model_from_json
import operator
import time
import sys, os
import matplotlib.pyplot as plt
# from hunspell import Hunspell
from string import ascii_uppercase

class Application1:
    def __init__(self):
        self.vs = cv2.VideoCapture(0)
        self.current_image = None
        self.current_image2 = None
        
        self.json_file = open("C:/Final Sign Lang/handsign/handsign/models/number models/model-num.json")
        self.model_json = self.json_file.read()
        self.json_file.close()
        self.loaded_model = model_from_json(self.model_json)
        self.loaded_model.load_weights("C:/Final Sign Lang/handsign/handsign/models/number models/model-num.h5")

        self.ct = {}
        self.ct['blank'] = 0
        self.blank_flag = 0
        check = [1,2,3,4,5,6,7,8,9]
        for i in check:
          self.ct[i] = 0
        print("Loaded model from disk")
        self.root = tk.Tk()
        self.root.title("Sign language to Text Converter")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("1600x900")
        self.root.config(bg='#6433FF')
        self.panel = tk.Label(self.root)
        self.panel.place(x = 335, y = 10, width = 640, height = 440)
        self.panel2 = tk.Label(self.root) # initialize image panel
        self.panel2.place(x = 660, y = 10, width = 310, height = 310)
        
        # self.T = tk.Label(self.root)
        # self.T.place(x=20,y = 17)
        # self.T.config(text = "Sign Language to Text",font=("courier",40,"bold"))
        self.panel3 = tk.Label(self.root) # Current SYmbol
        self.panel3.place(x = 335,y=470)
        self.panel3.config(bg='#6433FF',fg="white")
        self.T1 = tk.Label(self.root)
        self.T1.place(x = 50,y = 470)
        self.T1.config(text="Number :",font=("Courier",25,"bold"),bg='#6433FF')
        self.panel4 = tk.Label(self.root) # Word
        self.panel4.place(x = 220,y=510)
        self.panel4.config(bg='#6433FF',fg="white")
        # self.T2 = tk.Label(self.root)
        # self.T2.place(x = 50,y = 510)
        # self.T2.config(text ="Confirm Number :",font=("Courier",25,"bold"),bg='#6433FF')
        # # self.panel5 = tk.Label(self.root) # Sentence
        # self.panel5.place(x = 350,y=550)
        # self.T3 = tk.Label(self.root)
        # self.T3.place(x = 50,y = 550)
        # self.T3.config(text ="Sentence :",font=("Courier",25,"bold"))

        # self.T4 = tk.Label(self.root)
        # self.T4.place(x = 250,y = 590)
        # self.T4.config(text = "Suggestions",fg="red",font = ("Courier",25,"bold"))


        self.str=""
        self.word=""
        self.current_symbol="Empty"
        self.photo="Empty"
        self.video_loop()

    def video_loop(self):
        ok, frame = self.vs.read()
        if ok:
            cv2image = cv2.flip(frame, 1)
            x1 = int(0.5*frame.shape[1])
            y1 = 10
            x2 = frame.shape[1]-10
            y2 = int(0.5*frame.shape[1])
            cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)
            cv2image = cv2image[y1:y2, x1:x2]
            gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray,(5,5),2)
            th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
            ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            self.predict(res)
            self.current_image2 = Image.fromarray(res)
            imgtk = ImageTk.PhotoImage(image=self.current_image2)
            self.panel2.imgtk = imgtk
            self.panel2.config(image=imgtk)
            self.panel3.config(text=self.current_symbol,font=("Courier",25))
            self.panel4.config(text=self.word,font=("Courier",25))
            # self.panel5.config(text=self.str,font=("Courier",25))             
        self.root.after(30, self.video_loop)
    def predict(self,test_image):
        test_image = cv2.resize(test_image, (128,128))
        result = self.loaded_model.predict(test_image.reshape(1, 128, 128, 1))
        prediction={}
        prediction['blank'] = result[0][0]
        inde = 1
        check = [1,2,3,4,5,6,7,8,9]
        for i in check:
            prediction[i] = result[0][inde]
            inde += 1
        #LAYER 1
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        self.current_symbol = prediction[0][0]

        if(self.current_symbol == 'blank'):
            for i in check:
                self.ct[i] = 0
        self.ct[self.current_symbol] += 1
        if(self.ct[self.current_symbol] > 60):
            for i in check:
                if i == self.current_symbol:
                    continue
                tmp = self.ct[self.current_symbol] - self.ct[i]
                if tmp < 0:
                    tmp *= -1
                if tmp <= 20:
                    self.ct['blank'] = 0
                    for i in check:
                        self.ct[i] = 0
                    return
            self.ct['blank'] = 0
            for i in check:
                self.ct[i] = 0
            if self.current_symbol == 'blank':
                if self.blank_flag == 0:
                    self.blank_flag = 1
                    if len(self.str) > 0:
                        self.str += " "
                    self.str += self.word
                    self.word = ""
            else:
                if(len(self.str) > 16):
                    self.str = ""
                self.blank_flag = 0
                self.word += str(self.current_symbol)

    def destructor(self):
        print("Closing Application...")
        self.root.destroy()
        self.vs.release()
        cv2.destroyAllWindows()
    
    def destructor1(self):
        print("Closing Application...")
        self.root1.destroy()


