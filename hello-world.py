import time
import win32serviceutil
import win32service
import win32event
import servicemanager
import os

class HelloWorldSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "HelloWorld"
    _svc_display_name_ = "Hello World Service"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        self.isAlive = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.isAlive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_,''))
        self.main()

    def main(self):
        log_file = os.path.join(os.path.dirname(__file__), 'service.log')
        while self.isAlive:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            message = f"{current_time} - Hello World"
            
            # Escribir en el archivo de registro
            with open(log_file, 'a') as f:
                f.write(message + '\n')
            
            servicemanager.LogInfoMsg(message)  # Escribir en el registro de eventos
            time.sleep(5)  # Esperar 5 segundos

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(HelloWorldSvc)
