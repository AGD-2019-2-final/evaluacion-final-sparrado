import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
cont = 0
if __name__ == '__main__':
    
    for line in sys.stdin:
        if cont < 6:
            or_numero,letra,fecha,numero= line.split("\t")
            numero = int(numero)
            sys.stdout.write("{}   {}   {}\n".format(letra, fecha, numero))
            cont += 1