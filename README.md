# quijote
Queremos contar las palabras de un fichero dado. En este caso, el fichero dado es el libro "Don Quijote de La Mancha".
El programa "percentage.py" extrae de forma aleatoria un porcentaje de las lines del fichero. Como datos de entrada tenemos el nombre del fichero de entrada, el nombre del fichero de salida y el ratio. El ratio es un número aleatorio entre 0 y 1, en este caso se ha tomado ratio=0.25. Para cada linea, se toma un número aleatorio y, si es menor que el ratio, se escribe dicha linea en el fichero de salida.
El programa "words_count.py" cuenta las palabras que hay en un fichero dado. Como datos de entrada tenemos el nombre del fichero de entrada y el nombre del fichero de salida. En el fichero de salida encontramos una lista con el número de palabras de cada fila y el número de palabras total.
El fichero "quijote_s05.txt" es el resultado de aplicar el programa "percentage.py" al fichero "quijote.txt"
EL fichero "out_quijote_s05.txt" es el resultado de aplicar el programa "words_count.py" al fichero "quijote_s05.txt".
El fichero "out_quijote.txt" es el resultado de aplicar el programa "words_count.py" al fichero "quijote.txt".
