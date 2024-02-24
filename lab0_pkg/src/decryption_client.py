#!/usr/bin/env python

import rospy
from lab0_pkg.srv import Encryption

def decryption_client():
    rospy.wait_for_service('encryption_service')
    try:
        
        encrypt = rospy.ServiceProxy('encryption_service', Encryption)
        
        while not rospy.is_shutdown(): 
            response = encrypt()  # Send an empty request
            rospy.loginfo("Received encrypted data: %s" % response.response)
            rospy.sleep(1)  
            
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

def subscriber():
    rospy.init_node('decryption_client')
    decryption_client()

if __name__ == '__main__':
    subscriber()
