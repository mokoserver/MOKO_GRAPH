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

    a = zero + a
    a = "			.word 		" + a[len(a)-1::-1] + "b"
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
    time.sleep(4)

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

def SinusGenerator(x,Ampl,freq,phase):

    sine = Ampl * np.sin(2 * np.pi * freq * x + phase)
    sine = list(sine)
    return sine

def CosinusGenerator(x,Ampl,freq,phase):

    cos = Ampl * np.cos(2 * np.pi * freq * x + phase)
    cos = list(cos)
    return cos

MOKO.Plugin('Graph', 'init', '')

time.sleep(4)

ClearGraphCommand()

N = 256

Value_OyOx = [-400,400,0,N-1]
Name_OyOx = ["Amplitude", "Time"]
Autoscale = "Only Oy"
AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

sampling_freq = N
start = 0
stop = 1
x = np.arange(start,stop,stop/sampling_freq)
freq = 1
Ampl = 1
sinus = SinusGenerator(x,Ampl,freq,0)

x = np.arange(start,stop,stop/sampling_freq)
freq = 1
cosinus = CosinusGenerator(x,Ampl,freq,0)

x = np.arange(start,stop,stop/sampling_freq)
freq = 11
signal = SinusGenerator(x,Ampl,freq,0)
signal1 = SinusGenerator(x,Ampl,freq,0)

f = open('signalGar11_256.dat', 'w')
f.write("1651 1 c7 1 1" + '\n')
for i in range(N):
    a = str(round(signal1[i]*32767))
    f.write(a + '\n')
f.close()

f = open('sinus256_2.txt', 'w')
for i in range(N):
    a = "			.word " + str(round(sinus[i]*32767))
    f.write(a + '\n')
f.close()

f = open('cosinus256_2.txt', 'w')
for i in range(N):
    a = "			.word " + str(round(cosinus[i]*32767))
    f.write(a + '\n')
f.close()

ie = 1
N2 = round(N/2)
imag = list(range(N))
for i in range(N):
    imag[i] = 0

j_1 = 0
p = 0

while ie < N:
    j = 0
    k = 0
    while j < N2:
        i = j
        while i < N:
            real_PR = signal[i]/2 + signal[i+N2]/2
            imag_PR = imag[i]/2+imag[i+N2]/2
            real_QR = (signal[i]-signal[i+N2])/2*cosinus[k] + (imag[i]-imag[i+N2])/2*sinus[k]
            imag_QR = -(signal[i] - signal[i+N2])/2 * sinus[k] + (imag[i]-imag[i+N2])/2 * cosinus[k]

            signal[i] = real_PR
            signal[i+N2] = real_QR
            imag[i] = imag_PR
            imag[i+N2] = imag_QR

 #           if i == 159 and j_1 == 6:
 #               p = 1
 #               break

            i = i + 2*N2

#        if p == 1:
 #           break

        k = k + ie
        j = j + 1

    j_1 = j_1 + 1

#    if j_1 == 7 or p == 1:
#        break
    ie = 2 * ie
    N2 = round(N2/2)

#for i in range(N):
#    signal[i] = signal[i]*300000000000000

#First Plot
name = "Plot 1"  #hesh Plot 1: 40;90;3;Lime;Yes

ArrOx = list(x)
LineWidth = 2
Color = "00FF00" #Lime
Visible = "Yes"
AddLineCommand(name, signal, ArrOx,LineWidth,Color,Visible,1)

WriteGraphCommand()

MOKO.EndScript()