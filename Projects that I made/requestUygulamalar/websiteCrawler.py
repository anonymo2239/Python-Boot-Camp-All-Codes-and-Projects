import requests
from bs4 import BeautifulSoup


target_url = "https://www.youtube.com"
foundLinks = []


def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def crawl(url):
    links = make_request(url)
    for link in links.find_all('link'):
        found_link = link.get('href')
        if found_link:
            if '#' in found_link:
                found_link = found_link.split('#')[0]
            if target_url in found_link and found_link not in foundLinks:
                foundLinks.append(found_link)
                print(found_link)
                crawl(found_link)


crawl(target_url)
# html parsing, HTML belgelerinin ayrıştırılması ve içeriklerinin analiz edilmesi işlemidir.
# HTML, web sayfalarının yapısal olarak tanımlanmasını sağlayan bir işaretleme dilidir.
# HTML parsing, bir HTML belgesinin içeriğini programatik olarak okuyup işlemek için
# kullanılan bir işlemdir.
