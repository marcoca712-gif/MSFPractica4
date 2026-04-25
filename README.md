[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=marcoca712-gif/MSFPractica4)

# Práctica: Sistema Endocrino

## Información del estudiante

Campoy Alegria Marco Anytonio \[21212145]; L21212145@tectijuana.edu.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1.Dibujar el diagrama elÈctrico del sistema endocrino, identiÖcando cada uno de sus elementos, es decir,
componentes, voltajes, corrientes y nodos de entrada y salida. 
2. (Determine el modelo de ecuaciones integro-diferenciales.
3. Calcule la funciÛn de transferencia del sistema.
4. Calcule el error en estado estacionario.
5. Ilustre la respuesta en lazo abierto del control y del caso a un escalÛn unitario de entrada en Python
o Simulink.
6. DiseÒe un controlador en lazo cerrado, con base en el siguiente diagrama, que permita eliminar el
error en la respuesta del caso

## Descripción detallada del sistema
El sistema endócrino regula funciones fisiológicas mediante la liberación de hormonas en el torrente sanguíneo, las cuales viajan a órganos diana (u órganos blancos) para inducir respuestas específicas. Esta dinámica puede representarse de forma simplificada mediante un circuito eléctrico de segundo orden, modelando los procesos de secreción, transporte y respuesta hormonal bajo las siguientes suposiciones:

La secreción hormonal desde una glándula (como la hipófisis o el hipotálamo) se modela mediante una fuente de voltaje de entrada V_e(t), que representa un estímulo inicial al sistema (por ejemplo, una señal homeostática o neural).

El proceso de liberación y difusión hormonal en el torrente sanguíneo se modela con una resistencia R_1, asociada al retraso y pérdida de señal hormonal durante su transporte.

El almacenamiento o acumulación temporal de hormonas (por ejemplo, en tejidos o compartimentos intermedios) se representa con un capacitor C, que regula la disponibilidad hormonal en el tiempo.

La respuesta del órgano diana (como la glándula suprarrenal o la tiroides) se modela mediante una segunda rama con una resistencia R_2 y una inductancia L representando la resistencia al cambio hormonal en el tejido y la inercia de respuesta biológica, respectivamente.

Se identifican los siguientes dos flujos en el sistema: el flujo de la secreción hormonal F_e(t) y el flujo de la absorción hormonal en el órgano diana F_s(t).

Palabras clave: Funciones fisiologicas; Difusion hormonal; Flujo Fs (t); Torrente Sanguineo;

## Lista de archivos incluidos en el repositorio

1\. Cuaderno computacional de MATLAB \[.mlx].
2. Modelo de Simulink \[.slx].
3. Archivos de Spyder \[.py].
4. Imagen con los parámetros del controlador.
5. Imágenes de las simulaciones \[.pdf].
6. Evidencia del análisis matemático: función de transferencia, modelo de ecuaciones integro-diferenciales, error en estado estacionario y estabilidad en lazo abierto.

7\. Modelo fisiológico en Biorender o BioArt.

## Referencias

\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley \& Sons, 2020.

\[4] T. Kind, T. J. Faes, J. W. Lankhaar, A. Vonk-Noordegraaf \& M. Verhaegen, "Estimation of three-and four-element Windkessel parameters using subspace model identification", IEEE Transactions on Biomedical Engineering, vol. 57, issue 7, pp. 1531-1538, Jul 2010. https://doi.org/10.1109/TBME.2010.2041351

