import sys
import signal
from gpiozero import LED
#llamamos la clase Conexion de Conexion.py
from Conexion import Conexion

led = LED(17)

def procesa(respuesta):
    print respuesta

    if respuesta:
    	led.on()
    	print "Encendido"
    else:
    	led.off()
    	print "Apagado"
    sys.stdout.flush()


try:
	print "Inicio"
	t = Conexion(procesa)
	t.daemon=True
	t.start()
	signal.pause()
except (KeyboardInterrupt, SystemExit):
	raise
	print "Salida"
