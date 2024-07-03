# Noticias LUPI

Moverse entre carpetas con cd Nombredecarpeta para ir a la carpeta

Para volver se usa cd..

Asegurarse de que el entorno tenga los permisos adecuados usando set-executionpolicy remotesigned 
Crear entorno virtual de python con ./activate

Para poder acceder a las dependencias en el entorno virtual se debe usar el comando

pip install -r requirements.txt



Todo cambio al archivo models.py tiene que ser seguido por los comandos :

python manage.py makemigrations
python manage.py migrate


Levantar servidor con los comando python manage.py runserver

los sitios web son http://127.0.0.1:8000/SitioWebNoticiasCaos y http://127.0.0.1:8000/admin/
