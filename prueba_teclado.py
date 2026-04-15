"""
Programa de prueba para el teclado numérico
"""

import customtkinter as ctk
from teclado_numerico import TecladoNumerico

class PruebaTeclado:
    def __init__(self, root):
        self.root = root
        self.root.title("Prueba Teclado Numerico")
        self.root.geometry("600x400")
        
        # Frame principal
        main_frame = ctk.CTkFrame(root)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Prueba 1: Escalar
        titulo1 = ctk.CTkLabel(main_frame, text="PRUEBA 1: Escalar", font=("Arial", 14, "bold"))
        titulo1.pack(pady=10)
        
        frame1 = ctk.CTkFrame(main_frame)
        frame1.pack(fill="x", pady=5)
        
        ctk.CTkLabel(frame1, text="Valor:", font=("Arial", 11)).pack(side="left", padx=5)
        self.escalar_entry = ctk.CTkEntry(frame1, width=150, font=("Arial", 11))
        self.escalar_entry.pack(side="left", padx=5)
        
        btn1 = ctk.CTkButton(
            frame1,
            text="Abrir Teclado",
            command=self._abrir_teclado_escalar,
            font=("Arial", 11)
        )
        btn1.pack(side="left", padx=5)
        
        # Prueba 2: Matriz (tabla)
        titulo2 = ctk.CTkLabel(main_frame, text="PRUEBA 2: Matriz (2x2)", font=("Arial", 14, "bold"))
        titulo2.pack(pady=10)
        
        frame2 = ctk.CTkFrame(main_frame)
        frame2.pack(fill="x", pady=5)
        
        self.matriz_entries = []
        for i in range(2):
            fila_entries = []
            for j in range(2):
                entry = ctk.CTkEntry(frame2, width=80, font=("Arial", 11))
                entry.grid(row=i, column=j, padx=3, pady=3)
                fila_entries.append(entry)
            self.matriz_entries.append(fila_entries)
        
        btn2 = ctk.CTkButton(
            main_frame,
            text="Abrir Teclado (clickea una celda primero)",
            command=self._abrir_teclado_matriz,
            font=("Arial", 11)
        )
        btn2.pack(pady=10)
        
        # Instrucciones
        instrucciones = ctk.CTkLabel(
            main_frame,
            text="Para probar con las matrices:\n1. Haz click en una celda\n2. Luego click en 'Abrir Teclado'\n3. Escribe en el teclado y presiona ACEPTAR",
            font=("Arial", 10),
            text_color="gray"
        )
        instrucciones.pack(pady=10)
    
    def _abrir_teclado_escalar(self):
        """Abre el teclado para el escalar"""
        TecladoNumerico.mostrar_teclado(self.root, entry_widget=self.escalar_entry)
    
    def _abrir_teclado_matriz(self):
        """Abre el teclado para la matriz"""
        TecladoNumerico.mostrar_teclado(self.root)


if __name__ == "__main__":
    root = ctk.CTk()
    app = PruebaTeclado(root)
    root.mainloop()
