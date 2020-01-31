import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    line = line.strip()
    #line = line.split('\t1')
    line = line.split('   ')
    letra = line[0]
    maxi = line[2]
    mini = line[2]
    
    sys.stdout.write("{},{},{}\n".format(letra, maxi, mini))
