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
import os
from clinica import Clinica
from validaciones import solicitar_cadena, solicitar_entero, solicitar_obra_social
from turno import Turno

def generar_configs_json():
    """
    Genera el archivo configs.json si no existe, con las configuraciones iniciales.
    """
    if not os.path.exists('configs.json'):
        especialidades = {
            "Odontologia": 4000,
            "Medico Clinico": 4000,
            "Psicologia": 4000,
            "Traumatologia": 4000
        }
        obras_sociales = {
            "Swiss Medical": {"descuento": 0.4, "edad_extra": 0.1},
            "Apres": {"descuento": 0.25, "edad_extra": 0.03},
            "PAMI": {"descuento": 0.6, "edad_extra": 0.03},
            "Particular": {"recargo": 0.05, "edad_extra": 0.15}
        }
        configs = {
            "especialidades": especialidades,
            "obras_sociales": obras_sociales
        }
        with open('configs.json', 'w') as file:
            json.dump(configs, file, indent=4)
            print("Archivo configs.json creado exitosamente.")

def cargar_configs():
    """
    Carga las configuraciones desde el archivo configs.json.
    """
    with open("configs.json", "r") as f:
        configs = json.load(f)
    return configs

# Función principal de la aplicación
def main_app():
    generar_configs_json()
    configs = cargar_configs()
    
    clinica = Clinica("UTN-Medical Center", configs["especialidades"], configs["obras_sociales"])
    clinica.cargar_datos()
    while True:
        print("Menú de opciones:")
        print("1. Alta paciente")
        print("2. Alta turno")
        print("3. Ordenar turnos")
        print("4. Mostrar pacientes en espera")
        print("5. Atender pacientes")
        print("6. Cobrar atenciones")
        print("7. Cerrar caja")
        print("8. Mostrar informe")
        print("9. Salir")

        opcion = solicitar_entero("Seleccione una opción: ", 1, 9)

        match opcion:
            case 1:
                nombre = solicitar_cadena("Ingrese nombre del paciente: ", 30)
                apellido = solicitar_cadena("Ingrese apellido del paciente: ", 30)
                dni = solicitar_entero("Ingrese DNI del paciente: ")
                edad = solicitar_entero("Ingrese edad del paciente: ", 18, 90)
                obra_social = solicitar_obra_social(edad)
                clinica.cargar_paciente(nombre, apellido, dni, edad, obra_social)  # Corregido aquí
            case 2:
                id_paciente = solicitar_entero("Ingrese ID del paciente: ")
                especialidad = input("Ingrese especialidad (Medico Clinico, Odontologia, Psicologia, Traumatologia): ")
                #monto = 4000
                #turno = Turno(id_paciente, especialidad, monto)
                clinica.cargar_turno(id_paciente, especialidad)
            case 3:
                print("1. Ordenar por obra social ASC")
                print("2. Ordenar por monto DESC")
                criterio = solicitar_entero("Seleccione un criterio: ", 1, 2)
                clinica.ordenar_turnos('obra_social' if criterio == 1 else 'monto')
            case 4:
                clinica.mostrar_pacientes_en_espera()
            case 5:
                clinica.atender_pacientes()
            case 6:
                clinica.cobrar_atenciones()
            case 7:
                clinica.cerrar_caja()
            case 8:
                clinica.mostrar_informe()
            case 9:
                print("Saliendo del programa...")
                break
    #clinica.actualizar_archivos()

if __name__ == "__main__":
    main_app()