# Ejercicio 1
# num1 = int(input("Ingrese el primer numero"))
# num2 = int(input("Ingrese el segundo numero"))
# num3 = int(input("Ingrese el tercer numero"))

# suma = num1 + num2 + num3
# print(f"#1 {num1}  #2 {num2} #3 {num3} suma: {suma}")


# Ejercicio 2
# n1 = int(input("Ingrese el primer numero"))
# n2 = int(input("Ingrese el segundo numero"))

# suma = n1 + n2 
# print(f"#1 {n1}  #2 {n2} suma: {suma}")
# resta = n1 - n2
# print(f"#1 {n1}  #2 {n2} resta: {resta}")
# multiplicacion = n1 * n2
# print(f"#1 {n1}  #2 {n2} multiplicacion: {multiplicacion}")
# division = n1 / n2
# print(f"#1 {n1}  #2 {n2} division: {division}")


# Ejercicio 3
# contador = 0
# notas = []
# while contador < 3:
#     contador += 1
#     nota = float(input("Ingrese la nota: "))
#     notas.append(nota)

# definitiva = sum(notas) / len(notas)
# print(f"definitiva final: {definitiva}")


# Ejercicio 4
# contador = 0
# notas = []
# while contador < 3:
#     contador += 1
#     nota = float(input("Ingrese la nota: "))
#     notas.append(nota)

# definitiva = ((notas[0] * 0.20) + (notas[1] * 0.30) + (notas[2] * 0.50))
# print(f"definitiva final: {definitiva}")


# Ejercicio 5
# distancia = int(input("Ingrese la distancia en kl: "))
# tiempo = int(input("Ingrese el tiempo en el que recorrio la distancia en h: "))
# velocidad = distancia / tiempo
# print(f"un vehiculo que va a una distancia de {distancia} kilometros en un tiempo de {tiempo} hora(s) va a una velocidad de {velocidad} km/h")


# Ejercicio 6
# valor = int(input("Ingrese el valor correspondiente a la compra: "))
# IVA = 0.19
# DESCUENTO = 0.10
# valorIva = valor * IVA
# valorDescuento = valor - (valor * DESCUENTO) 
# if valor > 100:
#     valorfinal = valorDescuento + (valorDescuento * IVA) 
#     print(f"A su compra se le aplica descuento, total de la compra {valor} monto IVA {IVA} descuento {DESCUENTO} total a pagar {valorfinal}")
# else:
#     print(f"A su compra no se le aplica descuento, total de la compra {valor} monto IVA {IVA} valor a pagar {valorIva}")


# 7.	Dada una cantidad de tiempo medida en horas, minutos y segundos, diga a cuántos segundos equivale.
# def tiempo_a_segundos(horas, minutos, segundos):
#     total_segundos = horas * 3600 + minutos * 60 + segundos
#     return total_segundos

# horas = int(input("Ingrese las horas: "))
# minutos = int(input("Ingrese los minutos: "))
# segundos = int(input("Ingrese los segundos: "))

# resultado = tiempo_a_segundos(horas, minutos, segundos)
# print(f"El tiempo total en segundos es: {resultado}")


# 8) Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto
# dinero ganará después de un mes si el banco paga a razón de 2% mensual.
# capital = float(input("Ingrese el capital a invertir: "))

# interes = capital * 0.02

# total = capital + interes

# print(f"Interés ganado en un mes: ${interes}")
# print(f"Total después de un mes: ${total}")


# 9) Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber 
# cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza
# en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones
# sueldo_base = float(input("Ingrese el sueldo base del vendedor: "))

# venta1 = float(input("Ingrese el valor de la primera venta: "))
# venta2 = float(input("Ingrese el valor de la segunda venta: "))
# venta3 = float(input("Ingrese el valor de la tercera venta: "))

# comisiones = (venta1 + venta2 + venta3) * 0.10

# total_mes = sueldo_base + comisiones

# print(f"Comisiones del mes: ${comisiones}")
# print(f"Total a recibir en el mes: ${total_mes}")


# 10) Una tienda ofrece un descuento del 15% sobre el total de la compra
# y un cliente desea saber cuánto deberá pagar finalmente por su compra.
# total_compra = float(input("Ingrese el total de la compra: "))

# descuento = total_compra * 0.15

# total_final = total_compra - descuento

# print(f"Descuento aplicado: ${descuento}")
# print(f"Total a pagar: ${total_final}")


# 11) Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.  Dicha calificación se compone de los siguientes porcentajes:
# 	55% del promedio de sus tres calificaciones parciales.
#  	30% de la calificación del examen final. 
# 	15% de la calificación de un trabajo final

# parcial1 = float(input("Ingrese la calificación del primer parcial: "))
# parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
# parcial3 = float(input("Ingrese la calificación del tercer parcial: "))

# promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

# examen_final = float(input("Ingrese la calificación del examen final: "))

# trabajo_final = float(input("Ingrese la calificación del trabajo final: "))

# nota_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

# print(f"La calificación final en Algoritmos es: {nota_final}")


