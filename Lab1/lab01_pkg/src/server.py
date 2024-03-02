#!/usr/bin/env python

import rospy
import random
from lab01_pkg.srv import  Encrypt , EncryptRequest
import time  


def server():
    rospy.init_node('client')
    client = rospy.ServiceProxy('service', Encrypt)
    rospy.wait_for_service('service')
    
    while not rospy.is_shutdown():
        sentence = generate_random_sentence()
        rospy.loginfo(". Sentence:"+ str(sentence))

        key = random.randint(1, 100)
        
        ascii = [ord(char) for char in sentence]
        Xored_Char = [code ^ key for code in ascii]
        encrypted_sentence = ''.join([chr(code) for code in Xored_Char])

        request = EncryptRequest()
        request.key = key
        request.encrypted = encrypted_sentence

        response = client(request)

        rospy.loginfo(". Key:" + str(key))

        rospy.loginfo(". Encrypted Sentence:"+ str(encrypted_sentence))
        rospy.loginfo("..................................................")

        time.sleep(3)  # Adjust as needed


def generate_random_sentence():
    n = ["MCU", "servo", "camera", "batteries", "thrusters", "Raspberry", "Arduino", "sensors"]
    v = ["burns", "jumps", "works?", "bombs", "crushed", "milts"]

    noun = random.choice(n)
    verb = random.choice(v)
    
    sentence = f" {noun} {verb}."
    return sentence.capitalize()

if __name__ == '__main__':
    server()