#!/usr/bin/env python3

import rospy
import random
from ros_project.msg import sensor_readings



def publish_humidity():

    rospy.init_node('humidity_node',anonymous=True)
    pub_humidity = rospy.Publisher('humidity_data',sensor_readings,queue_size=10)
    
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        
        rate.sleep()
         # Actual humidity range + Out of range values for Validation
        sensor_reading = random.uniform(0.6, 1.05) # 0.7 <= h <= 0.95
        
        # random.random()  Random number between 0.0 and 1.0
        Humidity_Sensor_state = random.random() < 0.90 # 90% probability of choosing True
        
        sensor_state_msg = sensor_readings()
        sensor_state_msg.sensor_name = 'humidity'
        sensor_state_msg.state = Humidity_Sensor_state

        
        if Humidity_Sensor_state == False:
            sensor_state_msg.value = 0.0
        else:
            sensor_state_msg.value = sensor_reading



        rospy.loginfo(". SensorState : %s , Humidity: %.2f, ", "Working" if Humidity_Sensor_state else "Not Working ", sensor_state_msg.value)
        if Humidity_Sensor_state == False:
            rospy.logwarn("Humidity Sensor is not working properly, Please check the sensor") 

        pub_humidity.publish(sensor_state_msg)

        
        rate.sleep()

        
if __name__ == '__main__':
   
    publish_humidity()
    
    
#Validation for remote station node 

# if .95 <= sensor_reading <= 1.2 : 
#     temp_node_state = 'true'
# else:
#     temp_node_state = 'False'
