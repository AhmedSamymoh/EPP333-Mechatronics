#!/usr/bin/env python
import rospy
from lab01_pkg.srv import Encrypt, EncryptResponse

def decrypt(req):
    xored_codes = [ord(char) for char in req.encrypted]
    
    real_codes = [code ^ req.key for code in xored_codes]
    
    decrypted_sentence = ''.join([chr(code) for code in real_codes])

    response = EncryptResponse()
    response.decrypted = decrypted_sentence
    rospy.loginfo(". Received Sentence:" + req.encrypted)
    rospy.loginfo(". Key:" + str(req.key))
    rospy.loginfo(". Decrypted Sentence:" + decrypted_sentence)
    rospy.loginfo("..................................................")


    return response

if __name__ == '__main__':
    rospy.init_node('server')
    rospy.Service('service', Encrypt, decrypt)
    rospy.spin()
