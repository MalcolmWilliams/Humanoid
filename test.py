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

# Change to the port that you use #this will need to be updated whenever you switch from linux to windows.
rightPort = "COM6"
leftPort = "COM5"




i01.startRightHand(rightPort)
i01.startRightArm(rightPort)
#i01.startLeftArm(leftPort)
###servo mappings and limits###
i01.rightHand.thumb.map(0,180,10,170)
i01.rightHand.index.map(0,180,0,160)
i01.rightHand.majeure.map(0,180,10,170)
i01.rightHand.ringFinger.map(0,180,170,10)
i01.rightHand.pinky.map(0,180,160,20)
#i01.rightHand.thumb.setRest(90)

# tweak default RightArm
i01.rightArm.bicep.setMinMax(0,90)
i01.rightArm.rotate.setMinMax(20,180)
i01.rightArm.shoulder.setMinMax(0,180)
i01.rightArm.omoplate.setMinMax(10,75)

i01.rightArm.bicep.setRest(20)
i01.rightArm.rotate.setRest(90)
i01.rightArm.shoulder.setRest(90)
i01.rightArm.omoplate.setRest(90)

i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
#i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)

'''
depreciated accapela speech
# starting parts
i01.startMouth()
#to tweak the default voice
i01.mouth.setVoice("Ryan")
'''

#to tweak the default voice
Voice="cmu-slt-hsmm" # Default female for MarySpeech 
#Voice="cmu-bdl" #Male US voice.You need to add the necessary file.jar to myrobotlab.1.0.XXXX/library/jar
#https://github.com/MyRobotLab/pyrobotlab/blob/ff6e2cef4d0642e47ee15e353ef934ac6701e713/home/hairygael/voice-cmu-bdl-5.2.jar
voiceType = Voice
mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
mouth.setVoice(voiceType)

##############

# verbal commands
ear = i01.ear

ear.addCommand("attach your finger", "i01.rightHand.index", "attach")
ear.addCommand("disconnect your finger", "i01.rightHand.index", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

ear.addCommand("open your hand", "python", "handOpen")
ear.addCommand("close your hand", "python", "handClose")
ear.addCommand("hand to the middle", "python", "handMiddle")
ear.addCommand("give the middle finger", "python", "middleFinger")
ear.addCommand("raise your arm", "python", "armUp")
ear.addCommand("lower your arm", "python", "armDown")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley 
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

def armUp():
	i01.moveArm("right", 90, 90, 150, 90)
	#i01.moveArm("left", 90, 90, 150, 95)
	mouth.speak("i'm going to raise my arm")

def armDown():
	i01.moveArm("right", 20, 90, 90, 90)
	#i01.moveArm("left", 20, 90, 90, 95)
	mouth.speak("I'm going to lower my arm")

def handOpen():
	i01.moveHand("right", 180, 180, 180, 180, 180)
	mouth.speak("ok I will open my hand")

def handClose():
  i01.moveHand("right",0,0,0,0,0)
  mouth.speak("my hand is closed")

def handMiddle():
  i01.moveHand("right",90,90,90,90,90)
  mouth.speak("ok you have my attention")

def middleFinger():
	i01.moveHand("right", 0, 0, 180, 0, 0)
	mouth.speak("fuck! you!")

'''
def handOpen():
  i01.moveHand("right",170,160,170,10,20)
  i01.mouth.speak("ok I open my finger")

def handClose():
  i01.moveHand("right",10,0,10,170,160)
  i01.mouth.speak("my finger is closed")

def handMiddle():
  i01.moveHand("right",90,90,90,90,90)
  i01.mouth.speak("ok you have my attention")

def middleFinger():
	i01.moveHand("right", 10, 10, 170, 170, 170)
	i01.mouth.speak("middle finger")
'''