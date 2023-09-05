import requests
from pprint import pprint
import json
import datetime
from tkinter import *
from PIL import ImageTk, Image
from tkinter import StringVar

# necessary details
root = Tk()
root.title('Weather App')
root.geometry('400x400')
root['background'] = 'lightblue'


# image
img = ImageTk.PhotoImage(Image.open('weather.png'))
panel = Label(root, image = img)
panel.place(x=0, y=520)

API_key = '0919b78bbb94ccf36776d94b0d0c94e6'

#city = input("Enter a city: ")
#zip_code = input("Enter a zip code: ")

city_name = StringVar()
city_entry = Entry(root, textvariable=city_name)
city_entry.place(x=7, y=30)


zip_code = StringVar()
zip_code_entry = Entry(root, textvariable=zip_code)
zip_code_entry.place(x=160, y=30)

#pprint(weather_data)

if zip_code_entry.get() == '' and city_entry.get() == '':
    
    def zip_code():
        api_request= requests.get("http://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&zip="+zip_code_entry.get())
        api = json.loads(api_request.content)
        try:
            weather_data = api
            
            city_name = weather_data['name']

            temp = weather_data['main']['temp']

            description = weather_data['weather'][0]['description']

            fahrenheit = round((temp - 273.15) * 9/5 + 32)

            dt = datetime.datetime.fromtimestamp(weather_data['dt'])

            label_city.configure(text=city_name)
            label_fahrenheit.configure(text=fahrenheit)
            label_description.configure(text=description)
            label_dt.configure(text=dt)        

            #print('\nCity Name : ', city_name)
            #print('\nTemperature : ', fahrenheit)
            #print('\nDescription : ', description)
        except:
            label_reminder.configure(text='Please enter a valid city name and zip code')
else:   
    label_reminder = Label(root, text="Please enter a city name and zip code", width=0, bg='lightblue', font=("bold", 10))
    label_reminder.place(x=7, y=3)

label_reminder = Label(root, text=" ", width=0, bg='lightblue', font=("bold", 10))
label_reminder.place(x=7, y=3)

label_city_name = Label(root, text="City Name", width=0, bg='lightblue', font=("bold", 14)) 
label_city_name.place(x=7, y=50)

zip_codeButton = Button(root, text='Zip Code', font=("bold", 12), command=zip_code)
zip_codeButton.place(x=160, y=50)

label_city = Label(root, text="...", width=0, bg='lightblue', font=("bold", 15))
label_city.place(x=16, y=78)

label_fahrenheit = Label(root, text="...", width=0, bg='lightblue', font=("Helvetica", 15), fg='black')
label_fahrenheit.place(x=16, y=238)

label_description = Label(root, text="...", width=0, bg='lightblue', font=("Helvetica", 15), fg='black' )
label_description.place(x=16, y=293)

label_dt = Label(root, text="...", width=0, bg='lightblue',  font=("Helvetica", 15), fg='black')
label_dt.place(x=16, y=343)

img = ImageTk.PhotoImage(Image.open('weather.png'))
panel = Label(root, image=img, width=125, height=110)
panel.place(x=16, y=110)

root.mainloop()



