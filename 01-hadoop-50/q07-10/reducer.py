import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<

if __name__ == '__main__':

    for line in sys.stdin:
        letra,or_numero,fecha,numero= line.split("\t")
        numero = int(numero)
        sys.stdout.write("{}   {}   {}\n".format(letra, fecha, numero))