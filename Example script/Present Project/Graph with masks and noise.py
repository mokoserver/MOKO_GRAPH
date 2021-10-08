import MOKO
import time
import random

MOKO.Report('Graph', 'info', 'table', 'Commands#150')

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
    MOKO.Report('Graph', 'set', 'table', f'Delete Line №{numLine}')
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
    MOKO.Report('Graph', 'set', 'table', f'Show Line Only №{numLine}')
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
    MOKO.Report('Graph', 'set', 'table', f'Autoscale = {mode}')
    #time.sleep(4)

def ScreenshotCommand(index):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('Graph', 'set', "Screenshot")
    #MOKO.Report(f'Screenshot_{index}', 'set', 'string', f'Screenshot #{index} has done')
    MOKO.Report('Graph', 'set', 'table', f'Screenshot #{index} has done')
    #time.sleep(4)

def ClearGraphCommand():
    #Очистить график
    MOKO.Plugin('Graph', 'set', "Clear Graph")
    #MOKO.Report(f'ClearGraph_{index}', 'set', 'string', f'Clear Graph command has done')
    #MOKO.Report('Graph', 'set', 'table', 'Clear Graph command has done')
    #time.sleep(4)

def LegendCommand(index):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('Graph', 'set', "Legend")
    #MOKO.Report(f'Legend_{index}', 'set', 'string', f'LegendCommand has done')
    #MOKO.Report('Graph', 'set', 'table', f'LegendCommand has done')
    #time.sleep(4)

def MaxValueCommand(numLine):
    numLine = numLine #delete this
    #Найти максимальное значение выбранной линии и установить курсор на это место
    #MOKO.Plugin('Graph', 'set', f"Max={numLine}")
    #MOKO.Report(f'Autoscale_{index}', 'set', 'string', f'Autoscale = {mode}')
    #MOKO.Report('Graph', 'set', 'table', f'Max = {numLine}')
    #time.sleep(1)

def Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2):
    i = 0
    number = 4
    plot_with_masks_n_noise = ''
    while i < len(ArrOx1)/10 and i < 101:
        if i % 25 == 0 and i > 0:
            MOKO.Report(f'Graph_{number}', 'set', 'table', plot_with_masks_n_noise)
            plot_with_masks_n_noise = ''
            number = number + 1

        if i > len(ArrOx) - 1:
            plot_with_masks_n_noise = plot_with_masks_n_noise + f'{i+1};'';'';' \
                                      + f'{i+1};{round(ArrOx1[i],2)};{round(ArrOy1[i],2)};' \
                                      + f'{i+1};'';'';' \
                                      + '\\r'
        else:
            plot_with_masks_n_noise = plot_with_masks_n_noise + f'{i + 1};{round(ArrOx[i], 2)};{round(ArrOy[i], 2)};' \
                                  + f'{i + 1};{round(ArrOx1[i*10], 2)};{round(ArrOy1[i*10], 2)};' \
                                  + f'{i + 1};{round(ArrOx2[i], 2)};{round(ArrOy2[i], 2)};' \
                                  + '\\r'
        i = i + 1
#    while i < len(ArrOx1)/10 and i < 100:
#        if i % 25 == 0 and i > 0:
#            number = number + 1
#        if i > len(ArrOx) - 1:
#            MOKO.Report(f'Graph_{number}', 'set', 'table', f'{i+1};'';'';'
#                                              f'{i+1};{round(ArrOx1[i],2)};{round(ArrOy1[i],2)};'
#                                              f'{i+1};'';'';')
#        else:
#            MOKO.Report(f'Graph_{number}', 'set', 'table', f'{i + 1};{round(ArrOx[i], 2)};{round(ArrOy[i], 2)};'
#                                                           f'{i + 1};{round(ArrOx1[i*10], 2)};{round(ArrOy1[i*10], 2)};'
#                                                           f'{i + 1};{round(ArrOx2[i], 2)};{round(ArrOy2[i], 2)}')
#        i = i + 1


#MOKO.Plugin('Graph', 'init', '')

#time.sleep(4)

ClearGraphCommand()

#High Mask

Value_OyOx = [-160,-50,2.375,2.445]
Name_OyOx = ["Power Spectral Density (dBm/Hz)", "Frequency"]
Autoscale = "No"
AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

#Region Status
#description: Width;Color;Visible

name = 'Plot 4' #hesh Plot4:    2;Blue;Yes
MOKO.Report('Name13;Name16;Name19;Name22', 'set', 'strings', f'{name};{name};{name};{name}')
#MOKO.Report('Name16', 'set', 'string', f'{name}')
#MOKO.Report('Name19', 'set', 'string', f'{name}')
#MOKO.Report('Name22', 'set', 'string', f'{name}')
ArrOx = [2.379,2.383,2.4,2.402,2.422,2.424,2.441,2.445]
valueOy = -92
ArrOy = [valueOy,valueOy,valueOy+20,valueOy+40,valueOy+40,valueOy+20,valueOy,valueOy]
LineWidth = 2
Color = '00FFFF' #Blue
Visible = 'Yes'
AddLineCommand(name,ArrOy, ArrOx,LineWidth,Color,Visible,1)

