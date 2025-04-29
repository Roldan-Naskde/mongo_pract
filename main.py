#importamos mongoclient para conectar a MongoBD
from pymongo import MongoClient
#conectamos a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
#crear una base de datos
db = client["university"]

colection1 = db["students"]
colection2 = db["Teacher"]

list_students=[
{"name": "Juan Pérez", "age": 21, "career": "Ingeniería en Sistemas", "gmail": "juan.perez@example.com", "address": "Calle Ficticia 123, Ciudad X", "gender": "masculino"},
  {"name": "María González", "age": 22, "career": "Medicina", "gmail": "maria.gonzalez@example.com", "address": "Avenida Central 456, Ciudad Y", "gender": "femenino"},
  {"name": "Carlos Sánchez", "age": 20, "career": "Derecho", "gmail": "carlos.sanchez@example.com", "address": "Calle del Sol 789, Ciudad Z", "gender": "masculino"},
  {"name": "Ana López", "age": 23, "career": "Arquitectura", "gmail": "ana.lopez@example.com", "address": "Calle Luna 101, Ciudad A", "gender": "femenino"},
  {"name": "Luis Rodríguez", "age": 24, "career": "Psicología", "gmail": "luis.rodriguez@example.com", "address": "Calle Fuego 102, Ciudad B", "gender": "masculino"},
  {"name": "Marta Fernández", "age": 22, "career": "Pedagogía", "gmail": "marta.fernandez@example.com", "address": "Calle Viento 103, Ciudad C", "gender": "femenino"},
  {"name": "José Martínez", "age": 21, "career": "Contaduría", "gmail": "jose.martinez@example.com", "address": "Calle Mar 104, Ciudad D", "gender": "masculino"},
  {"name": "Laura Díaz", "age": 20, "career": "Enfermería", "gmail": "laura.diaz@example.com", "address": "Calle del Río 105, Ciudad E", "gender": "femenino"},
  {"name": "Pedro Pérez", "age": 23, "career": "Biología", "gmail": "pedro.perez@example.com", "address": "Calle Bosque 106, Ciudad F", "gender": "masculino"},
  {"name": "Paula Ramírez", "age": 25, "career": "Sociología", "gmail": "paula.ramirez@example.com", "address": "Calle Estrella 107, Ciudad G", "gender": "femenino"},
  {"name": "Raúl Hernández", "age": 21, "career": "Ingeniería Civil", "gmail": "raul.hernandez@example.com", "address": "Calle Muelle 108, Ciudad H", "gender": "masculino"},
  {"name": "Carmen Sánchez", "age": 22, "career": "Comunicación", "gmail": "carmen.sanchez@example.com", "address": "Calle Noche 109, Ciudad I", "gender": "femenino"},
  {"name": "Andrés Gómez", "age": 24, "career": "Historia", "gmail": "andres.gomez@example.com", "address": "Calle Sol 110, Ciudad J", "gender": "masculino"},
  {"name": "Verónica Ruiz", "age": 21, "career": "Letras", "gmail": "veronica.ruiz@example.com", "address": "Calle Lirio 111, Ciudad K", "gender": "femenino"},
  {"name": "Javier Ortega", "age": 23, "career": "Ingeniería Industrial", "gmail": "javier.ortega@example.com", "address": "Calle Templo 112, Ciudad L", "gender": "masculino"},
  {"name": "Silvia Jiménez", "age": 22, "career": "Diseño Gráfico", "gmail": "silvia.jimenez@example.com", "address": "Calle Nubes 113, Ciudad M", "gender": "femenino"},
  {"name": "Francisco Delgado", "age": 21, "career": "Medicina Veterinaria", "gmail": "francisco.delgado@example.com", "address": "Calle Campo 114, Ciudad N", "gender": "masculino"},
  {"name": "Beatriz Torres", "age": 23, "career": "Marketing", "gmail": "beatriz.torres@example.com", "address": "Calle Llama 115, Ciudad O", "gender": "femenino"},
  {"name": "Fernando Pérez", "age": 22, "career": "Matemáticas", "gmail": "fernando.perez@example.com", "address": "Calle Olivo 116, Ciudad P", "gender": "masculino"},
  {"name": "Teresa Castro", "age": 24, "career": "Filosofía", "gmail": "teresa.castro@example.com", "address": "Calle Árbol 117, Ciudad Q", "gender": "femenino"}
]


