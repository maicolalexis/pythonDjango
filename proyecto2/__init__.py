'''se importa pymsql que es para poder usar MYSQL
ademas que se necesita usar un comando antes para poder importar
si no contiene pymsql y se instala usando pip install pyMySQL
y ademas se instala pillow si tampoco contiene pillow de la misma manera
para verificar si estan instalador escribimos pip list'''
import pymysql

pymysql.install_as_MySQLdb()