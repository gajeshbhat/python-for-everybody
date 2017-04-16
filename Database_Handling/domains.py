import sqlite3
import re

fileContent = open("mbox.txt")
domainDict = dict()

#Process data for storage

for line in fileContent:
    line.rstrip()
    if not line.startswith("From: "):continue
    pieces = line.split()
    email = pieces[1]
    parts = email.split('@')
    org = parts[-1]
    domainDict[org] = domainDict.get(org,0)+1

#Connect and Store in Database
connSlot = sqlite3.connect("test.db")
commandCursor = connSlot.cursor()

commandCursor.execute(''' CREATE TABLE Counts (org TEXT, count INTEGER) ''')

#Iterate through dict and store values in Database

for key,value in domainDict.items():
    commandCursor.execute(''' INSERT INTO Counts (org,count) VALUES(?,?) ''',(key,value))

connSlot.commit()

connSlot.close()
