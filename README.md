# Detect_GuaninaCitosina
Esta herramienta  fue desarrollada en Python y complementos de desarrollo con Rscript, tiene la función de identificar un aminoácido que forma parte de una estructura secundaria de proteínas, además de detectar  la variación de contenidos de GC genómico
Se proporcionan los script en python GC.py y GC_complete.R
La forma de ejecución es la siguiente:
Deberas ejecutar el primer archivo GC.py
Dtect_GC.py -i input_file -o output_GC
Los parametros requeridos son:
-i Archivo de entrada (Acepta solo archivos fasta)
-o Especificar directorio de salida

Posteriormente deberás ejecutar el script en R, ya que la función de este refina los resultados obtenidos en la ejecución de Dtect_GC.py. Además , permite generar graficos sobre la variación de los contenidos de GC
GC_complete.R -i output_GC -o results_GC

Para ejecutar los scripts, es conveniente realizar la instalación de las siguientes librerias
-blast 2.0.9
-mouve 0.1.1
-brig 1.0

Se proporciona un archivo GC.yml de un ambiente conda para que lo descargue y configures el ambiente 
