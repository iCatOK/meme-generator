import os
from pywebio.output import output, put_column, put_image, put_scrollable, put_text, toast, use_scope
from pywebio.input import file_upload, input_group, input
import uuid
import time


# стиль главного контейнера
all_center_container_css = """
    position: absolute;
    top: 40%;
    transform: translateY(-60%);
    align-items: center;
    align-self: center;
    display: flex;
    flex-direction: column;
    width: 100vh;
"""

container = output()


def update_file_list():
    global container
    container = [put_text(i) for i in os.listdir("asset")]
    put_column(container)


def validate(data):
    start_time = time.time()
    open(f'asset/{uuid.uuid1()}_{data["source_1"]["filename"]}', 'wb').write(data['source_1']['content'])
    open(f'asset/{uuid.uuid1()}_{data["source_2"]["filename"]}', 'wb').write(data['source_2']['content'])
    toast(f"Успешно: время - {time.time() - start_time} сек.")
    update_file_list()


# домашнаяя страница
def home_page():
    input_group("Загрузите файлы для мема",[
            file_upload("Сурс 1", name='source_1'),
            file_upload("Сурс 2", name='source_2'),
            input('Текст для сурса 1', name='text_1'),
            input('Текст для сурса 2', name='text_2')
        ], validate=validate)

    update_file_list()