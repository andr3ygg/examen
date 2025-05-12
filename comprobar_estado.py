"""
- Hacer una peticion GET
- Si el status que devuelve es 200, imprimir OK, sino devolver ERROR
- Si ocurre algun problema de conexion, devolver FALLO DE CONEXIÒN
https://developer.mozilla.org/es/docs/Web/HTTP/Reference/Status
https://docs.python-requests.org/en/latest/user/quickstart/#response-status-codes
"""
import requests


def comprobar_estado(url):
    # Tomar la URL en request y despues obtener su estado
    # Comprobar que el request se pueda hacer con try
    # https://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions
    try:
        request = requests.get(url)
        estado_request = request.status_code
        # Resolver lo que dice el examen
        # https://stackoverflow.com/questions/9191388/it-is-more-efficient-to-use-if-return-return-or-if-else-return
        return "OK" if estado_request == 200 else "ERROR"

    except requests.exceptions.RequestException:
        # requests.exceptions.RequestException maneja todas las excepciones posibles que pueden haber
        return "FALLO DE CONEXIÒN"


def main():
    respuesta = comprobar_estado("http://github.com/andr3ygg")
    # respuesta = comprobar_estado('http://api.ejemplo.com/')
    # API.EJEMPLO si funciona
    # respuesta = comprobar_estado('https://api.github.com/user')
    print(respuesta)


if __name__ == "__main__":
    main()
