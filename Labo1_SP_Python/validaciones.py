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

def solicitar_entero(mensaje, min_value=None, max_value=None):
    """
    Solicita al usuario que ingrese un número entero dentro de un rango opcional.

    :param mensaje: Mensaje que se muestra al usuario.
    :param min_value: Valor mínimo aceptable (opcional).
    :param max_value: Valor máximo aceptable (opcional).
    :return: El valor entero ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if (min_value is not None and valor < min_value) or (max_value is not None and valor > max_value):
                print(f"El valor debe estar entre {min_value} y {max_value}")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese un número entero válido")

def solicitar_cadena(mensaje, max_length=None):
    """
    Solicita al usuario que ingrese una cadena de caracteres alfabéticos, con longitud máxima opcional.

    :param mensaje: Mensaje que se muestra al usuario.
    :param max_length: Longitud máxima permitida para la cadena (opcional).
    :return: La cadena de caracteres ingresada por el usuario.
    """
    while True:
        cadena = input(mensaje)
        if not cadena.isalpha():
            print("La cadena debe contener solo caracteres alfabéticos")
        elif max_length is not None and len(cadena) > max_length:
            print(f"La cadena no debe exceder {max_length} caracteres")
        else:
            return cadena

def solicitar_obra_social(edad):
    """
    Solicita al usuario que ingrese una obra social válida según la edad del paciente.

    :param edad: Edad del paciente.
    :return: La obra social ingresada por el usuario.
    """
    while True:
        obra_social = input("Ingrese obra social (Swiss Medical, Apres, PAMI, Particular): ")
        if edad >= 60:
            if obra_social != "PAMI":
                print("Para pacientes mayores de 60, solo PAMI está disponible")
            else:
                return obra_social
        else:
            if obra_social not in ["Swiss Medical", "Apres", "Particular"]:
                print("Obra social inválida")
            else:
                return obra_social

def validar_nombre_apellido(nombre):
    """
    Valida que un nombre o apellido contenga solo caracteres alfabéticos y no exceda 30 caracteres.

    :param nombre: El nombre o apellido a validar.
    :return: True si el nombre es válido, False en caso contrario.
    """
    return nombre.isalpha() and len(nombre) <= 30

def validar_edad(edad):
    """
    Valida que la edad esté entre 18 y 90 años.

    :param edad: La edad a validar.
    :return: True si la edad es válida, False en caso contrario.
    """
    return 18 <= edad <= 90

def validar_obra_social(obra_social, edad):
    """
    Valida que la obra social sea válida según la edad del paciente.

    :param obra_social: La obra social a validar.
    :param edad: La edad del paciente.
    :return: True si la obra social es válida, False en caso contrario.
    """
    obras_validas = ["Swiss Medical", "Apres", "PAMI", "Particular"]
    if edad >= 60 and obra_social != "PAMI":
        return False
    if edad < 60 and obra_social == "PAMI":
        return False
    return obra_social in obras_validas

def validar_especialidad(especialidad):
    """
    Valida que la especialidad médica sea una de las permitidas.

    :param especialidad: La especialidad médica a validar.
    :return: True si la especialidad es válida, False en caso contrario.
    """
    return especialidad in ["Medico Clinico", "Odontologia", "Psicologia", "Traumatologia"]