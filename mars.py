from stat import filemode
from time import time
import urllib.request
import requests
from tkinter import *
from PIL import Image
from tkinter.messagebox import *
import os
import time
import shutil
api = "pIrdFhGHvCOBVwFYeOXvw5PFAxBAUZN2zyCPhPfY"
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers"
root = Tk()
root.title("Mars Mission")
root.geometry("550x600")
root.iconbitmap('icon.ico')
def mars_images(rover, camera, sol):
   url = f"{base_url}/{rover}/photos?sol={sol}&camera={camera}&api_key={api}"
   data = requests.get(url)
   data = data.json()
   img_list = data["photos"]
   img_url_list = []
   for i in range(len(img_list)):
      img_url = data["photos"][i]["img_src"]
      img_url_list.append(img_url)
   return img_url_list
count = 0
shutil.rmtree('data')
os.mkdir('data')
def save_img():
   global count
   url_list = listbox.curselection()
   for i in url_list:
       Url = listbox.get(i)
   print(Url)
   count += 1
   filename = f"data/{count}.jpeg"
   urllib.request.urlretrieve(Url, filename)
   time.sleep(2)
   img = Image.open(filename)
   img.show()
heading = Label(root, text="Mars Mission! To the mars", font=("helvetica", 30))
heading.pack(pady=10)
def main_tab():
   global sol, default_rover, default_cam, sol_entry, main_frame, label_rover, cam_selection, sol_label, rover_selection, get_data_btn
   main_frame = Frame(root)
   try:
      clear_result()
   except:
      pass
   rover_list = ["opportunity", "curiosity", "spirit"]
   label_rover = Label(root, text="Select rover: ")
   label_rover.pack(pady=10)
   default_rover = StringVar()
   default_rover.set("curiosity")
   rover_selection = OptionMenu(root,default_rover, *rover_list)
   rover_selection.pack(pady=10)
   sol_label = Label(root, text="enter a proper sol of the rover: ")
   sol_label.pack(pady=10)
   sol_entry = Entry(root, width=30)
   sol_entry.pack(pady=10)
   cam_list = ["FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"]
   default_cam = StringVar()
   default_cam.set("FHAZ")
   cam_selection = OptionMenu(root, default_cam, *cam_list)
   cam_selection.pack(pady=10)
   get_data_btn = Button(text="Get Data",bg="#1EE8A0", width=30, command=result_tab)
   get_data_btn.pack(pady=10)
def get_data():
   try:
      sol = int(sol_entry.get())
   except:
      showerror("Sol error", "Please enter numbers\n")
   rover = default_rover.get()
   cam = default_cam.get()
   return rover, cam, sol
def clear_main():
    global rover, sol, cam
    rover, cam, sol = get_data()
    sol_entry.destroy()
    label_rover.destroy()
    cam_selection.destroy()
    sol_label.destroy()
    rover_selection.destroy()
    get_data_btn.destroy()
def clear_result():
    listbox.destroy()
    go_back_btn.destroy()
    save_btn.destroy()
def result_tab():
   clear_main()
   global listbox, go_back_btn, save_btn
   data_list = mars_images(rover, cam, sol)
   l = len(data_list)
   if l == 0:
      showerror("invalid sol", "the entered sol is not proper")
   else:
      pass
   listbox = Listbox(root, width=55, height=15, font=("aharoni", 10))
   length = len(data_list)
   for i in range(length):
      listbox.insert(i, data_list[i])
   save_btn = Button(root, text="Save", bg="#1EE8A0", width=30, command=save_img)
   listbox.pack(pady=10)
   save_btn.pack(pady=10)
   go_back_btn = Button(root, text="Go Back", bg="#1EE8A0", width=30, command=main_tab)
   go_back_btn.pack(pady=10)
main_tab()
root.mainloop()



