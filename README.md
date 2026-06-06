# Taller 4 - APIs Públicas, MongoDB y EDA

**Curso:** Bases de Datos - UdeA  
**API usada:** [The Simpsons API](https://thesimpsonsapi.com/)

## Descripción
Flujo de Ciencia de Datos que extrae personajes de Los Simpsons,
los almacena en MongoDB y realiza un análisis exploratorio (EDA).

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecución
1. Asegúrate de tener conexión a MongoDB Atlas
2. Ejecuta la ingesta:
```bash
python ingesta.py
```
3. Abre el notebook:
```bash
python -m jupyter notebook
```
## Insights encontrados
- El 66.7% de personajes son hombres y el 33.3% mujeres
- 110 personajes están vivos, 8 fallecidos y 2 con estado desconocido
- La edad promedio es 35.5 años
- La ocupación más común es "Student" con 9 personajes
- Solo 47 de 120 personajes tienen edad registrada