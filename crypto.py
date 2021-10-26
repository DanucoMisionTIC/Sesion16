import os
import sys
hashseed = os.getenv('PYTHONHASHSEED')
if not hashseed:
    os.environ['PYTHONHASHSEED'] = '0'
    os.execv(sys.executable, [sys.executable] + sys.argv)

dato= "Hola Mundo"
valor= "semilla2"
dato_hash= hash(dato+valor)
print(dato_hash, len(str(dato_hash)))
