import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

for line in sys.stdin:
    line = line.strip()
    word = line.split('   ')
    word = word[0]
    
    sys.stdout.write("{}\t1\n".format(word))
