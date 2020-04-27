[![speechRecognition Homepage](https://img.shields.io/badge/speechRecognition-develop-orange.svg)](https://github.com/davidvelascogarcia/speechRecognition/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/speechRecognition.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/speechRecognition/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/speechRecognition.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/speechRecognition)

# Speech Recognition: speechRecognition (Python API)

- [Introduction](#introduction)
- [Use](#use)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`speechRecognition` module use `Google Speech API` in `python`. This module performs speech recognition and converts to text. Also use `YARP` to send text detection by network. Also admits `YARP` source audio like input. This module also publish recognition results in `YARP` port.


## Use

`speechRecognition` requires audio like input.
The process to running the program:

1. Execute [programs/speechRecognition.py](./programs), to start de program.
```python
python speechRecognition.py
```
2. Connect recognition source.
```bash
yarp connect /speechRecognition/data:o /yourport/data:i
```

NOTE:

- Data results are published on `/speechRecognition/data:o`

## Requirements

`speechRecognition` requires:

* [Install YARP 2.3.XX+](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* Install SpeechRecognition:

(Using YARP with Python 2.7 bindings)
```bash
pip2 install SpeechRecognition
```

(Using YARP with Python 3 bindings)
```bash
pip3 install SpeechRecognition
```

Tested on: `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.


## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/speechRecognition.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/speechRecognition)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/speechRecognition.svg?label=Issues)](https://github.com/davidvelascogarcia/speechRecognition/issues)

## Related projects

* [realpython: python speech recognition](https://realpython.com/python-speech-recognition/)

