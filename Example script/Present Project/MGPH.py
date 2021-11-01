import MOKO

MOKO.Report('Graph', 'info', 'table', 'Commands#150')

def WriteGraphCommand(text):
    #Отобразить данные на графике
    MOKO.Plugin('Graph', 'set', "Write Graph")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def AddLineCommand(name: object, ArrOy: object, ArrOx: object, LineWidth: object, Color: object, Visible: object, text: object) -> object:
    #Добавление линии
    MOKO.Plugin('Graph', 'set', f"Add Line={name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    MOKO.Report('Graph', 'set', 'table', f'{text}')
    MOKO.Plugin('Graph', 'set', "Write Graph")

def ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth,Color,Visible,text):
    #Изменить параметры уже добавленной линии
    MOKO.Plugin('Graph', 'set', f"Change Line={numLine};{name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def DeleteLineCommand(numLine, text):
    #Команда "All" - удаление всех линий
    #Можно указывать как одну линию, так и массив с номерами линий для удаления
    MOKO.Plugin('Graph', 'set', f"Delete Line={numLine}")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def HideLineCommand(numLine, text):
    #Команд: "All" - скрыть все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для скрытия
    MOKO.Plugin('Graph', 'set', f"Hide Line={numLine}")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def ShowLineCommand(numLine, text):
    #Команд: "All" - показать все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами\именами линий для отображения
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line={numLine}")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def ShowLineOnlyCommand(numLine, text):
    #Опция "Only" - показать только те линии, номера или имена которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line=Only;{numLine}")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale, text):
    #Добавление подписей осей + min/max значения осей
    #Задание Autoscale: "Yes", "No", "Only Ox", "Only Oy"
    MOKO.Plugin('Graph', 'set', f"Add Graph Settings={Value_OyOx};{Name_OyOx};{Autoscale}")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def AutoscaleCommand(mode, text):
    #Команды: "No" - отключить Autoscale осей
    #         "Yes" - включить Autoscale осей
    #         "Only Ox" - включить Autoscale только для оси Ox
    #         "Only Oy" - включить Autoscale только для оси Оy
    MOKO.Plugin('Graph', 'set', f"Autoscale={mode}")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def ScreenshotCommand(index, text):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('Graph', 'set', "Screenshot")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def LegendCommand(text):
    #Показать легенду или скрыть
    MOKO.Plugin('Graph', 'set', "Legend")
    MOKO.Report('Graph', 'set', 'table', f'{text}')

def ClearGraphCommand(text):
    #Очистить график
    MOKO.Plugin('Graph', 'set', "Clear Graph")
    MOKO.Report('Graph', 'set', 'table', f'{text}')