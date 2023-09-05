# smena_bot
Установка пакетов в conda-окружение для всех юзеров из env.yml
```
micromamba env create -yq -f ./env.yml -p /opt/micromamba_envs/smena-bot-env
```

Активировать окружение
```
micromamba activate smena-bot-env
```

Скопировать env файл и обновить в нём токены
```
cp ./.env.example ./.env
```

Путь к интерпретатору
```
/opt/micromamba_envs/smena-bot-env
```