import MOKO
import time

MOKO.Report(f'MOKOGraph', 'info', 'table', 'Commands#150')

def AddLineCommand(ArrOy, ArrOx,LineWidth,Color,index):
    #Добавление линии, цвет можно передавать, как "Blue" or "Green", или как массив RGB:0,255,0;
    MOKO.Plugin('MOKO Graph', 'set', f"Add Line={ArrOy};{ArrOx};{LineWidth};{Color}")
    #MOKO.Report(f'AddLine_{index}', 'set', 'string', f'Add Line №{index}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Add Line №{index}')
    time.sleep(4)

def ChangeLineCommand(numLine, ArrOy, ArrOx,LineWidth,Color,index):
    #Изменить параметры уже добавленной линии
    MOKO.Plugin('MOKO Graph', 'set', f"Change Line={numLine};{ArrOy};{ArrOx};{LineWidth};{Color}")
    #MOKO.Report(f'ChangeLine_{index}', 'set', 'string', f'Change Line №{numLine}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Change Line №{numLine}')
    time.sleep(4)

def DeleteLineCommand(numLine, index):
    #Команда "All" - удаление всех линий
    #Можно указывать как одну линию, так и массив с номерами линий для удаления
    MOKO.Plugin('MOKO Graph', 'set', f"Delete Line={numLine}")
    #MOKO.Report(f'DeleteLine_{index}', 'set', 'string', f'Delete Line №{numLine}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Delete Line №{numLine}')
    time.sleep(4)

def HideLineCommand(numLine, index):
    #Команд: "All" - скрыть все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для скрытия
    MOKO.Plugin('MOKO Graph', 'set', f"Hide Line={numLine}")
    #MOKO.Report(f'DeleteLine_{index}', 'set', 'string', f'Delete Line №{numLine}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Hide Line №{numLine}')
    time.sleep(4)

def ShowLineCommand(numLine, index):
    #Команд: "All" - показать все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для отображения
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('MOKO Graph', 'set', f"Show Line={numLine}")
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Show Line №{numLine}')
    time.sleep(4)

def ShowLineOnlyCommand(numLine, index):
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('MOKO Graph', 'set', f"Show Line=Only;{numLine}")
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Show Line Only №{numLine}')
    time.sleep(4)

def AddGraphSettCommand(Value_OyOx, Name_OyOx, index):
    #Добавление подписей осей + min&max значения осей
    MOKO.Plugin('MOKO Graph', 'set', f"Add Graph Settings={Value_OyOx};{Name_OyOx}")
    #MOKO.Report(f'AddGraphSettings_{index}', 'set', 'string', f'Add Graph Settings')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Add Graph Settings')
    time.sleep(4)

def AutoscaleCommand(mode, index):
    #Команды: "No" - отключить Autoscale осей
    #         "Yes" - включить Autoscale осей
    #         "Only Ox" - включить Autoscale только для оси Ox
    #         "Only Oy" - включить Autoscale только для оси Оy
    MOKO.Plugin('MOKO Graph', 'set', f"Autoscale={mode}")
    #MOKO.Report(f'Autoscale_{index}', 'set', 'string', f'Autoscale = {mode}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Autoscale = {mode}')
    time.sleep(4)

def ScreenshotCommand(index):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('MOKO Graph', 'set', f"Screenshot")
    #MOKO.Report(f'Screenshot_{index}', 'set', 'string', f'Screenshot #{index} has done')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Screenshot #{index} has done')
    time.sleep(4)

def ClearGraphCommand(index):
    #Очистить график
    MOKO.Plugin('MOKO Graph', 'set', f"Clear Graph")
    #MOKO.Report(f'ClearGraph_{index}', 'set', 'string', f'Clear Graph command has done')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Clear Graph command has done')
    time.sleep(4)

AutoscaleCommand("No", 1)

ArrOx = [0,1,2,3,4]
ArrOy = [0,1,2,3,4]
LineWidth = 1
Color = 'Blue'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,1)

ArrOx = [0,1,2,3,4]
ArrOy = [1,2,3,4,5]
LineWidth = 2
Color = 'Green'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,2)

AutoscaleCommand("Only Oy", 2)

ArrOx = [0,1,2,3,4]
ArrOy = [2,3,4,5,6]
LineWidth = 3
Color = [255,0,0] #Red
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,3)

AutoscaleCommand("Only Ox", 3)

ArrOx = [0,1,2,3,5]
ArrOy = [3,4,5,6,8]
LineWidth = 4
Color = [255,255,0] #Yellow
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,4)

ArrOx = [0,1,2,3,4]
ArrOy = [4,5,6,7,8]
LineWidth = 5
Color = [255,0,255] #Magenta
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,5)

AutoscaleCommand("No", 4)

Value_OyOx = [-1,10,0,6]
Name_OyOx = ["Amplitude", "Frequency"]
AddGraphSettCommand(Value_OyOx, Name_OyOx, 1)

numLine = 0
ArrOx = [0,1,2,3,4]
ArrOy = [-1,0,1,2,3]
LineWidth = 5
Color = 'Green'
ChangeLineCommand(numLine, ArrOy, ArrOx,LineWidth,Color,1)

numLine = 1
DeleteLineCommand(numLine, 1)

numLine = 1
ArrOx = [0,1,2,3,4]
ArrOy = [1,2,3,4,5]
LineWidth = 1
Color = 'Green'
ChangeLineCommand(numLine, ArrOy, ArrOx,LineWidth,Color,2)

AutoscaleCommand("Yes", 5)

ScreenshotCommand(1)
screen = MOKO.Plugin('MOKO Graph', 'get', 'InstantScreenshot', 'string')
MOKO.Report("Screenshot_1", 'set', 'picture', screen)

numLine = [0,1,2,3]
HideLineCommand(numLine, 1)

AutoscaleCommand("No", 6)

Value_OyOx = [0,7,0,16]
Name_OyOx = ["Amplitude", "Frequency"]
AddGraphSettCommand(Value_OyOx, Name_OyOx, 2)

### M ###
ArrOx = [2,3,4,5,6]
ArrOy = [4,6,5,6,4]
LineWidth = 3
Color = 'Blue'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,6)

### O ###

ArrOx = [7,7,9,9,7]
ArrOy = [4,6,6,4,4]
LineWidth = 3
Color = 'Green'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,7)

### K ###

ArrOx = [10,10,10,11,10,11]
ArrOy = [4,6,5,6,5,4]
LineWidth = 3
Color = 'Blue'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,8)

### O ###

ArrOx = [12,12,14,14,12]
ArrOy = [4,6,6,4,4]
LineWidth = 3
Color = 'Green'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,9)

ShowLineCommand('All', 3)

numLine = [4,5,6,7]
ShowLineOnlyCommand(numLine, 2)

numLine = [0,1,2]
ShowLineCommand(numLine, 3)

ShowLineCommand('All', 4)

HideLineCommand('All', 3)

ShowLineCommand('All', 4)

numLine = [0,1,2,3]
DeleteLineCommand(numLine, 2)

DeleteLineCommand('All', 3)

AutoscaleCommand("Yes", 7)

ArrOx = [0.1,1.2,2.3,3.4,4.5]
ArrOy = [0.1,1.2,2.3,3.4,4.5]
LineWidth = 1
Color = 'Blue'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,1)

ClearGraphCommand(1)

MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()