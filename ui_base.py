"""
Módulo base de interfaz
Contiene la clase base con métodos comunes para todas las interfaces
"""

import customtkinter as ctk
from instrucciones import Instrucciones
from teclado_numerico import TecladoNumerico


class UIBase:
    """Clase base con métodos comunes para todas las interfaces"""
    
    def __init__(self, root, operaciones):
        """
        Inicializa la interfaz base
        
        Args:
            root: ventana principal de tkinter
            operaciones: instancia de OperacionesMatrices
        """
        self.root = root
        self.operaciones = operaciones
        self.widget_enfocado = None  # Almacenar el widget con focus
    
    def mostrar_instrucciones(self, titulo, contenido):
        """
        Muestra instrucciones en una ventana emergente
        
        Args:
            titulo: título de la ventana
            contenido: contenido de las instrucciones
        """
        ventana_ayuda = ctk.CTkToplevel(self.root)
        ventana_ayuda.title(titulo)
        ventana_ayuda.geometry("700x600")
        ventana_ayuda.resizable(True, True)
        ventana_ayuda.attributes("-topmost", True)
        
        # Frame principal
        main_frame = ctk.CTkFrame(ventana_ayuda)
        main_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Frame de título
        titulo_frame = ctk.CTkFrame(main_frame, fg_color="#2563eb")
        titulo_frame.pack(fill="x", padx=0, pady=0)
        
        titulo_label = ctk.CTkLabel(
            titulo_frame,
            text=titulo,
            font=("Arial", 16, "bold"),
            text_color="white"
        )
        titulo_label.pack(pady=15, padx=20)
        
        # Frame para el scroll
        scroll_frame = ctk.CTkFrame(main_frame)
        scroll_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Canvas con scrollbar
        canvas = ctk.CTkCanvas(scroll_frame, bg="white", highlightthickness=0)
        scrollbar = ctk.CTkScrollbar(scroll_frame, command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas, fg_color="white")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Texto de instrucciones
        texto_label = ctk.CTkLabel(
            scrollable_frame,
            text=contenido,
            font=("Courier", 10),
            justify="left",
            text_color="black"
        )
        texto_label.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Botón cerrar
        cerrar_frame = ctk.CTkFrame(main_frame)
        cerrar_frame.pack(fill="x", padx=15, pady=10)
        
        btn_cerrar = ctk.CTkButton(
            cerrar_frame,
            text="CERRAR",
            command=ventana_ayuda.destroy,
            font=("Arial", 11, "bold"),
            height=30,
            width=150
        )
        btn_cerrar.pack(side="right", padx=5)
    
    def limpiar_ventana(self):
        """Limpia todos los widgets de la ventana principal"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def crear_tabla_matriz(self, scrollable_frame, filas, cols):
        """
        Crea una tabla de entrada para una matriz
        
        Args:
            scrollable_frame: frame donde colocar la tabla
            filas: número de filas
            cols: número de columnas
            
        Returns:
            lista de listas con los Entry objects
        """
        # Limpiar frame anterior
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        
        matriz_entries = []
        
        # Frame con padding para centrar la matriz
        matriz_frame = ctk.CTkFrame(scrollable_frame, fg_color="white")
        matriz_frame.pack(pady=10, padx=10)
        
        # Crear entrada para cada celda
        for i in range(filas):
            fila_entries = []
            for j in range(cols):
                entry = ctk.CTkEntry(matriz_frame, width=50, font=("Arial", 9))
                entry.grid(row=i, column=j, padx=3, pady=3)
                
                # Agregar binding para detectar focus en esta celda
                def on_focus_in(event, entry_ref=entry):
                    self.widget_enfocado = entry_ref
                
                entry.bind("<FocusIn>", on_focus_in)
                
                fila_entries.append(entry)
            matriz_entries.append(fila_entries)
        
        return matriz_entries
    
    def vaciar_entrada(self, entrada):
        """Limpia el contenido de una entrada"""
        entrada.delete(0, len(entrada.get()))
    
    def limpiar_matriz_entries(self, matriz_entries):
        """Limpia todas las celdas de una matriz"""
        for fila_entries in matriz_entries:
            for entry in fila_entries:
                self.vaciar_entrada(entry)
    
    def mostrar_teclado_numerico(self, entry_widget=None, callback=None):
        """
        Muestra el teclado numérico
        
        Args:
            entry_widget: widget Entry donde insertar valores (opcional)
            callback: función callback cuando se completa la entrada (opcional)
        """
        # Si no se proporciona explícitamente, usar el widget enfocado guardado
        widget_a_usar = entry_widget or self.widget_enfocado
        TecladoNumerico.mostrar_teclado(self.root, widget_a_usar, callback)
