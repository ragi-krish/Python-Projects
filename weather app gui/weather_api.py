import requests
import tkinter as tk
from PIL import Image,ImageTk
import os

window = tk.Tk()
window.title("Weather App")
window.geometry("300x200")
window.resizable(False, False)

abs_path = os.path.abspath(__file__)
pic_path = os.path.join(os.path.dirname(abs_path),"WEATHER BACKGROUND.jpeg")
print(pic_path)
bg_image = Image.open(pic_path)
bg_image = bg_image.resize((300,200),Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

for i in range(2):
    window.columnconfigure(i, weight=1)

for i in range(5):
    window.rowconfigure(i, weight=1)

def get_details():
    city = entry1.get()
    apikey = "89a4a560ccbbe513443c5795ad3c1d91"
    url ="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apikey
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            label3.config(text="City not found!")
            label4.config(text="")
            label5.config(text="")
            return
            
        main,humidity = data["weather"][0]["main"],str(data["main"]["humidity"])
        temperature = round((data["main"]["temp"])-273.15,2)

        label3.config(text="weather: "+main)
        label4.config(text="Temperature: "+str(temperature)+"°C")
        label5.config(text="Humidity: "+humidity)

    except:
        label3.config(text="Error!")
        label4.config(text="")
        label5.config(text="")

bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = tk.Label(window,text="Weather App",font=("Arial", 14,"bold"),bg="#3c444c",fg="white")
label1.grid(row=0,columnspan=2)

label2 = tk.Label(window,text="City:",font=("Arial", 10,"bold"),bg="#555a55",fg="white")
label2.grid(row=1,column=0)

entry1 = tk.Entry(window,bg="#3c444c",fg="white",font=("Arial", 10,"bold"))
entry1.grid(row=1,column=1)
entry1.focus()

button1 = tk.Button(window,text = "Enter",font=("Arial", 10, "bold"),
    bg="#3c444c", fg="white", activebackground="#555a55", activeforeground="white",command = get_details)
button1.grid(row=2,columnspan=2)

label3 = tk.Label(window,font=("Arial", 10,"bold"),bg="#696552",fg="white")
label3.grid(row=3,column=0)
label4 = tk.Label(window,font=("Arial", 10,"bold"),bg="#696552",fg="white")
label4.grid(row=3,column=1)

label5 = tk.Label(window,font=("Arial", 10,"bold"),bg="#696552",fg="white")
label5.grid(row=4,column=0)

window.mainloop()
