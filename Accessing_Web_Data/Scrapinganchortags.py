import urllib
from BeautifulSoup import *
import re

def parseDeepURL(linkURL,linkPos):
    htmlContent = urllib.urlopen(linkURL)
    soupedHTML = BeautifulSoup(htmlContent)
    anchorTags = soupedHTML('a')
    countLink = 1
    for tag in anchorTags:
        hrefstrip = tag.get('href',None)
        if countLink == linkPos:
            return hrefstrip
        countLink+=1

link = raw_input("Enter Root URL ")
timesProcess = int(raw_input("Enter the Number times to Repeat the Process "))
urlPos = int(raw_input("Enter URL Position "))

while timesProcess != 0:
    link = parseDeepURL(str(link),urlPos)
    timesProcess-=1

lastLinkName = re.search('by_(.+?).html',link).group(1)

print lastLinkName
