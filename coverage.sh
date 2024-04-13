#!/bin/bash

FLASK_ENV=development DATABASE_URI=postgresql://postgres:mypassword@localhost:5432

# Ejecutar pruebas con cobertura
coverage run -m pytest

# Generar informe de cobertura en la consola
coverage report -m

# Generar informe HTML
coverage html
