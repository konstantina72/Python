import tkinter as tk
from tkinter import Button
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
# 0b8ea6a4b5e703f573cb8a6ba9e5e780

def format_response(weather):
    print(weather)
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s\nCondition: %s\nTemperature [F]: %s' %(name,desc,temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str
def get_weather(city):
    weather_key = '0b8ea6a4b5e703f573cb8a6ba9e5e780'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather=response.json()

    celsiusButton.pack(side='bottom')
    celsius_label.place(relwidth=1, relheight=1)
    label['text'] = format_response(weather)


def convert(city):
    weather_key = '0b8ea6a4b5e703f573cb8a6ba9e5e780'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()



    celsius_label['text'] = format(weather)

def format(weather):
    print(weather)
    try:
        temp = (weather['main']['temp'] -32)*5/9
        final_str = 'Temperature [C]: %s' %(temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str




root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="sky.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80b3ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=('Courier',12))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#80b3ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=('Courier',18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

in_frame = tk.Frame(lower_frame)
in_frame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.3, anchor="n")

celsius_label = tk.Label(in_frame, font=('Courier',10), anchor='n', justify='left', bd=4)


celsiusButton = tk.Button(in_frame, text="Convert into Celsius", font=18, command=lambda: convert(entry.get()))


root.mainloop()