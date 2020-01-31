import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == '__main__':

    curkey = None
    total = 0
    promedio = 0
    n=0
    

  
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
         
            total += val
            n += 1
            promedio = total/n
            
        else:
           
            if curkey is not None:
              
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, promedio))

            curkey = key
            total = val
            n = 1
            promedio = total/n

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, promedio))