"""result_list=colection1.insert_many(list_students)
print("Los alumnos insertados con ID:", result_list.inserted_ids)
for id_insertado in result_list.inserted_ids:
    print("El alumno insertado con ID", id_insertado)"""


list_Teacher=[
{"name": "Carlos Mendoza", "age": 45, "career": "Ingeniería Electrónica", "gmail": "carlos.mendoza@universidad.com", "address": "Avenida Universidad 204, Ciudad A", "gender": "masculino", "profession": "Profesor de Ingeniería Electrónica"},
  {"name": "Luisa Sánchez", "age": 38, "career": "Filosofía", "gmail": "luisa.sanchez@universidad.com", "address": "Calle del Saber 101, Ciudad B", "gender": "femenino", "profession": "Profesora de Filosofía"},
  {"name": "Juan Rodríguez", "age": 50, "career": "Matemáticas", "gmail": "juan.rodriguez@universidad.com", "address": "Calle Matemáticas 220, Ciudad C", "gender": "masculino", "profession": "Profesor de Matemáticas"},
  {"name": "Ana Morales", "age": 40, "career": "Psicología", "gmail": "ana.morales@universidad.com", "address": "Calle Mente 312, Ciudad D", "gender": "femenino", "profession": "Profesora de Psicología"},
  {"name": "Roberto Pérez", "age": 42, "career": "Derecho", "gmail": "roberto.perez@universidad.com", "address": "Avenida Justicia 543, Ciudad E", "gender": "masculino", "profession": "Profesor de Derecho"},
  {"name": "Marta Fernández", "age": 35, "career": "Historia", "gmail": "marta.fernandez@universidad.com", "address": "Calle Historia 607, Ciudad F", "gender": "femenino", "profession": "Profesora de Historia"},
  {"name": "Ricardo Gómez", "age": 48, "career": "Ingeniería Civil", "gmail": "ricardo.gomez@universidad.com", "address": "Calle Construcción 812, Ciudad G", "gender": "masculino", "profession": "Profesor de Ingeniería Civil"},
  {"name": "Elena Díaz", "age": 37, "career": "Medicina", "gmail": "elena.diaz@universidad.com", "address": "Calle Salud 911, Ciudad H", "gender": "femenino", "profession": "Profesora de Medicina"},
  {"name": "José García", "age": 52, "career": "Arquitectura", "gmail": "jose.garcia@universidad.com", "address": "Avenida Planificación 1001, Ciudad I", "gender": "masculino", "profession": "Profesor de Arquitectura"},
  {"name": "Patricia Romero", "age": 39, "career": "Sociología", "gmail": "patricia.romero@universidad.com", "address": "Calle Sociedad 222, Ciudad J", "gender": "femenino", "profession": "Profesora de Sociología"}
]

"""result_list2=colection2.insert_many(list_Teacher)
print("Los profesores insertados con ID:", result_list2.inserted_ids)
for id_insertado2 in result_list2.inserted_ids:
    print("El profesor insertado con ID", id_insertado2)"""


#actualizar documento
colection1.update_one(
    {"name": "Juan Pérez"},
    {"$set": {"age": 22}}
)

colection1.update_one(
    {"name": "María González"},
    {"$set": {"age": 23}}
)

colection1.update_one(
    {"name": "Carlos Sánchez"},
    {"$set": {"age": 21}}
)

colection1.update_one(
    {"name": "Ana López"},
    {"$set": {"age": 24}}
)

colection1.update_one(
    {"name": "Luis Rodríguez"},
    {"$set": {"age": 25}}
)

#eliminar un documento
colection2.update_one(
    {"nombre": "Carlos Mendoza"},
    {"$unset": {"gmail": ""}}
)
colection2.update_one(
    {"nombre": "Luisa Sánchez"},
    {"$unset": {"gmail": ""}}
)
colection2.update_one(
    {"nombre": "Juan Rodríguez"},
    {"$unset": {"gmail": ""}}
)