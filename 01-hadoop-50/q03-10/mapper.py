import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import csv
if __name__ == "__main__":

    dato = sys.stdin.readlines()
    for line in csv.reader(dato):

        letra = line[0]
        numero = line[1]

        sys.stdout.write("{},{}\n".format(numero, letra))
