#Este es script proporciona de identificar un aminoácido que forma parte de una estructura secundaria de proteínas
import pandas as pd
import subprocess
def run_gc_script(script_path):
    try:
        # Ejecuta el script R usando Rscript
        result = subprocess.run(
            ["Rscript", script_path],
            capture_output=True,
            text=True,
            check=True
        )
        print("Salida de R:\n", result.stdout)
    except FileNotFoundError:
        print("Error: No se encontró 'Rscript'. Asegúrate de tener R instalado y en el PATH.")
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el script R:\n", e.stderr)
