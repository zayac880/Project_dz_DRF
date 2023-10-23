## Запуск проекта в Docker-контейнере 

Для запуска проекта в Docker-контейнере выполните следующие шаги:

1. Установите Docker на своей системе. Инструкции по установке можно найти на официальном сайте Docker: https://www.docker.com/get-started

2. Склонируйте данный репозиторий на свой локальный компьютер:

   ```bash
   git clone https://github.com/zayac880/project_dz_drf.git

3. Соберите Docker-образ, выполнив команду:

    ```bash
    docker build -t project_dz_drf .

4. Запустите Docker-контейнер, используя следующую команду:

    ```bash
    docker run -p 8000:8000 project_dz_drf

Ваш проект будет доступен по адресу http://localhost:8000/