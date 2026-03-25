"""
Módulo de validadores
Contiene todas las funciones de validación de datos
"""

import re
from tkinter import messagebox


class Validador:
    """Clase con métodos estáticos para validar datos"""
    
    @staticmethod
    def es_numero_valido(valor_texto):
        """
        Valida que un texto sea un número válido (entero o decimal)
        
        Args:
            valor_texto: string con el número a validar
            
        Returns:
            tupla (es_valido, valor_float, mensaje_error)
        """
        valor_texto = valor_texto.strip()
        
        if not valor_texto:
            return False, None, "El campo está vacío"
        
        # Validar formato: debe tener parte entera
        if not re.match(r'^-?\d+(\.\d+)?$', valor_texto):
            return False, None, (
                f"❌ El formato '{valor_texto}' no es válido\n\n"
                f"Ejemplos correctos: 3, 0.3, 3.5, -1.2\n"
                f"Ejemplos incorrectos: .3, .05, 1., -.5"
            )
        
        try:
            valor = float(valor_texto)
            return True, valor, None
        except ValueError:
            return False, None, f"❌ El valor '{valor_texto}' no es un número válido"
    
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
                
                # Validar formato
                if not re.match(r'^-?\d+(\.\d+)?$', valor_texto):
                    return (False, None,
                        f"❌ Formato inválido '{valor_texto}' en Fila {fila_idx+1}, Columna {col_idx+1}\n\n"
                        f"Ejemplos correctos: 3, 0.3, 3.5, -1.2\n"
                        f"Ejemplos incorrectos: .3, .05, 1., -.5",
                        (fila_idx, col_idx))
                
                try:
                    fila.append(float(valor_texto))
                except ValueError:
                    return (False, None,
                        f"Valor inválido '{valor_texto}' en Fila {fila_idx+1}, Columna {col_idx+1}",
                        (fila_idx, col_idx))
            
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
