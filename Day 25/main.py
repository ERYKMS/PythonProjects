import pandas

list = []

#with open("weather_data.csv","r") as data_file:
    #data = data_file.readlines()
    #for added_data in data:
        #list.append(added_data)
#import csv

#with open("weather_data.csv") as data_file:
    #data=csv.reader(data_file)
    #temperatures=[]
    #for row in data:
        #if row[1] != "temp":
            #temperatures.append(int(row[1]))
    #print(temperatures)

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Farklı renklerin listesini alalım
farkli_renkler = data["Primary Fur Color"].unique()

# Her renk için sayacı başlat
renk_sayilari = {"Gray": 0, "Cinnamon": 0, "Black": 0}

# Her renk için sayıları sayalım
for renk in farkli_renkler:
    renk_sayilari[renk] = data[data["Primary Fur Color"] == renk].shape[0]

# Sonuçları yazdıralım
print(renk_sayilari)

# Renklerin sayısını ayrı değişkenlerde tutmak istiyorsanız:
gray = renk_sayilari["Gray"]
red = renk_sayilari["Cinnamon"]
black = renk_sayilari["Black"]
print("Gray:", gray, "Cinnamon:", red, "Black:", black)

df= pandas.DataFrame({"Renk":["Gray","Red","Black"],"Sayı":[gray,red,black]})

tablo=pd.pivot_table(df,index="Renk",values="Sayı",aggfunc="sum")
