#Challenge 190
#Youtube Comment Scrapper

import urllib2

test = urllib2.urlopen('https://plus.googleapis.com/u/0/_/widget/render/comments?first_party_property=YOUTUBE&href=https://www.youtube.com/watch?v=dQw4w9WgXcQ')

print test.info()

html = test.read()

print html

test.close()