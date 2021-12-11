from pywebio.output import output, put_column, put_image, put_scrollable, put_text, toast, use_scope
from pywebio.input import file_upload, input_group, input
import uuid
import os


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


def validate(data):
    open(f'asset/{uuid.uuid1()}_{data["source_1"]["filename"]}', 'wb').write(data['source_1']['content'])
    open(f'asset/{uuid.uuid1()}_{data["source_2"]["filename"]}', 'wb').write(data['source_2']['content'])


# домашнаяя страница
def home_page():
    container = output()
    put_column(container).style(all_center_container_css)

    input_group("Загрузите файлы для мема",[
            file_upload("Сурс 1", name='source_1'),
            file_upload("Сурс 2", name='source_2'),
            input('Текст для сурса 1', name='text_1'),
            input('Текст для сурса 2', name='text_2')
        ], validate=validate)