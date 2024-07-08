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

import datetime

class Paciente:
    def __init__(self, id, nombre, apellido, dni, edad, fecha_registro, obra_social):
        """
        Inicializa un objeto Paciente con los atributos dados.

        :param id: ID del paciente.
        :param nombre: Nombre del paciente.
        :param apellido: Apellido del paciente.
        :param dni: DNI del paciente.
        :param edad: Edad del paciente.
        :param fecha_registro: Fecha en la que el paciente fue registrado.
        :param obra_social: Obra social del paciente.
        """
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.fecha_registro = fecha_registro
        self.obra_social = obra_social

def __str__(self):
        """
        Devuelve una representación en cadena del objeto Paciente.

        :return: Una cadena que describe al paciente, incluyendo su nombre, apellido, DNI y obra social.
        """
        return f"Paciente {self.nombre} {self.apellido}, DNI: {self.dni}, Obra social: {self.obra_social}"