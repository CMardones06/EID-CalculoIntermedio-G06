# Integral definida y área geométrica 
**Cálculo Intermedio (MATE1134) — EID, Grupo 06**
### Integrantes:
- Camila Mardones
- Beatriz Martin 
- Patricio Salazar 

## Sobre el proyecto 
El objetivo de este trabajo es mostrar la diferencia entre una integral definida y el área geométrica total. Para llevarlo a cabo, se planteó el uso de la función $f(x) = x² − 4$ en el intervalo [0, 3] y se creó una animación con Manim. 

La gráfica queda bajo el eje X entre el intervalo [0,2] y sobre el eje X en el intervalo [2, 3]. Al calcular la integral, las contribuciones negativas y positivas se suman con su signo:

+ Región negativa: −16/3 
+ Región positiva: 7/3 
+ Integral definida: −3 
+ Área geométrica total: 23/3 ≈ 7,67 

En la animación se pueden observar ambas regiones, el cálculo de la integral y cómo cambia la gráfica al aplicar el valor absoluto para obtener el área total. 

## Cómo ejecutar la animación 
Se trabajó en el S.O de Windows con **Python 3.14.3** y **Manim Community 0.22.0.**, se utilizó **MiKTeX**, porque al inicio Manim no lograba procesar las fórmulas escritas en LaTeX. MiKTeX permitió generar las expresiones matemáticas usadas con `MathTex`. 

Con Manim y las demás dependencias instaladas, abrir una terminal en la carpeta del proyecto y ejecutar: 

```bash
python -m manim -pql proyecto.py AreasIntegral 
```
El archivo principal es `proyecto.py` y la escena se llama `AreasIntegral.` 

## Trabajo del grupo 
+ **Camila Mardones:** programación en Python y desarrollo de la animación con Manim 
+ **Beatriz Martin:** investigación de fundamentos matemáticos y desarrollo de los cálculos 
+ **Patricio Salazar:** edición del video e integración de audios 

## Fuentes consultadas 
+ Apunte del curso: Introducción a la integral: Apunte base común para el proyecto de investigación y visualización. 
+ Santiago Acosta, R. D. (2017). Cálculo integral. Pearson Educación. https://elibro.net/es/lc/uctemuco/titulos/113537 
+ Strang, G. y Herman, E. (2022). Cálculo volumen 1. OpenStax. https://openstax.org/details/books/c%C3%A1lculo-volumen-1 
+ Stewart, J. (2012). Cálculo de una variable: Trascendentes tempranas (7.ª ed.). Cengage Learning Editores. https://www.cozing.com.bo/uploads/document/file/7/15594248204566.pdf 
+ Documentación de Manim Community: https://docs.manim.community/en/stable/ 

## Uso de IA 
se usó **Gemini** y **ChatGPT** como apoyo para resolver dudas de cálculo, trabajar con el código de Manim, solucionar errores y revisar la redacción del guión y la documentación. Los cálculos se contrastaron con el material del curso y las fuentes consultadas, y todo código fue puesto a prueba y modificado para que cumpla su función de manera adecuada. 