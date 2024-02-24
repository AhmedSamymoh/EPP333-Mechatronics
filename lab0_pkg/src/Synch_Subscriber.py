#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import math
    

decrypted_num = 0

def Callback(data):
    global decrypted_num, encrypted_num
    encrypted_num = int(data.data)
    decrypted_num = math.sqrt(encrypted_num - 10)
    rospy.loginfo(". decrypted data %s", int(decrypted_num))

    

def Subscriber():
    global decrypted_num
    
    rospy.init_node(name='Synchronous_Subscriber', anonymous=True)
    sub = rospy.Subscriber('encrypted_data', String, Callback)
    
    pub = rospy.Publisher('decrypted_data', String, queue_size=10)

    pub.publish(str(int(decrypted_num)))
    
    rospy.spin()

if __name__ == '__main__':
    Subscriber()
