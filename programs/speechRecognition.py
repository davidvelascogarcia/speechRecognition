'''
 * ************************************************************
 *      Program: Speech Recognition Module
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
 */

/*
  *
  * | INPUT PORT                           | CONTENT                                                 |
  * |--------------------------------------|---------------------------------------------------------|
  * | /speechRecognition/data:i            | Input audio to recognize                                |
  *
  * | OUTPUT PORT                          | CONTENT                                                 |
  * |--------------------------------------|---------------------------------------------------------|
  * | /speechRecognition/data:o            | Recognized output text                                 |
  *
'''

import os
import speech_recognition as sr
import yarp

print("**************************************************************************")
print("**************************************************************************")
print("                 Program: Speech Recognition Module                       ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system ...")

print("")
print("Loading Speech Recognition module ...")


print("")
print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")

# Init YARP Network
yarp.Network.init()


print("")
print("[INFO] Opening data input port with name /speechRecognition/data:i ...")

# Open input tts port
speechRecognition_inputPort = yarp.Port()
speechRecognition_inputPortName = '/speechRecognition/data:i'
speechRecognition_inputPort.open(speechRecognition_inputPortName)

# Create input data bottle
inputBottle=yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /speechRecognition/data:o ...")

# Open output tts port
speechRecognition_outputPort = yarp.Port()
speechRecognition_outputPortName = '/speechRecognition/data:o'
speechRecognition_outputPort.open(speechRecognition_outputPortName)

# Create output data bottle
outputBottle=yarp.Bottle()

print("")
print("Initializing Speech Recognition engine ...")

# Init speechRecognition engine
speechRecognitionEngine = sr.Recognizer()

exit=0

print("")
print("")
print("**************************************************************************")
print("Processing:")
print("**************************************************************************")

while exit==0:

    try:
        # Get microphone as audio source
        print("")
        print("Getting system microphone ...")
        print("")
        with sr.Microphone() as microphoneSource:

            # Reduce ambiente noise
            print("Adjust ambient noise ...")
            speechRecognitionEngine.adjust_for_ambient_noise(microphoneSource, duration=0.2)

            # Listen audio source
            print("Listening ...")
            audio = speechRecognitionEngine.listen(microphoneSource, timeout=4.0)

            # Recognize audio source
            print("Recognizing ...")
            recognizedText = speechRecognitionEngine.recognize_google(audio, language='es-ES')

            print("")
            print("")
            print("**************************************************************************")
            print("Results:")
            print("**************************************************************************")
            print("")
            print("[RESULTS] You said: " + recognizedText)
            print("")

            # Publish recognized text
            outputBottle.clear()
            outputBottle.addString(recognizedText)
            speechRecognition_outputPort.write(outputBottle)

    except sr.RequestError as e:
        print("")
        print("[ERROR] Error, Request Google Speech API.")
        print("")
        print("**************************************************************************")

    except sr.UnknownValueError:
        print("")
        print("[ERROR] Unknown Error")
        print("")
        print("**************************************************************************")


# Close YARP ports
print("Closing YARP ports ...")
speechRecognition_inputPort.close()
speechRecognition_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
