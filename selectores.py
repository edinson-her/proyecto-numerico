"""
Módulo de selectores de dimensiones
Reutilizable para seleccionar dimensiones de matrices
"""

import customtkinter as ctk
import tkinter as tk


class SelectorDimensiones:
    """Clase para mostrar un selector de dimensiones reutilizable"""
    
    @staticmethod
    def mostrar_selector(parent_window, titulo, callback):
        """
        Muestra una ventana para seleccionar dimensiones de matriz
        
        Args:
            parent_window: ventana padre (root)
            titulo: título de la ventana emergente
            callback: función a ejecutar con (filas, cols) seleccionadas
        """
        ventana = ctk.CTkToplevel(parent_window)
        ventana.title(titulo)
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
        
        def seleccionar(filas, cols):
            """Ejecuta el callback y cierra la ventana"""
            callback(filas, cols)
            ventana.destroy()
        
        # Botón 2×2
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
        
        # Botón 3×3
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
