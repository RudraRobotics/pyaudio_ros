#!/usr/bin/env python3
import rospy
from pyaudio_ros.msg import Audio
import pyaudio
import struct

def talker():
    pub = rospy.Publisher('audio', Audio, queue_size=10)
    rospy.init_node('pyaudio_ros_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
   
    sample_rate = 16000
    frame_length = 512
    input_device_index = None

    if rospy.has_param('pyaudio_ros/sample_rate'):
        sample_rate = rospy.get_param('/pyaudio_ros/sample_rate')
    if rospy.has_param('pyaudio_ros/frame_length'):
        frame_length = rospy.get_param('/pyaudio_ros/frame_length')
    if rospy.has_param('pyaudio_ros/input_device_index'):
        input_device_index = rospy.get_param('/pyaudio_ros/input_device_index')
    
    rospy.loginfo('sample_rate: %s', sample_rate)
    rospy.loginfo('frame_length: %s', frame_length)
    rospy.loginfo('input_device_index: %s', input_device_index)

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
                rate=sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=frame_length,
                input_device_index=input_device_index)
    audio = Audio()
    while not rospy.is_shutdown():
        pcm = audio_stream.read(frame_length)
        pcm = struct.unpack_from("h" * frame_length, pcm)
        print(len(pcm))
        audio.AudioData.data = pcm
        pub.publish(audio)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

