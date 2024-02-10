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
    return int(price)


def price_display(price, root):
    label1 = tk.Label(root, text=price)
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


#ラジオボタン表示
# チェック有無変数
var = tk.IntVar()
# value=0のラジオボタンにチェックを入れる
var.set(0)

# ラジオボタン作成
rdo1 = tk.Radiobutton(root, value=0, variable=var, text='seagate 8TB')
rdo1.place(x=0, y=280)

rdo2 = tk.Radiobutton(root, value=1, variable=var, text='WD BLUE 8TB')
rdo2.place(x=200, y=280)

if var == 0:
    get = get_price("https://www.amazon.co.jp/Seagate-%E5%86%85%E8%94%B5%E3%83%8F%E3%83%BC%E3%83%89%E3%83%87%E3%82%A3%E3%82%B9%E3%82%AF-PC%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E5%90%91%E3%81%91-BarraCuda-ST8000DM004/dp/B07911QK3X/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3HF2VBU54NIGW&keywords=hdd+8tb&qid=1707474289&sprefix=hdd+8t%2Caps%2C330&sr=8-5")
    price_display(get, root)
elif var == 1:
    get = get_price("https://www.amazon.co.jp/Seagate-%E5%86%85%E8%94%B5%E3%83%8F%E3%83%BC%E3%83%89%E3%83%87%E3%82%A3%E3%82%B9%E3%82%AF-PC%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E5%90%91%E3%81%91-BarraCuda-ST8000DM004/dp/B07911QK3X/ref=sr_1_5?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=3HF2VBU54NIGW&keywords=hdd+8tb&qid=1707474289&sprefix=hdd+8t%2Caps%2C330&sr=8-5")
    price_display(get, root)



tk.mainloop()