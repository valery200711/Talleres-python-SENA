from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, date

app = Flask(__name__)

def estilo():
    return render_template("index.html")

class Persona:
    def __init__(self, nombre, telefono, email, identificacion):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        self.__identificacion = identificacion

    def nombre(self): return self.__nombre
    def telefono(self): return self.__telefono
    def email(self): return self.__email
    def identificacion(self): return self.__identificacion

    def mostrar_info(self):
        print("--- Información de Persona ---")
        print("Nombre:", self.__nombre)
        print("Teléfono:", self.__telefono)
        print("Email:", self.__email)

usuarios = []

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        identificacion = request.form["identificacion"]

        persona = Persona(nombre, telefono, email, identificacion)
        usuarios.append(persona)
        return redirect(url_for("ver_usuarios"))

    return render_template("index.html")

@app.route("/usuarios")
def ver_usuarios():
    return render_template("usuarios.html", usuarios = usuarios)

if __name__ == "__main__":
    app.run(debug=True)



class Huesped(Persona):
    def __init__(self, nombre, telefono, email, identificacion, fecha_nacimiento, pais_origen, preferencias):
        super().__init__(nombre, telefono, email, identificacion)
        self.__fecha_nacimiento = fecha_nacimiento
        self.__pais_origen = pais_origen
        self.__preferencias = preferencias

    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.__fecha_nacimiento.year - ((hoy.month, hoy.day) < (self.__fecha_nacimiento.month, self.__fecha_nacimiento.day))
        print("Edad:", edad)

    def mostrar_info(self):
        print("--- Informacion del Huésped ---")
        super().mostrar_info()
        self.calcular_edad()
        print("Pais de origen:", self.__pais_origen)
        print("Preferencias alimentarias:", self.__preferencias)

class Empleado(Persona):
    def __init__(self, nombre, telefono, email, identificacion, cargo, salario, fecha_ingreso):
        super().__init__(nombre, telefono, email, identificacion)
        self.__cargo = cargo
        self.__salario = salario
        self.__fecha_ingreso = fecha_ingreso

    def calcular_antiguedad(self):
        hoy = date.today()
        antiguedad = hoy.year - self.__fecha_ingreso.year - ((hoy.month, hoy.day) < (self.__fecha_ingreso.month, self.__fecha_ingreso.day))
        print("Antigüedad:", antiguedad, "años")

    def mostrar_info(self):
        print("--- Información del Empleado ---")
        super().mostrar_info()
        print("Cargo:", self.__cargo)
        print("Salario:", self.__salario)
        self.calcular_antiguedad()

class Alojamiento:
    def __init__(self, numero, tipo, capacidad, precio):
        self.__numero = numero
        self.__tipo = tipo
        self.__capacidad = capacidad
        self.__precio = precio
        self.__disponible = True

    def calcular_precio_temporada(self, temporada):
        factor = {"alta": 1.5, "media": 1.2, "baja": 1.0}
        precio = self.__precio * factor.get(temporada, 1)
        print("Precio por noche en temporada", temporada, ": $", precio)

    def reservar(self): self.__disponible = False
    def liberar(self): self.__disponible = True
    def esta_disponible(self): return self.__disponible
    def numero(self): return self.__numero
    def tipo(self): return self.__tipo

    def mostrar_info(self):
        print("--- Información del Alojamiento ---")
        print("Número:", self.__numero)
        print("Tipo:", self.__tipo)
        print("Capacidad máxima:", self.__capacidad)
        print("Precio base por noche:", self.__precio)
        print("Disponible:", self.__disponible)

class ServicioAdicional:
    def __init__(self, nombre, descripcion, precio, duracion):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__duracion = duracion

    def precio(self): return self.__precio

    def mostrar_info(self):
        print("--- Servicio Adicional ---")
        print("Nombre:", self.__nombre)
        print("Descripción:", self.__descripcion)
        print("Precio:", self.__precio)
        print("Duración (horas):", self.__duracion)

class Reserva:
    def __init__(self, codigo, huesped, alojamiento, fecha_inicio, fecha_salida):
        self.__codigo_reserva = codigo
        self.__huesped = huesped
        self.__alojamiento = alojamiento
        self.__fecha_inicio = fecha_inicio
        self.__fecha_salida = fecha_salida
        self.__servicios_adicionales = []
        self.__precio_total = 0
        self.__estado = "confirmada"

    def calcular_noches(self):
        noches = (self.__fecha_salida - self.__fecha_inicio).days
        print("Noches de estadía:", noches)

    def agregar_servicio(self, servicio):
        self.__servicios_adicionales.append(servicio)

    def calcular_precio_total(self, temporada):
        noches = (self.__fecha_salida - self.__fecha_inicio).days
        total = noches * self.__alojamiento._Alojamiento__precio * {"alta": 1.5, "media": 1.2, "baja": 1.0}.get(temporada, 1)
        total += sum(s.precio() for s in self.__servicios_adicionales)
        self.__precio_total = total
        print("Precio total de la reserva:", total)

    def cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def esta_activa(self):
        return self.__estado in ["confirmada", "en_curso"]

    def mostrar_info(self):
        print("--- Información de la Reserva ---")
        print("Código:", self.__codigo_reserva)
        print("Huésped:", self.__huesped.nombre())
        print("Alojamiento número:", self.__alojamiento.numero())
        print("Estado:", self.__estado)
        print("Precio total:", self.__precio_total)

class Glamping:
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__alojamientos = []
        self.__huespedes = []
        self.__empleados = []
        self.__reservas = []
        self.__servicios_disponibles = []

    def agregar_alojamiento(self, alojamiento):
        self.__alojamientos.append(alojamiento)

    def registrar_huesped(self, huesped):
        self.__huespedes.append(huesped)

    def contratar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def agregar_servicio_disponible(self, servicio):
        self.__servicios_disponibles.append(servicio)

    def crear_reserva(self, huesped_id, alojamiento_num, fecha_inicio, fecha_salida):
        huesped = None
        for h in self.__huespedes:
            if h.identificacion() == huesped_id:
                huesped = h
                break

        alojamiento = None
        for a in self.__alojamientos:
            if a.numero() == alojamiento_num and a.esta_disponible():
                alojamiento = a
                break

        if huesped and alojamiento:
            nueva_id = len(self.__reservas) + 1
            reserva = Reserva(nueva_id, huesped, alojamiento, fecha_inicio, fecha_salida)
            self.__reservas.append(reserva)
            alojamiento.reservar()
            print("Reserva creada exitosamente.")
            return reserva

        print("No se pudo crear la reserva.")
        return

    def buscar_alojamiento_disponible(self, tipo):
        for a in self.__alojamientos:
            if a.tipo() == tipo and a.esta_disponible():
                a.mostrar_info()

    def calcular_ocupacion_actual(self):
        ocupados = 0
        total = len(self.__alojamientos)

        for a in self.__alojamientos:
            if not a.esta_disponible():
                ocupados += 1

        if total > 0:
            porcentaje = ocupados / total * 100
        else:
            porcentaje = 0
        print("Porcentaje de ocupación:", porcentaje,"%")

    def listar_reservas_activas(self):
        print("--- Reservas Activas ---")
        for r in self.__reservas:
            if r.esta_activa():
                r.mostrar_info()

    def generar_reporte_ingresos_mes(self, mes, ano):
        ingresos = 0
        for r in self.__reservas:
            if r._Reserva__fecha_inicio.month == mes and r._Reserva__fecha_inicio.year == ano:
                ingresos += r._Reserva__precio_total
        print("Ingresos del mes:", ingresos)
