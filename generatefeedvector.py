import feedparser
import re

def getwordcounts(url):
    d = feedparser.parse(url)
    wc = {}

    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word] += 1
    return d.feed.title, wc

def getwords(html):
    txt = re.compile(r'<[^>]+>').sub('', html)
    words = re.compile(r'[^A-Z^a-z]+').split(txt)
    return [word.lower() for word in words if word!= '']

apcount = {}
wordcounts = {}
filedata = open('feedlist.txt')
feedlist = [line.strip('\n') for line in filedata.readlines()]
for feedurl in feedlist:
    print(feedlist.index(feedurl))
    title, wc = getwordcounts(feedurl)
    wordcounts[title] = wc
    for word, count in wc.items():
        apcount.setdefault(word,0)
        if count >= 1:
            apcount[word] += 1

wordlist = []
for w, bc in apcount.items():
    frac = float(bc)/len(feedlist)
    if frac >= 0.1 and frac <= 0.5:
        wordlist.append(w)

out = open('blogdata.txt', 'w')
out.write('Blog')
for word in wordlist:
    out.write(',' + word)
out.write('\n')
for blog,wc in wordcounts.items():
    out.write(blog)
    for word in wordlist:
        if word in wc:
            out.write(',' + str(wc[word]))
        else:
            out.write(',0')
    out.write('\n')


dicttt = sorted(apcount.items(), key=lambda d:d[1], reverse = True)
print(dicttt)




print(123)
print(123)