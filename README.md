Este proyecto implementa un backend en FastAPI y un frontend en Svelte, permitiendo visualizar gráficamente los datos del archivo data.json mediante eCharts.
La aplicación se ejecuta fácilmente mediante docker-compose.
Para lograr ejecutar el proyecto, una vez clonado, y teniendo instalado docker, y docker-compose se debe correr por terminal el siguiente comando:
docker-compose up --build
Una vez ejecutado, ingresando a https://localhost:8000 se logra visualizar la aplicacion
Para detener los contenedores: docker-compose down