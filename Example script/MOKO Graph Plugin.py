import MOKO
import time

MOKO.Report('Graph', 'info', 'table', 'Commands#150')

def WriteGraphCommand():
    #Отобразить данные на графике
    MOKO.Plugin('Graph', 'set', "Write Graph")
    #MOKO.Report(f'ClearGraph_{index}', 'set', 'string', f'Write Graph command has done')
    MOKO.Report('Graph', 'set', 'table', 'Write Graph command has done')
    #time.sleep(4)

def AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,index):
    #Добавление линии
    MOKO.Plugin('Graph', 'set', f"Add Line={name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    #MOKO.Report(f'AddLine_{index}', 'set', 'string', f'Add Line №{index}')
    MOKO.Report('Graph', 'set', 'table', f'Add Line №{index}')
    WriteGraphCommand()
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

def LegendCommand():
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
    #time.sleep(4)

MOKO.Plugin('Graph', 'init', '')

time.sleep(4)

AutoscaleCommand("No")

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

LegendCommand()

name = 'Plot 2'
ArrOx = [0,1,2,3,4]
ArrOy = [1,2,3,4,5]
LineWidth = 2
Color = '00FF00' #Green
Visible = 'No'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,2)

AutoscaleCommand("Only Oy")

name = 'Plot 3'
ArrOx = [0,1,2,3,4]
ArrOy = [2,3,4,5,6]
LineWidth = 3
Color = "FF0000" #Red
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,3)

LegendCommand()

AutoscaleCommand("Only Ox")

name = 'Plot 4'
ArrOx = [0,1,2,3,5]
ArrOy = [3,4,5,6,8]
LineWidth = 4
Color = "FFFF00" #Yellow
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,4)

name = 'Plot 5'
ArrOx = [0,1,2,3,4]
ArrOy = [4,5,6,7,8]
LineWidth = 5
Color = "FF00FF" #Magenta
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,5)

LegendCommand()

Value_OyOx = [-1,10,0,6]
Name_OyOx = ["Amplitude", "Frequency"]
Autoscale = "No"
AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

name = 'Plot 1'
numLine = 0
ArrOx = [0,1,2,3,4]
ArrOy = [-1,0,1,2,3]
LineWidth = 5
Color = '00FF00' #Green
Visible = 'Yes'
ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth,Color, Visible)

#numLine = 1
#DeleteLineCommand(numLine)

name = 'Plot 7'
numLine = 1
ArrOx = [0,1,2,3,4]
ArrOy = [1,2,3,4,5]
LineWidth = 1
Color = '00FF00' #Green
Visible = 'Yes'
ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth,Color,Visible)

AutoscaleCommand("Yes")

ScreenshotCommand(1)
screen = MOKO.Plugin('Graph', 'get', 'InstantScreenshot', 'string')
MOKO.Report("Screenshot_1", 'set', 'picture', screen)

numLine = [0,1,2,3]
HideLineCommand(numLine)

Value_OyOx = [0,7,0,16]
Name_OyOx = ["Amplitude", "Frequency"]
Autoscale = "No"
AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

### M ###
name = 'Plot 12'
ArrOx = [2,3,4,5,6]
ArrOy = [4,6,5,6,4]
LineWidth = 3
Color = '00FFFF'  #Blue
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,6)

### O ###

name = 'Plot 8'
ArrOx = [7,7,9,9,7]
ArrOy = [4,6,6,4,4]
LineWidth = 3
Color = '00FF00' #Green
Visible = 'No'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,7)

### K ###

name = 'Plot 9'
ArrOx = [10,10,10,11,10,11]
ArrOy = [4,6,5,6,5,4]
LineWidth = 3
Color = '00FFFF' #Blue
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,8)

### O ###

name = 'Plot 10'
ArrOx = [12,12,14,14,12]
ArrOy = [4,6,6,4,4]
LineWidth = 3
Color = '00FF00' #Green
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,9)

ShowLineCommand('All')

numLine = [4,5,6,7]
ShowLineOnlyCommand(numLine)

numLine = [0,1,2]
ShowLineCommand(numLine)

ShowLineCommand('All')

HideLineCommand('All')

ShowLineCommand('All')

numLine = [0,1,2,3]
DeleteLineCommand(numLine)

DeleteLineCommand('All')

AutoscaleCommand("Yes")

name = 'Plot 11'
ArrOx = [0.1,1.2,2.3,3.4,4.5]
ArrOy = [0.1,1.2,2.3,3.4,4.5]
LineWidth = 1
Color = '00FFFF' #Blue
Visible = 'Yes'
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,1)

ClearGraphCommand()

MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()