import logging

# DEBUG = 10 = debug
# INFO = 20 = info
# WARNING = 30 = warning
# ERROR = 40 = error
# CRITICAL = 50 = critical

logging.basicConfig(level=logging.INFO,
                    format="%(threadName)s - %(levelname)s - %(asctime)s - Message:%(message)s",
                    datefmt="%Y/%m/%d",
                    filename="codigofacilito.log",
                    filemode="a"
                )
                    

def suma(numero1: int, numero2: int) -> int:
    """Permite sumar 2 números enteros.

    Args:
        numero1 (int): 
        numero2 (int):

    Returns:
        : int
    """
    
    logging.debug('Entramos aquí!!!!')
    
    resultado = numero1 + numero2
    
    logging.debug('Nos encontramos en esta línea.')
    
    return resultado


if __name__ == '__main__':
    logging.debug('Antes del llamado de la función.')
    
    resultado = suma(15, 20)
    logging.info(resultado)
    