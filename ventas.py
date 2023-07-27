import tkinter as tk
from fpdf import FPDF
from reportlab.pdfgen import canvas
#debes instalar el modulo fpdf
# Clase para generar el PDF
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Sistema de Ventas - Informe", 0, 1, "C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(10)

    def chapter_body(self, content):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, content)
        self.ln()

    def chapter_table(self, headers, data):
        self.set_font("Arial", "B", 12)
        for header in headers:
            self.cell(40, 10, header, 1, 0, "C")
        self.ln()
        self.set_font("Arial", "", 12)
        for row in data:
            for item in row:
                self.cell(40, 10, str(item), 1, 0, "C")
            self.ln()
        self.ln()

# Función para generar el informe en PDF
def generar_informe():
    # Obtener los datos de ventas y realizar cálculos
    ventas = obtener_datos_ventas()
    total_ventas = sum(venta["monto"] for venta in ventas)

    # Crear el archivo PDF
    pdf = PDF()
    pdf.add_page()

    # Generar el contenido del informe
    pdf.chapter_title("Informe de Ventas")
    pdf.chapter_body(f"Total de Ventas: ${total_ventas:.2f}\n\n")
    pdf.chapter_table(["Fecha", "Producto", "Cantidad", "Monto"], [[venta["fecha"], venta["producto"], venta["cantidad"], venta["monto"]] for venta in ventas])

    # Guardar el archivo PDF
    pdf.output("informe_ventas.pdf")

    # Mostrar mensaje de confirmación
    tk.messagebox.showinfo("Informe generado", "Se ha generado el informe de ventas en el archivo informe_ventas.pdf")

# Función para obtener los datos de ventas (ejemplo)
def obtener_datos_ventas():
    return [
        {"fecha": "2023-07-01", "producto": "Producto A", "cantidad": 5, "monto": 100.0},
        {"fecha": "2023-07-02", "producto": "Producto B", "cantidad": 3, "monto": 75.0},
        {"fecha": "2023-07-03", "producto": "Producto C", "cantidad": 2, "monto": 50.0},
    ]

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Sistema de Ventas")

# Crear botón para generar el informe
boton_generar_informe = tk.Button(ventana_principal, text="Generar Informe", command=generar_informe)
boton_generar_informe.pack()

# Iniciar el bucle principal del programa
ventana_principal.mainloop()
