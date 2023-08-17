
NOTA: Se tiene quee abrir el termial como administrador

nssm remove HelloWorld confirm

crear directamente del .py a servicio

nssm install HelloWorld "C:\Users\alejandrohdo\AppData\Local\Programs\Python\Python36\python.exe" "C:\Users\alejandrohdo\personal-projects\hello-world-service\mi-servicio\hello_world_service.py"

nssm start HelloWorld

nssm status HelloWorld

nssm stop HelloWorld


crear el servicio a partir de .bat
nssm install HelloWorld "C:\Users\alejandrohdo\personal-projects\hello-world-service\mi-servicio\start_script.bat"
