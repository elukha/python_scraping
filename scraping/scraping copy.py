import tkinter as tk
import requests
from bs4 import BeautifulSoup
import re


def get_price(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find("span", class_="a-price-whole")
    pri = str(elems).replace(",", "")
    price = pri[-12:-7]
    label1 = tk.Label(text=price)
    label1.pack(side="bottom")


#Tkinter初期設定
root = tk.Tk()
root.title("価格")
root.minsize(800, 500)


#画像表示
seagate_8TB = tk.PhotoImage(file="seagate_8TB.png")
canvas = tk.Canvas(bg="black", width=183, height=272)
canvas.place(x=0, y=0)
canvas.create_image(0, 0, image=seagate_8TB, anchor=tk.NW)

WD_BLUE_8TB = tk.PhotoImage(file="WD_BLUE_8TB.png")
canvas = tk.Canvas(bg="black", width=183, height=272)
canvas.place(x=200, y=0)
canvas.create_image(0, 0, image=WD_BLUE_8TB, anchor=tk.NW)


#ボタン作成
button1 = tk.Button(root,text='seagate 8TB 表示', command=get_price("https://www.amazon.co.jp/Seagate-%E5%86%85%E8%94%B5%E3%83%8F%E3%83%BC%E3%83%89%E3%83%87%E3%82%A3%E3%82%B9%E3%82%AF-PC%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E5%90%91%E3%81%91-BarraCuda-ST8000DM004/dp/B07911QK3X/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3HF2VBU54NIGW&keywords=hdd+8tb&qid=1707474289&sprefix=hdd+8t%2Caps%2C330&sr=8-5"))
button1.place(x=0, y=280)

button2 = tk.Button(root, text='WD BLUE 8TB 表示', command=get_price("https://www.amazon.co.jp/%E3%80%90Amazon-co-jp%E9%99%90%E5%AE%9A%E3%80%91Western-Digital-%E3%82%A6%E3%82%A8%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%87%E3%82%B8%E3%82%BF%E3%83%AB-WD80EAAZ-AJP-%E3%82%A8%E3%82%B3%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%80%90%E5%9B%BD%E5%86%85%E6%AD%A3%E8%A6%8F%E5%8F%96%E6%89%B1%E4%BB%A3%E7%90%86%E5%BA%97%E3%80%91/dp/B0CP7D7QYK/ref=sr_1_6?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3HF2VBU54NIGW&keywords=hdd%2B8tb&qid=1707474289&sprefix=hdd%2B8t%2Caps%2C330&sr=8-6&th=1"))
button2.place(x=200, y=280)


tk.mainloop()