import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":
	for line in sys.stdin:
		numeros = int(line.split('\t')[0])
		numeros_f = "{:03.0f}".format(numeros)
		letra = line.split('\t')[1]
		letra = letra.rstrip('\r\n')
		letra_ = letra.split(',')
		for i in range(len(letra)):
			sys.stdout.write("{}\t{}\n".format(str(letra[i]),numeros_f))