# 12.	Un maestro desea saber qué porcentaje de hombres y qué porcentaje de mujeres hay en un grupo de alumnos.
# Solicitar el número de hombres y mujeres
# hombres = int(input("Ingrese la cantidad de hombres: "))
# mujeres = int(input("Ingrese la cantidad de mujeres: "))

# total = hombres + mujeres

# porcentaje_hombres = (hombres / total) * 100
# porcentaje_mujeres = (mujeres / total) * 100

# print(f"Porcentaje de hombres: {porcentaje_hombres}%")
# print(f"Porcentaje de mujeres: {porcentaje_mujeres}%")


# 13) Dada las horas trabajadas de una persona y el valor por hora. Calcular su salario e imprimirlo. 
# horas_trabajadas = int(input("Ingrese la cantidad de horas que trabajó: "))
# valor_hora = 75
# salario = horas_trabajadas*valor_hora
# print(f"Tu salario segun las horas trabajadas es de {salario}")


# 14) Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de varios artículos (4) determinados,
# del que se adquieren una o varias unidades. El IVA es del 19%.
# Lista de productos con nombre y precio

# productos = ["Pan", "Agua", "Huevos", "Arroz"]
# precios = [25000, 40000, 85000, 120000]
# IVA = 0.19

# def emitir_factura():
#     print("FACTURA DE COMPRA")
#     total_sin_iva = 0

#     for i in range(len(productos)):
#         cantidad = int(input(f"¿Cuántos '{productos[i]}' desea comprar? "))
#         subtotal = precios[i] * cantidad
#         print(f"{productos[i]} x {cantidad} = ${subtotal}")
#         total_sin_iva += subtotal

#     iva = total_sin_iva * IVA
#     total_con_iva = total_sin_iva + iva

#     print(f"Subtotal: ${total_sin_iva}")
#     print(f"IVA 19%: ${iva}")
#     print(f"Total a pagar: ${total_con_iva}")

# emitir_factura()



# 15) Suponga que tiene Ud. una tienda y desea registrar las ventas en una computadora. Diseñe un algoritmo en pseudocódigo que lea por cada cliente: 
# ●	El monto de la venta, calcule e imprima el IVA.
# ●	calcule e imprima el total a pagar 
# ●	lea la cantidad con la que paga el cliente (solo efectivo), calcule e imprima el cambio.
# IVA = 0.19
# def registrar_venta():
#     monto_venta = float(input("Ingrese el monto de la venta: "))
#     pago_cliente = float(input("Ingrese la cantidad con la que pagará: "))
#     monto_iva = monto_venta * IVA
#     total = monto_iva + monto_venta
#     print(f"Se paga con {pago_cliente}")
#     print(f"La venta es de {monto_venta}")
#     print(f"El IVA es de: {monto_iva}")
#     print(f"Total a pagar: {total}")
#     if pago_cliente >= total:
#         cambio = pago_cliente - total
#         print(f"El cambio es de {cambio}")
#         print(f"Compra realizada")
#     else:
#         print(f"Cantidad insuficiente")
#         print(f"No se realizó la compra")

# registrar_venta()


# 16) Suponga que un conductor le pide a usted que le haga un algoritmo para calcular cuánto le corresponde en un día trabajado,
# teniendo en cuenta que tiene derecho a el 19% del total recaudado.
# porcentaje = 0.19
# def pago_conductor():
#     total_recaudado = float(input("Ingrese el total que recaudó: "))
#     pago = total_recaudado * porcentaje
#     print(f"De {total_recaudado} recaudado, le corresponde {pago}")

# pago_conductor()


# 17) Desarrollar un algoritmo que permita generar la colilla de pago de los empleados de una empresa. La colilla debe mostrar:
# ●	El Salario del Empleado 
# ●	El Valor de Ahorro mensual programado.
# ●	La suma a deducir por aporte a la Salud (EPS) 12,5 %
# ●	La suma a deducir por aporte al Fondo de Pensiones  16%
# ●	Total a Recibir 
# ●	Toda la información que debe proveer el usuario del programa es el  Salario del Empleado y el Valor de Ahorro mensual programado.
# El programa debe calcular y devolver el resto de los datos.
# EPS = 0.125
# PENSION = 0.16  

# salario = float(input("Ingrese el salario del empleado: "))
# ahorro_programado = float(input("Ingrese el valor de ahorro mensual programado: "))

# deduccion_eps = salario * EPS
# deduccion_pension = salario * PENSION

# total_deducciones = deduccion_eps + deduccion_pension + ahorro_programado

# total_a_recibir = salario - total_deducciones

# print("--- COLILLA DE PAGO ---")
# print(f"Salario bruto: ${salario}")
# print(f"Ahorro mensual programado: ${ahorro_programado}")
# print(f"Deducción por EPS: ${deduccion_eps}")
# print(f"Deducción por Pensión: ${deduccion_pension}")
# print(f"Total a recibir: ${total_a_recibir}")


