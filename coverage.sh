#!/bin/bash

# Ejecutar pruebas con cobertura
coverage run -m pytest

# Generar informe de cobertura en la consola
coverage report -m

# Generar informe HTML
coverage html
