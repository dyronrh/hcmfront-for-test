# hcmfront-for-test
hcmfront-for-test
Este proyecto de muestra donde se gestiona la creacion, edicion, eliminacion y listado de jornadas de trabajo.

Modelo de datos de la BD
Jornada tiene relacion muchos a muchos con Horarios
Jornada tiene relacion uno a muchos con Actividades

Los horarios y las actividades pueden ser gestionados(CRUD)

se crearon las api con Django RestFramework
Listar las jornadas
La seguridad de las apis es basada en Sesion y autenticacion basica
Request:
http://127.0.0.1:8000/jornada/lista/
Credenciales:
Authorization: Basic ZHlyb25yaDphZG1pbjEyMzQ=
COntent Type: application/json
usuario:dyronrh
clave:admin1234
Response:
[{"id":1,"tipo":"COM","descripcion":"yoel","tipo_empresa":"ME","region":"RAP","actividad_economica":1,"horario":[2,1]}]
para crear una Jornada
Peticion tipo POST:
Request API endpoint URL:
http://127.0.0.1:8000/jornada/add-api/
Header Credenciales:
Authorization: Basic ZHlyb25yaDphZG1pbjEyMzQ=
COntent Type: application/json
usuario:dyronrh
clave:admin1234
Parametros:
    {
        "tipo": "COM",
        "descripcion": "Explotación mixta de minerales",
        "tipo_empresa": "ME",
        "region": "RAP",
        "actividad_economica": 1,
        "horario": [
            2,
            1
        ]
    }

 Respuesta:
 {
    "id": 2,
    "tipo": "COM",
    "descripcion": "Explotación mixta de minerales",
    "tipo_empresa": "ME",
    "region": "RAP",
    "actividad_economica": 1,
    "horario": [
        1,
        2
    ]
}