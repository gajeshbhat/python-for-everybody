import urllib
from BeautifulSoup import * #Importing all the Libraries.

htmlContent = urllib.urlopen("http://python-data.dr-chuck.net/comments_357365.html ")

pageData = BeautifulSoup(htmlContent)

spanTags = pageData('span')

tagNumSum = 0

for tag in spanTags:
    tagNumSum+=int(tag.contents[0])

print tagNumSum
