"""
Programmer 	:   EOF
E-mail 		:   jasonleaster@163.com
File        :   stanford.py
Date        :   2016.02.19

Description:
	This programmer will help user who is learn cs97 in stanford to download some pdf material in the website.

"""
import urllib
import urllib2
import json
import re
import time
try:
    from BeautifulSoup import *
except:
    from subprocess import call
    call(["pip", "install beautifulSoup"])

URL = "http://15445.courses.cs.cmu.edu/fall2017/slides/"
html = urllib.urlopen(URL).read()
soup = BeautifulSoup(html)
tags = soup('a')

downloadCount = 0

pattern = ".pdf$"
regex = re.compile(pattern)
for tag in tags:
    fileName = tag["href"]
    url = URL + fileName

    """
    search(string[, pos[, endpos]]) --> match object or None.
    Scan through string looking for a match, and return a corresponding
    MatchObject instance. Return None if no position in the string matches.
    """
    url = regex.search(url)
    regex.search
    if url is not None:
        url = url.string
        try:
            urllib.urlretrieve(url, fileName)
            print "Download from", url
            downloadCount += 1
        except:
            print "Analyse Failed"