"""
Módulo de validadores
Contiene todas las funciones de validación de datos
"""

import re
import math
from tkinter import messagebox


class Validador:
    """Clase con métodos estáticos para validar datos"""
    
    @staticmethod
    def evaluar_expresion(valor_texto):
        """
        Evalúa una expresión matemática de manera segura.
        Soporta: números, sqrt, log, cos, sin, tan, pi, e
        
        Args:
            valor_texto: string con la expresión a evaluar
            
        Returns:
            tupla (es_valido, valor_float, mensaje_error)
        """
        valor_texto = valor_texto.strip()
        
        if not valor_texto:
            return False, None, "El campo está vacío"
        
        # Crear un diccionario seguro con solo funciones matemáticas permitidas
        diccionario_seguro = {
            'sqrt': math.sqrt,
            'log': math.log10,  # logaritmo base 10
            'ln': math.log,     # logaritmo natural
            'cos': math.cos,
            'sin': math.sin,
            'tan': math.tan,
            'pi': math.pi,
            'e': math.e,
            '__builtins__': {}
        }
        
        try:
            # Permitir operaciones básicas también: +, -, *, /, ^, etc.
            # Reemplazar ^ por ** para potencia (notación matemática)
            expresion_procesada = valor_texto.replace('^', '**')
            
            # Evaluar la expresión en un entorno seguro
            resultado = eval(expresion_procesada, diccionario_seguro)
            
            # Convertir a float si es necesario
            valor = float(resultado)
            return True, valor, None
            
        except ValueError as e:
            # Error matemático (ej: sqrt de número negativo)
            return False, None, (
                f"❌ Error matemático: {str(e)}\n\n"
                f"Ejemplos: sqrt(4), log(100), cos(0), sin(0), tan(0)"
            )
        except Exception as e:
            # Error de sintaxis u otros
            return False, None, (
                f"❌ El formato '{valor_texto}' no es válido\n\n"
                f"Funciones permitidas: sqrt, log, ln, cos, sin, tan\n"
                f"Ejemplos correctos:\n"
                f"  • Números: 3, 0.3, -1.2\n"
                f"  • Raíz: sqrt(2), sqrt(9)\n"
                f"  • Logaritmo: log(100), ln(2.718)\n"
                f"  • Trigonometría: sin(0), cos(0), tan(45)\n"
                f"  • Operaciones: 2+3, 5*2, 10/2, 2^3"
            )
    
    @staticmethod
    def es_numero_valido(valor_texto):
        """
        Valida que un texto sea un número válido (entero, decimal o expresión matemática)
        
        Args:
            valor_texto: string con el número a validar
            
        Returns:
            tupla (es_valido, valor_float, mensaje_error)
        """
        # Usar la nueva función que soporta expresiones matemáticas
        return Validador.evaluar_expresion(valor_texto)
    
    @staticmethod
    def validar_escalar(valor_texto):
        """
        Valida un valor escalar
        
        Args:
            valor_texto: string con el escalar
            
        Returns:
            tupla (es_valido, valor_float, mensaje_error)
        """
        valor_texto = valor_texto.strip()
        
        if not valor_texto:
            return False, None, "❌ Debes ingresar un ESCALAR\n\nEscribe un número en el campo 'ESCALAR'"
        
        return Validador.es_numero_valido(valor_texto)
    
    @staticmethod
    def validar_matriz_llena(matriz_entries):
        """
        Valida que todas las celdas de una matriz estén llenas
        
        Args:
            matriz_entries: lista de listas con tkinter Entry objects
            
        Returns:
            tupla (es_valida, posicion_vacia)
        """
        for fila_idx, fila_entries in enumerate(matriz_entries):
            for col_idx, entry in enumerate(fila_entries):
                valor_texto = entry.get().strip()
                
                if not valor_texto:
                    return False, (fila_idx + 1, col_idx + 1)
                
                # Validar que sea número
                es_valido, _, _ = Validador.es_numero_valido(valor_texto)
                if not es_valido:
                    return False, (fila_idx + 1, col_idx + 1)
        
        return True, None
    
    @staticmethod
    def obtener_valores_matriz(matriz_entries):
        """
        Extrae los valores de una matriz y los convierte a float
        
        Args:
            matriz_entries: lista de listas con tkinter Entry objects
            
        Returns:
            tupla (exito, valores, mensaje_error, posicion_error)
        """
        valores = []
        
        for fila_idx, fila_entries in enumerate(matriz_entries):
            fila = []
            for col_idx, entry in enumerate(fila_entries):
                valor_texto = entry.get().strip()
                
                if not valor_texto:
                    return (False, None, 
                        f"Celda vacía en Fila {fila_idx+1}, Columna {col_idx+1}",
                        (fila_idx, col_idx))
                
                # Validar y evaluar la expresión (números o funciones matemáticas)
                es_valido, valor, error = Validador.evaluar_expresion(valor_texto)
                if not es_valido:
                    return (False, None,
                        f"❌ Error en Fila {fila_idx+1}, Columna {col_idx+1}\n\n{error}",
                        (fila_idx, col_idx))
                
                fila.append(valor)
            
            valores.append(fila)
        
        return (True, valores, None, None)
    
    @staticmethod
    def validar_dimensiones_compatibles(cols_m1, filas_m2):
        """
        Valida que dos matrices sean compatibles para multiplicación
        
        Args:
            cols_m1: número de columnas de matriz 1
            filas_m2: número de filas de matriz 2
            
        Returns:
            tupla (es_compatible, mensaje_error)
        """
        if cols_m1 != filas_m2:
            return (False, 
                f"❌ Dimensiones incompatibles\n\n"
                f"Columnas de Matriz 1: {cols_m1}\n"
                f"Filas de Matriz 2: {filas_m2}\n\n"
                f"Las COLUMNAS de la primera deben ser iguales\n"
                f"a las FILAS de la segunda.")
        
        return (True, None)
