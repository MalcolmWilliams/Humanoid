'''
this is a simple test document to show how to get started with MyRobotLab (mrl)

Installation procedure.
There is some information online, but a lot of it is confusing or out of date. Note that most of these steps can be skipped because it will already be setup. 
1. Download the mrl jar file. (http://myrobotlab.org/download)
2. Download java if needed (same link)
3. Open command promt at folder with the mrl jar file and run ``java -jar myRobotLab.jar``
4. This will start mrl. go to the runtime tab and click ``system\install all``
5. you can then load and run a python script. note the ports defined in the script will likely have to be changed if the computer is different. 

if the arduino has not had the mrlComm firmware flashed, it can be found in the mrl directory: ``.\resource\Arduino\MRLComm``. flash it the same as you would any other arduino file.
'''




# this will run with versions of MRL above 1695
# a very minimal script for InMoov
# although this script is very short you can still
# do voice control of a finger starter
# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
#The Finger Starter is considered here to be right index, 
#so make sure your servo is connected to pin3 of you Arduino

# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")

# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")



i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()





# Change to the port that you use
rightPort = "COM6"

i01.startRightHand(rightPort)
i01.startRightArm(rightPort)
i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)



# starting parts
i01.startMouth()
#to tweak the default voice
i01.mouth.setVoice("Ryan")
##############

# verbal commands
ear = i01.ear

ear.addCommand("attach your finger", "i01.rightHand.index", "attach")
ear.addCommand("disconnect your finger", "i01.rightHand.index", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("open your hand", "python", "handOpen")
ear.addCommand("close your hand", "python", "handClose")
ear.addCommand("hand to the middle", "python", "handMiddle")
ear.addCommand("give the middle finger", "python", "middleFinger")
ear.addCommand("raise your arm", "python", "armUp")
ear.addCommand("lower your arm", "python", "armDown")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley 
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")

ear.startListening()




def armUp():
	i01.moveArm("right", 80, 120, 120, 60)
	
	i01.mouth.speak("arm up")

def armDown():
	i01.moveArm("right", 10, 60, 60, 10)
	i01.mouth.speak("arm down")

def handOpen():
  i01.moveHand("right",170,150,170,10,30)
  i01.mouth.speak("ok I open my finger")

def handClose():
  i01.moveHand("right",10,10,10,170,170)
  i01.mouth.speak("my finger is closed")

def handMiddle():
  i01.moveHand("right",90,90,90,90,90)
  i01.mouth.speak("ok you have my attention")

def middleFinger():
	i01.moveHand("right", 10, 10, 170, 170, 170)
	i01.mouth.speak("middle finger")