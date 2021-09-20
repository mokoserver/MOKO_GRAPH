import MOKO
import time
import numpy as np
import scipy as sc
import random

#MOKO.Report('Graph', 'info', 'table', '№#50;x#70;y#70')

def WriteGraphCommand():
    #Вывести данные на графике
    MOKO.Plugin('Graph', 'set', "Write Graph")
    #MOKO.Report(f'ClearGraph_{index}', 'set', 'string', f'Write Graph command has done')
    #MOKO.Report('Graph', 'set', 'table', 'Write Graph command has done')
    #time.sleep(4)

def AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,index):
    #Добавление линии, цвет можно передавать, как "Blue" or "Green", или как массив RGB:0,255,0;
    MOKO.Plugin('Graph', 'set', f"Add Line={name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    #MOKO.Report(f'AddLine_{index}', 'set', 'string', f'Add Line №{index}')
    #MOKO.Report('Graph', 'set', 'table', f'Add Line №{index}')
    #time.sleep(4)

def ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth,Color,Visible):
    #Изменить параметры уже добавленной линии
    MOKO.Plugin('Graph', 'set', f"Change Line={numLine};{name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    #MOKO.Report(f'ChangeLine_{index}', 'set', 'string', f'Change Line №{numLine}')
    MOKO.Report('Graph', 'set', 'table', f'Change Line №{numLine}')
    #time.sleep(4)

def DeleteLineCommand(numLine):
    #Команда "All" - удаление всех линий
    #Можно указывать как одну линию, так и массив с номерами линий для удаления
    MOKO.Plugin('Graph', 'set', f"Delete Line={numLine}")
    #MOKO.Report(f'DeleteLine_{index}', 'set', 'string', f'Delete Line №{numLine}')
    #MOKO.Report('Graph', 'set', 'table', f'Delete Line №{numLine}')
    #time.sleep(4)

def HideLineCommand(numLine):
    #Команд: "All" - скрыть все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для скрытия
    MOKO.Plugin('Graph', 'set', f"Hide Line={numLine}")
    #MOKO.Report(f'DeleteLine_{index}', 'set', 'string', f'Delete Line №{numLine}')
    MOKO.Report('Graph', 'set', 'table', f'Hide Line №{numLine}')
    #time.sleep(4)

def ShowLineCommand(numLine):
    #Команд: "All" - показать все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для отображения
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line={numLine}")
    MOKO.Report('Graph', 'set', 'table', f'Show Line №{numLine}')
    #time.sleep(4)

def ShowLineOnlyCommand(numLine):
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line=Only;{numLine}")
    #MOKO.Report('Graph', 'set', 'table', f'Show Line Only №{numLine}')
    #time.sleep(4)

def AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale):
    #Добавление подписей осей + min&max значения осей
    #Задание Autoscale: "Yes", "No", "Only Ox", "Only Oy"
    MOKO.Plugin('Graph', 'set', f"Add Graph Settings={Value_OyOx};{Name_OyOx};{Autoscale}")
    #MOKO.Report(f'AddGraphSettings_{index}', 'set', 'string', f'Add Graph Settings')
    #MOKO.Report('Graph', 'set', 'table', 'Add Graph Settings')
    #time.sleep(4)

def AutoscaleCommand(mode):
    #Команды: "No" - отключить Autoscale осей
    #         "Yes" - включить Autoscale осей
    #         "Only Ox" - включить Autoscale только для оси Ox
    #         "Only Oy" - включить Autoscale только для оси Оy
    MOKO.Plugin('Graph', 'set', f"Autoscale={mode}")
    #MOKO.Report(f'Autoscale_{index}', 'set', 'string', f'Autoscale = {mode}')
    #MOKO.Report('Graph', 'set', 'table', f'Autoscale = {mode}')
    #time.sleep(4)

def ScreenshotCommand(index):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('Graph', 'set', "Screenshot")
    #MOKO.Report(f'Screenshot_{index}', 'set', 'string', f'Screenshot #{index} has done')
    #MOKO.Report('Graph', 'set', 'table', f'Screenshot #{index} has done')
    #time.sleep(4)

