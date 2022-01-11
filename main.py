from pywebio.platform import start_server
from pywebio.session import go_app
from home import home_page
import argparse


# главная страница сайта - редирект на страницу авторизации
def index():
    go_app('home_page', new_window=False)


# основные модули сайта
main_router = [
    index,
    home_page
]


# запуск сайта
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8081)
    args = parser.parse_args()
    start_server(main_router, port=args.port, debug=True)