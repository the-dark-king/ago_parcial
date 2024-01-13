import json
import zipfile
import os
api_token = {"username":"angelgarciaobispo","key":"8754f3144a5560fcd4f7357afa2ba68e"}
# Ruta al archivo kaggle.json
kaggle_json_path = "C:/Users/usuario/.kaggle/kaggle.json"
# Crear la carpeta .kaggle si no existe
kaggle_folder = os.path.dirname(kaggle_json_path)
if not os.path.exists(kaggle_folder):
    os.makedirs(kaggle_folder)
# Escribir el token en el archivo kaggle.json
with open(kaggle_json_path, "w") as file:
    json.dump(api_token, file)
# Ruta a la carpeta del dataset
location = "D:/proyecto_parcial/dataset"
# Validar que la carpeta exista
if not os.path.exists(location):
    # Si no existe la carpeta dataset, entonces la creo
    os.mkdir(location)
else:
    # Si la carpeta sí existe, entonces elimino su contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))  # Elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root, name))  # Elimino todas las carpetas
# Descargar dataset de Kaggle
os.system("kaggle datasets download -d henryshan/starbucks -p D:/proyecto_parcial/dataset")

# Descomprimir el archivo de Kaggle
os.chdir(location)
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file, "r")  # Lee archivo .zip
    zip_ref.extractall()  # Extrae contenido de archivo .zip
    zip_ref.close()  # Cierra archivo
