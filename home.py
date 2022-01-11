import os
from threading import Thread
from pywebio.output import output, put_column, put_image, put_link, put_markdown, put_row, put_scrollable, put_table, put_text, style, toast, use_scope
from pywebio.input import file_upload, input_group, input


# ссылки на лабы
def lab_works():
    style(put_row([
            put_table([
            ["          Список лабораторных работ           "],
            [put_link("ЛР 1", app="lab_one")]
        ])
    ]), "align-items: center; width: 100vh; display: flex; flex-direction: column")


# домашнаяя страница
def home_page():
    put_markdown("# Камиль Мамбетов БПО-18-01: лабораторные работы")
    put_markdown("Надо будет придумать описание")
    put_markdown("---")

    lab_works()