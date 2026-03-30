import db
from sqlalchemy import Column, Integer, Boolean, String, Date
from datetime import date

'''
Creamos una clase llamada Tarea 
Esta clase va a ser nuestro modelo de datos de la taresa (el cual nos servira luego para la base de datos 
Esta clase va a almacenar la información a una tarea 
'''
class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) # Identificador unico de la tarea (no puede haber dos tareas)
    contenido = Column(String(200), nullable=False)  # Contenido de la tarea, un texto de maximo 200 caracteres
    categoria = Column(String(50), nullable=False) # El campo nuevo categoria
    hecha = Column(Boolean, default=False) # Booleano que indica si una tarea ha sido hecha o no
    fecha_limite = Column(Date, nullable=True) # Campo nuevo de fecha limite

    def __init__(self, contenido, categoria="", hecha=False, fecha_limite=None):
        # Recordemos que el id no es necesario crearlo manualmente, lo añade la base de datos automaticamente
        self.contenido = contenido
        self.categoria = categoria
        self.hecha = hecha
        self.fecha_limite = fecha_limite

    def __repr__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.categoria, self.hecha)

    def __str__(self):
        return "Tarea {}: {} ({})".format(self.id, self.contenido, self.hecha)


