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


from datetime import date

class Turno:
    def __init__(self, id_paciente, especialidad, monto, fecha=date.today(), estado='Activo'):
        """
        Inicializa un objeto Turno con los atributos dados.

        :param id_paciente: ID del paciente asociado al turno.
        :param especialidad: Especialidad médica del turno.
        :param monto: Monto a pagar por el turno.
        :param fecha: Fecha del turno (por defecto es la fecha actual).
        :param estado: Estado del turno (por defecto es 'Activo').
        """
        self.id_paciente = id_paciente
        self.especialidad = especialidad
        self.monto = monto
        self.fecha = fecha
        self.estado = estado

    def __dict__(self):
        """
        Convierte el objeto Turno en un diccionario.

        :return: Un diccionario con los atributos del turno.
        """
        return {
            'id': self.id,
            'id_paciente': self.id_paciente,
            'especialidad': self.especialidad,
            'monto': self.monto,
            'estado': self.estado
        }