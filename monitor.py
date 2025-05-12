"""
https://psutil.readthedocs.io/en/latest/

- Mostrar el numero total de procesos en ejecucion
- Mostrar los nombres de los 3 procesos que màs CPU estàn utilizando
- Si hay mas de 100 procesos, imprimir "ALERTA: demasiados procesos"

"""
import psutil

def cantidad_procesos():
    # Mostrar todos los procesos en ejecucion
    # https://psutil.readthedocs.io/en/latest/#psutil.pids
    todos_procesos = psutil.pids()
    # .pids() devuelve una lista de todos los procesos. El numero total es el len de la lista
    print(f"Total de procesos en ejecucion: {len(todos_procesos)}")
    return todos_procesos



def mas_uso(procesos):
    # https://stackoverflow.com/questions/41206809/psutil-measuring-the-cpu-usage-of-a-specific-process
    # https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent
    # No pude hacer esta funcion

    uso = psutil.cpu_percent(interval=1, percpu=True)
        # Devuelve una lista con el uso CPU (en cada cpu) el mio tiene 8
    total = (sum(uso))/(len(uso)) # Suma todo el porcentaje de la lista y lo divide para sacar el average
    return total
        



def alerta(procesos):
    if (len(procesos ) > 100):
        return 'ALERTA: demasiados procesos'



def monitor():
    procesos = cantidad_procesos()
    print(alerta(procesos))
    print(f"Proceso que mas consume: {mas_uso(procesos)}")



def main():
    monitor()


if __name__ == "__main__":
    main()
