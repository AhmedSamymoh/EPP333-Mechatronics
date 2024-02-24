#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import random

num = 0
flag = False
firstData = True
pervious = 0
recevied = 0

def Callback(data):
    global flag ,recevied
    recevied = int(data.data)
    rospy.loginfo(". state of data : %s", flag)
    
def Publisher():
    global num ,recevied , firstData , pervious
    
    rospy.init_node(name='Synchronous_Publisher' , anonymous= True)
    pub = rospy.Publisher('encrypted_data',String,queue_size=10)

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        sub = rospy.Subscriber('decrypted_data', String, Callback)
        
        num = random.randint(1,100)
        encrypted_num = num ** 2 + 10
        
        e_str = ". data = " + str(num) + "  . encrypted_data = " + str(encrypted_num)
        rospy.loginfo("Waiting ...")  
        if recevied == pervious :
            rospy.loginfo("Data is synch")  
            rospy.loginfo(e_str)
            pub.publish(str(encrypted_num))
        
        # Wait for subscriber's response
              
        rate.sleep()

        
if __name__ == '__main__':
    try:
        Publisher()
        
    except rospy.ROSInterruptException:
        pass
    
    