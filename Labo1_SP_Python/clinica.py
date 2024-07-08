# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import json
from paciente import Paciente
from turno import Turno
from validaciones import validar_nombre_apellido, validar_edad, validar_obra_social, validar_especialidad
from datetime import date, datetime


class Clinica:
    def __init__(self, razon_social, especialidades, obras_sociales):
        self.razon_social = razon_social
        self.lista_pacientes = []
        self.lista_turnos = []
        self.especialidades = especialidades
        self.obras_sociales_validas = obras_sociales
        self.recaudacion = 0
        self.next_patient_id = 1

    def cargar_datos(self):
        try:
            with open('pacientes.json', 'r') as file:
                pacientes_data = json.load(file)
                for paciente_data in pacientes_data:
                    if paciente_data:
                        paciente = Paciente(
                            paciente_data.get('id', 0),
                            paciente_data.get('nombre', ''),
                            paciente_data.get('apellido', ''),
                            paciente_data.get('dni', ''),
                            paciente_data.get('edad', 0),
                            datetime.strptime(paciente_data.get('fecha_registro', '1970-01-01'), '%Y-%m-%d').date(),
                            paciente_data.get('obra_social', '')
                        )
                        self.lista_pacientes.append(paciente)
                self.next_patient_id = max([p.id for p in self.lista_pacientes], default=0) + 1
        except FileNotFoundError:
            pass

        try:
            with open('turnos.json', 'r') as file:
                turnos_data = json.load(file)
                for turno_data in turnos_data:
                    if turno_data:
                        turno = Turno(
                            turno_data.get('id_paciente', 0),
                            turno_data.get('especialidad', ''),
                            turno_data.get('monto', 0.0),
                            datetime.strptime(turno_data.get('fecha', '1970-01-01'), '%Y-%m-%d').date(),
                            turno_data.get('estado', 'Activo')
                        )
                        self.lista_turnos.append(turno)
        except FileNotFoundError:
            pass

    def actualizar_archivos(self):
        with open('pacientes.json', 'w') as file:
            pacientes_serializados = [
                {
                    'id': paciente.id,
                    'nombre': paciente.nombre,
                    'apellido': paciente.apellido,
                    'dni': paciente.dni,
                    'edad': paciente.edad,
                    'fecha_registro': paciente.fecha_registro.strftime('%Y-%m-%d'),
                    'obra_social': paciente.obra_social
                }
                for paciente in self.lista_pacientes
            ]
            json.dump(pacientes_serializados, file, indent=4)

        with open('turnos.json', 'w') as file:
            turnos_serializados = [
                {
                    'id_paciente': turno.id_paciente,
                    'especialidad': turno.especialidad,
                    'monto': turno.monto,
                    'fecha': turno.fecha.strftime('%Y-%m-%d'),
                    'estado': turno.estado
                }
                for turno in self.lista_turnos
            ]
            json.dump(turnos_serializados, file, indent=4)

    def cargar_configuracion(self, configs):
        self.especialidades = configs['especialidades']
        self.obras_sociales_validas = configs['obras_sociales']

    def cargar_paciente(self, nombre, apellido, dni, edad, obra_social):
        if not validar_nombre_apellido(nombre) or not validar_nombre_apellido(apellido):
            print("Error: Nombre o apellido inválido.")
            return
        if not validar_edad(edad):
            print("Error: Edad inválida.")
            return
        if not validar_obra_social(obra_social, edad):
            print("Error: Obra social inválida.")
            return
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("Error: Ya existe un paciente con ese DNI.")
                return
        nuevo_paciente = Paciente(self.next_patient_id, nombre, apellido, dni, edad, date.today(), obra_social)
        self.lista_pacientes.append(nuevo_paciente)
        self.next_patient_id += 1
        print(f"Paciente {nombre} {apellido} registrado con éxito.")

    def cargar_turno(self, id_paciente, especialidad):
        paciente = next((p for p in self.lista_pacientes if p.id == id_paciente), None)
        if paciente is None:
            print("Error: Paciente no encontrado.")
            return

        monto_a_pagar = self.calcular_monto_a_pagar(id_paciente, especialidad)
        if monto_a_pagar is None:
            print("Error al calcular el monto a pagar.")
            return

        nuevo_turno = Turno(id_paciente, especialidad, monto_a_pagar, fecha=date.today())
        self.lista_turnos.append(nuevo_turno)
        print(f"Turno para {especialidad} registrado con éxito.")

    def calcular_monto_a_pagar(self, id_paciente, especialidad):
        precio_base = self.especialidades.get(especialidad, 4000)
        paciente = next((p for p in self.lista_pacientes if p.id == id_paciente), None)
        if not paciente:
            return None

        obra_social = paciente.obra_social
        edad = paciente.edad

        descuento = 0
        if obra_social == 'Swiss Medical':
            descuento = 0.40
            if 18 <= edad <= 60:
                descuento += 0.10
        elif obra_social == 'Apres':
            descuento = 0.25
            if 26 <= edad <= 59:
                descuento += 0.03
        elif obra_social == 'PAMI':
            descuento = 0.60
            if edad >= 80:
                descuento += 0.03
        elif obra_social == 'Particular':
            descuento = -0.05
            if 40 <= edad <= 60:
                descuento -= 0.15

        monto_a_pagar = precio_base * (1 - descuento)
        return monto_a_pagar
    
    def ordenar_turnos(self, criterio):
        if (criterio == 'obra_social'):
            self.lista_turnos.sort(key=lambda t: next((p.obra_social for p in self.lista_pacientes if p.id == t.id_paciente)))
        elif (criterio == 'monto'):
            self.lista_turnos.sort(key=lambda t: t.monto, reverse=True)
        print("Turnos ordenados.")

    def mostrar_pacientes_en_espera(self):
        pacientes_en_espera = [t for t in self.lista_turnos if t.estado == 'Activo']
        for turno in pacientes_en_espera:
            paciente = next((p for p in self.lista_pacientes if p.id == turno.id_paciente), None)
            if paciente:
                print(f"Paciente: {paciente.nombre} {paciente.apellido}, DNI: {paciente.dni}, Especialidad: {turno.especialidad}")

    def atender_pacientes(self):
        turnos_activados = [t for t in self.lista_turnos if t.estado == 'Activo']
        if not turnos_activados:
            print("No hay pacientes en espera.")
            return
        turnos_a_atender = turnos_activados[:2]
        for turno in turnos_a_atender:
            turno.estado = 'Finalizado'
        print("Pacientes atendidos.")

    def cobrar_atenciones(self):
        turnos_finalizados = [t for t in self.lista_turnos if t.estado == 'Finalizado']
        for turno in turnos_finalizados:
            turno.estado = 'Pagado'
            self.recaudacion += turno.monto
        print("Atenciones cobradas.")

    def cerrar_caja(self):
        turnos_activados = [t for t in self.lista_turnos if t.estado == 'Activo' or t.estado == 'Finalizado']
        if turnos_activados:
            print("Aún hay pacientes por atender.")
            return
        print(f"Total recaudado: ${self.recaudacion:.2f}")
        self.actualizar_archivos()

    def mostrar_informe(self):
        especialidades_count = {especialidad: 0 for especialidad in self.especialidades}
        for turno in self.lista_turnos:
            especialidades_count[turno.especialidad] += 1
        especialidad_menos_solicitada = min(especialidades_count, key=especialidades_count.get)
        print(f"La especialidad menos solicitada es: {especialidad_menos_solicitada}")
        
    """
    def actualizar_archivos(self):
        with open('pacientes.json', 'w') as file:
            json.dump([paciente.__dict__ for paciente in self.lista_pacientes], file, indent=4)
        with open('turnos.json', 'w') as file:
            json.dump([turno.__dict__ for turno in self.lista_turnos], file, indent=4)
    """