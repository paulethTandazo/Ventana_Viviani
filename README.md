# Ventana De Viviani

Descripción: Este proyecto utiliza técnicas númericas para calcular la aproximación del perímetro de la ventana de viviani, una curva espacial que surge de la intersección de una esfera y un cilindro.

 ![Pantalla del Paciente](https://i.postimg.cc/fLjmPdZ3/ventana-viviani-2-0.png)
## Fórmulas para la aproximación del perímetro
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
```
### Explicación
**- r:**  radio de la esfera

**- n:** El número de subdivisiones (subintervalos) utilizados para aproximar 
### Cálculo
**1. delta_t:** Es el paso de la subdivisión, que es igual a 2π/n.

**2. t:** Un arreglo de valores en el intervalo [0, 2π], dividido en n partes iguales.

**3. dx_dt, dy_dt, dz_dt:** Derivadas de las coordenadas x, y, z con respecto al parámetro t, que describen la curva de la Ventana de Viviani.

**4. integrando:** La longitud de arco elemental de la curva en cada subdivisión, calculada como la raíz cuadrada de la suma de los cuadrados de dx_dt, dy_dt y dz_dt.

**5. L:** El perímetro aproximado, obtenido sumando todas las longitudes elementales y multiplicándolas por delta_t
