import csv
import pygame
import sys
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

#creating the root window
root=Tk()
root.title('Surviving Titanic Odds Calc App ')
#initialize mixer
mixer.init()


#font is defined which is to be used for the button font
defined_font = font.Font(family="Helvetica")

songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=7,width=40,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=12)

songs_list.insert(END, "Hi! Welcome to the Titanic calulator!")
songs_list.insert(END, "Give us some information and")
songs_list.insert(END, "we'll determine what you're odds were!")


gender = ""
status = ""

def LC_male():
  gender = "male"
  status = "3"
  counter = 0
  with open("titanic_data.csv", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
      if record["Sex"] == gender and record["Pclass"] == status and record["Survived"] == "1":
        counter = counter + 1
    songs_list.insert(END, "You're odds of surviving were " + str(counter/891) + "%!")
    
def LC_female():
  gender = "female"
  status = "3"
  counter = 0
  with open("titanic_data.csv", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
      if record["Sex"] == gender and record["Pclass"] == status and record["Survived"] == "1":
        counter = counter + 1
    songs_list.insert(END, "You're odds of surviving were " + str(counter/891) + "%!")

def UC_male():
  gender = "male"
  status = "1"
  counter = 0
  with open("titanic_data.csv", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
      if record["Sex"] == gender and record["Pclass"] == status and record["Survived"] == "1":
        counter = counter + 1
    songs_list.insert(END, "You're odds of surviving were " + str(counter/891) + "%!")

def UC_female():
  gender = "female"
  status = "1"
  counter = 0
  with open("titanic_data.csv", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
      if record["Sex"] == gender and record["Pclass"] == status and record["Survived"] == "1":
        counter = counter + 1
    songs_list.insert(END, "You're odds of surviving were " + str(counter/891) + "%!")

def MC_male():
  gender = "male"
  status = "2"
  counter = 0
  with open("titanic_data.csv", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
      if record["Sex"] == gender and record["Pclass"] == status and record["Survived"] == "1":
        counter = counter + 1
    songs_list.insert(END, "You're odds of surviving were " + str(counter/891) + "%!")

def MC_female():
  gender = "female"
  status = "3"
  counter = 0
  with open("titanic_data.csv", encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for record in reader:
      if record["Sex"] == gender and record["Pclass"] == status and record["Survived"] == "1":
        counter = counter + 1
    songs_list.insert(END, "You're odds of surviving were " + str(counter/891) + "%!")



# LC Male button
#need another paraemetr for command=(name of function)
play_button=Button(root,text="LC Male",width =7,command=LC_male)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

# LC Female button
pause_button=Button(root,text="MC Male",width =7,command=MC_male)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#1st class button
stop_button=Button(root,text="UC Male",width =7,command=UC_male)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#2nd class button
Resume_button=Button(root,text="LC female",width =7,command=LC_female)
Resume_button['font']=defined_font
Resume_button.grid(row=2,column=0)

#3rd class button
previous_button=Button(root,text="MC Female",width =7,command=MC_female)
previous_button['font']=defined_font
previous_button.grid(row=2,column=1)

#other button 
previous_button=Button(root,text="UC Female",width =7,command=UC_female)
previous_button['font']=defined_font
previous_button.grid(row=2,column=2)

root.mainloop()