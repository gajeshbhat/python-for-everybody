import urllib
import xml.etree.ElementTree as ET
from xml.dom import minidom

def parse_xml(url):
    counts = []
    page = urllib.urlopen(url)
    tree = ET.parse(page)

    comments = tree.findall('comments/comment')

    for comment in comments:
        counts.append(int(comment.find('count').text))

    return sum(counts)

xmlURL=raw_input("Enter a XML URL Source : ")

print parse_xml(xmlURL)
