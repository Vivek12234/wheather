# importing the libraries
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image

# API key (replace 'your_api_key_here' with your actual API key)
api_key = 'your_api_key_here'

# necessary details
root = Tk()
root.title("Weather App")
root.geometry("450x700")
root['background'] = "white"

# Image
new = ImageTk.PhotoImage(Image.open('logo.png'))
panel = Label(root, image=new)
panel.place(x=0, y=520)

# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

# Time
hour = Label(root, text=dt.strftime('%I : %M %p'),
             bg='white', font=("bold", 15))
hour.place(x=10, y=160)

# Theme for the respective time the application is used
hour_int = int(dt.strftime('%H'))
if 8 <= hour_int <= 17:
    img = ImageTk.PhotoImage(Image.open('sun.png'))
else:
    img = ImageTk.PhotoImage(Image.open('moon.png'))
panel = Label(root, image=img)
panel.place(x=210, y=200)

# City Search
city_name_var = StringVar()
city_entry = Entry(root, textvariable=city_name_var, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)

def get_weather():
    try:
        # API Call
        api_request = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city_entry.get()}&units=metric&appid={api_key}")
        api = api_request.json()

        if api_request.status_code == 200:
            # Temperatures
            y = api['main']
            current_temperature = y['temp']
            humidity = y['humidity']
            tempmin = y['temp_min']
            tempmax = y['temp_max']

            # Coordinates
            x = api['coord']
            longitude = x['lon']
            latitude = x['lat']

            # Country
            z = api['sys']
            country = z['country']
            city = api['name']

            # Adding the received info into the screen
            label_temp.configure(text=current_temperature)
            label_humidity.configure(text=humidity)
            max_temp.configure(text=tempmax)
            min_temp.configure(text=tempmin)
            label_lon.configure(text=longitude)
            label_lat.configure(text=latitude)
            label_country.configure(text=country)
            label_city.configure(text=city)
        else:
            label_city.configure(text="City not found")
    except Exception as e:
        label_city.configure(text="Error: " + str(e))

# Search Bar and Button
city_name_button = Button(root, text="Search", command=get_weather)
city_name_button.grid(row=1, column=1, padx=5, stick=W+E+N+S)

# Country Names and Coordinates
label_city = Label(root, text="...", width=0,
                   bg='white', font=("bold", 15))
label_city.place(x=10, y=63)

label_country = Label(root, text="...", width=0,
                      bg='white', font=("bold", 15))
label_country.place(x=135, y=63)

label_lon = Label(root, text="...", width=0,
                  bg='white', font=("Helvetica", 15))
label_lon.place(x=25, y=95)
label_lat = Label(root, text="...", width=0,
                  bg='white', font=("Helvetica", 15))
label_lat.place(x=95, y=95)

# Current Temperature
label_temp = Label(root, text="...", width=0, bg='white',
                   font=("Helvetica", 110), fg='black')
label_temp.place(x=18, y=220)

# Other temperature details
humi = Label(root, text="Humidity: ", width=0,
             bg='white', font=("bold", 15))
humi.place(x=3, y=400)

label_humidity = Label(root, text="...", width=0,
                       bg='white', font=("bold", 15))
label_humidity.place(x=107, y=400)

maxi = Label(root, text="Max. Temp.: ", width=0,
             bg='white', font=("bold", 15))
maxi.place(x=3, y=430)

max_temp = Label(root, text="...", width=0,
                 bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

mini = Label(root, text="Min. Temp.: ", width=0,
             bg='white', font=("bold", 15))
mini.place(x=3, y=460)

min_temp = Label(root, text="...", width=0,
                 bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

# Note
note = Label(root, text="All temperatures in degree celsius",
             bg='white', font=("italic", 10))
note.place(x=95, y=495)

root.mainloop()
