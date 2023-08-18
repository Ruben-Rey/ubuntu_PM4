import time

carpeta = "/home/ibiza/.pm2/logs/bot-prueba-out.log"
while True:
    with open(carpeta, "a") as log_file:
        print("Enviando informacion a ......")
        log_file.write("Enviando informacion a ......\n")
    
    time.sleep(0.1)  # Esperar 1 segundo entre cada registro