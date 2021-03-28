import random
import maya.cmds as cmds

#cmds.file(f=True, new=True)
# Une classe de personnages
class Perso():
    #random name generator:
    def nameGenerator(self):
        listAbc = ['a','b', 'c', 'd', 'e', 'f', 'g','h', 'i']
        listedAbc = random.sample(listAbc,8)
        listNumbers = list(range(8))
        listedNC = random.shuffle(listNumbers)
        global randomNaming
        randomNaming =  random.choice(listedAbc) + str(random.choice(listNumbers))
        print(randomNaming)
    def generate(self, nombre):
    #model head:
        headName = 'head' + randomNaming
        cmds.polyCube(name=headName)
        cmds.move(10, y=True)
        cmds.polySmooth( headName + '.f[0:5]', dv=1 )
    #model body:
        bodyName = 'body' + randomNaming
        cmds.polyCube(name=bodyName, w = 1, h = 3)
        cmds.move(8, y=True)
        cmds.polySmooth( bodyName+'.f[0:5]', dv=1 )
    #model leftArm:
        leftArm = 'leftArm' + randomNaming
        cmds.polyCube(name=leftArm, w = 2, h = 0.25)
        cmds.scale(0.3, z = True)
        cmds.move(1.3,9,0)
        cmds.polySmooth( leftArm+'.f[0:5]', dv=1 )
    #model rightArm:
        rightArm = 'rightArm' + randomNaming
        cmds.polyCube(name=rightArm, w = 2, h = 0.25)
        cmds.scale(0.3, z = True)
        cmds.move(-1.3,9,0)
        cmds.polySmooth( rightArm + '.f[0:5]', dv=1 )
    #model leftLeg:
        leftLeg = 'leftLeg' + randomNaming
        cmds.polyCube(name=leftLeg, w = 0.3, h = 3.5)
        cmds.scale(0.3, z = True)
        cmds.move(-0.3,6,0)
        cmds.polySmooth( leftLeg + '.f[0:5]', dv=1 )
    #model rightLeg:
        rightLeg = 'rightLeg' + randomNaming
        cmds.polyCube(name=rightLeg, w = 0.3, h = 3.5)
        cmds.scale(0.3, z = True)
        cmds.move(0.3,6,0)
        cmds.polySmooth( rightLeg +'.f[0:5]', dv=1 )
    #group everything:
        cmds.group(headName, bodyName, leftArm, rightArm, leftLeg, rightLeg, n=nombre)
        
#toto=Perso('pepe')
winName = 'Perso'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 400 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='Perso', h=200,  bgc=(backgroundColor), tlb=True)
#reference to the main columnLayout
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth, winWidth]
cmds.columnLayout(width=mainRLWidth[0])
cmds.textFieldGrp('newNames', label = 'Perso Name: ')
cmds.button(label='Generate', width=mainRLWidth[1]*0.60, height=40, c='rename()')
def rename(*args):
    global text_A
    text_A = cmds.textFieldGrp( 'newNames', query = True, text = True)
    toto = Perso()
    toto.nameGenerator()
    toto.generate(text_A)
cmds.showWindow()
cmds.window(winName, e=True, width=winWidth, height=200)