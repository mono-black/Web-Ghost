from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup as bs

def get(url):
    try :
        page = urlopen(url)


        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = bs(html,"html.parser")
        prettyHTML = soup.prettify()
        return(prettyHTML)
    except HTTPError as e :
        print("\n--->> Something went wrong when opening the url or wrong url\n")
        print('Error code: ', e.code)
    except URLError as e:
        print("\n--->> Something went wrong when opening the url or wrong url\n")
        print('Reason: ', e.reason)




def find_element(attr,url,value):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = bs(html,"html.parser")
    if value == "":
        return(soup.find_all('a', href=True))
            
    else :
        if attr == 1:
            attr = "id"
        elif attr == 2:
            attr = "class"
        elif attr == 3:
            attr = "name"
        elif attr == 4:
            attr = "method"
        elif attr == 5:
            attr = "action"
        elif attr == 6:
            attr = "type"
        else :
            return(0)

        elements = soup.find_all(attrs={f'{attr}':f'{value}'})

        return(elements)