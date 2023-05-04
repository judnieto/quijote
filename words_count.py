"""
@author: Judit Nieto Parla
"""
import random
import sys
from pyspark import SparkContext


#Cuenta las palabras y las escribe en el fichero de salida

def main(infilename, outfilename):
    with SparkContext() as sc:
        sc.setLogLevel("ERROR")
        data = sc.textFile(infilename)
        words_rdd = data.map(lambda x: len(x.split()))
        words_list_collect = str(words_rdd.collect())
        suma = str(words_rdd.sum())
        with open (outfilename, 'w') as outfile:
             outfile.write(words_list_collect)
             outfile.write("\n RESULTS----------")
             outfile.write("\n")
             outfile.write(suma)

if __name__ == "__main__":
    if len(sys.argv)<3:
       print(f"Usage: {sys.argv[0]} <infilename> <outfilename>")
       exit(1)
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    main(infilename, outfilename)
