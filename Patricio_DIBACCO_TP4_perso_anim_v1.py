import random
import maya.cmds as cmds

cmds.file(f=True, new=True)
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
    def generate(self, nombre, headVal, bodyVal, leftArmVal, rightArmVal, leftLegVal, rightLegVal):
    #model body:
        bodyName = 'body' + randomNaming
        bodyJ1 = 'bodyJ1' + randomNaming
        bodyJ2 = 'bodyJ2' + randomNaming
        bodyJ3 = 'bodyJ3' + randomNaming
        cmds.polyCube(name=bodyName, w = bodyVal, h = bodyVal*3, d= bodyVal)
        #cmds.move(8, y=True)
        cmds.polySmooth( bodyName+'.f[0:5]', dv=bodyVal )
        cmds.select( d=True )
        cmds.joint(n=bodyJ1, p=(0, 9, 0) )
        cmds.joint(n=bodyJ2, p=(0, 8, 0) )
        cmds.joint(n=bodyJ3, p=(0, 7, 0) )
        cmds.ikHandle( sj=bodyJ1, ee=bodyJ3)
        cmds.bindSkin( bodyName, bodyJ1)
    #model leftArm:
        leftArm = 'leftArm' + randomNaming
        leftArmJ = 'leftArmJ' + randomNaming
        leftElbowJ = 'leftElbowJ'+randomNaming
        leftWristJ = 'leftWristJ'+randomNaming
        cmds.polyCube(name=leftArm, w = leftArmVal*2, h = leftArmVal*0.25, d = leftArmVal)
        cmds.scale(0.3, z = True)
        cmds.move(3,0,0)
        cmds.xform(r= True, ro=(0, 0, -45) )
        cmds.polySmooth( leftArm+'.f[0:5]', dv=leftArmVal )
        cmds.select( d=True )
        cmds.joint(n=leftArmJ, p=(0.5, 9, 0) )
        cmds.joint(n=leftElbowJ, p=(1, 8.5, 0) )
        cmds.joint(n=leftWristJ, p=(1.5, 8, 0) )
        cmds.ikHandle( sj=leftArmJ, ee=leftWristJ)
        cmds.bindSkin( leftArm, leftArmJ)
    #model rightArm:
        rightArm = 'rightArm' + randomNaming
        rightArmJ = 'rightArmJ'+ randomNaming
        rightElbowJ = 'rightElbowJ'+randomNaming
        rightWristJ = 'rightWristJ'+randomNaming
        cmds.polyCube(name=rightArm, w =rightArmVal*2, h = rightArmVal*0.25, d = rightArmVal)
        cmds.scale(0.3, z = True)
        cmds.move(-3,0,0)
        cmds.xform(r= True, ro=(0, 0, 45) )
        cmds.polySmooth( rightArm + '.f[0:5]', dv=rightArmVal )
        cmds.select( d=True )
        cmds.joint(n=rightArmJ, p=(-0.5, 9, 0) )
        cmds.joint(n=rightElbowJ, p=(-1, 8.5, 0) )
        cmds.joint(n=rightWristJ, p=(-1.5, 8, 0) )
        cmds.ikHandle( sj=rightArmJ, ee=rightWristJ)
        cmds.bindSkin( rightArm, rightArmJ)
    #model leftLeg:
        leftLeg = 'leftLeg' + randomNaming
        leftLegJ = 'leftLegJ' + randomNaming
        leftLegKneeJ = 'leftLegKneeJ'+randomNaming
        leftLegCalvesJ = 'leftLegCalvesJ' +randomNaming
        cmds.polyCube(name=leftLeg, w =leftLegVal*0.3, h = leftLegVal*3.5, d = leftLegVal)
        cmds.scale(0.3, z = True)
        cmds.move(-0.3,6,0)
        cmds.polySmooth( leftLeg + '.f[0:5]', dv=leftLegVal )
        cmds.select( d=True )
        cmds.joint(n=leftLegJ, p=(-0.3, 7, 0) )
        cmds.joint(n=leftLegKneeJ, p=(-0.3, 6, 0) )
        cmds.joint(n=leftLegCalvesJ, p=(-0.3, 5, 0) )
        cmds.ikHandle( sj=leftLegJ, ee=leftLegCalvesJ)
        cmds.bindSkin( leftLeg, leftLegJ)
    #model rightLeg:
        rightLeg = 'rightLeg' + randomNaming
        rightLegJ = 'rightLegJ'+ randomNaming
        rightLegKneeJ = 'rightLegKneeJ'+randomNaming
        rightLegCalvesJ = 'rightLegCalvesJ'+randomNaming
        cmds.polyCube(name=rightLeg, w = rightLegVal*0.3, h = rightLegVal*3.5, d = rightLegVal)
        cmds.scale(0.3, z = True)
        cmds.move(0.3,6,0)
        cmds.polySmooth( rightLeg +'.f[0:5]', dv=rightLegVal )
        cmds.select( d=True )
        cmds.joint(n=rightLegJ, p=(0.3, 7, 0) )
        cmds.joint(n=rightLegKneeJ, p=(0.3, 6, 0) )
        cmds.joint(n=rightLegCalvesJ, p=(0.3, 5, 0) )
        cmds.ikHandle( sj=rightLegJ, ee=rightLegCalvesJ)
        cmds.bindSkin( rightLeg, rightLegJ)
    #group everything:
        cmds.group(bodyName, leftArm, rightArm, leftLeg, rightLeg, n=nombre)
        