def ClearGraphCommand():
    #Очистить график
    MOKO.Plugin('Graph', 'set', "Clear Graph")
    #MOKO.Report(f'ClearGraph_{index}', 'set', 'string', f'Clear Graph command has done')
    #MOKO.Report('Graph', 'set', 'table', 'Clear Graph command has done')
    #time.sleep(4)

def MaxValueCommand(numLine):
    numLine = numLine #delete this
    #Найти максимальное значение выбранной линии и установить курсор на это место
    #MOKO.Plugin('Graph', 'set', f"Max={numLine}")
    #MOKO.Report(f'Autoscale_{index}', 'set', 'string', f'Autoscale = {mode}')
    #MOKO.Report('Graph', 'set', 'table', f'Max = {numLine}')
    #time.sleep(1)

def LegendCommand(index):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('Graph', 'set', "Legend")
    #MOKO.Report(f'Legend_{index}', 'set', 'string', f'LegendCommand has done')
    #MOKO.Report('Graph', 'set', 'table', f'LegendCommand has done')
    #time.sleep(4)

def SinusGenerator(x,Ampl,freq,phase):

    sine = Ampl * np.sin(2 * np.pi * freq * x + phase)
    sine = list(sine)
    return sine

def Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1):
    i = 0
    number = 8
    while i < 100:
        if i % 25 == 0 and i > 0:
            number = number + 1

        MOKO.Report(f'Graph_{number}', 'set', 'table', f'{i + 1};{round(ArrOx[i], 2)};{round(ArrOy[i], 2)};'
                                                       f'{i + 1};{round(ArrOx1[i], 2)};{round(ArrOy1[i], 2)}')
        i = i + 1


#MOKO.Plugin('Graph', 'init', '')

#time.sleep(4)
ClearGraphCommand()

#DeleteLineCommand("All", 1)

Value_OyOx = [-1.1,1.1,-0.01,1]
Name_OyOx = ["Amplitude", "Time"]
Autoscale = "No"
AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

#Region Status
#description: Frequency;Phase;Width;Color;Visible

#First Plot
name = "Plot 7" #hesh Plot7: 4;0;2;Magenta;Yes
sampling_freq = 1000
MOKO.Report('Name25', 'set', 'string', f'{name}')
MOKO.Report('Name27', 'set', 'string', f'{name}')
MOKO.Report('Name29', 'set', 'string', f'{name}')
MOKO.Report('Name31', 'set', 'string', f'{name}')
start = 0
stop = 0.5
x = np.arange(start,stop,stop/sampling_freq)
freq = 4
Ampl = 1
ArrOy = SinusGenerator(x,Ampl,freq,0)
ArrOx = list(x)

LineWidth = 2
Color = "FF00FF" #Magenta
Visible = "Yes"
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,1)

WriteGraphCommand()

MOKO.Program('tree', 'set', 'select = ' + 'Plot7')
MOKO.Program('tree', 'set', 'chosen = passed')

name = "Plot 8"     #hesh Plot8:  30;0;2;DarkTurquoise;Yes
MOKO.Report('Name26', 'set', 'string', f'{name}')
MOKO.Report('Name28', 'set', 'string', f'{name}')
MOKO.Report('Name30', 'set', 'string', f'{name}')
MOKO.Report('Name32', 'set', 'string', f'{name}')
start = 0
stop = 0.5
x = np.arange(start,stop,stop/sampling_freq)
freq = 30
Ampl = 1
ArrOy1 = SinusGenerator(x,Ampl,freq,0)
start = 0.5
stop = 1.0
x = np.arange(start,stop,stop/sampling_freq)
ArrOx1 = list(x)

LineWidth = 2
Color = "00CED1" #DarkTurquoise
Visible = "Yes"
AddLineCommand(name, ArrOy1, ArrOx1,LineWidth,Color,Visible,1)

WriteGraphCommand()

MOKO.Program('tree', 'set', 'select = ' + 'Plot8')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Status

Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1)

screen = MOKO.Plugin('Graph', 'get', 'Screenshot', 'string')
MOKO.Report("Screenshot_3", 'set', 'picture', screen)

MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()