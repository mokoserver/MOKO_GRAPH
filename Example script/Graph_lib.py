import MOKO


def write_graph():
    """ Отображение данных на графике. """
    MOKO.Plugin('Graph', 'set', 'Write Graph')
    return


def add_line(*args):
    """ Добавление линии.
        args[0]: name - имя линии;
        args[1]: ArrOy - координаты линии по оси оридант;
        args[2]: ArrOx - координаты линии по оси абсцисс;
        args[3]: LineWidth - толщина линии;
        args[4]: Color - цвет линии;
        args[5]: Visible - видимость линии;
    """
    MOKO.Plugin('Graph', 'set', f'Add Line={args[0]};{args[1]};{args[2]};{args[3]};{args[4]};{args[5]}')
    return


def change_line(*args):
    """ Изменение параметров добавленной линии.
        args[0]: numLine - номер линии;
        args[1]: name - имя линии;
        args[2]: ArrOy - координаты линии по оси оридант;
        args[3]: ArrOx - координаты линии по оси абсцисс;
        args[4]: LineWidth - толщина линии;
        args[5]: Color - цвет линии;
        args[6]: Visible - видимость линии.
    """
    MOKO.Plugin('Graph', 'set', f'Change Line={args[0]};{args[1]};{args[2]};{args[3]};{args[4]};{args[5]};{args[6]}')
    return


def delete_line(*args):
    """ Удаление линии.
        args[0]: numLine - номер линии или массив из номеров нескольких линий;
        args[0]: numLine='All' - удаление всех линий.
    """
    MOKO.Plugin('Graph', 'set', f'Delete Line={args[0]}')
    return


def hide_line(*args):
    """ Скрытие линии.
        args[0]: numLine - номер линии или массив из номеров нескольких линий;
        args[0]: numLine='All' - скрытие всех линий.
    """
    MOKO.Plugin('Graph', 'set', f'Hide Line={args[0]}')
    return


def show_line(*args):
    """ Сделать линию видимой.
        args[0]: numLine - номер линии или массив из номеров нескольких линий;
        args[0]: numLine='All' - сделать видимыми все линии;
        args[0]: numLine='Only;*номера линии или линий*' - сделать видимыми линии, номера которых переданы после Only,
                          а все остальные скрыть.
    """
    MOKO.Plugin('Graph', 'set', f'Show Line={args[0]}')
    return


def add_graph_sett(*args):
    """ Настройки графика: добавление подписей осей, min и max значения осей, Autoscale.
        args[0]: Value_OyOx - координаты min,max; первые 2 - min,max для оси оридант, 3я и 4я значения - min и max
                              соответсвенно для оси абсцисс.
        args[1]: Name_OyOx - подписи осей y и x соответственно.
        args[2]: Autoscale - значение Autoscale: "Yes", "No", "Only Ox", "Only Oy".
    """
    MOKO.Plugin('Graph', 'set', f'Add Graph Settings={args[0]};{args[1]};{args[2]}')
    return


def autoscale(*args):
    """ Задание Autoscale.
        args[0]: mode - значение Autoscale: "Yes", "No", "Only Ox", "Only Oy".
    """
    MOKO.Plugin('Graph', 'set', f"Autoscale={args[0]}")
    return


def screenshot(*args):
    """ Сделать скриншот, который сохраняется в /MOKO SE/Plugins/MOKO Graph/screenshots.
        args[0]: mode - тип команды: 'set', 'get'.
    """
    if args[0] == 'set':
        MOKO.Plugin('Graph', 'set', 'Screenshot')
    elif args[0] == 'get':
        screenshot = MOKO.Plugin('Graph', 'get', 'Screenshot', 'string')
        return screenshot
    return


def legend():
    """ Отображение/скрытие легенды. """
    MOKO.Plugin('Graph', 'set', 'Legend')
    return


def clear_graph():
    """ Очистить график. """
    MOKO.Plugin('Graph', 'set', 'Clear Graph')
    return
