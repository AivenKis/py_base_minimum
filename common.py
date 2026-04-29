                                                        Переводим проект `py_base_minimum` на HTTPS

Проблема: сейчас проекты используют два разных способа подключения:

- `qa-auto-course` — использует HTTPS (работает)
- `py_base_minimum` — использует SSH (проблемный, из-за `.ssh/config`)

Необходимо перевести `py_base_minimum` на HTTPS. Вот как это сделать правильно.


                                                                 Шаги            

1. Перейди в папку проекта:
cd D:\py_base_minimum

2. Посмотри текущие remote
git remote -v


3. Замени SSH-адрес на HTTPS
git remote set-url origin https://gitlab.com/aivenkis92/py_base_minimum.git


4. Проверь, что изменилось
git remote -v

Должно стать примерно так:

origin  https://gitlab.com/aivenkis92/py_base_minimum.git (fetch)
origin  https://gitlab.com/aivenkis92/py_base_minimum.git (push)


После изменения попробуй запушить:
git push -u origin master
