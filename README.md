# Examen
# CRUD de Usuarios + Ataque de Fuerza Bruta (Educativo)

## Descripción

Este proyecto implementa una API REST con FastAPI para gestión de usuarios (CRUD) y un experimento controlado de fuerza bruta contra el endpoint de login.

## Tecnologías

* Python
* FastAPI
* SQLModel

## Ejecutar la API

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Abrir:
http://127.0.0.1:8000/docs

## Usuario de prueba

```json
{
  "username": "admin",
  "password": "abc"
}
```

## Ejecutar ataque de fuerza bruta

```bash
python bf.py
```

## Ejemplo de salida

```
Contraseña encontrada: abc
Intentos: 731
Tiempo: 0.15 segundos
```

## Análisis

El tiempo crece exponencialmente al aumentar:

* Longitud de la contraseña
* Tamaño del alfabeto

Ejemplo:

* 3 letras → rápido
* 6 letras → millones de intentos
* 8+ caracteres con símbolos → prácticamente inviable

## Vulnerabilidades detectadas

* No hay límite de intentos
* Contraseñas en texto plano
* No hay bloqueo de usuario

## Medidas de mitigación
* Hash de contraseñas
* Bloqueo tras múltiples intentos
* Uso de autenticación multifactor

