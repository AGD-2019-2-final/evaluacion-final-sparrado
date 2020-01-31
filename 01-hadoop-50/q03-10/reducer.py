import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import re

if __name__ == '__main__':
    for line in sys.stdin:

        orden = re.sub("\n","",line)
        lista = orden.split(",")

        sys.stdout.write("{},{}\n".format(lista[1],lista[0]))