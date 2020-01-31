import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        line = line.split('   ')
        letra = line[0]
        fecha = line[1]
        numero = int(line[2])
        or_numero = "{:03.0f}".format(numero)
       
        
        sys.stdout.write("{}\t{}\t{}\t{}\n".format(letra,or_numero,fecha,numero))