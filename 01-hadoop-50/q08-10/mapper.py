import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        line = line.split('   ')
        letra = line[0]
        numero = int(line[2])
        
        sys.stdout.write("{}\t{}\n".format(letra, numero))