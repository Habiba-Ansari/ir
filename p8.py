from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links.append(newUrl)

    def getLinks(self, url):
        self.links = []
        self.baseUrl = url

        response = urlopen(url)
        html = response.read().decode('utf-8')
        self.feed(html)

        return html, self.links


def crawl(url, word):
    parser = LinkParser()
    data, links = parser.getLinks(url)

    for link in links:
        print("Checking:", link)
        if word in data:
            print("Word found in:", url)
            break


# Example
crawl("https://example.com", "example")
