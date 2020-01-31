import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    def_min = 30
    def_maxi = 0

   
    for line in sys.stdin:

        key, val1, val2= line.split(",")
        val1 = float(val1)
        val2 = float(val2)

        if key == curkey:
            
            if def_maxi > val1:
                def_maxi= def_maxi
                
            else:
                def_maxi=val1
                
            if def_min < val2:
                def_min= def_min
                
            else:
                def_min=val2
            
        else:
           
            if curkey is not None:
               
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, def_maxi, def_min))

            curkey = key
            def_min = val2
            def_maxi = val1

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, def_maxi, def_min))