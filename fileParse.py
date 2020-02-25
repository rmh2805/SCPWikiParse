import sys

def main(htmlFile):
    fp = open(htmlFile)
    lines = fp.readlines()
    fp.close()
    print('got lines')


argc = len(sys.argv)
if argc < 2:
    print('ERROR: USAGE `' + sys.rgv[0] + ' <htmlFile>`')
main(sys.argv[1])

