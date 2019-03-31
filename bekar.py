from tkinter import *
import os
from os import path
import sys
import tkinter.font
import tkinter.messagebox
import subprocess
from subprocess import Popen
from subprocess import run
from time import sleep
import PIL.Image
from PIL import Image, ImageTk

# Admin can exit the app by pressing ctrl + C on keyboard




def run():
    try:
        main()
    except:
        os.system('killall omxplayer.bin')
        sys.exit()
        root.destroy()
            
            


def main():


    def quit(event):
        
        print("Ended the Program")
        root.destroy()
        root.quit()
        sys.exit()
        os.system('killall omxplayer.bin')

    
    root =Tk()
    frame = Frame(root)
    bottomframe = Frame(root)
    root.title('[VIDEO-APPLICATION]')



    #the below two lines are two modes of full screen (enjoy what youy want !)

    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    #root.attributes("-fullscreen", True)








    root.focus_set()


    def Video_One():
        movie_path = '/home/pi/text.mp4'
        omxp = Popen(['omxplayer',movie_path])


    def Video_two():
        movie_path2 = '/home/pi/video2aiv.mp4'
        omxp = Popen(['omxplayer',movie_path2])

    def image_file():
        image = Image.open('tes1.jpg')
        image.show()
        sleep(3)
        sys.exit()


    def Text_box():
        tkinter.messagebox.showinfo( "Python", "Hey Dude !!!")



    def Video_Five():
        tkinter.messagebox.showinfo( "Hello", "How are you ? Sir !!!")

    def Video_Six():
        tkinter.messagebox.showinfo( "Project", "Hey man, It's Party Time !!!")

    def Video_Seven():
        movie_path = '/home/pi/echi.mp4'
        omxp = Popen(['omxplayer',movie_path])

    def Video_Eight():
        movie_path = '/home/pi/cloud.mp4'
        omxp = Popen(['omxplayer',movie_path])

    def Video_Nine():
        image = Image.open('Test1.png')
        image.show()
        
    def Video_Ten():
        movie_path = '/home/pi/nig.mp4'
        omxp = Popen(['omxplayer',movie_path])
    
    
    
    
    
    


        
            
    redbutton=Button(text="Video One", command = Video_One)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=0, column=2, padx=40, pady=40)



    # If you want the button to disabled, please uncomment the following line
    # and also delete the second line in upper pair of 4 lines
    # redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white', state = 'disabled')





    redbutton =Button(text="Video Two", command = Video_two)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=0, column=3, padx=40, pady=40)

    redbutton =Button(text="Image File", command = image_file)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=2, column=2, padx=40, pady=40)


    redbutton =Button(text="Text_Button", command =Text_box)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=2, column=3, padx=40, pady=40)


    redbutton =Button(text="Video Five", command = Video_Five)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=4, column=2, padx=40, pady=40)



    redbutton =Button(text="Video Six", command =Video_Six)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=4, column=3, padx=40, pady=40)



    redbutton =Button(text="Video Seven", command = Video_Seven)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=6, column=2, padx=40, pady=40)


    redbutton =Button(text="Video Eight", command = Video_Eight)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=6, column=3, padx=40, pady=40)



    redbutton =Button(text="Image Two", command = Video_Nine)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=8, column=2, padx=40, pady=40)



    redbutton =Button(text="Video Ten", command = Video_Ten)
    redbutton.config(bg='dark red', width='10', bd='4', relief='groove', fg='white')
    redbutton.config(font=('helvetica',20,'bold italic'))
    redbutton.grid(row=8, column=3, padx=40, pady=40)

    root.bind('<Control-c>', quit)
    root.mainloop()



if __name__ == '__main__':
    run()
