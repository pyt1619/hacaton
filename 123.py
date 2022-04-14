import requests
from bs4 import BeautifulSoup
import threading
import os
def getText(url, foo):
    # response2 = requests.get()
        while True:
            response2 = requests.get(url=f'https://college.edunetwork.ru{url}')
            soup2 = BeautifulSoup(response2.text, 'lxml')
            # Название
            description = ''
            title = ''
            metro = ''
            info = ''
            gpa = ''
            try:
                title = soup2.find('div', attrs={'id':'unit-header'}).find('h1', attrs={'itemprop':'name'}).text
            except:
                pass
            # Метро
            try:
                metro = soup2.find('div', attrs={'id':'unit-header'}).find('li',class_="metro truncate").text
            except:
                pass
            # Общая информация
            try:
                info = soup2.find('section', attrs={'id':'general'}).text.strip()
            except:
                pass
            # Средний балл аттестата(grade point average)
            try:
                gpa = soup2.find('div', class_="row unit-values").text
            except:
                pass
            # Описание
            try:

                for i in range(100):
                    try:
                        description += soup2.find('section', attrs={'id':'about'}).findAll('p')[i].text
                        description += '\n'
                    except IndexError:
                        break
            except:
                pass
            print(f'{title}\n{metro}\n{description}\n{info}\n{gpa}')
            if(title!=''):
                break
names = []

for page in range(5):
    while True:
        try:

            response = requests.get(f'https://college.edunetwork.ru/77/?page={page}')
            soup = BeautifulSoup(response.text, 'lxml')
            soup = soup.find('div', class_ = 'col l9 s12')
            soup = soup.find("div", { "id" : "units-list" })
                    
                
            for i in soup.findAll("p", class_ = 'unit-name'):
                # print(i.text.strip())
                names.append(i.text.strip())
                # z = threading.Thread(target=getText, args=())
                # z.start()
                getText(i.find('a')['href'], "foo")
                print(i.text.strip()+":::::"+i.find('a')['href'])
                # os.system(f"{i.text.strip()} > names.text")
            break 
            # print("error")
        # for i in soup.findAll("p", class_ = 'unit-name'):
            # print(i.text.strip())
        except :
            pass
# name = 
# print(soup.text)

