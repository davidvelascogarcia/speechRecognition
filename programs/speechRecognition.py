'''
 * ************************************************************
 *      Program: Speech Recognition Module
 *      Type: Python
 *      Author: David Velasco Garcia @davidvelascogarcia
 * ************************************************************
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

# Libraries
import datetime
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

print("")
print("Loading Speech Recognition module ...")
print("")

print("")
print("Initializing Speech Recognition engine ...")
print("")


print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("Initializing YARP network ...")
print("")

# Init YARP Network
yarp.Network.init()

print("")
print("[INFO] Opening data input port with name /speechRecognition/data:i ...")
print("")

# Open speechRecognition input tts port
speechRecognition_inputPort = yarp.Port()
speechRecognition_inputPortName = '/speechRecognition/data:i'
speechRecognition_inputPort.open(speechRecognition_inputPortName)

# Create speechRecognition input data bottle
speechRecognitionInputBottle = yarp.Bottle()

print("")
print("[INFO] Opening data output port with name /speechRecognition/data:o ...")
print("")

# Open speechRecognition output tts port
speechRecognition_outputPort = yarp.Port()
speechRecognition_outputPortName = '/speechRecognition/data:o'
speechRecognition_outputPort.open(speechRecognition_outputPortName)

# Create speechRecognition output data bottle
speechRecognitionOutputBottle = yarp.Bottle()

print("")
print("[INFO] YARP network configured correctly.")
print("")

print("")
print("[INFO] System configured correctly at " + str(datetime.datetime.now()) + ".")
print("")

# Init speechRecognition engine
speechRecognitionEngine = sr.Recognizer()

# Variable to loopControlListen
loopControlListen = 0

while int(loopControlListen) == 0:

    try:
        print("")
        print("**************************************************************************")
        print("Waiting for input request:")
        print("**************************************************************************")
        print("")
        print("[INFO] Waiting for input request at " + str(datetime.datetime.now()) + " ...")
        print("")

        # Get microphone as audio source
        print("")
        print("[INFO] Getting system microphone ...")
        print("")

        with sr.Microphone() as microphoneSource:

            # Reduce ambiente noise
            print("")
            print("[INFO] Adjust ambient noise ...")
            print("")

            speechRecognitionEngine.adjust_for_ambient_noise(microphoneSource, duration=0.2)

            # Listen audio source
            print("")
            print("[INFO] Listening ...")
            print("")

            try:

                audio = speechRecognitionEngine.listen(microphoneSource, timeout=4.0)

                # Recognize audio source
                print("")
                print("[INFO] Recognizing ...")
                print("")

                recognizedText = speechRecognitionEngine.recognize_google(audio, language='es-ES')

                print("")
                print("**************************************************************************")
                print("speechRecognition results:")
                print("**************************************************************************")
                print("")
                print("[RESULTS] Listened: " + str(recognizedText) + " at " + str(datetime.datetime.now()) + ".")
                print("")

                # Publish recognized text
                speechRecognitionOutputBottle.clear()
                speechRecognitionOutputBottle.addString(recognizedText)
                speechRecognition_outputPort.write(speechRecognitionOutputBottle)
                
            except:
                print("")
                print("**************************************************************************")
                print("speechRecognition results:")
                print("**************************************************************************")
                print("")
                print("[ERROR] Error void audio, timeout limit.")
                print("")

    except sr.RequestError as e:

        print("")
        print("**************************************************************************")
        print("speechRecognition results:")
        print("**************************************************************************")
        print("")
        print("[ERROR] Error, Request Google Speech API.")
        print("")

    except sr.UnknownValueError:

        print("")
        print("**************************************************************************")
        print("speechRecognition results:")
        print("**************************************************************************")
        print("")
        print("[ERROR] Unknown Error")
        print("")

# Close YARP ports
print("[INFO] Closing YARP ports ...")
speechRecognition_inputPort.close()
speechRecognition_outputPort.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("speechRecognition program finished correctly.")
print("")
