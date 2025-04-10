# Обрезка ссылок с помощью Битли (через VK API)
Это консольное приложение помогает работать со ссылками через VK API. Оно умеет сокращать длинные ссылки и показывать статистику по уже сокращённым. Скрипт сам определяет тип ссылки и выбирает нужное действие: если ссылка длинная — сократит, если короткая — подсчитает переходы.

## Установка и настройка
Для начала вам понадобится токен VK, который можно получить через [Implicit Flow](https://dev.vk.com/ru/api/access-token/implicit-flow-community). При создании токена укажите в правах доступа `utils`. После авторизации вы получите ссылку, в которой будет параметр `access_token` — его и нужно использовать.

Создайте в корне проекта файл .env и добавьте в него полученный токен в следующем формате:
```ini
VK_IMPLICIT_FLOW_TOKEN=ваш_токен
```
Убедитесь, что у вас установлен Python 3. Затем установите зависимости с помощью pip. Если у вас установлен Python 3 как python3, используйте pip3:
```bash
pip install -r requirements.txt
```
## Как пользоваться 
Запустите скрипт из командной строки, передав ему ссылку. Пример использования:
```bash
python main.py https://example.com
```
Если переданная ссылка является обычной длинной ссылкой, скрипт сократит её с помощью VK API и выведет короткую версию. Если вы передаёте уже сокращённую ссылку (например, `https://vk.cc/abc123`), приложение получит статистику переходов по ней и выведет общее количество кликов.

## Цель проекта
Этот проект написан в образовательных целях на курсе для веб-разработчиков от [dvmn.org](https://dvmn.org/). Он поможет разобраться в работе с VK API, а также попрактиковаться в работе с HTTP-запросами.