winName = 'PersoRIG'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 400 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='PersoRIG', h=200,  bgc=(backgroundColor), tlb=True)

mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth, winWidth]
cmds.rowLayout(numberOfColumns=1, cw=mainRLWidth)
#values for sliders:
headSlider = cmds.floatSliderGrp( label='Head', field=True, minValue=1, maxValue=3, fieldMinValue=1, fieldMaxValue=2, value=1)
#cmds.floatSlider(min= 0.1, max= 3, step = 0.1)
cmds.setParent('..')
bodySlider = cmds.floatSliderGrp( label='Body', field=True, minValue=1, maxValue=3, fieldMinValue=1, fieldMaxValue=3, value=1 )
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, cw2=mainRLWidth)
leftArmSlider = cmds.floatSliderGrp( label='Left Arm', field=True, minValue=1, maxValue=2, fieldMinValue=1, fieldMaxValue=2, value=1 )
rightArmSlider = cmds.floatSliderGrp( label='Right Arm', field=True, minValue=1, maxValue=2, fieldMinValue=1, fieldMaxValue=2, value=1 )
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, columnWidth2=mainRLWidth)
leftLegSlider = cmds.floatSliderGrp( label='Left Leg', field=True, minValue=1, maxValue=4, fieldMinValue=1, fieldMaxValue=4, value=1 )
rightLegSlider = cmds.floatSliderGrp( label='Right Leg', field=True, minValue=1, maxValue=4, fieldMinValue=1, fieldMaxValue=4, value=1 )
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, cw2=mainRLWidth)
cmds.textFieldGrp('newNames', label = 'Perso Name: ', width=mainRLWidth[0])
cmds.button(label='Generate', width=mainRLWidth[1]*0.60, height=40, c='rename()')
cmds.setParent('..')
cmds.rowLayout(numberOfColumns=2, cw=[(1,100),(2,300)])
cmds.text(label='')
cmds.button(label='Reset', width=mainRLWidth[1]*0.60, height=40, c='reset()', align= 'center')
def rename(*args):
    #query values:
    text_A = cmds.textFieldGrp( 'newNames', query = True, text = True)
    toto = Perso()
    toto.nameGenerator()
    toto.generate(text_A)

cmds.showWindow()
cmds.window(winName, e=True, width=winWidth, height=200)
