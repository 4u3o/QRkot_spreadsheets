# Кошачий благотворительный фонд

---

*Учебный проект по FastAPI.  
Python 3.7.9, FastAPI 0.78.0*

1. [Описание](#description)
2. [Настройка](#settings)
   * [Пример переменных окружения](#env)
3. [Документация](#docs)
4. [Автор](#author)

## Описание <a id="description"></a>

> Благотворительного фонда поддержки котиков **QRKot**.  
> Фонд собирает пожертвования на различные целевые проекты. Пожертвования 
> в проекты поступают по принципу First In, First Out: все пожертвования 
> идут в проект, открытый раньше других; когда этот проект набирает необходимую 
> сумму и закрывается — пожертвования начинают поступать в следующий проект.  

## Настройка <a id="settings"></a>

- Клонируйте репозиторий
- Создайте виртуальное окружение
- Установите зависимости
- Добавьте переменные окружения
- Примените миграции:
    
        alembic upgrade head

- Запустите приложение:

        uvicorn app.main:app --reload

### Пример переменных окружения <a id="env"></a>

    DATABASE_URL=
    SECRET=SECRET
    TYPE=service_account
    PROJECT_ID=
    PRIVATE_KEY_ID=
    PRIVATE_KEY=""
    CLIENT_EMAIL=
    CLIENT_ID=
    AUTH_URI=
    TOKEN_URI=
    AUTH_PROVIDER_X509_CERT_URL=
    CLIENT_X509_CERT_URL=
    EMAIL=

## Документация <a id="docs"></a>

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Автор <a id="author"></a>

[Антон Горошко](https://github.com/4u3o) <a href='https://t.me/goroshko'><img width="21px" src="https://cdn.cdnlogo.com/logos/t/39/telegram.svg"></a>