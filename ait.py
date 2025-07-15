import pyfiglet
import os
import time
from termcolor import colored

os.system("clear")
banner = pyfiglet.figlet_format("AIT SYSTEM", font="slant")
print(colored(banner, "green"))

print(colored("Initializing system...", "yellow"))
time.sleep(1)
print(colored("Loading modules...", "cyan"))
time.sleep(1)
print(colored("Access granted. Welcome back, agent.", "green"))
time.sleep(1)
import requests
import pyfiglet
import os

print(r"""⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣴⡶⠶⠾⠿⠛⠛⠛⠛⠿⠿⠶⢶⣦⣤⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⡶⠟⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠛⠻⢶⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣴⠾⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⠷⣦⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⡼⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⢷⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣠⡾⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢷⣄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣀⡾⠏⠄⠄⠄⠄⢀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡀⠄⠄⠄⠄⠹⢷⣀⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣼⠏⠄⠄⠄⡀⣰⣾⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣷⣦⢀⠄⠄⠄⠹⣷⡀⠄⠄⠄⠄
⠄⠄⠄⠄⡾⠃⠄⢀⣴⠋⣴⣿⢋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡙⣿⣦⠙⣦⡀⠄⠘⢷⡄⠄⠄⠄
⠄⠄⠄⣼⠁⠄⢀⣿⡏⢰⠟⢡⡎⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡠⣤⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢱⣌⠻⡇⢹⣿⡀⠄⠈⢧⠄⠄⠄
⠄⠄⣼⠏⣠⡎⢸⣿⢣⣥⡾⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠿⠄⠈⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢷⣬⣜⣿⡇⢱⣄⠸⣧⠄⠄
⠄⣸⡟⠄⣿⡇⢸⣷⡿⢋⡔⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡼⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢢⡙⢿⣾⡇⢸⣿⡀⢻⣇⠄
⢀⣿⠁⠄⣿⣧⠸⢋⣴⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣦⡙⠇⣸⣿⡇⠈⣿⡀
⢸⡏⠄⡄⣿⡿⣰⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣆⢻⣿⢣⠄⢹⡇
⣾⡇⢠⣧⠹⣧⡿⠋⣰⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣦⠙⢿⣼⠏⢸⡄⢸⣿
⣿⠄⠘⣿⡀⢻⢁⣼⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⠄⠛⢿⡿⠛⠄⣲⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣧⡈⡿⢀⣾⠃⠄⣿
⣿⠄⠄⢿⣷⠄⣾⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣿⡏⠄⠠⢻⡟⠄⠄⢹⣿⣶⣦⣤⣤⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣷⠄⣾⡿⠄⠄⣿
⢿⡇⢰⠘⣿⡇⣿⡏⢸⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⣼⣧⠄⠄⢈⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⢀⡇⢹⣿⢸⣿⠇⡆⢸⡿
⢸⣇⠈⣷⠈⢻⣿⠄⣼⣇⠄⠄⠄⠄⠄⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⣿⣿⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⣸⣧⠄⣿⡟⠁⣼⠁⣸⡇
⠈⣿⡀⠹⣷⣄⠙⠄⣿⣿⢀⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⣿⣿⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⡀⣿⣿⠄⠋⣠⣾⡏⢀⣿⠁
⠄⢹⣧⠄⠻⣿⣷⡄⣿⣿⠄⣇⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄⠄⣠⠄⣿⣿⢠⣾⣿⠟⠄⣼⡏⠄
⠄⠄⢻⣆⠡⣈⠻⠿⣞⣿⡄⢸⣆⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣰⣿⢠⣿⣳⠿⠟⣁⠌⢰⡿⠄⠄
⠄⠄⠄⢻⡀⠹⣷⣦⣀⠙⠳⣸⣿⣇⢀⡀⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⢀⡀⣸⣿⡏⠞⠋⣀⣴⣾⠏⢀⡞⠄⠄⠄
⠄⠄⠄⠄⢷⡄⠈⠻⢿⣿⣷⣆⡻⣿⡄⢻⣦⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣴⡟⢠⣿⢟⣠⣾⣿⡿⠟⠁⢠⡾⠃⠄⠄⠄
⠄⠄⠄⠄⠈⢿⣆⠄⠄⣉⠛⠿⢿⣮⣿⣄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣠⣿⣵⡿⠿⠛⣉⠄⠄⣰⡿⠁⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠙⢷⣄⠈⠓⢦⣤⣤⣤⣭⣥⣭⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣭⣤⣭⣤⣤⣤⡴⠚⠁⣠⡾⠋⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠙⢷⣄⡀⠈⢉⠛⠛⠛⠛⠛⠉⣁⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣈⠉⠙⠛⠛⠛⠛⡉⠁⠄⣠⡾⠋⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢳⣄⡀⠙⠳⢶⣶⣾⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣷⣶⡶⠞⠋⢀⣠⡾⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⠻⢶⣄⡀⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⢀⣠⣶⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠓⠶⣦⣤⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣤⣴⡶⠚⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⠛⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
""")

url = "https://onlineislemler.egm.gov.tr/sayfalar/ihbar.aspx"


logo = pyfiglet.figlet_format('BY HACKER İHBAR TOOL')
print(logo)


title = input("İhbar Başlığı= ")
description = input("İhbar Açıklaması= ")
city = input("Şehir= ")
district = input("İlçe= ")
phone = input("Telefon Numarası= ")


data = {
    "ctl00$ContentPlaceHolder1$txtIcerik": description,
    "ctl00$ContentPlaceHolder1$txtSehir": city,
    "ctl00$ContentPlaceHolder1$txtIlce": district,
    "ctl00$ContentPlaceHolder1$txtGsm": phone,
    "ctl00$ContentPlaceHolder1$txtAdres": "",  
    "ctl00$ContentPlaceHolder1$txtTarih": "",
    "ctl00$ContentPlaceHolder1$txtMail": "",  
    "ctl00$ContentPlaceHolder1$btnIhbar": "Gönder",
}


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "272",  
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "onlineislemler.egm.gov.tr",
    "Origin": "https://onlineislemler.egm.gov.tr",
    "Referer": "https://onlineislemler.egm.gov.tr/sayfalar/ihbar.aspx",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}


cookies = {
    "_ga": "GA1.2.1508078992.1622750070",
    "_gid": "GA1.2.347325198.1622750070",
}


response = requests.post(url, data=data, headers=headers, cookies=cookies)


if response.status_code == 200:
    print("İhbar giti yara yedi")
else:
    print("siktigimin ihbarı gitmedi sıkıntı sende oc")
