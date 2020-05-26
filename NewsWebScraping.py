import requests
from bs4 import BeautifulSoup
import easygui #message box


class HackerNews:
    def __init__(self):
        self.hn = []
        self.new_hn = []
        self.title = None
        self.vote = None
        self.points = None

    def get_custom_hn(self):
        try:
            for n in range(1,5):
                req = requests.get("https://news.ycombinator.com/news?p=" + str(n))
            soup = BeautifulSoup(req.text, "html.parser") # beautiful soup
            link = soup.select(".storylink") # link
            subtext = soup.select(".subtext") # text
            for i, item in enumerate(link):
                self.title = item.getText()
                link = item.get("href", None)
                self.vote = subtext[i].select(".score")
                if len(self.vote):
                    self.points = int(self.vote[0].getText().split()[0])
                    if self.points > 100:
                        self.hn.append({"Title": self.title, "Link": link, "Points": self.points})
                        self.new_hn = sorted(self.hn[:3], key=lambda x:x["Points"], reverse=True)
            return sorted(self.new_hn, key=lambda x:x["Points"], reverse=True)
        except:
            self.handleError(self.get_custom_hn, "Hacker News Page - Error... ")

    def getTitles(self, index):
        try:
        # pprint.pprint(self.hacker_news.get_custom_hn())
            list_of_titles = []
            for item in self.get_custom_hn():
                list_of_titles.append(item['Title'])
            return list_of_titles[index]
        except:
            self.handleError(self.getTitles, "Titles can not be retrieved...")

    def getLinks(self, index):
        try:
            list_of_links = []
            for item in self.get_custom_hn():
                list_of_links.append(item["Link"])
            return list_of_links[index]
        except:
            self.handleError(self.getLinks, "Links can not be retrieved...")

    def getPoints(self, index):
        try:
            list_of_points = []
            for item in self.get_custom_hn():
                list_of_points.append(item['Points'])
                # list_of_points.append({'Points: ' : {item['Points']}})
            return list_of_points[index]
        except:
            self.handleError(self.getPoints, "Points can not be retrieved...")

    def handleError(self, funct, msg):
        title = "'Oops, something is wrong'"
        if easygui.ccbox(msg, title):  # show a Try Again/Cancel dialog
            funct.__call__()  # user chose Try Again


