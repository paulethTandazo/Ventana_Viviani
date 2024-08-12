# Ventana_Viviani
##Descripción 
Este proyecto utiliza técnicas númericas para calcular la aproximación del perímetro de la ventana de viviani, una curva espacial que surge de la intersección de una esfera y un cilindro. 
## Fórmulas para la aproximación del perímetro}
El cálculo del perímetro de la ventana de viviani se realiza utilizando la siguiente aproximación mediante la suma de riema: 
```python
def perimetro_viviani(r, n):
    delta_t = 2 * np.pi / n
    t = np.linspace(0, 2 * np.pi, n)
    
    dx_dt = -r * np.sin(t)
    dy_dt = r * np.cos(t)
    dz_dt = r * np.cos(t / 2)
    
    integrando = np.sqrt(dx_dt**2 + dy_dt**2 + dz_dt**2)
    
    L = np.sum(integrando) * delta_t
    return L
