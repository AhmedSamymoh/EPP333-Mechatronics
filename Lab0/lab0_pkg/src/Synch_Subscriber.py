#!/usr/bin/env python3
import rospy 
import math as m
from std_msgs.msg import Int16 ,Float32
import time

i = 0

def my_callback (data):
    
    rospy.loginfo(". Encrypted num %i",data.data) 
    global i
    i=m.sqrt((data.data)-10)
    rospy.loginfo(". Decrypted num %i",i)
    pubb.publish(data.data)
    rospy.loginfo("Data Recieved correctlly")
    time.sleep(3)

if __name__ == '__main__': 
    rospy.init_node("Synchronous_Subscriber", anonymous = True)
    
    pubb = rospy.Publisher('dycrypted_data', Float32, queue_size=10)
    sub = rospy.Subscriber('encrypted_data', Int16, my_callback)
    rospy.spin()
