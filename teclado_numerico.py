"""
Módulo de Teclado Numérico
Proporciona una interfaz de teclado numérico para ingresar expresiones matemáticas
"""

import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk


class TecladoNumerico:
    """Clase para mostrar un teclado numérico con funciones matemáticas"""
    
    def __init__(self, root, entry_widget=None, callback=None):
        """
        Inicializa el teclado numérico
        
        Args:
            root: ventana padre
            entry_widget: widget Entry donde insertar valores (opcional)
            callback: función callback cuando se completa la entrada (opcional)
        """
        self.root = root
        self.entry_widget = entry_widget
        self.callback = callback
        self.ventana = None
        
    def mostrar(self):
        """Muestra la ventana del teclado numérico"""
        # SIEMPRE detectar el widget enfocado en este momento
        widget_enfocado = None
        try:
            w = self.root.focus_get()
            # Verificar si tiene el método get() (es un Entry)
            if w and hasattr(w, 'get') and hasattr(w, 'delete') and hasattr(w, 'insert'):
                widget_enfocado = w
        except:
            pass
        
        # Usar el widget enfocado detectado AHORA, no el que se pasó al constructor
        if widget_enfocado:
            self.entry_widget = widget_enfocado
        
        # Si aún no hay widget, mostrar error
        if not self.entry_widget:
            messagebox.showwarning(
                "Sin enfoque",
                "Por favor, haz clic en la celda o en el campo ESCALAR\ndonde quieres escribir"
            )
            return
        
        # Crear ventana
        self.ventana = ctk.CTkToplevel(self.root)
        self.ventana.title("TECLADO NUMÉRICO")
        self.ventana.geometry("500x600")
        self.ventana.resizable(False, False)
        self.ventana.attributes("-topmost", True)
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.ventana)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Frame para mostrar valor actual
        display_frame = ctk.CTkFrame(main_frame)
        display_frame.pack(fill="x", pady=(0, 10))
        
        display_label = ctk.CTkLabel(
            display_frame,
            text="ENTRADA:",
            font=("Arial", 10),
            text_color="gray"
        )
        display_label.pack(side="left", padx=5)
        
        self.display_entry = ctk.CTkEntry(
            display_frame,
            font=("Arial", 14, "bold"),
            height=40
        )
        self.display_entry.pack(side="left", fill="x", expand=True, padx=5)
        
        # Frame para botones
        botones_frame = ctk.CTkFrame(main_frame)
        botones_frame.pack(fill="both", expand=True)
        
        # Definir botones
        botones = [
            # Números y operaciones básicas
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "(", ")"],
            
            # Operaciones
            ["+", "^", "←", "C"],
            
            # Funciones matemáticas
            ["sqrt", "log", "ln", "sin"],
            ["cos", "tan", "pi", "e"],
        ]
        
        # Crear botones
        for fila_idx, fila in enumerate(botones):
            fila_frame = ctk.CTkFrame(botones_frame)
            fila_frame.pack(fill="x", pady=3)
            
            for col_idx, texto in enumerate(fila):
                if texto == "C":
                    # Botón limpiar (rojo)
                    btn = ctk.CTkButton(
                        fila_frame,
                        text=texto,
                        font=("Arial", 12, "bold"),
                        width=100,
                        height=40,
                        fg_color=("#E74C3C", "#C0392B"),
                        hover_color=("#C0392B", "#A93226"),
                        command=self._limpiar
                    )
                elif texto == "←":
                    # Botón retroceso
                    btn = ctk.CTkButton(
                        fila_frame,
                        text=texto,
                        font=("Arial", 12, "bold"),
                        width=100,
                        height=40,
                        fg_color=("#F39C12", "#D68910"),
                        hover_color=("#D68910", "#BA4A00"),
                        command=self._retroceso
                    )
                elif texto in ["sqrt", "log", "ln", "sin", "cos", "tan", "pi", "e"]:
                    # Botones de funciones (azules)
                    btn = ctk.CTkButton(
                        fila_frame,
                        text=texto,
                        font=("Arial", 11, "bold"),
                        width=100,
                        height=40,
                        fg_color=("#3498DB", "#2980B9"),
                        hover_color=("#2980B9", "#1F618D"),
                        command=lambda t=texto: self._agregar_funcion(t)
                    )
                else:
                    # Botones normales
                    btn = ctk.CTkButton(
                        fila_frame,
                        text=texto,
                        font=("Arial", 12, "bold"),
                        width=100,
                        height=40,
                        command=lambda t=texto: self._agregar(t)
                    )
                
                btn.pack(side="left", fill="x", expand=True, padx=2)
        
        # Frame para botones de acción
        accion_frame = ctk.CTkFrame(main_frame)
        accion_frame.pack(fill="x", pady=(10, 0))
        
        # Botón aceptar
        btn_aceptar = ctk.CTkButton(
            accion_frame,
            text="ACEPTAR",
            font=("Arial", 12, "bold"),
            height=40,
            fg_color=("#27AE60", "#229954"),
            hover_color=("#229954", "#1E8449"),
            command=self._aceptar
        )
        btn_aceptar.pack(side="left", fill="x", expand=True, padx=2)
        
        # Botón cancelar
        btn_cancelar = ctk.CTkButton(
            accion_frame,
            text="CANCELAR",
            font=("Arial", 12, "bold"),
            height=40,
            command=self._cancelar
        )
        btn_cancelar.pack(side="left", fill="x", expand=True, padx=2)
        
        # No cargar valores anteriores - el display siempre comienza vacío
        # El usuario verá el valor anterior en el campo si ya existe
        
        # Asegurarse que el display_entry tiene focus para que los botones escriban aquí
        self.display_entry.focus()
    
    def _agregar(self, caracter):
        """Agrega un carácter en la posición actual del cursor"""
        # Obtener posición actual del cursor
        cursor_pos = self.display_entry.index(ctk.INSERT)
        # Insertar en la posición actual, no al final
        self.display_entry.insert(cursor_pos, caracter)
        # Mantener focus
        self.display_entry.focus()
    
    def _agregar_funcion(self, funcion):
        """Agrega una función con paréntesis en la posición actual"""
        cursor_pos = self.display_entry.index(ctk.INSERT)
        
        if funcion in ["pi", "e"]:
            # Constantes sin paréntesis
            self.display_entry.insert(cursor_pos, funcion)
        else:
            # Funciones con paréntesis
            self.display_entry.insert(cursor_pos, f"{funcion}()")
            # Posicionar cursor dentro de los paréntesis
            nueva_pos = str(int(cursor_pos) + len(funcion) + 1)  # +1 para el "("
            self.display_entry.icursor(nueva_pos)
        
        # Asegurarse que el display_entry tiene focus
        self.display_entry.focus()
    
    def _retroceso(self):
        """Elimina el carácter antes del cursor"""
        cursor_pos = self.display_entry.index(ctk.INSERT)
        if cursor_pos > 0:
            self.display_entry.delete(str(int(cursor_pos) - 1), cursor_pos)
        self.display_entry.focus()
    
    def _limpiar(self):
        """Limpia toda la entrada"""
        self.display_entry.delete(0, ctk.END)
        self.display_entry.focus()
    
    def _aceptar(self):
        """Acepta la entrada y la coloca en el widget"""
        valor = self.display_entry.get().strip()
        
        if not valor:
            messagebox.showwarning(
                "Entrada vacía",
                "Por favor, ingresa un valor o una expresión",
                parent=self.ventana
            )
            return
        
        # Si hay un widget de entrada, actualizar su valor
        if self.entry_widget:
            try:
                self.entry_widget.delete(0, tk.END)
                self.entry_widget.insert(0, valor)
                self.entry_widget.focus()  # Dar focus de nuevo al widget
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo escribir en el campo: {e}", parent=self.ventana)
                return
        
        # Llamar callback si existe
        if self.callback:
            self.callback(valor)
        
        # Cerrar ventana
        self.ventana.destroy()
    
    def _cancelar(self):
        """Cancela y cierra la ventana"""
        self.ventana.destroy()
    
    @staticmethod
    def mostrar_teclado(root, entry_widget=None, callback=None):
        """
        Método estático para mostrar el teclado directamente
        
        Args:
            root: ventana padre
            entry_widget: widget Entry donde insertar valores
            callback: función callback cuando se completa la entrada
        """
        teclado = TecladoNumerico(root, entry_widget, callback)
        teclado.mostrar()
