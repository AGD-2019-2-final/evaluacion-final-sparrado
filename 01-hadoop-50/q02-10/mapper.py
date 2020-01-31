import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<

import csv
if __name__ == "__main__":

    dato = sys.stdin.readlines()
    for line in csv.reader(dato):

        purpose = line[3]
        ammount = line[4]

        sys.stdout.write("{}\t{}\n".format(purpose, ammount))
