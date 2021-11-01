import MOKO
import MGPH
import time

MOKO.Plugin('Graph', 'init', '')

time.sleep(4)

MGPH.AutoscaleCommand("No", 1)

name = 'Plot 1'
ArrOx = [0,1,2,3,4]
ArrOy = [0,1,2,3,4]
LineWidth = 1
Color = '00FFFF' #Blue
Visible = 'Yes'
MGPH.AddLineCommand(name,ArrOy, ArrOx,LineWidth,Color,Visible,1)

name = 'Plot 1'
ArrOx = [0,1,2,3,4]
ArrOy = [1,2,3,4,5]
LineWidth = 2
Color = '00FF00' #Green
Visible = 'Yes'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,2)

MGPH.LegendCommand(1)

MGPH.AutoscaleCommand("Only Oy",1)

name = 'Plot 3'
ArrOx = [0,1,2,3,4]
ArrOy = [2,3,4,5,6]
LineWidth = 3
Color = "FF0000" #Red
Visible = 'Yes'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,3)

MGPH.LegendCommand(1)

MGPH.AutoscaleCommand("Only Ox",1)

name = 'Plot 4'
ArrOx = [0,1,2,3,5]
ArrOy = [3,4,5,6,8]
LineWidth = 4
Color = "FFFF00" #Yellow
Visible = 'Yes'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,4)

name = 'Plot 5'
ArrOx = [0,1,2,3,4]
ArrOy = [4,5,6,7,8]
LineWidth = 5
Color = "FF00FF" #Magenta
Visible = 'Yes'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,5)

MGPH.LegendCommand(1)

Value_OyOx = [-1,10,0,6]
Name_OyOx = ["Amplitude", "Frequency"]
Autoscale = "No"
MGPH.AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale,1)

name = 'Plot 1'
numLine = 0
ArrOx = [0,1,2,3,4]
ArrOy = [-1,0,1,2,3]
LineWidth = 5
Color = '00FF00' #Green
Visible = 'Yes'
MGPH.ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth,Color, Visible,1)

#numLine = 1
#DeleteLineCommand(numLine)

name = 'Plot 7'
numLine = 1
ArrOx = [0,1,2,3,4]
ArrOy = [6,2,3,4,5]
LineWidth = 1
Color = '00FF00' #Green
Visible = 'Yes'
MGPH.ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth,Color,Visible,2)

MGPH.AutoscaleCommand("Yes",1)

MGPH.ScreenshotCommand(1,1)
screen = MOKO.Plugin('Graph', 'get', 'Screenshot', 'string')
MOKO.Report("Screenshot_1", 'set', 'picture', screen)

numLine = [0,1,2,3]
MGPH.HideLineCommand(numLine,1)

Value_OyOx = [0,7,0,16]
Name_OyOx = ["Amplitude", "Frequency"]
Autoscale = "No"
MGPH.AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale,1)

### M ###
name = 'Plot 12'
ArrOx = [2,3,4,5,6]
ArrOy = [4,6,5,6,4]
LineWidth = 3
Color = '00FFFF'  #Blue
Visible = 'Yes'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,6)

### O ###

name = 'Plot 8'
ArrOx = [7,7,9,9,7]
ArrOy = [4,6,6,4,4]
LineWidth = 3
Color = '00FF00' #Green
Visible = 'No'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,7)

### K ###

name = 'Plot 9'
ArrOx = [10,10,10,11,10,11]
ArrOy = [4,6,5,6,5,4]
LineWidth = 3
Color = '00FFFF' #Blue
Visible = 'Yes'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,8)

### O ###

name = 'Plot 10'
ArrOx = [12,12,14,14,12]
ArrOy = [4,6,6,4,4]
LineWidth = 3
Color = '00FF00' #Green
Visible = 'Yes'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,9)

MGPH.ShowLineCommand('All',1)

numLine = [4,5,6,7]
MGPH.ShowLineOnlyCommand(numLine,1)

numLine = [0,1,2]
MGPH.ShowLineCommand(numLine,1)

MGPH.ShowLineCommand('All',1)

MGPH.HideLineCommand('All',1)

MGPH.ShowLineCommand('All',1)

numLine = [0,1,2,3]
MGPH.DeleteLineCommand(numLine,1)

MGPH.DeleteLineCommand('All',1)

MGPH.AutoscaleCommand("Yes",1)

name = 'Plot 11'
ArrOx = [0.1,1.2,2.3,3.4,4.5]
ArrOy = [0.1,1.2,2.3,3.4,4.5]
LineWidth = 1
Color = '00FFFF' #Blue
Visible = 'Yes'
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible,1)

MGPH.ClearGraphCommand(1)

MOKO.Program('control', 'set', 'save word report')

MOKO.EndScript()