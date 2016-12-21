#to enable and disable different body parts
RIGHT_HAND = True
RIGHT_ARM  = True
LEFT_HAND  = False
LEFT_ARM   = True
SPEECH     = False

# It uses WebkitSpeechRecognition, so you need to use Chrome as your default browser for this script to work
# Start the webgui service without starting the browser
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()
# Then start the browsers and show the WebkitSpeechRecognition service named i01.ear
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")

# As an alternative you can use the line below to show all services in the browser. In that case you should comment out all lines above that starts with webgui. 
# webgui = Runtime.createAndStart("webgui","WebGui")

if(SPEECH):
	#Speech
	Voice="cmu-slt-hsmm" # Default female for MarySpeech 
	#Voice="cmu-bdl" #Male US voice.You need to add the necessary file.jar to myrobotlab.1.0.XXXX/library/jar
	#Voice ="upmc-pierre-hsmm" #untested other voiice
	#https://github.com/MyRobotLab/pyrobotlab/blob/ff6e2cef4d0642e47ee15e353ef934ac6701e713/home/hairygael/voice-cmu-bdl-5.2.jar
	voiceType = Voice
	mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
	mouth.setVoice(voiceType)

i01 = Runtime.createAndStart("i01", "InMoov")
i01.startEar()
if(SPEECH): i01.startMouth()	#disabled because speech is not working

# Change to the port that you use, this might need to be updated whenever you switch computers.
rightPort = "COM6"
leftPort = "COM5"

if(RIGHT_HAND):
	i01.startRightHand(rightPort)
 
	i01.rightHand.thumb.map(0,180,10,170)
	i01.rightHand.index.map(0,180,0,160)
	i01.rightHand.majeure.map(0,180,10,170)
	i01.rightHand.ringFinger.map(0,180,170,10)
	i01.rightHand.pinky.map(0,180,160,20)

	#i01.rightHand.thumb.setRest(90)

	i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)


if(RIGHT_ARM):
	i01.startRightArm(rightPort)
 
	i01.rightArm.bicep.setMinMax(0,90)
	i01.rightArm.rotate.setMinMax(20,180)
	i01.rightArm.shoulder.setMinMax(0,180)
	i01.rightArm.omoplate.setMinMax(10,75)

	i01.rightArm.bicep.setRest(20)
	i01.rightArm.rotate.setRest(90)
	i01.rightArm.shoulder.setRest(90)
	i01.rightArm.omoplate.setRest(90)

	i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)

if(LEFT_ARM):
	i01.startLeftArm(leftPort)
 
	i01.leftArm.bicep.setMinMax(15,100)
	i01.leftArm.rotate.setMinMax(20,180)
	i01.leftArm.shoulder.setMinMax(0,180)
	i01.leftArm.omoplate.setMinMax(95, 150)

	i01.leftArm.bicep.setRest(20)
	i01.leftArm.rotate.setRest(90)
	i01.leftArm.shoulder.setRest(90)
	i01.leftArm.omoplate.setRest(90)

	i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)

if(LEFT_HAND):
	print "Need to implement left hand"	
	#TODO: make left hand.


# verbal commands
ear = i01.ear

#default voice commonds
ear.addCommand("attach your finger", "i01.rightHand.index", "attach")
ear.addCommand("disconnect your finger", "i01.rightHand.index", "detach")
ear.addCommand("rest", i01.getName(), "rest")
ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

#custom gestures
ear.addCommand("open your hand", "python", "handOpen")
ear.addCommand("close your hand", "python", "handClose")
ear.addCommand("hand to the middle", "python", "handMiddle")
ear.addCommand("give the middle finger", "python", "middleFinger")
ear.addCommand("raise your arms", "python", "armUp")
ear.addCommand("lower your arms", "python", "armDown")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley 
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")

ear.startListening()

def armUp():
  if(RIGHT_ARM): i01.moveArm("right", 90, 90, 150, 90)
  if (LEFT_ARM): i01.moveArm("left", 90, 90, 150, 150)
  if (SPEECH): mouth.speak("I'm going to raise my arm")

def armDown():
  if(RIGHT_ARM): i01.moveArm("right", 20, 90, 90, 90)
  if(LEFT_ARM): i01.moveArm("left", 20, 90, 90, 95)
  if(SPEECH): mouth.speak("I'm going to lower my arm")

def handOpen():
  if(RIGHT_HAND): i01.moveHand("right", 180, 180, 180, 180, 180)
  if(SPEECH): mouth.speak("I will open my hand")

def handClose():
  if(RIGHT_HAND): i01.moveHand("right",0,0,0,0,0)
  if(SPEECH): mouth.speak("My hand is closed")

def handMiddle():
  if(RIGHT_HAND): i01.moveHand("right",90,90,90,90,90)
  if(SPEECH): mouth.speak("ok you have my attention")

def middleFinger():
  if(RIGHT_HAND): i01.moveHand("right", 0, 0, 180, 0, 0)
  if(SPEECH): mouth.speak("Fuck! You!")
