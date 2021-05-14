import requests
import lxml.html as html
import os
import datetime

HOME_URL = 'https://chequeado.com/'

XPATH_LINK_TO_ARTICLE = '//div/a[@href and not(@class)]/@href'
XPATH_TITLE = '//div[@class = "title"]/h1/text()'
XPATH_SUMMARY = '//div[@class = "main-article"]/article/ul/li/text()'
XPATH_BODY =  '//div[@class = "main-article"]/article/p/text()'

def parse_notice(link, today, count):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            
            notice = response.content.decode("utf-8")
            parsed = html.fromstring(notice)
            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('"','')
                title = title.replace(':','')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            except IndexError:
                return
            
            print(title)
            with open(f"{today}/{count}.txt", 'w', encoding = "utf-8") as f:
                count += 1
                f.write(title)
                f.write("\n\n")
                f.write(summary)
                f.write("\n\n")
                for p in body:
                    f.write(p)
                    f.write("\n")

        else:
            raise ValueError(f"Error: {response.status_code}")
    except ValueError:
        print(f"")


def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode("utf-8")
            parsed = html.fromstring(home)
            links = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            today = datetime.date.today().strftime("%d-%m-%Y")
            if not os.path.isdir(today):
                os.mkdir(today)
            count = 0
            for link in links:
                count += 1
                parse_notice(link, today, count)
        else:
            raise ValueError(f"Error:{response.status_code}")
    except ValueError:
        print(ValueError)

    pass

def run():
    parse_home()

if __name__ == "__main__":
    run()