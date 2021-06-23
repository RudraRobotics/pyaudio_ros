#!/usr/bin/env python3
import rospy
from tts_ros.msg import Audio

import pyaudio
import numpy as np

class PyAudioRos:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paFloat32,channels=1,rate=22050,output=True)
        self.stream.start_stream()

        rospy.Subscriber("audio", Audio, self.callback)
   
    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()

    def callback(self, audio):
        chunk = np.array(audio.data, np.float32)
        chunk = chunk.tobytes()
        self.stream.write(chunk)

def listener():
    rospy.init_node('pyaudio_play')
    pyaudio_ros = PyAudioRos()
    rospy.spin()

if __name__ == '__main__':
    listener()
