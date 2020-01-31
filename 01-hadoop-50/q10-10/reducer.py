import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    total = 0

  
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
         
            total = str(total) + ',' + str(val)
        else:
         
            if curkey is not None:
                if curkey !=',':
                    sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = int(val)

    sys.stdout.write("{}\t{}\n".format(curkey, total))