"""
Módulo de interfaz para Escalar × Matriz
"""

import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk
import numpy as np

from ui_base import UIBase
from validadores import Validador
from selectores import SelectorDimensiones
from instrucciones import Instrucciones


class UIEscalarMatriz(UIBase):
    """Interfaz para la operación Escalar × Matriz"""
    
    def mostrar(self):
        """Muestra la interfaz de Escalar × Matriz"""
        self.limpiar_ventana()
        self.root.geometry("900x800")
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Frame de título con ayuda
        titulo_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        titulo_frame.pack(fill="x", pady=(0, 10))
        
        # Título
        titulo = ctk.CTkLabel(
            titulo_frame,
            text="ESCALAR × MATRIZ",
            font=("Arial", 24, "bold")
        )
        titulo.pack(side="left", expand=True)
        
        # Botón de ayuda
        btn_ayuda = ctk.CTkButton(
            titulo_frame,
            text="❓",
            font=("Arial", 16),
            width=35,
            height=35,
            command=lambda: self.mostrar_instrucciones(
                "INSTRUCCIONES - ESCALAR × MATRIZ",
                Instrucciones.get_instrucciones_escalar_matriz()
            )
        )
        btn_ayuda.pack(side="right", padx=5)
        
        # Frame de configuración
        config_frame = ctk.CTkFrame(main_frame)
        config_frame.pack(fill="x", pady=10)
        
        # Etiqueta y entrada del escalar
        ctk.CTkLabel(config_frame, text="ESCALAR:", font=("Arial", 11)).pack(side="left", padx=5)
        escalar_entry = ctk.CTkEntry(config_frame, width=100, font=("Arial", 11))
        escalar_entry.pack(side="left", padx=5)
        
        # Etiqueta de dimensión
        dimension_label = ctk.CTkLabel(
            config_frame,
            text="MATRIZ: (sin seleccionar)",
            font=("Arial", 11)
        )
        dimension_label.pack(side="left", padx=20)
        
        # Campos ocultos para almacenar filas y columnas
        filas_entry = ctk.CTkEntry(config_frame, width=1, font=("Arial", 11))
        filas_entry.pack(side="left", padx=0)
        filas_entry.pack_forget()
        
        cols_entry = ctk.CTkEntry(config_frame, width=1, font=("Arial", 11))
        cols_entry.pack(side="left", padx=0)
        cols_entry.pack_forget()
        
        # Variables para las matrices
        matriz_entries = []
        
        # Función para manejar selección de dimensiones
        def on_seleccionar_dimensiones(filas, cols, ventana_selector=None):
            filas_entry.delete(0, tk.END)
            filas_entry.insert(0, str(filas))
            cols_entry.delete(0, tk.END)
            cols_entry.insert(0, str(cols))
            dimension_label.configure(text=f"MATRIZ: {filas}×{cols}")
            
            # Crear tabla
            nonlocal matriz_entries
            matriz_entries = self.crear_tabla_matriz(scrollable_frame, filas, cols)
            return True
        
        # Botón selector
        btn_selector = ctk.CTkButton(
            config_frame,
            text="SELECCIONAR DIMENSIONES",
            command=lambda: SelectorDimensiones.mostrar_selector(
                self.root,
                "SELECCIONAR DIMENSIONES",
                on_seleccionar_dimensiones
            ),
            font=("Arial", 11),
            width=180
        )
        btn_selector.pack(side="left", padx=10)
        
        # Botón vaciar
        def vaciar_tabla():
            if not matriz_entries:
                messagebox.showwarning("Advertencia", "No hay tabla creada aún")
                return
            self.limpiar_matriz_entries(matriz_entries)
        
        btn_vaciar = ctk.CTkButton(
            config_frame,
            text="VACIAR TABLA",
            command=vaciar_tabla,
            font=("Arial", 10),
            width=120
        )
        btn_vaciar.pack(side="left", padx=5)
        
        # Frame principal para tabla y resultado lado a lado
        tabla_frame = ctk.CTkFrame(main_frame)
        tabla_frame.pack(fill="both", expand=True, pady=15, padx=10)
        
        # Frame para la tabla (izquierda)
        tabla_container = ctk.CTkFrame(tabla_frame)
        tabla_container.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        tabla_titulo = ctk.CTkLabel(tabla_container, text="MATRIZ", font=("Arial", 13, "bold"))
        tabla_titulo.pack(pady=8)
        
        # Canvas con scroll para la tabla
        tabla_scroll_frame = ctk.CTkFrame(tabla_container)
        tabla_scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        canvas = ctk.CTkCanvas(tabla_scroll_frame, bg="white", highlightthickness=0, height=350)
        scrollbar = ctk.CTkScrollbar(tabla_scroll_frame, command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas, fg_color="white")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Frame para el resultado (derecha)
        resultado_container = ctk.CTkFrame(tabla_frame)
        resultado_container.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        resultado_title = ctk.CTkLabel(resultado_container, text="RESULTADO", font=("Arial", 13, "bold"))
        resultado_title.pack(pady=8)
        
        # Frame para el contenido del resultado
        resultado_scroll_frame = ctk.CTkFrame(resultado_container)
        resultado_scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Función para calcular
        def calcular():
            # Validar que la tabla exista
            if not matriz_entries:
                messagebox.showwarning("Advertencia", "Por favor, crea una tabla primero")
                return
            
            # Validar escalar
            es_valido, escalar, error = Validador.validar_escalar(escalar_entry.get())
            if not es_valido:
                messagebox.showerror("Error de entrada", error)
                escalar_entry.focus()
                return
            
            # Validar que la matriz no esté vacía
            es_valida, posicion = Validador.validar_matriz_llena(matriz_entries)
            if not es_valida:
                messagebox.showerror(
                    "Matriz vacía o inválida",
                    f"Error en Fila {posicion[0]}, Columna {posicion[1]}\n\n"
                    f"Por favor, rellena todas las celdas con valores válidos"
                )
                matriz_entries[posicion[0]-1][posicion[1]-1].focus()
                return
            
            # Obtener valores
            exito, valores, error, pos = Validador.obtener_valores_matriz(matriz_entries)
            if not exito:
                messagebox.showerror("Error", error)
                if pos:
                    matriz_entries[pos[0]][pos[1]].focus()
                return
            
            # Calcular
            try:
                matriz = np.array(valores)
                resultado = self.operaciones.multiplicar_escalar_matriz(escalar, matriz)
                
                # Limpiar frame de resultado
                for widget in resultado_scroll_frame.winfo_children():
                    widget.destroy()
                
                # Mostrar resultado
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
                messagebox.showerror("Error en cálculo", f"❌ Error:\n\n{str(e)}")
        
        # Frame de botones
        botones_frame = ctk.CTkFrame(main_frame)
        botones_frame.pack(fill="both", pady=10, padx=10)
        
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
