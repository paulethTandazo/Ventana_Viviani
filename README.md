# Ventana De Viviani

**Descripción:** Este proyecto utiliza técnicas númericas para calcular la aproximación del perímetro de la ventana de viviani, una curva espacial que surge de la intersección de una esfera y un cilindro.

 ![Pantalla del Paciente](https://i.postimg.cc/Dyv8mN4c/viviani.png)
## 1. Generación de puntos en la Ventana de Viviani
Para dibujar esta curva en la computadora, necesitamos calcular muchos puntos en ese camino y luego conectarlos para ver la curva completa:
```python
ddef viviani_points(r, n):
    t = np.linspace(0, 2 * np.pi, n)
    x = r * (1 + np.cos(t))
    y = r * np.sin(t)
    z = 2 * r * np.sin(t / 2)
    return x, y, z

```
### La función viviani_points se encarga de calcular: 
**- r:**  Es como el tamaño de la curva; cuanto más grande es r, más grande es la curva.

**- n:**  Es cuántos puntos vamos a calcular a lo largo de la curva. Más puntos (n más grande) hacen que la curva se vea más suave y detallada.

**- t:**  Es una variable que va cambiando, y con cada cambio calculamos un nuevo punto en la curva. Es como si siguiéramos un mapa para trazar la curva.

Con estos valores, calculamos las coordenadas x, y, z, que son como las direcciones de cada punto en el espacio (imaginemos que x es adelante/atrás, y es izquierda/derecha, y z es arriba/abajo).

### 2. Cálculo del perímetro aproximado de la Ventana de Viviani

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

**- delta_t:** 2 np.pi / n: Calcula el pequeño incremento en t, correspondiente a la distancia entre los puntos de la curva para la aproximación.

**- dx_dt, dy_dt, dz_dt:**  Son las derivadas de las funciones x(t), y(t) y z(t) con respecto a t. Estas derivadas representan la velocidad de cambio de las coordenadas con respecto al parámetro t.

**- dx_dt: -r * np.sin(t):** Derivada de x(t) con respecto a t.

**- dy_dt: r * np.cos(t):** Derivada de y(t) con respecto a t.

**- dz_dt: r * np.cos(t / 2):** Derivada de z(t) con respecto a t.

**- integrando: np.sqrt(dx_dt**2+dy_dt**2+dz_dt**2): Este término representa la longitud diferencial a lo largo de la curva. Es decir, la longitud de un pequeño segmento de la curva en el espacio tridimensional.

**- L:np.sum(integrando) * delta_t:** Aquí se suma la longitud de todos los pequeños segmentos para aproximar el perímetro total de la Ventana de Viviani.


Este método de suma de Riemann es una técnica de integración numérica que divide la curva en pequeños segmentos y suma sus longitudes para obtener una aproximación del perímetro total.

