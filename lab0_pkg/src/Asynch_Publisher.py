#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import random

num = 0

def Publisher():
    global num
    
    rospy.init_node(name='Asynch_Publisher' , anonymous= True)
    pub = rospy.Publisher('encrypted_data',String,queue_size=10)
    
    rate = rospy.Rate(2)
    
    while not rospy.is_shutdown():
        num = random.randint(1,100)
        encrypted_num = num ** 2 + 10
        
        e_str = ". data = " + str(num) + "  . encrypted_data = " + str(encrypted_num)
        rospy.loginfo(e_str)
        pub.publish(str(encrypted_num))
        rate.sleep()
        
if __name__ == '__main__':
    try:
        Publisher()
    except rospy.ROSInterruptException:
        pass