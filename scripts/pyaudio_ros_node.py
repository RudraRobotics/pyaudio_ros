#!/usr/bin/env python3
import rospy
from tts_ros.msg import Audio

import pyaudio
import numpy as np

class PyAudioRos:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,channels=1,rate=22050,output=True)
        
        rospy.Subscriber("audio", Audio, self.callback)
   
    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()

    def callback(self, audio_input):
        audio = np.array(audio_input.data, dtype=np.float32)
        self.stream.write(audio)

def listener():
    rospy.init_node('pyaudio_play')
    pyaudio_ros = PyAudioRos()
    rospy.spin()

if __name__ == '__main__':
    listener()
