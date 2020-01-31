import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.strip()
    fecha = line.split('   ')
    fecha = fecha[0]
    mes = line.split('-')
    mes = mes[1]
    
    
    sys.stdout.write("{}\t1\n".format(mes))