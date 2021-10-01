import MOKO
import time
import numpy as np
import math
import os

os.chdir("C://Users/sasha/OneDrive/Рабочий стол/Универ/4 курс/ППОВСРВ/lab_5")

#MOKO.Report('Graph', 'info', 'table', '№#50;x#70;y#70;№#50;x#70;y#70;№#50;x#70;y#70')
N = 256
Gar = 11

f = open('positions.txt', 'w')
for i in range(N):
#    f = open('positions.txt', 'w')
    a = bin(i) # a = 0b0
    a = a[2:len(a):1]
    zero = ""
    if len(a) < math.log(N, 2):
        j = 0
        while j < 8-len(a):
            zero = zero + "0"
            j = j + 1

 #   print(zero)
    a = zero + a
#    print("a = ", a)
#    break
    if i == 127:
        print(a)
    a = "			.word 		" + a[len(a)-1::-1] + "b"

    if i == 127:
        print(a)
    f.write(a + '\n')

f.close()


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
   # MOKO.Report('Graph', 'set', 'table', f'Change Line №{numLine}')
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
    #MOKO.Report('Graph', 'set', 'table', f'Hide Line №{numLine}')
    #time.sleep(4)

def ShowLineCommand(numLine):
    #Команд: "All" - показать все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для отображения
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line={numLine}")
    #MOKO.Report('Graph', 'set', 'table', f'Show Line №{numLine}')
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
    #MOKO.Report('Graph', 'set', 'table', f'Autoscale = {mode}')
    #time.sleep(4)

def ScreenshotCommand(index):
    #Сделать скриншот и сохранить в папку
    MOKO.Plugin('Graph', 'set', "Screenshot")
    #MOKO.Report(f'Screenshot_{index}', 'set', 'string', f'Screenshot #{index} has done')
    #MOKO.Report('Graph', 'set', 'table', f'Screenshot #{index} has done')
    #time.sleep(4)

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
    #MOKO.Report('Graph', 'set', 'table', 'Clear Graph command has done')
    #time.sleep(4)

def MaxValueCommand(numLine):
    numLine = numLine #delete this
    #Найти максимальное значение выбранной линии и установить курсор на это место
    #MOKO.Plugin('Graph', 'set', f"Max={numLine}")
    #MOKO.Report(f'Autoscale_{index}', 'set', 'string', f'Autoscale = {mode}')
    #MOKO.Report('Graph', 'set', 'table', f'Max = {numLine}')
    #time.sleep(1)

def SinusGenerator(x,Ampl,freq,phase):

    sine = Ampl * np.sin(2 * np.pi * freq * x + phase)
    sine = list(sine)
    return sine

def Filling_the_Table(ArrOx,ArrOy,ArrOx1,ArrOy1,ArrOx2,ArrOy2):
    i = 0
    number = 0
    while i < len(ArrOx):
        if i % 25 == 0 and i > 0:
            number = number + 1
        MOKO.Report(f'Graph_{number}', 'set', 'table', f'{i+1};{round(ArrOx[i],2)};{round(ArrOy[i],2)};'
                                              f'{i+1};{round(ArrOx1[i],2)};{round(ArrOy1[i],2)};'
                                              f'{i+1};{round(ArrOx2[i],2)};{round(ArrOy2[i],2)}')
        i = i + 1

MOKO.Plugin('Graph', 'init', '')

time.sleep(4)

ClearGraphCommand()

#High Mask
Value_OyOx = [-1,1,0,N-1]
Name_OyOx = ["Amplitude", "Time"]
Autoscale = "OnlyOy"
AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

#Region Status
#description: Frequency;Phase;Width;Color;Visible

#First Plot
name = "Plot 1"  #hesh Plot 1: 40;90;3;Lime;Yes
#MOKO.Report('Name1', 'set', 'string', f'{name}')
#MOKO.Report('Name4', 'set', 'string', f'{name}')
#MOKO.Report('Name7', 'set', 'string', f'{name}')
#MOKO.Report('Name10', 'set', 'string', f'{name}')
sampling_freq = N
start = 0
stop = N
x = np.arange(start,stop,stop/sampling_freq)
freq = 1/N
Ampl = 1
ArrOy = SinusGenerator(x,Ampl,freq,0)
sinus = SinusGenerator(x,Ampl,freq,0)
ArrOx = list(x)
LineWidth = 1
Color = "00FF00" #Lime
Visible = "Yes"
#AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,1)

WriteGraphCommand()

