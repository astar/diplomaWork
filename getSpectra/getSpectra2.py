import sys, re, urllib2
if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'ssa'

print 'file:\t' + file

def readInput(file):
    f = open(file,'r')
    data = f.readlines()
    f.close()
    return data


def getLinks(data):
    good = list()
    goodLink = list()
    bad = list()
    for link in data:
        page = urllib2.urlopen(link)
        spage = page.read()
        page.close()
        s = re.findall('CDATA\[http.*\]',spage)
	if s:
       good.append(re.match(".*(http://.*)\]\]",s[0]).group(1))
	    goodLink.append(link)
	else:
	    bad.append(link)
    return good, goodLink, bad

def saveResult(file, data):
    """ Just save the data """
    """"""
    f = open(file,'w')
    f.write("\n".join(map(lambda x: str(x), data)) + "\n")
    f.close()

data = readInput(file)
good, goodLink, bad = getLinks(data)
saveResult('good',good)
saveResult('goodLink',goodLink)
saveResult('bad',bad)

print 'good:\t' + str(len(good))
print 'bad:\t' + str(len(bad))
