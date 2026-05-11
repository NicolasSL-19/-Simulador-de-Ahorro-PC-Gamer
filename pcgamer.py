import datetime
import math
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
 while True:
   try:
     precio_placa = int(input("Cuanto cuesta la placa madre? "))
     precio_ram = int(input("Cuanto cuesta la RAM? "))
     precio_ssd = int(input("Cuanto cuesta el SSD? "))
     precio_fuente = int(input("Cuanto cuesta la fuente de poder? "))
     precio_case = int(input("Cuanto cuesta el case? "))
     precio_del_procesador=int(input("Cuanto cuesta el procesador? "))
     precio_de_la_tarjeta_de_video=int(input("Cuanto cuesta la tarjeta de video? "))
     edad_actual=int(input("Cuantos años tienes? "))
     Ahorro_actual=int(input("Cuanto dinero tienes ahorrado hoy? "))
     Ahorro_semanal=int(input("Cuanto vas a ahorrar durante la semana? "))
     break
   except ValueError:
        print("Por favor, ingresa un número válido para los precios.")
 otros_componentes = precio_placa + precio_ram + precio_ssd + precio_fuente + precio_case
 cupon=input("Cual es tu codigo de descuento? (si no tienes presiona enter) ").upper()
 total=precio_del_procesador+precio_de_la_tarjeta_de_video+otros_componentes
 if cupon == "GIUX20":
     total_con_descuento = total * 0.20 # Aplicar descuento del 20% 
 else :
     total_con_descuento = 0
     print("No se aplico un descuento")
 total_final =total - total_con_descuento
 Faltante=total_final -Ahorro_actual
 nombre=input("Cual es tu nombre papu? ")
 moneda_local=input("Cual es tu moneda local ")
 mes_meta=input("En que mes del año quieres comprar tu PC gamer? ")
 print(f"Soy {nombre} tengo {edad_actual} años para mi Pc gamer de {mes_meta} necesito un {procesador} de {precio_del_procesador} {moneda_local} y una {Tarjeta_de_video} de {precio_de_la_tarjeta_de_video}  {moneda_local} y otros componentes de {otros_componentes} {moneda_local} en total necesito {total_final} {moneda_local} para comprar mi PC gamer")
 if Ahorro_actual >=total:
  print("¡Felicidades! Ya tienes suficiente dinero para comprar tu Pc gamer.")
 else:
    print(f"Ponte a ahorrar solo te faltan {Faltante} {moneda_local}.")
    semanas_faltantes = math.ceil(Faltante / Ahorro_semanal)
    print(f"Ponte a ahorrar {Faltante} {moneda_local} en {semanas_faltantes} semanas.")
    Fecha_log=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ahorro_pc_gamer.txt", "a") as archivo:
        archivo.write(f" fecha:{Fecha_log}Total: {total} {moneda_local}, Faltante: {Faltante} {moneda_local}, Semanas Faltantes: {semanas_faltantes}\n")
 continuar = input("\n¿Quieres hacer otro cálculo? (si/no): ").lower()



