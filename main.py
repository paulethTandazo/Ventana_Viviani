import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from tkinter import ttk

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text, background="yellow", relief="solid", borderwidth=1, font=("Arial", 10))
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

# Función para dibjar la esfera de radio r
def dibujar_esfera(r):
    u = np.linspace(0, 2*np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = r*np.outer(np.cos(u), np.sin(v))
    y = r*np.outer(np.sin(u), np.sin(v))
    z = r*np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color="w", alpha=0.3)

# Función para dibujar el cilindo de radio r/2
def dibujar_cilindro(r):
    u = np.linspace(0, 2*np.pi, 30)
    z = np.linspace(-r, r, 30)
    X = r/2 * (1 + np.cos(u))
    Y = r/2 * np.sin(u)
    a,Z = np.meshgrid(u,z)
    ax.plot_surface(X, Y, Z, color="b", alpha=0.1)

# Función para calcular los puntos de la Ventana de Viviani
def obtener_puntos_viviani(r, n):
    t = np.linspace(0, 2 * np.pi, n)
    x = r/2 * (1 + np.cos(t))
    y = r/2 * np.sin(t)
    z = r * np.sin(t / 2)
    return x, y, z

# Función para calcular el perímetro aproximado usando suma de Riemann
def calcular_perimetro_viviani(r, n):
    delta_t = 2 * np.pi / n
    t = np.linspace(0, 2 * np.pi, n)
    
    dx_dt = -r/2 * np.sin(t)
    dy_dt = r/2 * np.cos(t)
    dz_dt = r/2 * np.cos(t / 2)
    
    integrando = np.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
    
    L = np.sum(integrando) * delta_t
    return L

# Función para actualizar la gráfica
def update_plot():
    try:
        r = float(entry_radius.get())
        n = int(entry_subdiv.get())
        
        if r <= 0:
            raise ValueError("El radio debe ser mayor que 0.")
        if n <= 2:
            raise ValueError("El número de subdivisiones debe ser mayor que 2.")
        
        ax.clear()
        
        dibujar_esfera(r)
        dibujar_cilindro(r)

        x, y, z = obtener_puntos_viviani(r, n)
        ax.plot(x, y, z, color="r")
        ax.plot(x,y,-z, color="r")
        perimetro = calcular_perimetro_viviani(r, n)
        label_result.config(text=f"Perímetro aproximado: {perimetro:.2f}")
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        # Configuración de la cuadrícula como hoja milimetrada
        ax.xaxis._axinfo['grid'].update(color = 'lightgray', linestyle = '-', linewidth = 0.5)
        ax.yaxis._axinfo['grid'].update(color = 'lightgray', linestyle = '-', linewidth = 0.5)
        ax.zaxis._axinfo['grid'].update(color = 'lightgray', linestyle = '-', linewidth = 0.5)
        
        canvas.draw()
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))

# Función para limpiar la gráfica y las entradas
def clear_plot():
    entry_radius.delete(0, tk.END)
    entry_subdiv.delete(0, tk.END)
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    label_result.config(text="")
    canvas.draw()

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Visualización de la Ventana de Viviani")

# Estilo y color de la ventana principal
root.configure(bg="white")

# Marco superior (HBox) con borde negro grueso y esquinas redondeadas
frame_top = tk.Frame(root, bg="white", bd=0.0005, relief="solid", highlightbackground="black", highlightthickness=2, highlightcolor="black")
frame_top.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Entradas para el radio y el número de subdivisiones
label_radius = tk.Label(frame_top, text="Radio:", bg="white", font=('Arial', 12))
label_radius.grid(row=0, column=0, pady=10, padx=5, sticky="w")

entry_radius = tk.Entry(frame_top, font=('Arial', 10))
entry_radius.grid(row=0, column=1, pady=10, padx=5, sticky="w")
ToolTip(entry_radius, "Radio: El radio de la figura a graficar.")

label_subdiv = tk.Label(frame_top, text="Subdivisiones:", bg="white", font=('Arial', 12))
label_subdiv.grid(row=0, column=2, pady=10, padx=5, sticky="w")

entry_subdiv = tk.Entry(frame_top, font=('Arial', 10))
entry_subdiv.grid(row=0, column=3, pady=10, padx=5, sticky="w")
ToolTip(entry_subdiv, "Subdivisiones: Número de particiones para aproximar el perímetro.")

# Botones de generación y limpieza
button_update = tk.Button(frame_top, text="Generar", command=update_plot, bg="#4CAF50", fg="white", font=('Arial', 10))
button_update.grid(row=0, column=4, pady=10, padx=5, sticky="w")

button_clear = tk.Button(frame_top, text="Limpiar", command=clear_plot, bg="#f44336", fg="white", font=('Arial', 10))
button_clear.grid(row=0, column=5, pady=10, padx=5, sticky="w")

# Etiqueta para mostrar el resultado del perímetro
label_result = tk.Label(frame_top, text="", font=('Arial', 12, 'bold'), bg="white", fg="blue")
label_result.grid(row=1, column=0, columnspan=6, pady=10)

# Marco inferior (VBox) con borde negro grueso, esquinas redondeadas, y fondo amarillo pastel
frame_bottom = tk.Frame(root, bg="#FFFACD", bd=0.00005, relief="solid", highlightbackground="black", highlightthickness=2, highlightcolor="black")
frame_bottom.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Crear la figura de Matplotlib con fondo amarillo pastel
fig = plt.figure(facecolor='#FFFACD')
ax = fig.add_subplot(111, projection='3d')

canvas = FigureCanvasTkAgg(fig, master=frame_bottom)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Inicializar la gráfica vacía con hoja milimetrada
ax.clear()
ax.set_facecolor('#FFFACD')  # Fondo amarillo pastel también en el área del gráfico
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.xaxis._axinfo['grid'].update(color = 'lightgray', linestyle = '-', linewidth = 0.5)
ax.yaxis._axinfo['grid'].update(color = 'lightgray', linestyle = '-', linewidth = 0.5)
ax.zaxis._axinfo['grid'].update(color = 'lightgray', linestyle = '-', linewidth = 0.5)
canvas.draw()

# Iniciar el bucle principal de la interfaz
root.mainloop()
