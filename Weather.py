import requests
import os
import json
import win32com.client as w
s= w.Dispatch("SAPI.SpVoice")

i=input("Enter the name of city")
url = f"https://api.weatherapi.com/v1/current.json?key=b73cf79ee3544b30bc3182639250505&q={i}&"
r=requests.get(url)
print(r.text)
dic = json.loads(r.text)
a= (dic["current"]["temp_c"])
s.speak(a)

