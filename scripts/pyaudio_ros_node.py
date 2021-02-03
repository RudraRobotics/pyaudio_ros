#!/usr/bin/env python3
import rospy
from pyaudio_ros.msg import Audio

def talker():
    pub = rospy.Publisher('audio', Audio, queue_size=10)
    rospy.init_node('pyaudio_ros_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        audio = Audio()
        pub.publish(audio)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
