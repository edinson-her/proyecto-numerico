"""
Módulo de interfaz para Matriz × Matriz
"""

import customtkinter as ctk
from tkinter import messagebox
import numpy as np

from ui_base import UIBase
from validadores import Validador
from selectores import SelectorDimensiones
from instrucciones import Instrucciones


class UIMatrizMatriz(UIBase):
    """Interfaz para la operación Matriz × Matriz"""
    
    def mostrar(self):
        """Muestra la interfaz de Matriz × Matriz"""
        self.limpiar_ventana()
        self.root.geometry("1000x800")
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Frame de título con ayuda
        titulo_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        titulo_frame.pack(fill="x", pady=(0, 10))
        
        # Título
        titulo = ctk.CTkLabel(
            titulo_frame,
            text="MATRIZ × MATRIZ",
            font=("Arial", 24, "bold")
        )
        titulo.pack(side="left", expand=True)
        
        # Botón de ayuda
        btn_ayuda_mm = ctk.CTkButton(
            titulo_frame,
            text="❓",
            font=("Arial", 16),
            width=35,
            height=35,
            command=lambda: self.mostrar_instrucciones(
                "INSTRUCCIONES - MATRIZ × MATRIZ",
                Instrucciones.get_instrucciones_matriz_matriz()
            )
        )
        btn_ayuda_mm.pack(side="right", padx=5)
        
        # Frame principal de dos columnas
        contenedor_principal = ctk.CTkFrame(main_frame)
        contenedor_principal.pack(fill="both", expand=False, pady=15, padx=10, side="top")
        
        # LADO IZQUIERDO: MATRICES
        contenedor_matrices = ctk.CTkFrame(contenedor_principal)
        contenedor_matrices.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # ===== MATRIZ 1 =====
        frame_m1 = ctk.CTkFrame(contenedor_matrices)
        frame_m1.pack(fill="both", expand=True, pady=5)
        
        titulo_m1 = ctk.CTkLabel(frame_m1, text="MATRIZ 1", font=("Arial", 13, "bold"))
        titulo_m1.pack(pady=8)
        
        config_m1 = ctk.CTkFrame(frame_m1)
        config_m1.pack(fill="x", pady=5, padx=5)
        
        dimension1_label = ctk.CTkLabel(config_m1, text="DIMENSIÓN: (sin seleccionar)", font=("Arial", 10))
        dimension1_label.pack(side="left", padx=5)
        
        matriz1_entries = []
        
        def on_seleccionar_m1(filas, cols, ventana_selector=None):
            dimension1_label.configure(text=f"DIMENSIÓN: {filas}×{cols}")
            nonlocal matriz1_entries
            matriz1_entries = self.crear_tabla_matriz(scrollable1, filas, cols)
            
            # Validar compatibilidad con Matriz 2 de una vez (si ya existe)
            if matriz2_entries:
                cols1 = cols
                filas2 = len(matriz2_entries)
                es_compatible, error = Validador.validar_dimensiones_compatibles(cols1, filas2)
                if not es_compatible:
                    messagebox.showerror("Dimensiones incompatibles", error, parent=ventana_selector)
                    return False
            return True
        
        btn_selector1 = ctk.CTkButton(
            config_m1,
            text="SELECCIONAR",
            command=lambda: SelectorDimensiones.mostrar_selector(
                self.root,
                "SELECCIONAR DIMENSIONES - MATRIZ 1",
                on_seleccionar_m1
            ),
            font=("Arial", 10),
            width=120
        )
        btn_selector1.pack(side="left", padx=5)
        
        btn_limpiar1 = ctk.CTkButton(
            config_m1,
            text="LIMPIAR TABLA",
            command=lambda: self.limpiar_matriz_entries(matriz1_entries),
            font=("Arial", 10),
            width=140
        )
        btn_limpiar1.pack(side="left", padx=5)
        
        btn_eliminar1 = ctk.CTkButton(
            config_m1,
            text="ELIMINAR TABLA",
            command=lambda: (scrollable1.destroy(), matriz1_entries.clear() if True else None, dimension1_label.configure(text="DIMENSIÓN: (sin seleccionar)")),
            font=("Arial", 10),
            width=140,
            fg_color=("#E74C3C", "#C0392B"),
            hover_color=("#C0392B", "#A93226")
        )
        btn_eliminar1.pack(side="left", padx=5)
        
        # Tabla 1
        tabla1_frame = ctk.CTkFrame(frame_m1)
        tabla1_frame.pack(fill="both", expand=True, pady=5, padx=5)
        
        canvas1 = ctk.CTkCanvas(tabla1_frame, bg="white", highlightthickness=0, height=180)
        scrollbar1 = ctk.CTkScrollbar(tabla1_frame, command=canvas1.yview)
        scrollable1 = ctk.CTkFrame(canvas1, fg_color="white")
        
        scrollable1.bind(
            "<Configure>",
            lambda e: canvas1.configure(scrollregion=canvas1.bbox("all"))
        )
        
        canvas1.create_window((0, 0), window=scrollable1, anchor="nw")
        canvas1.configure(yscrollcommand=scrollbar1.set)
        
        canvas1.pack(side="left", fill="both", expand=True)
        scrollbar1.pack(side="right", fill="y")
        
        # ===== MATRIZ 2 =====
        frame_m2 = ctk.CTkFrame(contenedor_matrices)
        frame_m2.pack(fill="both", expand=True, pady=5)
        
        titulo_m2 = ctk.CTkLabel(frame_m2, text="MATRIZ 2", font=("Arial", 13, "bold"))
        titulo_m2.pack(pady=8)
        
        config_m2 = ctk.CTkFrame(frame_m2)
        config_m2.pack(fill="x", pady=5, padx=5)
        
        dimension2_label = ctk.CTkLabel(config_m2, text="DIMENSIÓN: (sin seleccionar)", font=("Arial", 10))
        dimension2_label.pack(side="left", padx=5)
        
        matriz2_entries = []
        
        def on_seleccionar_m2(filas, cols, ventana_selector=None):
            dimension2_label.configure(text=f"DIMENSIÓN: {filas}×{cols}")
            nonlocal matriz2_entries
            matriz2_entries = self.crear_tabla_matriz(scrollable2, filas, cols)
            
            # Validar compatibilidad con Matriz 1 de una vez
            if matriz1_entries:
                cols1 = len(matriz1_entries[0])
                es_compatible, error = Validador.validar_dimensiones_compatibles(cols1, filas)
                if not es_compatible:
                    messagebox.showerror("Dimensiones incompatibles", error, parent=ventana_selector)
                    return False
            return True
        
        btn_selector2 = ctk.CTkButton(
            config_m2,
            text="SELECCIONAR",
            command=lambda: SelectorDimensiones.mostrar_selector(
                self.root,
                "SELECCIONAR DIMENSIONES - MATRIZ 2",
                on_seleccionar_m2
            ),
            font=("Arial", 10),
            width=120
        )
        btn_selector2.pack(side="left", padx=5)
        
        btn_limpiar2 = ctk.CTkButton(
            config_m2,
            text="LIMPIAR TABLA",
            command=lambda: self.limpiar_matriz_entries(matriz2_entries),
            font=("Arial", 10),
            width=140
        )
        btn_limpiar2.pack(side="left", padx=5)
        
        btn_eliminar2 = ctk.CTkButton(
            config_m2,
            text="ELIMINAR TABLA",
            command=lambda: (scrollable2.destroy(), matriz2_entries.clear() if True else None, dimension2_label.configure(text="DIMENSIÓN: (sin seleccionar)")),
            font=("Arial", 10),
            width=140,
            fg_color=("#E74C3C", "#C0392B"),
            hover_color=("#C0392B", "#A93226")
        )
        btn_eliminar2.pack(side="left", padx=5)
        
        # Tabla 2
        tabla2_frame = ctk.CTkFrame(frame_m2)
        tabla2_frame.pack(fill="both", expand=True, pady=5, padx=5)
        
        canvas2 = ctk.CTkCanvas(tabla2_frame, bg="white", highlightthickness=0, height=180)
        scrollbar2 = ctk.CTkScrollbar(tabla2_frame, command=canvas2.yview)
        scrollable2 = ctk.CTkFrame(canvas2, fg_color="white")
        
        scrollable2.bind(
            "<Configure>",
            lambda e: canvas2.configure(scrollregion=canvas2.bbox("all"))
        )
        
        canvas2.create_window((0, 0), window=scrollable2, anchor="nw")
        canvas2.configure(yscrollcommand=scrollbar2.set)
        
        canvas2.pack(side="left", fill="both", expand=True)
        scrollbar2.pack(side="right", fill="y")
        
        # ===== LADO DERECHO: RESULTADO =====
        resultado_container = ctk.CTkFrame(contenedor_principal)
        resultado_container.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        resultado_title = ctk.CTkLabel(resultado_container, text="RESULTADO", font=("Arial", 13, "bold"))
        resultado_title.pack(pady=8)
        
        resultado_scroll_frame = ctk.CTkFrame(resultado_container)
        resultado_scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Función para calcular
        def calcular():
            # Validar que existan tablas
            if not matriz1_entries or not matriz2_entries:
                messagebox.showerror("Advertencia", "Por favor, selecciona las dimensiones de ambas matrices")
                return
            
            filas1 = len(matriz1_entries)
            cols1 = len(matriz1_entries[0])
            filas2 = len(matriz2_entries)
            cols2 = len(matriz2_entries[0])
            
            # Validar compatibilidad
            es_compatible, error = Validador.validar_dimensiones_compatibles(cols1, filas2)
            if not es_compatible:
                messagebox.showerror("Dimensiones incompatibles", error)
                return
            
            # Validar M1 llena
            es_valida, posicion = Validador.validar_matriz_llena(matriz1_entries)
            if not es_valida:
                messagebox.showerror(
                    "Matriz 1 vacía o inválida",
                    f"Error en Fila {posicion[0]}, Columna {posicion[1]}"
                )
                matriz1_entries[posicion[0]-1][posicion[1]-1].focus()
                return
            
            # Validar M2 llena
            es_valida, posicion = Validador.validar_matriz_llena(matriz2_entries)
            if not es_valida:
                messagebox.showerror(
                    "Matriz 2 vacía o inválida",
                    f"Error en Fila {posicion[0]}, Columna {posicion[1]}"
                )
                matriz2_entries[posicion[0]-1][posicion[1]-1].focus()
                return
            
            # Obtener valores M1
            exito, valores1, error, pos = Validador.obtener_valores_matriz(matriz1_entries)
            if not exito:
                messagebox.showerror("Error en Matriz 1", error)
                if pos:
                    matriz1_entries[pos[0]][pos[1]].focus()
                return
            
            # Obtener valores M2
            exito, valores2, error, pos = Validador.obtener_valores_matriz(matriz2_entries)
            if not exito:
                messagebox.showerror("Error en Matriz 2", error)
                if pos:
                    matriz2_entries[pos[0]][pos[1]].focus()
                return
            
            # Calcular
            try:
                matriz1 = np.array(valores1)
                matriz2 = np.array(valores2)
                resultado = self.operaciones.multiplicar_matrices(matriz1, matriz2)
                
                # Limpiar y mostrar resultado
                for widget in resultado_scroll_frame.winfo_children():
                    widget.destroy()
                
                tabla_resultado = ctk.CTkFrame(resultado_scroll_frame, fg_color="white")
                tabla_resultado.pack(expand=True, padx=10, pady=10)
                
                for i, fila in enumerate(resultado):
                    for j, valor in enumerate(fila):
                        celda_frame = ctk.CTkFrame(
                            tabla_resultado,
                            fg_color="white",
                            border_width=1,
                            border_color="#cccccc"
                        )
                        celda_frame.grid(row=i, column=j, padx=2, pady=2)
                        
                        celda_label = ctk.CTkLabel(
                            celda_frame,
                            text=f"{valor:.4f}".replace(".", ","),
                            font=("Arial", 12),
                            text_color="black",
                            fg_color="white"
                        )
                        celda_label.pack(padx=12, pady=8)
                
            except Exception as e:
                messagebox.showerror("Error en cálculo", f"Error:\n\n{str(e)}")
        
        # Frame de botones
        botones_frame = ctk.CTkFrame(main_frame)
        botones_frame.pack(fill="x", pady=10, padx=10)
        
        btn_regresar = ctk.CTkButton(
            botones_frame,
            text="ATRÁS",
            command=self._regresar_menu,
            font=("Arial", 10),
            height=30,
            width=80
        )
        btn_regresar.pack(side="left", padx=5)
        
        btn_calcular = ctk.CTkButton(
            botones_frame,
            text="CALCULAR",
            command=calcular,
            font=("Arial", 12, "bold"),
            height=45,
            width=150
        )
        btn_calcular.pack(side="right", padx=5, fill="y")
    
    def _regresar_menu(self):
        """Método que será sobrescrito en main.py"""
        pass
