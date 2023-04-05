First Step: download in your system.

```
    git clone https://github.com/siddharth018/botman-chatbot.git

```

```
    cd botman-chatbot
```

```

    composer install

```


```

    cp .env.example .env

```


Put your credentils .env file.

```.env

    DB_CONNECTION=mysql
    DB_HOST=127.0.0.1
    DB_PORT=3306
    DB_DATABASE=botman
    DB_USERNAME=root
    DB_PASSWORD=root@123

```

Step second: Run server
```
    php artisan serve

```
Check from this url
```
    http://127.0.0.1:8000
```
