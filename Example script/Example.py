import MOKO
import time

MOKO.Report('Graph', 'info', 'table', 'Commands#150')

def AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,index):
    #Добавление линии, цвет можно передавать, как "Blue" or "Green", или как массив RGB:0,255,0;
    MOKO.Plugin('Graph', 'set', f"Add Line={name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    #MOKO.Report(f'AddLine_{index}', 'set', 'string', f'Add Line №{index}')
    MOKO.Report('Graph', 'set', 'table', f'Add Line №{index}')
    time.sleep(4)

def ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth,Color,Visible):
    #Изменить параметры уже добавленной линии
    MOKO.Plugin('Graph', 'set', f"Change Line={numLine};{name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    #MOKO.Report(f'ChangeLine_{index}', 'set', 'string', f'Change Line №{numLine}')
    MOKO.Report('Graph', 'set', 'table', f'Change Line №{numLine}')
    time.sleep(4)

def DeleteLineCommand(numLine):
    #Команда "All" - удаление всех линий
    #Можно указывать как одну линию, так и массив с номерами линий для удаления
    MOKO.Plugin('Graph', 'set', f"Delete Line={numLine}")
    #MOKO.Report(f'DeleteLine_{index}', 'set', 'string', f'Delete Line №{numLine}')
    MOKO.Report('Graph', 'set', 'table', f'Delete Line №{numLine}')
    time.sleep(4)

def HideLineCommand(numLine):
    #Команд: "All" - скрыть все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для скрытия
    MOKO.Plugin('Graph', 'set', f"Hide Line={numLine}")
    #MOKO.Report(f'DeleteLine_{index}', 'set', 'string', f'Delete Line №{numLine}')
    MOKO.Report('Graph', 'set', 'table', f'Hide Line №{numLine}')
    time.sleep(4)

def ShowLineCommand(numLine):
    #Команд: "All" - показать все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для отображения
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line={numLine}")
    MOKO.Report('Graph', 'set', 'table', f'Show Line №{numLine}')
    time.sleep(4)

def ShowLineOnlyCommand(numLine):
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line=Only;{numLine}")
    MOKO.Report('Graph', 'set', 'table', f'Show Line Only №{numLine}')
    time.sleep(4)

def AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale):
    Autoscale = "No"
    #Добавление подписей осей + min&max значения осей
    #Задание Autoscale: "Yes", "No", "Only Ox", "Only Oy"
    MOKO.Plugin('Graph', 'set', f"Add Graph Settings={Value_OyOx};{Name_OyOx};{Autoscale}")
    #MOKO.Report(f'AddGraphSettings_{index}', 'set', 'string', f'Add Graph Settings')
    MOKO.Report('Graph', 'set', 'table', 'Add Graph Settings')
    time.sleep(4)

def AutoscaleCommand(mode):
    #Команды: "No" - отключить Autoscale осей
    #         "Yes" - включить Autoscale осей
    #         "Only Ox" - включить Autoscale только для оси Ox
    #         "Only Oy" - включить Autoscale только для оси Оy
    MOKO.Plugin('Graph', 'set', f"Autoscale={mode}")
    #MOKO.Report(f'Autoscale_{index}', 'set', 'string', f'Autoscale = {mode}')
    MOKO.Report('Graph', 'set', 'table', f'Autoscale = {mode}')
    time.sleep(4)

def ScreenshotCommand(index):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('Graph', 'set', "Screenshot")
    #MOKO.Report(f'Screenshot_{index}', 'set', 'string', f'Screenshot #{index} has done')
    MOKO.Report('Graph', 'set', 'table', f'Screenshot #{index} has done')
    time.sleep(4)

def LegendCommand(index):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('Graph', 'set', "Legend")
    #MOKO.Report(f'Legend_{index}', 'set', 'string', f'LegendCommand has done')
    #MOKO.Report('Graph', 'set', 'table', f'LegendCommand has done')
    #time.sleep(4)

def ClearGraphCommand():
    #Очистить график
    MOKO.Plugin('Graph', 'set', "Clear Graph")
    #MOKO.Report(f'ClearGraph_{index}', 'set', 'string', f'Clear Graph command has done')
    MOKO.Report('Graph', 'set', 'table', 'Clear Graph command has done')
    time.sleep(4)

def MaxValueCommand(numLine):
    numLine = numLine #delete this
    #Найти максимальное значение выбранной линии и установить курсор на это место
    #MOKO.Plugin('Graph', 'set', f"Max={numLine}")
    #MOKO.Report(f'Autoscale_{index}', 'set', 'string', f'Autoscale = {mode}')
    #MOKO.Report('Graph', 'set', 'table', f'Max = {numLine}')
    #time.sleep(1)

MOKO.Plugin('Graph', 'init', '')

time.sleep(4)

#Value_OyOx = [0,5,0,8]
#Name_OyOx = ["Amplitude", "Frequency"]
#AddGraphSettCommand(Value_OyOx, Name_OyOx)

name = 'Plot 1'
ArrOx = [0,1,2,3,4]
ArrOy = [0,1,2,3,4]
LineWidth = 1
Color = '00FFFF' #Blue
Visible = 'Yes'
AddLineCommand(name,ArrOy, ArrOx,LineWidth,Color,Visible,1)

name = 'Plot 1'
ArrOx = [0,1,2,3,4]
ArrOy = [1,2,3,4,5]
LineWidth = 2
Color = '00FF00' #Green
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,2)

name = 'Plot 2'
ArrOx = [0,1,2,3,4]
ArrOy = [2,3,4,5,6]
LineWidth = 3
Color = '00FF00' #Green
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,2)

HideLineCommand("All")

numLine = [0]
LineWidth = 5

ShowLineCommand("All")

numLine = [0,2]

#ShowLineCommand(numLine)

ShowLineOnlyCommand(numLine)

#DeleteLineCommand("All")

#MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()