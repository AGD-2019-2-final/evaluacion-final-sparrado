import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import csv
if __name__ == "__main__":

    file = sys.stdin.readlines()
    for line in csv.reader(file):
        
        word = line[2]
        
        sys.stdout.write("{}\t1\n".format(word))

