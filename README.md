# Curso de Python Intermedio

![Logo](https://static.platzi.com/media/achievements/badge-intermedio-de-python-d0d16518-5edd-450a-b2a9-0710bded1494.png)

**Instructor:** Facundo García Martoni

## Indice

1. [Preparación antes de empezar](#preparación-antes-de-empezar)
    * [Bienvenida](#bienvenida)
    * [El Zen de Python](#el-zen-de-python)
    * [¿Qué es la documentación?](#qué-es-la-documentación)
2. [Entorno virtual](#entorno-virtual)
    * [¿Qué es un entorno virtual?](#qué-es-un-entorno-virtual)
    * [El primer paso profesional: creación de un entorno virtual](#el-primer-paso-profesional-creación-de-un-entorno-virtual)
    * [Instalación de dependencias con pip](#instalación-de-dependencias-con-pip)
    * [Una alternativa: Anaconda](#una-alternativa-anaconda)
3. [Alternativa a los ciclos: comprehensions](#alternativa-a-los-ciclos-comprehensions)
    * [Listas y diccionarios anidados](#listas-y-diccionarios-anidados)
    * [List comprehensions](#list-comprehensions)
    * [Dictionary comprehensions](#dictionary-comprehensions)
4. [Conceptos avanzados de funciones](#conceptos-avanzados-de-funciones)
    * [Funciones anónimas: lambda](#funciones-anónimas-lambda)

---

# Preparación antes de empezar

## Bienvenida

Fortalece tus habilidades para profesionalizarte con Python, uno de los lenguajes más utilizados en el mundo en desarrollo backend, ciencia de datos e inteligencia artificial. Aprende conceptos y practica con retos que elevarán tu nivel al programar.

* Utiliza list y dictionary comprehensions, y high order functions.
* Preparar un entorno virtual con pip.
* Maneja archivos de texto con el context manager.
* Aprende qué significan los errores y cómo manejarlos.

## El Zen de Python

[PEP 20 -- The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

Está escondido en la consola, una vez instalado Python se instala este secretito.
```py
python3

import this
"""
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
```
**En Español.**

* Bello es mejor que feo.
* Explícito es mejor que implícito.
* Simple es mejor que complejo.
* Complejo es mejor que complicado.
* Plano es mejor que anidado.
* Espaciado es mejor que denso.
* La legibilidad es importante.
* Los casos especiales no son lo suficientemente especiales como para romper las reglas.
* Sin embargo la practicidad le gana a la pureza.
* Los errores nunca deberían pasar silenciosamente.
* A menos que se silencien explícitamente.
* Frente a la ambigüedad, evitar la tentación de adivinar.
* Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
* A pesar de que esa manera no sea obvia a menos que seas holandés.
* Ahora es mejor que nunca.
* A pesar de que nunca es muchas veces mejor que *ahora* mismo.
* Si la implementación es difícil de explicar, es una mala idea.
* Si la implementación es fácil de explicar, puede que sea una buena idea.
* Los espacios de nombres son una gran idea, ¡tengamos más de esos!

## ¿Qué es la documentación?

[Python 3.9.4 documentation](https://docs.python.org/3/)

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

**La documentación es la biblia de cualquier programador.**

No puedes aspirar a aprender un lenguaje si no lees documentación. Sé que muchas personas se saltan eso porque piensan “ufff, es mucho texto, se ve feo”, etc. Pero es la documentación quien nos va a decir exactamente cómo funciona el lenguaje (y cualquier tecnología). No hay un solo desarrollador profesional que no lea documentación.

¡Y claro!, con esto no quiero decir que tengas que estar metido en la documentación siempre, pero quiero que sepas que la vas a consultar muchas veces cuando tengas problemas ❤️.

En ese paso de programador novato a programador profesional se encuentra aprender a consultar documentación, da el paso, no le temas a la documentación, es tu mejor amiga 😄.

# Entorno virtual

## ¿Qué es un entorno virtual?

**Sin entorno virtual**

![Sin VENV](/images/venv.png)

**Con entorno virtual**

![Con VENV](/images/with-venv.png)

Un entorno virtual es un directorio que contiene una instalación de Python de una versión en particular, además de unos cuantos paquetes adicionales.

**Ejemplo:**

La aplicación A puede tener su propio entorno virtual con la versión 1.0 instalada mientras que la aplicación B tiene otro entorno virtual con la versión 2.0. Si la aplicación B requiere que actualizar la librería a la versión 3.0, ésto no afectará el entorno virtual de la aplicación A.

[Venv](https://docs.python.org/es/3/tutorial/venv.html)

## El primer paso profesional: creación de un entorno virtual

Creación de ambiente Virtual:
```py
python3 -m venv nombre_venv
```
* Usualmente el nombre del ambiente virtual es venv.

Activación del ambiente virtual:

* Windows:
```
.\venv\Scripts\activate
```
* Unix o MacOS:
```
source venv/bin/activate
```
* Desactivar el ambiente virtual:
```
deactivate
```

## Instalación de dependencias con pip

**Pip** (package installer for python) Nos permite descargar paquetes de terceros para utilizarlos en nuestro enviroment, ademas se puede definir una versión especifica del paquete.

```py
pip install <paquete> # instala el paquete(pandas , matplotlib, bokeh, etc) que se especifique

pip freeze # muestra todos los paquetes instalados en tu ambiente virtual
```

Si quisiéramos que alguien mas pueda ejecutar nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se realiza con el comando:
```
pip freeze > requirements.txt
```
El resultado de `pip freeze` se escribe en `requirements.txt` (puedes usar otro nombre pero el mostrado es una buena practica)

para instalar paquetes desde un archivo como `requirements.txt` ejecutamos:
```
pip install -r requirements.txt 
```

## Una alternativa: Anaconda

Anaconda es un programa de Python que contiene los paquetes más utilizados en temas de ingeniería, matemáticas o ciencia, como pueden ser Matplotlib, SciPy y NumPy. Cuenta con versiones para los tres sistemas operativos más importantes: Mac, Windows y Linux.

Y es un ambiente de trabajo para la ciencia de datos que permite hacer funcionar aplicaciones y administrar fácilmente distintos paquetes. Así, Anaconda Navigator puede buscar paquetes en Anaconda Cloud o en otros repositorios, y está disponible para ambientes Windows, macOS y Linux.

[Anaconda](https://www.anaconda.com/products/individual)

# Alternativa a los ciclos: comprehensions

## Listas y diccionarios anidados

En esta clase vimos que podemos recorrer listas que contienes dicionarios y diccionarios que contienen listas.

Otro punto a resaltar es que por convención se debe utilizar el idioma inglés.
```py
def main():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname':'Oscar','lastname':'Palomino'}
    
    super_list = [
        {'firstname':'Oscar','lastname':'Palomino'},
        {'firstname':'Eduardo','lastname':'Cardenas'},
        {'firstname':'Lisney','lastname':'Gomez'},
        {'firstname':'Jurenni','lastname':'Berdugo'},
        {'firstname':'Ana','lastname':'Cardenas'},
        {'firstname':'Doris','lastname':'Toscano'},
    ]
    
    super_dict = {
        'natural_nums':[1,2,3,4,5,6],
        'integer_nums':[-1,-2,0,1,2],
        'floating_nums':[1.1,2.5,5.7,7.3,9.7]
    }
    
    for key, value in super_dict.items():
        print(f"""
Key: {key}
  * Value: {value}""")
    
    for item in super_list:
        print(item)


if __name__ == '__main__':
    main()
```

[Archivo local](/code/lists_and_dicts.py)

## List comprehensions

[List Comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

![List comprehension](/images/list-comprehension.PNG)

[Archivo local](/code/list_comprehension.py)

## Dictionary comprehensions

[PEP 274 -- Dict Comprehensions](https://www.python.org/dev/peps/pep-0274/)

![Dict comprehension](/images/dictionary-comprehension.PNG)

[Archivo local](/code/dictionary_comprehension.py)

# Conceptos avanzados de funciones

## Funciones anónimas: lambda

**lambda**: Es una funcion que solo toma un argumento y su funcion es para abreviar hacer la sintaxys del codigo un poco mas ligera y ahorrar tiempo

