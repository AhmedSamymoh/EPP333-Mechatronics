#!/usr/bin/env python

import rospy
from lab0_pkg.srv import Encryption
import random

def handle_encryption(request):
    num = random.randint(0, 100)  
    encrypted_num = num ** 2 + 10
    rospy.loginfo("Original: %s, Encrypted: %s", num, encrypted_num)
    return str(encrypted_num) 

def encryption_server():
    rospy.init_node('encryption_server')
    s = rospy.Service('encryption_service', Encryption, handle_encryption)
    rospy.loginfo("Encryption Server Ready.")
    rospy.spin()

if __name__ == "__main__":
    encryption_server()
