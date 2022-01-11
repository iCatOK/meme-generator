import os
from threading import Thread
from pywebio.output import output, put_column, put_image, put_scrollable, put_text, toast, use_scope
from pywebio.input import file_upload, input_group, input


# домашнаяя страница
def home_page():
    put_text('hello world')