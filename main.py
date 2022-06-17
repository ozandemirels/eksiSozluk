import requests
from bs4 import BeautifulSoup
import smtplib
import time


def check_contents():
    global url, headers
    url = ('https://eksisozluk.com/')
    headers = {'User-Agent': 'my user agent(google)'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title_ul = soup.find('ul', class_='topic-list partial')
    title_lis = title_ul.find_all('li')
    for title_li in title_lis:
        try:
            a = 0
            volume = title_li.a.small.text
            urls = title_li.find('a', href=True)
            urls = url + urls['href']
            title_li = title_li.text.replace('\n', '')
            for i in (title_li[::-1]):
                a += 1
                if i == ' ' and int(volume) >= 200:
                    count = 0
                    content = title_li[:-a]
                    for element in content_list:
                        if element[0] == content:
                            count += 1
                            break
                    if count == 0:
                        content_list.append([content, volume])
                        print(content)
                        print('123123')
                        time.sleep(1555)
                        send_mail(content, urls)
                    break
        except:
            pass


def send_mail(title, urls):
    gmail_user = 'ozandemirel.93@gmail.com'
    gmail_password = '****************'
    to = 'ozandemirel.93@gmail.com'
    try:
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(gmail_user, gmail_password)
        subject = "Ekşi Sözlük'teki " + title + " başlığı yoğun ilgi görüyor.\n\nEkşi Sözlük'teki " + title + ' başlığı yoğun ilgi görüyor.\n\nİncelemek için linke tıklayınız --> ' + urls
        mail_content = f"To:{to}\nFrom:{gmail_user}\nSubject:{subject}"
        mail_content = mail_content.encode('utf-8')
        smtpserver.sendmail(gmail_user, to, mail_content)
    except smtplib.SMTPException as error:
        print(error)
    smtpserver.close()


content_list = []
while True:
    check_contents()
    time.sleep(3)





