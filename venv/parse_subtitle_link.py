from bs4 import BeautifulSoup
import urllib.request

def parseLink(link):
    print(link)
    print(urllib.request.urlopen(link))
    sauce = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(sauce,'lxml')

    download_links = soup.find_all('a')