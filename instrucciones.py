"""
Módulo de instrucciones del programa
Contiene los textos de ayuda para cada operación
"""

class Instrucciones:
    """Clase que contiene las instrucciones de uso del programa"""
    
    ESCALAR_MATRIZ = """
╔════════════════════════════════════════════════════════════════╗
║           INSTRUCCIONES: ESCALAR × MATRIZ                     ║
╚════════════════════════════════════════════════════════════════╝

¿QUÉ ES ESTA OPERACIÓN?
Multiplica un número simple (escalar) por todos los elementos de una matriz.

PASOS A SEGUIR:

1.  SELECCIONAR DIMENSIONES DE LA MATRIZ
   • Haz clic en el botón "SELECCIONAR DIMENSIONES"
   • Elige el tamaño de tu matriz (filas × columnas)
   • Ejemplos:
     - 2×2 para una matriz pequeña
     - 3×3 para una matriz mediana
   • Se creará automáticamente una tabla para llenar

2.  INGRESAR EL ESCALAR
   • En el campo "ESCALAR:", escribe un número
   • Puede ser entero o decimal:
     ✓ Ejemplos correctos: 2, 3.5, -1, -2.7
     ✗ Ejemplos incorrectos: .5, 1., -0.

3.  LLENAR LA MATRIZ
   • En la tabla de "MATRIZ", ingresa números en cada celda
   • Presiona TAB para moverte entre celdas
   • Todos los campos deben estar llenos
   • Acepta números enteros y decimales

4.  CALCULAR RESULTADO
   • Haz clic en el botón "CALCULAR"
   • El resultado aparecerá en la columna "RESULTADO"
   • Verás cada elemento multiplicado por el escalar

📝 EJEMPLO:
   Escalar: 2
   Matriz:  [1, 2]
            [3, 4]
   
   Resultado: [2, 4]
              [6, 8]

"""

    MATRIZ_MATRIZ = """
╔════════════════════════════════════════════════════════════════╗
║           INSTRUCCIONES: MATRIZ × MATRIZ                      ║
╚════════════════════════════════════════════════════════════════╝

¿QUÉ ES ESTA OPERACIÓN?
Multiplica dos matrices entre sí siguiendo las reglas del álgebra linear.

⚠️ REGLA IMPORTANTE:
Las COLUMNAS de la Matriz 1 deben ser IGUALES a las FILAS de la Matriz 2.
Ejemplo válido: Matriz 1 (2×3) × Matriz 2 (3×2) ✓
Ejemplo inválido: Matriz 1 (2×3) × Matriz 2 (2×3) ✗

PASOS A SEGUIR:

1.  SELECCIONAR DIMENSIONES - MATRIZ 1
   • Haz clic en "SELECCIONAR" de la MATRIZ 1
   • Elige el tamaño (filas × columnas)
   • Ejemplos: 2×2, 2×3, 3×2, etc.
   • Se creará una tabla para llenar

2.  LLENAR MATRIZ 1
   • Ingresa números en todas las celdas
   • Puedes usar enteros o decimales
   • Ejemplo:
     [1, 2]
     [3, 4]

3.  SELECCIONAR DIMENSIONES - MATRIZ 2
   • Haz clic en "SELECCIONAR" de la MATRIZ 2
   • Las FILAS deben coincidir con las COLUMNAS de Matriz 1
   • Si Matriz 1 tiene 3 columnas, 
     entonces Matriz 2 debe tener 3 filas
   • Ejemplo si Matriz 1 es 2×3:
     ✓ Matriz 2 puede ser 3×2, 3×3, 3×4, etc.
     ✗ Matriz 2 NO puede ser 2×2, 4×2, etc.

4.  LLENAR MATRIZ 2
   • Completa todas las celdas igual que con Matriz 1
   • Todos los valores deben estar presentes

5.  CALCULAR RESULTADO
   • Haz clic en "CALCULAR"
   • El resultado aparecerá en "RESULTADO"
   • La matriz resultante tendrá:
     (Filas de Matriz 1) × (Columnas de Matriz 2)

📝 EJEMPLO:
   Matriz 1 (2×2):    Matriz 2 (2×2):      Resultado (2×2):
   [1, 2]             [5, 6]               [19, 22]
   [3, 4]             [7, 8]               [43, 50]

"""

    @staticmethod
    def get_instrucciones_escalar_matriz():
        """Retorna las instrucciones para Escalar × Matriz"""
        return Instrucciones.ESCALAR_MATRIZ
    
    @staticmethod
    def get_instrucciones_matriz_matriz():
        """Retorna las instrucciones para Matriz × Matriz"""
        return Instrucciones.MATRIZ_MATRIZ
    
    @staticmethod
    def get_instrucciones_principal():
        """Retorna las instrucciones de la pantalla principal"""
        return """
╔════════════════════════════════════════════════════════════════╗
║      BIENVENIDO AL PROGRAMA DE ANÁLISIS NUMÉRICO              ║
║             Operaciones con Matrices                          ║
╚════════════════════════════════════════════════════════════════╝

ESTE PROGRAMA PERMITE REALIZAR DOS OPERACIONES PRINCIPALES:

1.  ESCALAR × MATRIZ
   Multiplica un número único por todos los elementos de una matriz
   Ideal para: Escalado, ajuste de magnitudes
   
2.  MATRIZ × MATRIZ
   Multiplica dos matrices siguiendo reglas del álgebra linear
   Ideal para: Transformaciones, sistemas de ecuaciones

CÓMO USAR ESTE PROGRAMA:

✓ Selecciona una operación haciendo clic en su botón
✓ Sigue las instrucciones paso a paso
✓ Los botones "?" en cada pantalla te ayudarán
✓ El programa valida todos tus datos automáticamente

¿NECESITAS AYUDA?

En cada pantalla encontrarás:
• Un botón "?" que explica esa operación
• Botón "ATRÁS" para volver al menú principal
• Botón "CALCULAR" para procesar tus datos

¡Selecciona una operación para comenzar!
"""
