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
    def generate(self, nombre):
    #model body:
        bodyName = 'body' + randomNaming
        seatName = 'seat' + randomNaming
        steeringWheelName = 'steeringwheelname'+randomNaming
        bodyJ1 = 'bodyJ1' + randomNaming
        bodyJ2 = 'bodyJ2' + randomNaming
        bodyJ3 = 'bodyJ3' + randomNaming
        cmds.polyCube(name=bodyName, w = 4, h = 1, d= 1)
        cmds.move(1,1.2,0)
        cmds.rotate( 0, 0, '15deg', r=True )
        cmds.polySmooth( bodyName+'.f[0:5]', dv=1 )
        cmds.polyCube(name=seatName, w = 1, h = 1, d= 0.5)
        cmds.move(-1,1.5,0)
        cmds.rotate( 0, 0, '-15deg', r=True )
        cmds.polySmooth( seatName+'.f[0:3]', dv=1 )
        cmds.polyCube(name=steeringWheelName, w = 3, h = 0.2, d= 0.2)
        cmds.move(2.4,2,0)
        cmds.rotate( 0, 90,0, r=True )
        # cmds.select( d=True )
        # cmds.joint(n=bodyJ1, p=(0, 9, 0) )
        # cmds.joint(n=bodyJ2, p=(0, 8, 0) )
        # cmds.joint(n=bodyJ3, p=(0, 7, 0) )
        # cmds.ikHandle( sj=bodyJ1, ee=bodyJ3)
        # cmds.bindSkin( bodyName, bodyJ1)
    #model frontWheel:
        frontWheel = 'frontWheel' + randomNaming
        frontWheelStick = 'frontWheelStick'+randomNaming
        frontWheelJ = 'frontWheelJ' + randomNaming
        leftElbowJ = 'leftElbowJ'+randomNaming
        leftWristJ = 'leftWristJ'+randomNaming
        cmds.polyCylinder(r=1, n=frontWheel)
        cmds.rotate(90,0,0)
        cmds.scale(0.1, y = True)
        cmds.move(3,0,0)
        cmds.polyCube(h=2,w=0.4,d=0.3, n= frontWheelStick)
        cmds.move(2.5,1,0)
        cmds.rotate(0,0,45)
        # cmds.xform(r= True, ro=(0, 0, -45) )
        # cmds.polySmooth( frontWheel+'.f[0:5]', dv=2 )
        # cmds.select( d=True )
        # cmds.joint(n=frontWheelJ, p=(0.5, 9, 0) )
        # cmds.joint(n=leftElbowJ, p=(1, 8.5, 0) )
        # cmds.joint(n=leftWristJ, p=(1.5, 8, 0) )
        # cmds.ikHandle( sj=frontWheelJ, ee=leftWristJ)
        # cmds.bindSkin( frontWheel, frontWheelJ)
    #model backWheel:
        backWheel = 'backWheel' + randomNaming
        backWheelStick = 'backWheelStick'+randomNaming
        backWheelJ = 'backWheelJ'+ randomNaming
        rightElbowJ = 'rightElbowJ'+randomNaming
        rightWristJ = 'rightWristJ'+randomNaming
        cmds.polyCylinder(r=1, n=backWheel)
        cmds.rotate(90,0,0)
        cmds.scale(0.1, y = True)
        cmds.move(-2.3,0,0)
        cmds.polyCube(h=2,w=0.4,d=0.3, n=backWheelStick)
        cmds.move(-1.8,1,0)
        cmds.rotate(0,0,-45)
        # cmds.select( d=True )
        # cmds.joint(n=backWheelJ, p=(-0.5, 9, 0) )
        # cmds.joint(n=rightElbowJ, p=(-1, 8.5, 0) )
        # cmds.joint(n=rightWristJ, p=(-1.5, 8, 0) )
        # cmds.ikHandle( sj=backWheelJ, ee=rightWristJ)
        # cmds.bindSkin( backWheel, backWheelJ)
    #group everything:
        gp = cmds.group(bodyName, seatName, steeringWheelName, frontWheel, frontWheelStick, backWheel, backWheelStick, n=nombre)
        cmds.select(gp)
        # Clé1
        cmds.currentTime(1)
        cmds.setKeyframe( v=uniform(-20,-10), at='translateX' )
        cmds.setKeyframe( v=uniform(-5,5), at='translateZ' )
        
        # Clé intermédiaire
        cmds.currentTime(12)
        cmds.setKeyframe( v=uniform(-20,20), at='translateZ' )
        
        # Clé 2
        cmds.currentTime(120)
        cmds.setKeyframe( v=uniform(10,20), at='translateX' )
        cmds.setKeyframe( v=uniform(-5,5), at='translateZ' )
        

winName = 'PersoRIG'
backgroundColor = [40.0/255.0,35.0/255.0,39.0/255.0]
winWidth = 400 # set a target width and reference this when you specify width
if cmds.window(winName, exists=True):
    cmds.deleteUI(winName)
cmds.window(winName, width=winWidth, title='PersoRIG', h=200,  bgc=(backgroundColor), tlb=True)
mainCL = cmds.columnLayout() 
mainRLWidth = [winWidth, winWidth]
cmds.rowLayout(numberOfColumns=1, cw=mainRLWidth)
cmds.rowLayout(numberOfColumns=2, cw2=mainRLWidth)
cmds.textFieldGrp('newNames', label = 'Motorcycle Name: ', width=mainRLWidth[0])
cmds.button(label='Generate', width=mainRLWidth[1]*0.60, height=40, c='rename()')
cmds.setParent('..')
def rename(*args):
    #query values:
    text_A = cmds.textFieldGrp( 'newNames', query = True, text = True)
    toto = Perso()
    toto.nameGenerator()
    toto.generate(text_A)
cmds.showWindow()
cmds.window(winName, e=True, width=winWidth, height=200)
