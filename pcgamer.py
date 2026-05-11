import datetime
import math
from time import strftime
continuar="si"
while continuar == "si" :
 print("\n--- Simulador de Ahorro para PC Gamer ---")
 procesador=input("Que procesador quieres para tu PC gamer? ")
 Tarjeta_de_video=input("Que tarjeta de video quieres para tu PC gamer? ") 
 Placa_madre=input("Que placa madre quieres para tu PC gamer? ")
 Ram=input("Cuanta RAM quieres para tu PC gamer? ")
 Fuente_de_poder=input("Que fuente de poder quieres para tu PC gamer? ")
 ssd=input("Que SSD quieres para tu PC gamer? ")
 case=input("Que case quieres para tu PC gamer? ")
 precio_placa = int(input("Cuanto cuesta la placa madre? "))
 precio_ram = int(input("Cuanto cuesta la RAM? "))
 precio_ssd = int(input("Cuanto cuesta el SSD? "))
 precio_fuente = int(input("Cuanto cuesta la fuente de poder? "))
 precio_case = int(input("Cuanto cuesta el case? "))
 otros_componentes = precio_placa + precio_ram + precio_ssd + precio_fuente + precio_case
 precio_del_procesador=int(input("Cuanto cuesta el procesador? "))
 precio_de_la_tarjeta_de_video=int(input("Cuanto cuesta la tarjeta de video? "))
 Ahorro_actual=int(input("Cuanto dinero tienes ahorrado hoy? "))
 total=precio_del_procesador+precio_de_la_tarjeta_de_video+otros_componentes
 Faltante=total-Ahorro_actual
 nombre="input('Cual es tu nombre papu? ')"
 edad_actual=int(input("Cuantos años tienes? "))
 mes_meta=input("En que mes del año quieres comprar tu PC gamer? ")
 print(f"Soy {nombre} tengo {edad_actual} años para mi Pc gamer de {mes_meta} necesito un {procesador} de {precio_del_procesador} soles y una {Tarjeta_de_video} de {precio_de_la_tarjeta_de_video} y otros componentes de {otros_componentes} soles me saldrian {total} soles.")
 if Ahorro_actual >=total:
  print("¡Felicidades! Ya tienes suficiente dinero para comprar tu Pc gamer.")
 else:
    print(f"Ponte a ahorrar solo te faltan {Faltante} soles.")
    Ahorro_semanal=int(input("Cuanto vas a ahorrar durante la semana? "))
    semanas_faltantes = math.ceil(Faltante / Ahorro_semanal)
    print(f"Ponte a ahorrar {Faltante} soles en {semanas_faltantes} semanas.")
    Fecha_log=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ahorro_pc_gamer.txt", "a") as archivo:
        archivo.write(f" fecha:{Fecha_log}Total: {total} soles, Faltante: {Faltante} soles, Semanas Faltantes: {semanas_faltantes}\n")
 continuar = input("\n¿Quieres hacer otro cálculo? (si/no): ").lower()