WriteGraphCommand()

MOKO.Program('tree', 'set', 'select = ' + 'Plot4')
MOKO.Program('tree', 'set', 'chosen = passed')

#Main Graffic

noise = []
array = []
i = 0
while i < 200:
    noise.append(random.uniform(-136,-118))
    array.append(2.379+(2.39-2.379)/200*i)
    i = i + 1

i = 0
startY = -128
stopY = -108
startX = 2.39
stopX = 2.393
cnt = 75
while i < cnt:
    noise.append(random.uniform(startY,stopY))
    array.append(startX+(stopX-startX)/cnt*i)
    i = i + 1
    if i == cnt and startY == -128:
        i = 0
        startY = -120
        stopY = -102
        startX = 2.393
        stopX = 2.397
    elif i == cnt and startY == -120:
        i = 0
        startY = -112
        stopY = -94
        startX = 2.397
        stopX = 2.401
    elif i == cnt and startY == -112:
        cnt = 25
        i = 0
        startY = -99
        stopY = -86
        startX = 2.401
        stopX = 2.4028

#qweqweq
i = 0
while i < 400:
    noise.append(random.uniform(-80,-56))
    array.append(2.403+(2.422-2.403)/400*i)
    i = i + 1

#afafafaf
i = 0
while i < 10:
    noise.append(random.uniform(-78,-70))
    array.append(2.422+(2.4225-2.422)/10*i)
    i = i + 1

i = 0
while i < 10:
    noise.append(random.uniform(-86,-76))
    array.append(2.4225+(2.423-2.4225)/10*i)
    i = i + 1

i = 0
while i < 10:
    noise.append(random.uniform(-92,-84))
    array.append(2.423+(2.4235-2.423)/10*i)
    i = i + 1

i = 0
while i < 10:
    noise.append(random.uniform(-98,-90))
    array.append(2.4235+(2.424-2.4235)/10*i)
    i = i + 1

i = 0
while i < 10:
    noise.append(random.uniform(-104,-96))
    array.append(2.424+(2.4245-2.424)/10*i)
    i = i + 1

i = 0
while i < 20:
    noise.append(random.uniform(-104,-96))
    array.append(2.4245+(2.4248-2.4245)/20*i)
    i = i + 1

i = 0
while i < 100:
    noise.append(random.uniform(-112,-96))
    array.append(2.4248+(2.43-2.4248)/100*i)
    i = i + 1

i = 0
while i < 100:
    noise.append(random.uniform(-116,-99))
    array.append(2.43+(2.434-2.43)/100*i)
    i = i + 1

i = 0
while i < 200:
    noise.append(random.uniform(-123,-106)) #106
    array.append(2.433+(2.445-2.433)/200*i)
    i = i + 1

name = 'Plot 5' #hesh Plot5: 1;Red;Yes
MOKO.Report('Name14;Name17;Name20;Name23', 'set', 'strings', f'{name};{name};{name};{name}')
#MOKO.Report('Name14', 'set', 'string', f'{name}')
#MOKO.Report('Name17', 'set', 'string', f'{name}')
#MOKO.Report('Name20', 'set', 'string', f'{name}')
#MOKO.Report('Name23', 'set', 'string', f'{name}')
ArrOx1 = array
ArrOy1 = noise
LineWidth = 1
Color = 'FF0000' #Red
Visible = 'Yes'
AddLineCommand(name,ArrOy1, ArrOx1,LineWidth,Color,Visible,2)

WriteGraphCommand()

MOKO.Program('tree', 'set', 'select = ' + 'Plot5')
MOKO.Program('tree', 'set', 'chosen = passed')

#Low Mask

name = 'Plot 6' #hesh Plot6:  2;Lime;Yes
MOKO.Report('Name15;Name18;Name21;Name24', 'set', 'strings', f'{name};{name};{name};{name}')
#MOKO.Report('Name15', 'set', 'string', f'{name}')
#MOKO.Report('Name18', 'set', 'string', f'{name}')
#MOKO.Report('Name21', 'set', 'string', f'{name}')
#MOKO.Report('Name24', 'set', 'string', f'{name}')
ArrOx2 = [2.379,2.383,2.4,2.402,2.422,2.424,2.441,2.445]
valueOy= -150
ArrOy2 = [valueOy,valueOy,valueOy+20,valueOy+40,valueOy+40,valueOy+20,valueOy,valueOy]
LineWidth = 2
Color = '00FF00' #Lime
Visible = 'Yes'
AddLineCommand(name,ArrOy2, ArrOx2,LineWidth,Color,Visible,1)

WriteGraphCommand()

MOKO.Program('tree', 'set', 'select = ' + 'Plot6')
MOKO.Program('tree', 'set', 'chosen = passed')
#EndRegion Status

Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2)

screen = MOKO.Plugin('Graph', 'get', 'Screenshot', 'string')
MOKO.Report("Screenshot_2", 'set', 'picture', screen)

#MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()