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
    * [High order functions: filter, map y reduce](#high-order-functions-filter-map-y-reduce)
    * [Proyecto: filtrando datos](#proyecto-filtrando-datos)
5. [Manejo de errores](#manejo-de-errores)
    * [Los errores en el código](#los-errores-en-el-código)
    * [Debugging](#debugging)
    * [Manejo de excepciones](#manejo-de-excepciones)
    * [Poniendo a prueba el manejo de excepciones](#poniendo-a-prueba-el-manejo-de-excepciones)
    * [Assert statements](#assert-statements)
6. [Manejo de archivos](#manejo-de-archivos)
    * [¿Cómo trabajar con archivos?](#cómo-trabajar-con-archivos)
    * [Trabajando con archivos de texto en Python](#trabajando-con-archivos-de-texto-en-python)

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

**lambda**: Es una funcion que solo toma un argumento y su funcion es para abreviar hacer la sintaxis del codigo un poco mas ligera y ahorrar tiempo
```py
palindrome = lambda string: string == string[::-1]

palindrome('ana')
# True

def palindrome(string):
    return string == string[::-1]

palindrome('ana')
# True
```

## High order functions: filter, map y reduce

Es una función que recibe como parámetro otra función.
```py
def saludo(func):
    return func()

def hola():
    print('Hola')

def adios():
    print('Adios')

saludo(hola)
# Hola
saludo(adios)
# Adios
```
### Filter
```py
my_list = [1,4,5,6,9,13,19,21]

odd = list(filter(lambda x: x&2 != 0, my_list))

print(odd)
# [1,5,9,13,19,21]
```
Filter recibe 2 parámetros, una función y un iterable.

### map
```py
my_list = [1,2,3,4,5]

squares = list(map(lambda x: x**2, my_list))

print(squares)
# [1,4,9,16,25]
```
Map recibe 2 parámetros, una función y un iterable.

### reduce
```py
from functools import reduce

my_list = [2,2,2,2,2]

all_multiplied = reduce(lambda a, b: a*b, my_list)

print(all_multiplied)
# 32
```
Reduce es importada del módulo functools. Recibe 2 parámetros, una función y un iterable.

## Proyecto: filtrando datos

```py
DATA = [
{
'name': 'Facundo',
'age':
72
'organization': 'Platzi',
'position': 'Technical Coach',
'language': 'python',
},
{
'name': 'Luisana',
'age':
33
'organization': 'Globant',
'position': 'UX Designer',
'language': 'javascript',
}
]
```

[Archivo local](/code/filtrando_datos.py)

# Manejo de errores

## Los errores en el código

![Errores](/images/errors.PNG)

El manejo de errores es muy importante y los mejores trucos como ya lo dijo Facundo son:

* Leer el error (Conozco programadores y hasta yo en un inicio trataba de revisar el código sin revisar el traceback)
* Leer el traceback de abajo hacia arriba

[Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)

[Python Excepcions - Local](/files/python_exceptions.pdf)

**Errores en el código**

Cuando python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos como traceback, puesde ser debido a:

* **Errores de Sintaxis (SyntaxError)** → escribimos mal alguna palabra clave (typo), el programa no se ejecuta.
* **Excepciones (Exception)** → Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, tambipen pueden generarse dentro del código o fuera de el (elevar una excepción)
    
    * KeyboardInterrupt -> Ctrl + C
    * KeyError -> Cuando tratamos de acceder a una llave que no existe
    * IndexError -> Cuando tratamos de acceder a un índice que no existe
    * FileNotFoundError -> Archivo que no existe
    * ZeroDivisionError -> Dividir entre 0
    * ImportError -> Intentamos importar un módulo que tiene un error

    Estos son solo algunos ejemplos, hay más de 50 excepciones. 

**Lectura de un traceback**

* La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
* En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
* La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
* La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)
```
Traceback (most recent call last):
    File "<stdin>", line 1 , in <module>
ZeroDivisionError: division by zero
```

**Elevar una excepción**

* Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback

## Debugging

Debugging o depuración es una herramienta que traen varios editores de código con el objetivo de solucionar nuestros errores de lógica. Revisemos la herramienta debugging de VSCode

En este entorno podemos acceder a funcionalidades como:
* pause → permite pausar la ejecución del programa
* step over → permite avanazr un solo paso en el programa
* step in → igresamos a un bloque secundario del programa (funciones)
* step out → salimos del bloque secundario
* restart → reinicia el programa
* stop → detiene el programa
Además podemos generar breakpoints, que son puntos en los que el programa se detendrá para ayudarnos a depurar el código

**Nota:**

Existen herramientas de debugging propias de python como el módulo pdb o los breakpoints (a partir de python 3.7)

[Python debug configurations in Visual Studio Code](https://code.visualstudio.com/docs/python/debugging)

[Archivo local](/code/debugging.py)

## Manejo de excepciones

* **TRY**: En el try se coloca código que esperamos que pueda lanzar algún error.
* **EXCEPT**: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
* **ELSE**: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
* **FINALLY**: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

[Exceptions](https://docs.python.org/3/tutorial/errors.html#exceptions)

[Archivo local](/code/exceptions.py)

### raise

Esta instrucción nos permite generar errores, es decir crear nuestros propios errores cuando detectemos que nuestro programa no actúa como debería con cierto tipo de datos

Su sintaxis es:
```py
	raise <NombreError>("<descripción del error>")
```

## Poniendo a prueba el manejo de excepciones

Vamos a tomar en cuenta el archivo de la clase anterior y lo vamos a mejorar, por el momento solo funciona para describir errores, ahora, vamos a optimizarlo para tener diferentes casos de uso y que levante los errores dependiendo de los casos de uso.

[Archivo local](/code/manejo_excepciones.py)

## Assert statements

Definicion que nos da Al Sweigart en su libro “How to automate the boring stuff with Python”:

>In plain English, an assert statement says, “I assert that this condition holds true, and if not, there is a bug somewhere in the program.” Unlike exceptions, your code should not handle assert statements with try and except; if an assert fails, your program should crash. By failing fast like this, you shorten the time between the original cause of the bug and when you first notice the bug. This will reduce the amount of code you will have to check before finding the code that’s causing the bug.Assertions are for programmer errors, not user errors. For errors that can be recovered from (such as a file not being found or the user enter-ing invalid data), raise an exception instead of detecting it with an assertstatement.


Es una manera poco usual de manejar los errores en python.

Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo AssertionError y nos muestra un mensaje.

Su sintaxis es:
```py
assert <condicion>, <"mensaje">
<código>
```

Ejemplo de la función palindromo.
```py
def palindrome(string):
    assert len(string) > 0, 'No se puede ingresar una cadena vacía'
    return string == string[::-1]

print(palindrome(''))
# AssertionError: No se puede ingresar una cadena vacía
```

### Reto

Utiliza assert statements para evitar que el usuario ingrese un número negativo en nuestro programa de divisores.

[Archivo local](/code/asserts_statements.py)

# Manejo de archivos

## ¿Cómo trabajar con archivos?

Modos de Apertura

* r -> Solo lectura
* r+ -> Lectura y escritura
* w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
* w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
* a -> Añadido (agregar contenido). Crea el archivo si éste no existe
* a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

Para abrir un archivo seguimos las siguiente estructura
```py
with open(<ruta>, <modo_apertura>) as <nombre>
```
`with` Es un manejador contextual, nos ayuda a controlar el flujo del archivo (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)

`open(ruta,modo_apertura):` es una función que necesita de dos parámetros

* ruta: es donde se encuentra nuestro archivo en nuestro equipo.
* modo_de_apertura: como vamos a abrir el archivo.
    
`as <nombre>` nos ayuda a darle una abreviatura o un nombre a los datos que acabamos de leer.

## Trabajando con archivos de texto en Python

[CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

[Archivo local](/code/archivos.py)