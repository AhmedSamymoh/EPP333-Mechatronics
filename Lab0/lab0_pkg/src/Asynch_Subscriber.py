#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import math

        
def Callback(data):
    decrypted_num =  math.sqrt(int(data.data) - 10) 
    rospy.loginfo(". decrypted data %s", int(decrypted_num))
    
def Subscriber():
    rospy.init_node(name='Asynch_Subscriber' , anonymous= True)
    pub = rospy.Subscriber('encrypted_data',String,Callback)
    
    rospy.spin()
    
if __name__ == '__main__':
    Subscriber()