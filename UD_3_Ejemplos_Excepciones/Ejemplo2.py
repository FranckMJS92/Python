import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | Linea %(lineno)d | %(messsage)s",
)

logging.info("INICIO DEL PROGRAMA")

contadorPositivos = 0
contadorTotal = 0
while contadorPositivos < 5:
    logging.debug(f"Iteracion {contadorTotal +1}")
    n = int(input("Ingresa un numero : "))
    contadorTotal += 1

    if n > 0:
        contadorPositivos += 1
    else:
        logging.warning("Numero negativo")

print(f"N° positivos {contadorPositivos}")
logging.info("FIN DEL PROGRAMA")
