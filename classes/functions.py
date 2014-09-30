import os
import sys
import subprocess


def gen_rc(path: str):
    """
    Генерирует ресурсы *.qrc и *.ui по заданному пути

    :param path:
    :type path:
    :return:
    :rtype:
    """
    for temp_file_name in os.listdir(path):
        input_file_path = os.path.join(path, temp_file_name)
        if os.path.isfile(input_file_path):
            file_name, file_ext = os.path.splitext(temp_file_name)
            if file_ext == '.qrc':
                file_name += '_rc.py'
                program = 'pyrcc5'
            elif file_ext == '.ui':
                file_name = 'ui_' + file_name + '.py'
                program = 'pyuic5'
            else:
                continue
        else:
            continue
        out_file_path = os.path.join(path, file_name)

        if not os.path.exists(out_file_path) or os.path.getmtime(input_file_path) > os.path.getmtime(out_file_path):
            subprocess.Popen([program, '-o', out_file_path, input_file_path])


def init(path_lib: str):
    """
    Инициализация

    :param path_lib:
    :type path_lib:
    :return:
    :rtype:
    """
    path_lib_window = os.path.join(path_lib, 'window')
    path_lib_widget = os.path.join(path_lib, 'widget')
    path_lib_class = os.path.join(path_lib, 'classes')
    sys.path.append(path_lib_window)
    sys.path.append(path_lib_widget)
    sys.path.append(path_lib_class)

    if __debug__:
        gen_rc(path_lib_widget)
        gen_rc(path_lib_window)