name = "Plot 2"  #hesh Plot 1: 40;90;3;Lime;Yes
#MOKO.Report('Name1', 'set', 'string', f'{name}')
#MOKO.Report('Name4', 'set', 'string', f'{name}')
#MOKO.Report('Name7', 'set', 'string', f'{name}')
#MOKO.Report('Name10', 'set', 'string', f'{name}')
sampling_freq = N
start = 0
stop = N
x = np.arange(start,stop,stop/sampling_freq)
freq = 1/N
Ampl = 1
ArrOy = SinusGenerator(x,Ampl,freq,90)
cosinus = SinusGenerator(x,Ampl,freq,90)
ArrOx = list(x)
LineWidth = 1
Color = "00FF00" #Lime
Visible = "Yes"
#AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,1)

WriteGraphCommand()

name = "Plot 2"  #hesh Plot 1: 40;90;3;Lime;Yes
#MOKO.Report('Name1', 'set', 'string', f'{name}')
#MOKO.Report('Name4', 'set', 'string', f'{name}')
#MOKO.Report('Name7', 'set', 'string', f'{name}')
#MOKO.Report('Name10', 'set', 'string', f'{name}')
sampling_freq = N
start = 0
stop = N
x = np.arange(start,stop,stop/sampling_freq)
freq = 1*Gar/N
Ampl = 1
ArrOy = SinusGenerator(x,Ampl,freq,0)
real = SinusGenerator(x,Ampl,freq,0)
ArrOx = list(x)
LineWidth = 1
Color = "00FF00" #Lime
Visible = "Yes"
#AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,1)

imag = list(range(N))

for i in range(N):
    imag[i] = 0
#    real[i] = 0

#real[0] = 1
IE = 1; N2 = round(N/2)
j1 = 0
#print(IE)

#print(len(sinus))
#real = sinus

while IE < N:
  #  break
    k = 0
    j = 0
    while j < N2:
        i = j
        while i < N:
#            print(N2,IE,j,i,i+N2,k,"\n")
            real1 = real[i]
            real2 = real[i+N2]
            imag1 = imag[i]
            real[i] = real[i]/2 + real[i+N2]/2
            imag[i] = imag[i]/2+imag[i+N2]/2
            real[i+N2] = (real1/2-real[i+N2]/2)*cosinus[k] + (imag1/2-imag[i+N2]/2)*sinus[k]
            imag[i+N2] = (imag1/2-imag[i+N2]/2)*cosinus[k] - (real1/2-real2/2)*sinus[k]
            i = i + 2*N2

        k = k + IE; j = j + 1
    if j1 == 0:
        break
    j1 = j1+1
    IE = 2*IE; N2 = round(N2/2)

#for i in range(round(N/2)):

#real1 = real[2]
#real2 = real[1]
#real3 = real[3]
#real4 = real[4];real5 = real[6];real6 = real[5];real7 = real[7]

#real[1] = real1
#real[2] = real2
#real[3] = real3
#real[4] = real4
#real[5] = real5
#real[6] = real6
#real[7] = real7

#print(real)



#    temp = real[i]
#    real[i] = real[i+round(N/2)-1]
#    real[i+round(N/2)-1] = temp
#    i = i + 2

#while j < N:#round(N/2):
#    temp = real[i+1]
#    real[i+1] = real[i+round(N/2)]
#    real.insert(i, real[j+round(N/2)])
    #print(len(real))
 #   j = j + 2
 #   i = i + 2


#real2 = real[1]
#real4 = real[2]
#real6 = real[3]
#real1 = real[4];real3 = real[5];real5 = real[6];real7 = real[7]

#real[1] = real1
#real[2] = real2
#real[3] = real3
#real[4] = real4
#real[5] = real5
#real[6] = real6
#real[7] = real7

name = "Plot 2"  #hesh Plot 1: 40;90;3;Lime;Yes
sampling_freq = N
start = 0
stop = N
x = np.arange(start,stop,stop/sampling_freq)
ArrOy = real
ArrOx = list(x)
LineWidth = 1
Color = "00FF00" #Lime
Visible = "Yes"
AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,1)

WriteGraphCommand()

MOKO.EndScript()


#0      0       0       0       0           #0          0       0       0
#8      4       2       2       2           #2          16      4       2
#4      8       6       4       4           #4          8       8       4
#12     12      10      8       6           #6          24      12      6
#2      2       4       6       8           #8          4       16      8
#10     6       8       10      10          #10         20      20      10
#6      10      12      12      12          #12         12      24      12
#14     14      14      14      14          #14         28      28
#                                                       2       2       16
#                                                       18      6       18
#                                                       10      10      20
#                                                       26      14
#                                                       6       18      24
#                                                       22      22
#                                                       14      26
#                                                       30      30      30

# 0000  #0000   #0
# 0001  #1000   #8
# 0010  #0100   #4
# 0011  #1100   #12

#    100  = 4
#    100 + 010 - 100 = 010


