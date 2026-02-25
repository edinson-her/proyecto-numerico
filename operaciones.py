import numpy as np

class OperacionesMatrices:
    """Clase para realizar operaciones con matrices"""
    
    @staticmethod
    def multiplicar_escalar_matriz(escalar, matriz):
        """
        Multiplica un escalar por una matriz
        
        Args:
            escalar: número (int o float)
            matriz: array de numpy
            
        Returns:
            Matriz resultante
        """
        try:
            resultado = escalar * matriz
            return resultado
        except Exception as e:
            raise ValueError(f"Error en operación: {str(e)}")
    
    @staticmethod
    def multiplicar_matrices(matriz1, matriz2):
        """
        Multiplica dos matrices
        
        Args:
            matriz1: primera matriz (array de numpy)
            matriz2: segunda matriz (array de numpy)
            
        Returns:
            Matriz resultante
        """
        try:
            if matriz1.shape[1] != matriz2.shape[0]:
                raise ValueError(
                    f"Dimensiones incompatibles: "
                    f"Matriz 1 ({matriz1.shape[0]}x{matriz1.shape[1]}) y "
                    f"Matriz 2 ({matriz2.shape[0]}x{matriz2.shape[1]})"
                )
            resultado = np.matmul(matriz1, matriz2)
            return resultado
        except Exception as e:
            raise ValueError(f"Error en operación: {str(e)}")
    
    @staticmethod
    def parse_matriz_desde_texto(texto):
        """
        Convierte texto en formato matriz a array de numpy
        Formato esperado: filas separadas por ; y elementos por comas
        Ejemplo: "1,2,3;4,5,6" -> [[1,2,3],[4,5,6]]
        
        Args:
            texto: string con la matriz
            
        Returns:
            Array de numpy
        """
        try:
            filas = texto.strip().split(';')
            matriz_list = []
            
            for fila in filas:
                elementos = [float(x.strip()) for x in fila.split(',') if x.strip()]
                if not elementos:
                    raise ValueError("Fila vacía detectada")
                matriz_list.append(elementos)
            
            if not matriz_list:
                raise ValueError("Matriz vacía")
            
            # Verificar que todas las filas tengan el mismo número de elementos
            num_columnas = len(matriz_list[0])
            for i, fila in enumerate(matriz_list):
                if len(fila) != num_columnas:
                    raise ValueError(
                        f"Fila {i+1} tiene {len(fila)} elementos, "
                        f"pero se esperaban {num_columnas}"
                    )
            
            return np.array(matriz_list)
        except ValueError as e:
            raise ValueError(f"Error al parsear matriz: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error inesperado: {str(e)}")
    
    @staticmethod
    def formato_matriz(matriz):
        """
        Convierte una matriz numpy a formato string legible
        
        Args:
            matriz: array de numpy
            
        Returns:
            String formateado
        """
        if len(matriz.shape) == 1:
            # Vector fila
            return "[" + "  ".join(f"{x:,.4g}" for x in matriz) + "]"
        else:
            # Matriz 2D
            filas = []
            for fila in matriz:
                filas.append("[" + "  ".join(f"{x:,.4g}" for x in fila) + "]")
            return "\n".join(filas)
