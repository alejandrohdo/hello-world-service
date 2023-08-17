import time
import os
import subprocess

class HelloWorldSvc:
    def __init__(self):
        self.isAlive = True

    def stop(self):
        self.isAlive = False

    def run(self):
        log_file = os.path.join(os.path.dirname(__file__), 'service.log')
        while self.isAlive:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            message = f"{current_time} - Hello World"
            
            # Escribir en el archivo de registro
            with open(log_file, 'a') as f:
                f.write(message + '\n')
            
            print(message)  # Mostrar mensaje en la consola
            time.sleep(5)  # Esperar 5 segundos

if __name__ == '__main__':
    svc = HelloWorldSvc()
    svc.run()
