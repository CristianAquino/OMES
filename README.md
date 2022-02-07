# OMES
### Pasos para ejecutar el proyecto
- Ingresar a cmd y verificar que se cuenta con `virtualenv`
- En caso de no tenerlo, instalar con el comando `pip install venv`
- Crear un entorno virtual desde el cmd teniendo en cuenta la ruta del repositorio del proyecto
- En el `cmd` ejecutar: `python -m venv (ruta del repositorio)\ env `
- Abrir el IDE de preferencia y proceder a activar el entorno virtual creado `env`
### Pasos para activar el env
- Ubicarnos en el la rutal del repositorio y dirigirnos a la carpeta `env`
- Luego ejecutamos `Scripts\activate`
- Una vez iniciado `env`, procedemos a instalar `requirements.txt` mendiante `pip install -r requirements.txt`
- Luego en la ruta de nuestro repositorio dirigirnos a la carpeta donde se encuetra el proyecto y ejecutar `python (nombre del script).py`
- Para ejecutar el proyecto que se encuentra en la carpeta web_face_flask, tenemos que entrar a la carpeta mediante la consola y ejecutar `python app.py`

### Paginas referencia opencv
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html

### Paginas referencia streaming Flask
https://medium.datadriveninvestor.com/video-streaming-using-flask-and-opencv-c464bf8473d6

https://towardsdatascience.com/video-streaming-in-web-browsers-with-opencv-flask-93a38846fe00

https://blog.miguelgrinberg.com/post/video-streaming-with-flask/page/5