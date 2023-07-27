# ventas-python
Este código es un programa en Python que utiliza la biblioteca tkinter para crear una interfaz gráfica simple y generar un informe de ventas en formato PDF utilizando la biblioteca fpdf.
Importa las bibliotecas necesarias: tkinter para la interfaz gráfica y FPDF para generar el PDF.

Define una clase PDF que hereda de la clase FPDF para personalizar el formato del PDF.

Define varios métodos en la clase PDF para agregar contenido al PDF, como encabezado, título, texto y tabla.

Define una función generar_informe() que obtiene datos de ventas (simulados en este ejemplo) y utiliza la clase PDF para crear un informe en formato PDF con esos datos.

Define una función obtener_datos_ventas() que devuelve datos de ventas ficticios (como ejemplo).

Crea una ventana principal utilizando tkinter con un botón llamado "Generar Informe".

Cuando el usuario hace clic en el botón "Generar Informe", se llama a la función generar_informe() que crea el informe en PDF con los datos de ventas y lo guarda en un archivo llamado "informe_ventas.pdf".

Finalmente, muestra un mensaje de confirmación en una ventana emergente utilizando tk.messagebox.showinfo() para notificar al usuario que el informe ha sido generado y guardado.
Es importante tener en cuenta que este código es un ejemplo y utiliza datos de ventas simulados. Para que el programa funcione con datos reales, deberás reemplazar la función obtener_datos_ventas() con una función que realmente obtenga los datos de ventas de una fuente externa, como una base de datos o un archivo. Además, el diseño y el formato del PDF se pueden personalizar según las necesidades del usuario modificando los métodos en la clase PDF.
