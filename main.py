import customtkinter as ctk
from operaciones import OperacionesMatrices
import tkinter as tk
from tkinter import messagebox
import numpy as np
import re

# Configurar tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class AplicacionMatrices:
    def __init__(self, root):
        self.root = root
        self.root.title("Análisis Numérico - Operaciones con Matrices")
        self.root.geometry("900x600")
        self.root.resizable(False, False)
        
        self.operaciones = OperacionesMatrices()
        self.opcion_actual = None
        self.matriz_entries = []
        
        self.crear_interfaz_principal()
    
    def crear_interfaz_principal(self):
        """Crea la interfaz principal con las opciones"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Título principal
        titulo = ctk.CTkLabel(
            main_frame,
            text="ANÁLISIS NUMÉRICO",
            font=("Arial", 32, "bold")
        )
        titulo.pack(pady=15)
        
        # Subtítulo
        subtitulo = ctk.CTkLabel(
            main_frame,
            text="Operaciones con Matrices",
            font=("Arial", 14)
        )
        subtitulo.pack(pady=5)
        
        # Descripción
        desc = ctk.CTkLabel(
            main_frame,
            text="Selecciona la operación que deseas realizar",
            font=("Arial", 11)
        )
        desc.pack(pady=20)
        
        # Frame para botones
        botones_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        botones_frame.pack(fill="both", expand=True, pady=20)
        
        # Botón 1 - Escalar × Matriz
        btn1 = ctk.CTkButton(
            botones_frame,
            text="⚡ ESCALAR × MATRIZ\n\nMultiplica un escalar por una matriz",
            font=("Arial", 14, "bold"),
            height=100,
            corner_radius=10,
            command=lambda: self.mostrar_escalar_matriz()
        )
        btn1.pack(fill="both", expand=True, pady=10)
        
        # Botón 2 - Multiplicación entre Matrices
        btn2 = ctk.CTkButton(
            botones_frame,
            text="🔗 MATRIZ × MATRIZ\n\nMultiplica dos matrices",
            font=("Arial", 14, "bold"),
            height=100,
            corner_radius=10,
            fg_color=("#8b5cf6", "#6d28d9"),
            hover_color=("#7c3aed", "#5b21b6"),
            command=lambda: self.mostrar_matriz_matriz()
        )
        btn2.pack(fill="both", expand=True, pady=10)
    
    def mostrar_escalar_matriz(self):
        """Interfaz para multiplicar escalar × matriz"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.geometry("900x800")
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Título
        titulo = ctk.CTkLabel(
            main_frame,
            text="ESCALAR × MATRIZ",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=10)
        
        # Frame de configuración
        config_frame = ctk.CTkFrame(main_frame)
        config_frame.pack(fill="x", pady=10)
        
        # Escalar
        ctk.CTkLabel(config_frame, text="ESCALAR:", font=("Arial", 11)).pack(side="left", padx=5)
        escalar_entry = ctk.CTkEntry(config_frame, width=100, font=("Arial", 11))
        escalar_entry.pack(side="left", padx=5)
        
        # Variable para almacenar dimensiones seleccionadas
        dimension_label = ctk.CTkLabel(config_frame, text="MATRIZ: (sin seleccionar)", font=("Arial", 11))
        dimension_label.pack(side="left", padx=20)
        
        # Función para abrir el diálogo de selección de dimensiones
        def abrir_selector_dimensiones():
            """Abre una ventana emergente para seleccionar dimensiones"""
            ventana = ctk.CTkToplevel(self.root)
            ventana.title("SELECCIONAR DIMENSIONES")
            ventana.geometry("500x600")
            ventana.resizable(False, False)
            ventana.attributes("-topmost", True)
            ventana.grab_set()
            
            # Título
            titulo_ventana = ctk.CTkLabel(
                ventana,
                text="SELECCIONA LAS DIMENSIONES",
                font=("Arial", 14, "bold")
            )
            titulo_ventana.pack(pady=10)
            
            # Subtítulo recomendadas
            recomendadas_label = ctk.CTkLabel(
                ventana,
                text="RECOMENDADAS:",
                font=("Arial", 12, "bold"),
                text_color="green"
            )
            recomendadas_label.pack(pady=5)
            
            # Frame para opciones recomendadas
            recomendadas_frame = ctk.CTkFrame(ventana)
            recomendadas_frame.pack(fill="x", padx=20, pady=5)
            
            def crear_tabla_automatica(filas, cols):
                """Crea la tabla automáticamente después de seleccionar dimensiones"""
                try:
                    # Limpiar tabla anterior
                    for widget in scrollable_frame.winfo_children():
                        widget.destroy()
                    
                    self.matriz_entries = []
                    
                    # Frame con padding para centrar la matriz
                    matriz_frame = ctk.CTkFrame(scrollable_frame, fg_color="white")
                    matriz_frame.pack(pady=20, padx=20)
                    
                    # Crear entrada para cada celda
                    for i in range(filas):
                        fila_entries = []
                        for j in range(cols):
                            entry = ctk.CTkEntry(matriz_frame, width=60, font=("Arial", 10))
                            entry.grid(row=i, column=j, padx=5, pady=5)
                            fila_entries.append(entry)
                        self.matriz_entries.append(fila_entries)
                except Exception as e:
                    messagebox.showerror("Error", f"Error al crear la tabla: {str(e)}")
            
            def seleccionar(filas, cols):
                filas_entry.delete(0, tk.END)
                filas_entry.insert(0, str(filas))
                cols_entry.delete(0, tk.END)
                cols_entry.insert(0, str(cols))
                dimension_label.configure(text=f"MATRIZ: {filas}×{cols}")
                crear_tabla_automatica(filas, cols)
                ventana.destroy()
            
            # Botones recomendados
            btn_2x2 = ctk.CTkButton(
                recomendadas_frame,
                text="2×2",
                command=lambda: seleccionar(2, 2),
                width=70,
                height=40,
                font=("Arial", 11, "bold"),
                fg_color="green"
            )
            btn_2x2.pack(side="left", padx=5, pady=5)
            
            btn_3x3 = ctk.CTkButton(
                recomendadas_frame,
                text="3×3",
                command=lambda: seleccionar(3, 3),
                width=70,
                height=40,
                font=("Arial", 11, "bold"),
                fg_color="green"
            )
            btn_3x3.pack(side="left", padx=5, pady=5)
            
            # Subtítulo otras opciones
            otras_label = ctk.CTkLabel(
                ventana,
                text="OTRAS OPCIONES:",
                font=("Arial", 12, "bold")
            )
            otras_label.pack(pady=10)
            
            # Frame con scroll para otras opciones
            scroll_frame = ctk.CTkFrame(ventana)
            scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)
            
            canvas = ctk.CTkCanvas(scroll_frame, bg="white", highlightthickness=0)
            scrollbar = ctk.CTkScrollbar(scroll_frame, command=canvas.yview)
            otras_frame = ctk.CTkFrame(canvas, fg_color="white")
            
            otras_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=otras_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            # Listado de otras dimensiones
            dimensiones = [
                (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                (2, 1), (2, 3), (2, 4), (2, 5),
                (3, 1), (3, 2), (3, 4), (3, 5),
                (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
                (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
            ]
            
            for i, (filas, cols) in enumerate(dimensiones):
                fila = i // 5
                col = i % 5
                
                btn = ctk.CTkButton(
                    otras_frame,
                    text=f"{filas}×{cols}",
                    command=lambda f=filas, c=cols: seleccionar(f, c),
                    width=60,
                    height=35,
                    font=("Arial", 10)
                )
                btn.grid(row=fila, column=col, padx=3, pady=3)
        
        btn_selector = ctk.CTkButton(
            config_frame,
            text="SELECCIONAR DIMENSIONES",
            command=abrir_selector_dimensiones,
            font=("Arial", 11),
            width=180
        )
        btn_selector.pack(side="left", padx=10)
        
        # Campos ocultos para almacenar filas y columnas
        filas_entry = ctk.CTkEntry(config_frame, width=1, font=("Arial", 11))
        filas_entry.pack(side="left", padx=0)
        filas_entry.pack_forget()
        
        cols_entry = ctk.CTkEntry(config_frame, width=1, font=("Arial", 11))
        cols_entry.pack(side="left", padx=0)
        cols_entry.pack_forget()
        
        def vaciar_tabla():
            """Vacía todos los campos de la tabla actual"""
            if not self.matriz_entries:
                messagebox.showwarning("Advertencia", "No hay tabla creada aún")
                return
            
            for fila_entries in self.matriz_entries:
                for entry in fila_entries:
                    entry.delete(0, tk.END)
        
        btn_vaciar = ctk.CTkButton(
            config_frame,
            text="VACIAR TABLA",
            command=vaciar_tabla,
            font=("Arial", 10),
            width=120
        )
        btn_vaciar.pack(side="left", padx=5)
        
        def calcular():
            # Validar que la tabla exista
            if not self.matriz_entries:
                messagebox.showwarning("Advertencia", "Por favor, crea una tabla primero")
                return
            
            # Validar que el escalar esté completo
            escalar_texto = escalar_entry.get().strip()
            if not escalar_texto:
                messagebox.showerror("Error de entrada", "❌ Debes ingresar un ESCALAR\n\nEscribe un número en el campo 'ESCALAR'")
                escalar_entry.focus()
                return
            
            # Validar formato del escalar (debe tener parte entera)
            if not re.match(r'^-?\d+(\.\d+)?$', escalar_texto):
                messagebox.showerror("Formato inválido", 
                    f"❌ El formato '{escalar_texto}' no es válido\n\n"
                    f"Ejemplos correctos: 3, 0.3, 3.5, -1.2\n"
                    f"Ejemplos incorrectos: .3, .05, -.5")
                escalar_entry.delete(0, tk.END)
                escalar_entry.focus()
                return
            
            # Validar que el escalar sea un número válido
            try:
                escalar = float(escalar_texto)
            except ValueError:
                messagebox.showerror("Error de entrada", f"❌ El valor '{escalar_texto}' no es un número válido\n\nIngresa un número entero o decimal (ej: 2, 3.5, -1.2)")
                escalar_entry.delete(0, tk.END)
                escalar_entry.focus()
                return
            
            # Validar que la matriz no esté vacía
            matriz_vacia = True
            for fila_entries in self.matriz_entries:
                for entry in fila_entries:
                    if entry.get().strip():
                        matriz_vacia = False
                        break
                if not matriz_vacia:
                    break
            
            if matriz_vacia:
                messagebox.showerror("Matriz vacía", "Por favor, rellena todos los valores de la MATRIZ")
                return
            
            # Obtener valores de la tabla y validar que todos estén llenos
            valores = []
            
            for fila_idx, fila_entries in enumerate(self.matriz_entries):
                fila = []
                for col_idx, entry in enumerate(fila_entries):
                    valor_texto = entry.get().strip()
                    if valor_texto:
                        # Validar formato (debe tener parte entera)
                        if not re.match(r'^-?\d+(\.\d+)?$', valor_texto):
                            messagebox.showerror("Formato inválido", 
                                f"❌ El formato '{valor_texto}' en Fila {fila_idx+1}, Columna {col_idx+1} no es válido\n\n"
                                f"Ejemplos correctos: 3, 0.3, 3.5, -1.2\n"
                                f"Ejemplos incorrectos: .3, .05, 1., -.5")
                            entry.delete(0, tk.END)
                            entry.focus()
                            return
                        try:
                            fila.append(float(valor_texto))
                        except ValueError:
                            messagebox.showerror("Error de entrada", f"❌ El valor '{valor_texto}' en la matriz no es válido\n\nTodos los valores deben ser números")
                            entry.focus()
                            return
                    else:
                        messagebox.showerror("Celda vacía", 
                            f"Matriz - Fila {fila_idx+1}, Columna {col_idx+1}\n\n"
                            f"Por favor, rellena todas las celdas")
                        entry.focus()
                        return
                valores.append(fila)
            
            try:
                matriz = np.array(valores)
                resultado = self.operaciones.multiplicar_escalar_matriz(escalar, matriz)
                
                # Mostrar resultado en tabla
                # Limpiar frame de resultado
                for widget in resultado_scroll_frame.winfo_children():
                    widget.destroy()
                
                # Crear tabla del resultado con mejor centrado
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
                            text=f"{valor:.10g}",
                            font=("Arial", 12),
                            text_color="black",
                            fg_color="white"
                        )
                        celda_label.pack(padx=12, pady=8)
                
            except Exception as e:
                messagebox.showerror("Error en cálculo", f"❌ Error al realizar la operación:\n\n{str(e)}")
        
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
        
        # Frame de botones
        botones_frame = ctk.CTkFrame(main_frame)
        botones_frame.pack(fill="both", pady=10, padx=10)
        
        btn_regresar = ctk.CTkButton(
            botones_frame,
            text="ATRÁS",
            command=self.crear_interfaz_principal,
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
    
    def mostrar_matriz_matriz(self):
        """Interfaz para multiplicar matriz × matriz"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.geometry("1000x800")
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Título
        titulo = ctk.CTkLabel(
            main_frame,
            text="MATRIZ × MATRIZ",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=10)
        
        # Frame principal de dos columnas: izquierda (matrices) y derecha (resultado)
        contenedor_principal = ctk.CTkFrame(main_frame)
        contenedor_principal.pack(fill="both", expand=False, pady=15, padx=10, side="top")
        
        # ===== LADO IZQUIERDO: MATRICES 1 Y 2 =====
        contenedor_matrices = ctk.CTkFrame(contenedor_principal)
        contenedor_matrices.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        # MATRIZ 1
        frame_m1 = ctk.CTkFrame(contenedor_matrices)
        frame_m1.pack(fill="both", expand=True, pady=5)
        
        titulo_m1 = ctk.CTkLabel(frame_m1, text="MATRIZ 1", font=("Arial", 13, "bold"))
        titulo_m1.pack(pady=8)
        
        # Config para matriz 1
        config_m1 = ctk.CTkFrame(frame_m1)
        config_m1.pack(fill="x", pady=5, padx=5)
        
        dimension1_label = ctk.CTkLabel(config_m1, text="DIMENSIÓN: (sin seleccionar)", font=("Arial", 10))
        dimension1_label.pack(side="left", padx=5)
        
        # Campos ocultos para matriz 1
        filas1_entry = ctk.CTkEntry(config_m1, width=1, font=("Arial", 10))
        filas1_entry.pack(side="left", padx=0)
        filas1_entry.pack_forget()
        
        cols1_entry = ctk.CTkEntry(config_m1, width=1, font=("Arial", 10))
        cols1_entry.pack(side="left", padx=0)
        cols1_entry.pack_forget()
        
        def abrir_selector_matriz1():
            """Abre selector de dimensiones para Matriz 1"""
            ventana = ctk.CTkToplevel(self.root)
            ventana.title("SELECCIONAR DIMENSIONES - MATRIZ 1")
            ventana.geometry("500x600")
            ventana.resizable(False, False)
            ventana.attributes("-topmost", True)
            ventana.grab_set()
            
            titulo_ventana = ctk.CTkLabel(
                ventana,
                text="SELECCIONA LAS DIMENSIONES",
                font=("Arial", 14, "bold")
            )
            titulo_ventana.pack(pady=10)
            
            recomendadas_label = ctk.CTkLabel(
                ventana,
                text="RECOMENDADAS:",
                font=("Arial", 12, "bold"),
                text_color="green"
            )
            recomendadas_label.pack(pady=5)
            
            recomendadas_frame = ctk.CTkFrame(ventana)
            recomendadas_frame.pack(fill="x", padx=20, pady=5)
            
            def seleccionar1(filas, cols):
                filas1_entry.delete(0, tk.END)
                filas1_entry.insert(0, str(filas))
                cols1_entry.delete(0, tk.END)
                cols1_entry.insert(0, str(cols))
                dimension1_label.configure(text=f"DIMENSIÓN: {filas}×{cols}")
                crear_tabla_matriz1(filas, cols)
                ventana.destroy()
            
            btn_2x2 = ctk.CTkButton(
                recomendadas_frame,
                text="2×2",
                command=lambda: seleccionar1(2, 2),
                width=70,
                height=40,
                font=("Arial", 11, "bold"),
                fg_color="green"
            )
            btn_2x2.pack(side="left", padx=5, pady=5)
            
            btn_3x3 = ctk.CTkButton(
                recomendadas_frame,
                text="3×3",
                command=lambda: seleccionar1(3, 3),
                width=70,
                height=40,
                font=("Arial", 11, "bold"),
                fg_color="green"
            )
            btn_3x3.pack(side="left", padx=5, pady=5)
            
            otras_label = ctk.CTkLabel(
                ventana,
                text="OTRAS OPCIONES:",
                font=("Arial", 12, "bold")
            )
            otras_label.pack(pady=10)
            
            scroll_frame = ctk.CTkFrame(ventana)
            scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)
            
            canvas = ctk.CTkCanvas(scroll_frame, bg="white", highlightthickness=0)
            scrollbar = ctk.CTkScrollbar(scroll_frame, command=canvas.yview)
            otras_frame = ctk.CTkFrame(canvas, fg_color="white")
            
            otras_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=otras_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            dimensiones = [
                (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                (2, 1), (2, 3), (2, 4), (2, 5),
                (3, 1), (3, 2), (3, 4), (3, 5),
                (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
                (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
            ]
            
            for i, (filas, cols) in enumerate(dimensiones):
                fila = i // 5
                col = i % 5
                
                btn = ctk.CTkButton(
                    otras_frame,
                    text=f"{filas}×{cols}",
                    command=lambda f=filas, c=cols: seleccionar1(f, c),
                    width=60,
                    height=35,
                    font=("Arial", 10)
                )
                btn.grid(row=fila, column=col, padx=3, pady=3)
        
        btn_selector1 = ctk.CTkButton(
            config_m1,
            text="SELECCIONAR",
            command=abrir_selector_matriz1,
            font=("Arial", 10),
            width=120
        )
        btn_selector1.pack(side="left", padx=5)
        
        def limpiar_matriz1():
            """Limpia los valores de la Matriz 1"""
            for fila_entries in matriz1_entries:
                for entry in fila_entries:
                    entry.delete(0, tk.END)
        
        btn_limpiar1 = ctk.CTkButton(
            config_m1,
            text="LIMPIAR MATRIZ",
            command=limpiar_matriz1,
            font=("Arial", 10),
            width=140,
            fg_color=("#E74C3C", "#C0392B"),
            hover_color=("#C0392B", "#A93226")
        )
        btn_limpiar1.pack(side="left", padx=5)
        
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
        
        matriz1_entries = []
        
        def crear_tabla_matriz1(filas, cols):
            """Crea tabla para matriz 1"""
            for widget in scrollable1.winfo_children():
                widget.destroy()
            
            matriz1_entries.clear()
            
            matriz_frame = ctk.CTkFrame(scrollable1, fg_color="white")
            matriz_frame.pack(pady=10, padx=10)
            
            for i in range(filas):
                fila_entries = []
                for j in range(cols):
                    entry = ctk.CTkEntry(matriz_frame, width=50, font=("Arial", 9))
                    entry.grid(row=i, column=j, padx=3, pady=3)
                    fila_entries.append(entry)
                matriz1_entries.append(fila_entries)
        
        # MATRIZ 2
        frame_m2 = ctk.CTkFrame(contenedor_matrices)
        frame_m2.pack(fill="both", expand=True, pady=5)
        
        titulo_m2 = ctk.CTkLabel(frame_m2, text="MATRIZ 2", font=("Arial", 13, "bold"))
        titulo_m2.pack(pady=8)
        
        # Config para matriz 2
        config_m2 = ctk.CTkFrame(frame_m2)
        config_m2.pack(fill="x", pady=5, padx=5)
        
        dimension2_label = ctk.CTkLabel(config_m2, text="DIMENSIÓN: (sin seleccionar)", font=("Arial", 10))
        dimension2_label.pack(side="left", padx=5)
        
        # Campos ocultos para matriz 2
        filas2_entry = ctk.CTkEntry(config_m2, width=1, font=("Arial", 10))
        filas2_entry.pack(side="left", padx=0)
        filas2_entry.pack_forget()
        
        cols2_entry = ctk.CTkEntry(config_m2, width=1, font=("Arial", 10))
        cols2_entry.pack(side="left", padx=0)
        cols2_entry.pack_forget()
        
        def abrir_selector_matriz2():
            """Abre selector de dimensiones para Matriz 2"""
            ventana = ctk.CTkToplevel(self.root)
            ventana.title("SELECCIONAR DIMENSIONES - MATRIZ 2")
            ventana.geometry("500x600")
            ventana.resizable(False, False)
            ventana.attributes("-topmost", True)
            ventana.grab_set()
            
            titulo_ventana = ctk.CTkLabel(
                ventana,
                text="SELECCIONA LAS DIMENSIONES",
                font=("Arial", 14, "bold")
            )
            titulo_ventana.pack(pady=10)
            
            recomendadas_label = ctk.CTkLabel(
                ventana,
                text="RECOMENDADAS:",
                font=("Arial", 12, "bold"),
                text_color="green"
            )
            recomendadas_label.pack(pady=5)
            
            recomendadas_frame = ctk.CTkFrame(ventana)
            recomendadas_frame.pack(fill="x", padx=20, pady=5)
            
            def seleccionar2(filas, cols):
                filas2_entry.delete(0, tk.END)
                filas2_entry.insert(0, str(filas))
                cols2_entry.delete(0, tk.END)
                cols2_entry.insert(0, str(cols))
                dimension2_label.configure(text=f"DIMENSIÓN: {filas}×{cols}")
                crear_tabla_matriz2(filas, cols)
                ventana.destroy()
            
            btn_2x2 = ctk.CTkButton(
                recomendadas_frame,
                text="2×2",
                command=lambda: seleccionar2(2, 2),
                width=70,
                height=40,
                font=("Arial", 11, "bold"),
                fg_color="green"
            )
            btn_2x2.pack(side="left", padx=5, pady=5)
            
            btn_3x3 = ctk.CTkButton(
                recomendadas_frame,
                text="3×3",
                command=lambda: seleccionar2(3, 3),
                width=70,
                height=40,
                font=("Arial", 11, "bold"),
                fg_color="green"
            )
            btn_3x3.pack(side="left", padx=5, pady=5)
            
            otras_label = ctk.CTkLabel(
                ventana,
                text="OTRAS OPCIONES:",
                font=("Arial", 12, "bold")
            )
            otras_label.pack(pady=10)
            
            scroll_frame = ctk.CTkFrame(ventana)
            scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)
            
            canvas = ctk.CTkCanvas(scroll_frame, bg="white", highlightthickness=0)
            scrollbar = ctk.CTkScrollbar(scroll_frame, command=canvas.yview)
            otras_frame = ctk.CTkFrame(canvas, fg_color="white")
            
            otras_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=otras_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            dimensiones = [
                (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                (2, 1), (2, 3), (2, 4), (2, 5),
                (3, 1), (3, 2), (3, 4), (3, 5),
                (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
                (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
            ]
            
            for i, (filas, cols) in enumerate(dimensiones):
                fila = i // 5
                col = i % 5
                
                btn = ctk.CTkButton(
                    otras_frame,
                    text=f"{filas}×{cols}",
                    command=lambda f=filas, c=cols: seleccionar2(f, c),
                    width=60,
                    height=35,
                    font=("Arial", 10)
                )
                btn.grid(row=fila, column=col, padx=3, pady=3)
        
        btn_selector2 = ctk.CTkButton(
            config_m2,
            text="SELECCIONAR",
            command=abrir_selector_matriz2,
            font=("Arial", 10),
            width=120
        )
        btn_selector2.pack(side="left", padx=5)
        
        def limpiar_matriz2():
            """Limpia los valores de la Matriz 2"""
            for fila_entries in matriz2_entries:
                for entry in fila_entries:
                    entry.delete(0, tk.END)
        
        btn_limpiar2 = ctk.CTkButton(
            config_m2,
            text="LIMPIAR MATRIZ",
            command=limpiar_matriz2,
            font=("Arial", 10),
            width=140,
            fg_color=("#E74C3C", "#C0392B"),
            hover_color=("#C0392B", "#A93226")
        )
        btn_limpiar2.pack(side="left", padx=5)
        
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
        
        matriz2_entries = []
        
        def crear_tabla_matriz2(filas, cols):
            """Crea tabla para matriz 2"""
            for widget in scrollable2.winfo_children():
                widget.destroy()
            
            matriz2_entries.clear()
            
            matriz_frame = ctk.CTkFrame(scrollable2, fg_color="white")
            matriz_frame.pack(pady=10, padx=10)
            
            for i in range(filas):
                fila_entries = []
                for j in range(cols):
                    entry = ctk.CTkEntry(matriz_frame, width=50, font=("Arial", 9))
                    entry.grid(row=i, column=j, padx=3, pady=3)
                    fila_entries.append(entry)
                matriz2_entries.append(fila_entries)
        
        # ===== LADO DERECHO: RESULTADO =====
        resultado_container = ctk.CTkFrame(contenedor_principal)
        resultado_container.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        resultado_title = ctk.CTkLabel(resultado_container, text="RESULTADO", font=("Arial", 13, "bold"))
        resultado_title.pack(pady=8)
        
        # Frame para el contenido del resultado
        resultado_scroll_frame = ctk.CTkFrame(resultado_container)
        resultado_scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        def calcular():
            # Validar que las tablas existan
            if not matriz1_entries or not matriz2_entries:
                messagebox.showerror("Advertencia", "Por favor, selecciona las dimensiones de ambas matrices")
                return
            
            filas1 = len(matriz1_entries)
            cols1 = len(matriz1_entries[0])
            filas2 = len(matriz2_entries)
            cols2 = len(matriz2_entries[0])
            
            # Validación de compatibilidad
            if cols1 != filas2:
                messagebox.showerror("Dimensiones incompatibles", 
                    f"No se pueden multiplicar estas matrices\n\n"
                    f"Columnas de Matriz 1: {cols1}\n"
                    f"Filas de Matriz 2: {filas2}\n\n"
                    f"Las COLUMNAS de la primera deben ser iguales\n"
                    f"a las FILAS de la segunda.")
                return
            
            # Validar que Matriz 1 no esté vacía
            matriz1_vacia = True
            for fila_entries in matriz1_entries:
                for entry in fila_entries:
                    if entry.get().strip():
                        matriz1_vacia = False
                        break
                if not matriz1_vacia:
                    break
            
            if matriz1_vacia:
                messagebox.showerror("Matriz vacía", "Por favor, rellena todos los valores de la MATRIZ 1")
                return
            
            # Validar que Matriz 2 no esté vacía
            matriz2_vacia = True
            for fila_entries in matriz2_entries:
                for entry in fila_entries:
                    if entry.get().strip():
                        matriz2_vacia = False
                        break
                if not matriz2_vacia:
                    break
            
            if matriz2_vacia:
                messagebox.showerror("Matriz vacía", "Por favor, rellena todos los valores de la MATRIZ 2")
                return
            
            # Obtener y validar valores de tabla 1
            valores1 = []
            for fila_idx, fila_entries in enumerate(matriz1_entries):
                fila = []
                for col_idx, entry in enumerate(fila_entries):
                    valor_texto = entry.get().strip()
                    if valor_texto:
                        # Validar formato (debe tener parte entera)
                        if not re.match(r'^-?\d+(\.\d+)?$', valor_texto):
                            messagebox.showerror("Formato inválido", 
                                f"❌ El formato '{valor_texto}' en Matriz 1 - Fila {fila_idx+1}, Columna {col_idx+1} no es válido\n\n"
                                f"Ejemplos correctos: 3, 0.3, 3.5, -1.2\n"
                                f"Ejemplos incorrectos: .3, .05, 1., -.5")
                            entry.delete(0, tk.END)
                            entry.focus()
                            return
                        try:
                            fila.append(float(valor_texto))
                        except ValueError:
                            messagebox.showerror("Entrada inválida", 
                                f"Error en Matriz 1 - Fila {fila_idx+1}, Columna {col_idx+1}\n\n"
                                f"El valor '{valor_texto}' no es un número válido")
                            entry.focus()
                            return
                    else:
                        messagebox.showerror("Celda vacía", 
                            f"Matriz 1 - Fila {fila_idx+1}, Columna {col_idx+1}\n\n"
                            f"Por favor, rellena todas las celdas")
                        entry.focus()
                        return
                valores1.append(fila)
            
            # Obtener y validar valores de tabla 2
            valores2 = []
            for fila_idx, fila_entries in enumerate(matriz2_entries):
                fila = []
                for col_idx, entry in enumerate(fila_entries):
                    valor_texto = entry.get().strip()
                    if valor_texto:
                        # Validar formato (debe tener parte entera)
                        if not re.match(r'^-?\d+(\.\d+)?$', valor_texto):
                            messagebox.showerror("Formato inválido", 
                                f"❌ El formato '{valor_texto}' en Matriz 2 - Fila {fila_idx+1}, Columna {col_idx+1} no es válido\n\n"
                                f"Ejemplos correctos: 3, 0.3, 3.5, -1.2\n"
                                f"Ejemplos incorrectos: .3, .05, 1., -.5")
                            entry.delete(0, tk.END)
                            entry.focus()
                            return
                        try:
                            fila.append(float(valor_texto))
                        except ValueError:
                            messagebox.showerror("Entrada inválida", 
                                f"Error en Matriz 2 - Fila {fila_idx+1}, Columna {col_idx+1}\n\n"
                                f"El valor '{valor_texto}' no es un número válido")
                            entry.focus()
                            return
                    else:
                        messagebox.showerror("Celda vacía", 
                            f"Matriz 2 - Fila {fila_idx+1}, Columna {col_idx+1}\n\n"
                            f"Por favor, rellena todas las celdas")
                        entry.focus()
                        return
                valores2.append(fila)
            
            try:
                matriz1 = np.array(valores1)
                matriz2 = np.array(valores2)
                
                resultado = self.operaciones.multiplicar_matrices(matriz1, matriz2)
                
                # Limpiar frame de resultado
                for widget in resultado_scroll_frame.winfo_children():
                    widget.destroy()
                
                # Crear tabla del resultado con mejor centrado
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
                            text=f"{valor:.10g}",
                            font=("Arial", 12),
                            text_color="black",
                            fg_color="white"
                        )
                        celda_label.pack(padx=12, pady=8)
                
            except Exception as e:
                messagebox.showerror("Error en cálculo", f"Error al realizar la multiplicación:\n\n{str(e)}")
        
        # Frame de botones (AL FINAL para que esté en la parte inferior)
        botones_frame = ctk.CTkFrame(main_frame)
        botones_frame.pack(fill="x", pady=10, padx=10)
        
        btn_regresar = ctk.CTkButton(
            botones_frame,
            text="ATRÁS",
            command=self.crear_interfaz_principal,
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


if __name__ == "__main__":
    root = ctk.CTk()
    app = AplicacionMatrices(root)
    root.mainloop()