# 18) En una universidad los estudiantes pueden pagar el valor de su matrícula en cuatro cuotas de la siguiente forma 
# ●	Primera cuota: 40% 
# ●	Segunda cuota: 25%
# ●	 Tercera cuota: 20% 
# ●	Cuarta cuota: 15% 

# cuota1_pct = 0.40
# cuota2_pct = 0.25
# cuota3_pct = 0.20
# cuota4_pct = 0.15

# matricula = float(input("Ingrese el valor de la matrícula: "))

# cuota1 = matricula * cuota1_pct
# cuota2 = matricula * cuota2_pct
# cuota3 = matricula * cuota3_pct
# cuota4 = matricula * cuota4_pct

# print("--- VALORES DE LAS CUOTAS ---")
# print(f"Primera cuota (40%): ${cuota1}")
# print(f"Segunda cuota (25%): ${cuota2}")
# print(f"Tercera cuota (20%): ${cuota3}")
# print(f"Cuarta cuota (15%): ${cuota4}")


# 19) Ingresar, para un estudiante, sus 5 notas de un curso, nombre, programa, ficha.  Hacer un algoritmo que:
# Muestre el nombre
# Muestre el programa de formación
# Se debe calcular y mostrar su promedio final.
# nombre = str(input("Ingresa tu nombre: "))
# programa = str(input("Ingresa tu programa: "))
# ficha = int(input("Ingresa tu ficha: "))
# notas_curso = []

# while len(notas_curso) < 5:
#     nota = float(input("Ingresa una nota: "))
#     notas_curso.append(nota)

# promedio = sum(notas_curso) / len(notas_curso)
# print(f"El promedio final es de {promedio}")


# 20) Ingresar el precio de compra unitario de un producto y la cantidad de compra de dicho producto y un descuento. Calcular y mostrar el subtotal, el monto del IVA que es el 19% del subtotal, y el precio neto (precio parcial con el Monto del IVA).
# precio = float(input("ingresa el precio de tu producto"))
# cantidad = int(input("ingresa la cantidad del producto que llevas"))
# descuento = int(input("ingresa un descuento a aplicar (0.1-100)"))
# IVA = 0.19
# if descuento < 0:
#     print("no se puede tener un descuento negativo")
# elif descuento == 100:
#     print("tu compra ha sido gratis. feli dia")
# else: 
#     subtotal = precio * cantidad
#     subtotalDescuento = (precio * cantidad) - ((precio*cantidad) * (descuento * 0.1) )
#     total = subtotalDescuento + (subtotal*IVA)
#     print(f"subtotal: {subtotal} monto IVA: {subtotal*IVA} valor neto a pagar: {total} ")

# 21) Realice un algoritmo que permita realizar el cálculo del siguiente enunciado, se solicita el año de nacimiento del aprendiz, el nombre, la dirección, se requiere conocer la edad de la persona y la información completa ingresada. 
# añoNacimiento = int(input("ingresa tu año de nacimiento"))
# nombre = input("ingresa tu nombre")
# direccion = input("ingresa tu direccion")
# edad = 2025 - añoNacimiento
# print(f"nombre: {nombre}, edad: {edad}, direccion: {direccion}")

# 22)Se tienen tres baldes de agua, uno de cinco litros, otros de tres litros y otro de un litro; si el de un litro tarda una hora y media en llenarse, resuelva cuanto tiempo pueden tardar en llenarse los otros baldes. 

# Si tiene tres baldes, pero se desconoce su tamaño debe de resolver igualmente el ejercicio. 
# def calcularTiempo(*capacidad):
#     contador = 1
#     for balde in capacidad:
#         print(f"tiempo balde #{contador}: {balde * 1.5}") 
#         contador+=1

# def calcularCapacidad(*tiempos):
#     contador = 1
#     for tiempo in tiempos:
#         print(f"capacidad balde #{contador}: {11.111 * tiempo}") 
#         contador+=1

# 23) Una persona tarda 5 horas en subir una montaña de 7 metros, si un escalador desea subir más o menos de la montaña, cuanto tiempo tarda en subir. Debe de resolver el ejercicio. 

# 24) Un estudiante realiza un préstamo a un plazo de 5 años, donde la tasa fija de interés es del 5% anual, se debe solicitar el monto del préstamo y se desea calcular la siguiente información. 
# • Cuanto dinero se ha pagado de intereses en un año. 
# • Cuanto dinero se ha pagado de intereses en el tercer trimestre del año. 
# • Cuanto dinero se ha pagado de intereses en el primer mes. 
# • Cuanto dinero se paga en total del préstamo solicitado incluyendo intereses. 
# prestamo = int(input("ingresa el monto de tu prestamo"))
# interesAnual = prestamo * 0.05
# interesMensual = interesAnual / 12
# interesTotal = (prestamo * 0.05) * 5
# print(f"interes a pagar el primer año: {interesAnual} interes a pagar al tercer trimestre:{interesMensual*9} interes a pagar al primer mes {interesMensual} total a pagar: {total + interesTotal}")