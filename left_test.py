#file : InMoov3.minimalFingerStarter.py

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
leftPort = "COM6"

i01.startLeftArm(leftPort)

# tweak default RightArm
i01.leftArm.bicep.setMinMax(15,100)
i01.leftArm.rotate.setMinMax(20,180)
i01.leftArm.shoulder.setMinMax(0,180)
i01.leftArm.omoplate.setMinMax(95, 150)

i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)

#to tweak the default voice
#Voice="cmu-slt-hsmm" # Default female for MarySpeech 
#Voice="cmu-bdl" #Male US voice.You need to add the necessary file.jar to myrobotlab.1.0.XXXX/library/jar
#https://github.com/MyRobotLab/pyrobotlab/blob/ff6e2cef4d0642e47ee15e353ef934ac6701e713/home/hairygael/voice-cmu-bdl-5.2.jar
#voiceType = Voice
#mouth = Runtime.createAndStart("i01.mouth", "MarySpeech")
#mouth.setVoice(voiceType)
##############
# starting parts

#i01.startMouth()
##############

# verbal commands
ear = i01.ear

ear.addCommand("attach your finger", "i01.rightHand.index", "attach")
ear.addCommand("disconnect your finger", "i01.rightHand.index", "detach")
ear.addCommand("rest", i01.getName(), "rest")

ear.addCommand("capture gesture", ear.getName(), "captureGesture")
ear.addCommand("manual", ear.getName(), "lockOutAllGrammarExcept", "voice control")
ear.addCommand("voice control", ear.getName(), "clearLock")

ear.addCommand("raise your arm", "python", "armUp")
ear.addCommand("lower your arm", "python", "armDown")

# Confirmations and Negations are not supported yet in WebkitSpeechRecognition
# So commands will execute immediatley 
ear.addComfirmations("yes","correct","yeah","ya") 
ear.addNegations("no","wrong","nope","nah")

ear.startListening()


def armUp():
	i01.moveArm("left", 90, 90, 150, 150)
	#i01.moveArm("left", 90, 90, 150, 95)
	#mouth.speak("i'm going to raise my arm")

def armDown():
	i01.moveArm("left", 20, 90, 90, 95)
	#i01.moveArm("left", 20, 90, 90, 95)
	#mouth.speak("I'm going to lower my arm")