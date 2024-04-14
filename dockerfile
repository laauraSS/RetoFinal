# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /Retofinal

# Copia los archivos de la aplicación al contenedor
COPY . /Retofinal

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# ENV DATABASE_URI=postgresql://postgres:mypassword@db:5432/mydatabase
# ENV FLASK_ENV=development

# Expone el puerto en el que se ejecutará la aplicación Flask
EXPOSE 5000

CMD ["sh", "-c", "sleep 10 && python manage.py && python run.py"]
