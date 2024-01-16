import tkinter
import tkinter as tk
import customtkinter
import requests
from tkinter import *
from PIL import Image, ImageTk
import ttkbootstrap
def searching():
    city= location_entry.get()
    result = get_weth(city)
    if result is None:
        return
    pic_label.destroy()
    icon_url, temp, desc, city, country = result
    loc_label.configure(text=f"{city},{country}")

    image= Image.open(requests.get(icon_url,stream=True).raw)
    ic= ImageTk.PhotoImage(image)

    image_label.configure(image=ic)
    image_label.image = ic

    temp_label.configure(text=f"Temperature -> {temp:.2f}°C")
    detail_label.configure(text=f"Expected weather -> {desc}")
def get_weth(city):
    api_key= "38acec96a2af5d46a355a4f46322e4de"
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res= requests.get(url)
    if res.status_code == 404:
        tkinter.messagebox("city not found")
        return None

    weather = res.json()
    icon_key = weather['weather'][0]['icon']
    temp = weather['main']['temp']-273.15
    desc = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']


    icon_url = f"https://openweathermap.org/img/wn/{icon_key}@2x.png"

    return(icon_url, temp, desc, city, country)




root = ttkbootstrap.Window(themename="solar")
root.title("weather app")
root.geometry("720x480")

location_entry= customtkinter.CTkEntry(root,font=("Helvetica",15),width=200,corner_radius=20,placeholder_text="enter location............",placeholder_text_color="grey")
location_entry.pack(pady=20)

search = ttkbootstrap.Button(root,text="Search", bootstyle="warning", command=searching,)
search.pack(pady=10)

loc_label = ttkbootstrap.Label(root,font=("Helvetica",18))
loc_label.pack(pady=10)

pic= ttkbootstrap.PhotoImage(file="pic3.com.png")
pic_label=ttkbootstrap.Label(root,image=pic)
pic_label.pack(pady=50)



image_label= tk.Label(root)
image_label.pack()

temp_label = ttkbootstrap.Label(root,font=("Helvetica",18))
temp_label.pack(pady=10)

detail_label= ttkbootstrap.Label(root,font=("Helvetica",18))
detail_label.pack(pady=10)
root.mainloop()
