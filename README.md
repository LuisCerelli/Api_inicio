### Extracción de Información de Personajes de Rick and Morty

---

#### Descripción General

Este script tiene como objetivo realizar solicitudes HTTP a la API de **Rick and Morty** para obtener información de los personajes y sus características, como su nombre y especie. El código está diseñado para extraer los nombres de los personajes de un episodio específico de la serie y clasificarlos en dos categorías: **Humanos** y **No Humanos**.

El código se ha construido paso a paso, comenzando por la obtención de datos de personajes individuales, luego expandiéndose para realizar la misma operación para un grupo de personajes asociados a un episodio en particular. Finalmente, se filtran los personajes según su especie.

---

### Funcionamiento del Código

1. **Solicitud de Datos**:
   El código comienza realizando una solicitud `GET` a la API de Rick and Morty para obtener la información de los personajes de un episodio específico (en este caso, el episodio 1). Se utiliza la biblioteca `requests` para enviar las solicitudes HTTP y `json` para analizar las respuestas en formato JSON.

2. **Recorrido de Personajes**:
   Una vez que se extraen las URLs de los personajes del episodio, el código realiza solicitudes adicionales para cada personaje por separado. Luego, se analiza la información de cada uno para extraer su nombre y especie.

3. **Clasificación de Personajes**:
   Los personajes son clasificados en dos listas:
   - **lista_names_human**: Contiene los nombres de todos los personajes cuya especie es "Human".
   - **lista_names_other**: Contiene los nombres de todos los personajes de especies distintas a "Human".

4. **Impresión de Resultados**:
   Los nombres de los personajes se imprimen en formato de columna para mejorar la legibilidad, tanto para los humanos como para los no humanos.

---

### Ejemplo de Uso

Este código es útil para obtener y filtrar información de personajes de la serie. Por ejemplo, si se desea conocer cuántos personajes humanos y no humanos aparecen en el episodio 1, el código proporcionará la información organizada de manera sencilla. A continuación, se presenta un ejemplo de la salida:

```
La lista de los nombres de seres humanos es: 
Rick Sanchez
Morty Smith
...

En cambio, la lista de los seres NO humanos es: 
Birdperson
Gearhead
...
```

---

### Consideraciones

- **API Requests**: El código envía múltiples solicitudes a la API de Rick and Morty. Es importante considerar que el uso excesivo de solicitudes podría verse limitado por las políticas de la API. En proyectos más grandes, es recomendable implementar mecanismos de control de velocidad o manejo de errores.
  
- **Estructura de los Datos**: El script utiliza listas para almacenar los nombres de los personajes. Esto es eficiente para casos sencillos, pero para aplicaciones más complejas se podría considerar almacenar estos datos en estructuras más avanzadas, como bases de datos.

---

### Utilidad para la Ingeniería de Datos

***Este código es una excelente introducción a la integración con APIs externas en proyectos de Data Engineering. La habilidad de conectarse a una API, procesar la información obtenida y filtrarla según criterios específicos es fundamental en el trabajo diario de un Ingeniero de Datos. Este tipo de procesamiento es especialmente útil para la creación de pipelines de datos que extraen, transforman y cargan (ETL) información de fuentes dinámicas como APIs.***

Además, el proceso de clasificación y filtrado de datos en listas es un ejemplo de cómo los ingenieros de datos pueden preparar la información para análisis posteriores o visualizaciones, lo que facilita la toma de decisiones basada en datos precisos y actualizados.

---

### Posibles Mejoras y Extensiones

1. **Uso de Bases de Datos**: Los resultados pueden almacenarse en una base de datos para su uso posterior, lo cual es útil para proyectos de mayor envergadura.
   
2. **Automatización con Airflow**: Este script puede ser parte de un proceso automatizado utilizando Airflow, donde las solicitudes y el procesamiento de datos ocurren en intervalos programados.

3. **Optimización del Manejo de Errores**: Implementar un mejor manejo de errores, como la gestión de respuestas fallidas o solicitudes con límite de tiempo, es una mejora que aumentaría la robustez del código.

