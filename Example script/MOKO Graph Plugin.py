import MOKO
import time

MOKO.Report(f'MOKOGraph', 'info', 'table', 'Commands#150')

def AddLineCommand(ArrOy, ArrOx,LineWidth,Color,index):
    MOKO.Plugin('MOKO Graph', 'set', f"Add Line={ArrOy};{ArrOx};{LineWidth};{Color}")
    #MOKO.Report(f'AddLine_{index}', 'set', 'string', f'Add Line №{index}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Add Line №{index}')

def ChangeLineCommand(numLine, ArrOy, ArrOx,LineWidth,Color,index):
    MOKO.Plugin('MOKO Graph', 'set', f"Change Line={numLine};{ArrOy};{ArrOx};{LineWidth};{Color}")
    #MOKO.Report(f'ChangeLine_{index}', 'set', 'string', f'Change Line №{numLine}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Change Line №{numLine}')

def DeleteLineCommand(numLine, index):
    MOKO.Plugin('MOKO Graph', 'set', f"Delete Line={numLine}")
    #MOKO.Report(f'DeleteLine_{index}', 'set', 'string', f'Delete Line №{numLine}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Delete Line №{numLine}')

def HideLineCommand(numLine, index):
    MOKO.Plugin('MOKO Graph', 'set', f"Hide Line={numLine}")
    #MOKO.Report(f'DeleteLine_{index}', 'set', 'string', f'Delete Line №{numLine}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Hide Line №{numLine}')

def ShowLineCommand(numLine, index):
    MOKO.Plugin('MOKO Graph', 'set', f"Show Line={numLine}")
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Show Line №{numLine}')

def ShowLineOnlyCommand(numLine, index):
    MOKO.Plugin('MOKO Graph', 'set', f"Show Line=Only;{numLine}")
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Show Line Only №{numLine}')

def AddGraphSettCommand(Value_OyOx, Name_OyOx, index):
    MOKO.Plugin('MOKO Graph', 'set', f"Add Graph Settings={Value_OyOx};{Name_OyOx}")
    #MOKO.Report(f'AddGraphSettings_{index}', 'set', 'string', f'Add Graph Settings')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Add Graph Settings')

def AutoscaleCommand(mode, index):
    MOKO.Plugin('MOKO Graph', 'set', f"Autoscale={mode}")
    #MOKO.Report(f'Autoscale_{index}', 'set', 'string', f'Autoscale = {mode}')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Autoscale = {mode}')

def ScreenshotCommand(index):
    MOKO.Plugin('MOKO Graph', 'set', f"Screenshot")
    #MOKO.Report(f'Screenshot_{index}', 'set', 'string', f'Screenshot #{index} has done')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Screenshot #{index} has done')

def ClearGraphCommand(index):
    MOKO.Plugin('MOKO Graph', 'set', f"Clear Graph")
    #MOKO.Report(f'ClearGraph_{index}', 'set', 'string', f'Clear Graph command has done')
    MOKO.Report(f'MOKOGraph', 'set', 'table', f'Clear Graph command has done')

AutoscaleCommand("No", 1)

time.sleep(4)

#MOKO.EndScript()

ArrOx = [0,1,2,3,4]
ArrOy = [0,1,2,3,4]
LineWidth = 1
Color = 'Blue'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,1)

time.sleep(3)

ArrOx = [0,1,2,3,4]
ArrOy = [1,2,3,4,5]
LineWidth = 2
Color = 'Green'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,2)

time.sleep(4)

AutoscaleCommand("Only Oy", 2)

time.sleep(3)

ArrOx = [0,1,2,3,4]
ArrOy = [2,3,4,5,6]
LineWidth = 3
Color = 'Blue'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,3)

time.sleep(4)

AutoscaleCommand("Only Ox", 3)

time.sleep(4)

ArrOx = [0,1,2,3,5]
ArrOy = [3,4,5,6,8]
LineWidth = 4
Color = 'Green'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,4)

time.sleep(4)

ArrOx = [0,1,2,3,4]
ArrOy = [4,5,6,7,8]
LineWidth = 5
Color = 'Blue'
AddLineCommand(ArrOy, ArrOx,LineWidth,Color,5)

time.sleep(4)

AutoscaleCommand("No", 4)

time.sleep(4)

Value_OyOx = [-1,10,0,6]
Name_OyOx = ["Amplitude", "Frequency"]
AddGraphSettCommand(Value_OyOx, Name_OyOx, 1)

time.sleep(4)

numLine = 0
ArrOx = [0,1,2,3,4]
ArrOy = [-1,0,1,2,3]
LineWidth = 5
Color = 'Green'
ChangeLineCommand(numLine, ArrOy, ArrOx,LineWidth,Color,1)

time.sleep(4)

numLine = 1
DeleteLineCommand(numLine, 1)

time.sleep(4)

numLine = 1
ArrOx = [0,1,2,3,4]
ArrOy = [1,2,3,4,5]
LineWidth = 1
Color = 'Green'
ChangeLineCommand(numLine, ArrOy, ArrOx,LineWidth,Color,2)

time.sleep(4)

AutoscaleCommand("Yes", 5)

time.sleep(4)

ScreenshotCommand(1)
screen = MOKO.Plugin('MOKO Graph', 'get', 'InstantScreenshot', 'string')
MOKO.Report("Screenshot_1", 'set', 'picture', screen)

HideLineCommand(0, 1)
HideLineCommand(1, 2)
HideLineCommand(2, 3)
HideLineCommand(3, 4)

AutoscaleCommand("No", 6)

Value_OyOx = [0,7,0,16]
Name_OyOx = ["Amplitude", "Frequency"]
AddGraphSettCommand(Value_OyOx, Name_OyOx, 2)

### M ###
ArrOx = [2,3,3,4,4,5,5,6]
ArrOy = [4,6,6,5,5,6,6,4]
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

time.sleep(4)

ShowLineCommand('All', 3)

time.sleep(4)

numLine = [4,5,6,7]
ShowLineOnlyCommand(numLine, 2)

time.sleep(4)

ShowLineCommand('All', 3)

time.sleep(4)

numLine = 0
DeleteLineCommand(numLine, 2)
numLine = 0
DeleteLineCommand(numLine, 3)
numLine = 0
DeleteLineCommand(numLine, 4)
numLine = 0
DeleteLineCommand(numLine, 5)

time.sleep(4)

ClearGraphCommand(1)

MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()

#MOKO.Plugin('MOKO Graph', 'set', f"Autoscale=Yes") Autoscale on
#MOKO.Plugin('MOKO Graph', 'set', f"Autoscale=No")  Autoscale off
#MOKO.Plugin('MOKO Graph', 'set', f"Autoscale=Ox")  Autoscale Ox on, Oy без изменений
#MOKO.Plugin('MOKO Graph', 'set', f"Autoscale=Oy")  Autoscale Oy on, Ox без изменений