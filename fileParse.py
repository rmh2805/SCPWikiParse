import sys

def main(htmlFile, divID="page-content", outputFile='out.txt'):
    fp = open(htmlFile)
    lines = fp.readlines()
    fp.close()
    

    j = 0
    while lines[j].strip() != "<div id=\""+ divID +"\">":
        j += 1
    
    j += 1
    divStart = j
    divCount = 1
    
    while divCount > 0:
        line = lines[j]
        divCount += line.count('<div')
        divCount -= line.count('</div')
        j += 1
    
    divEnd = j + 1

    links = []
    for i in range(divStart, divEnd):
        line = lines[i]
        line = line.split("<a href=\"")
        
        for j in range(1, len(line)):
            links.append(line[j].split('"')[0])
    
    toReturn = set()
    for link in links[:-2]:
        if link in toRemove or 'http://' in link:
            continue
        toReturn.add(link)

    return toReturn


toRemove = {'/heritage-collection-arc'} 


argc = len(sys.argv)
if argc < 2:
    print('ERROR: USAGE `' + sys.rgv[0] + ' <htmlFile>`')

links = main(sys.argv[1])
for link in links:
    print(link)


