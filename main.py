import customtkinter as ctk
from operaciones import OperacionesMatrices
from instrucciones import Instrucciones
from ui_base import UIBase
from ui_escalar_matriz import UIEscalarMatriz
from ui_matriz_matriz import UIMatrizMatriz

# Configurar tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class AplicacionMatrices(UIBase):
    def __init__(self, root):
        """Inicializa la aplicación"""
        super().__init__(root, OperacionesMatrices())
        
        self.root.title("Análisis Numérico - Operaciones con Matrices")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        
        # Instancias de interfaces
        self.ui_escalar = UIEscalarMatriz(self.root, self.operaciones)
        self.ui_matriz = UIMatrizMatriz(self.root, self.operaciones)
        
        # Asignar función de regreso
        self.ui_escalar._regresar_menu = self.crear_interfaz_principal
        self.ui_matriz._regresar_menu = self.crear_interfaz_principal
        
        self.crear_interfaz_principal()
    
    def crear_interfaz_principal(self):
        """Crea el menú principal"""
        self.limpiar_ventana()
        self.root.geometry("900x600")
        
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        
        # Frame superior con título y botón help
        titulo_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        titulo_frame.pack(fill="x", pady=(0, 15))
        
        # Título principal
        titulo = ctk.CTkLabel(
            titulo_frame,
            text="ANÁLISIS NUMÉRICO",
            font=("Arial", 32, "bold")
        )
        titulo.pack(side="left", expand=True)
        
        # Botón de ayuda
        btn_ayuda_principal = ctk.CTkButton(
            titulo_frame,
            text="❓",
            font=("Arial", 18),
            width=40,
            height=40,
            command=lambda: self.mostrar_instrucciones(
                "INSTRUCCIONES - MENÚ PRINCIPAL",
                Instrucciones.get_instrucciones_principal()
            )
        )
        btn_ayuda_principal.pack(side="right", padx=5)
        
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
            command=self.ui_escalar.mostrar
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
            command=self.ui_matriz.mostrar
        )
        btn2.pack(fill="both", expand=True, pady=10)


if __name__ == "__main__":
    root = ctk.CTk()
    app = AplicacionMatrices(root)
    root.mainloop()
