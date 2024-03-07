#!/usr/bin/env python3

import rospy
from ros_project.msg import sensor_readings
from ros_project.msg import aggregator_data

def callback1(data):
    # Create a sensor readings message for Temperature Sensor
    aggregated_data1 = sensor_readings()
    aggregated_data1.sensor_name = 'Temperature_Sensor'
    aggregated_data1.state = data.state
    aggregated_data1.value = data.value
    
    # Aggregated data message is an array of sensor readings
    aggregated_msg = aggregator_data()
    aggregated_msg.aggregated_data.append(aggregated_data1)
    
    pub.publish(aggregated_msg)

    rospy.loginfo(data)

def callback2(data):
    # Create a sensor readings message for 
    # Humidity Sensor to give it to Aggregator data message
    aggregated_data2 = sensor_readings()
    aggregated_data2.sensor_name = 'Humidity_Sensor'
    aggregated_data2.state = data.state
    aggregated_data2.value = data.value
    
    aggregated_msg = aggregator_data()
    aggregated_msg.aggregated_data.append(aggregated_data2)
    
    pub.publish(aggregated_msg)
    rospy.loginfo(data)

def callback3(data):
    # guess what?? Create a sensor readings message for Pressure Sensor
    aggregated_data3 = sensor_readings()
    aggregated_data3.sensor_name = 'Pressure_Sensor'
    aggregated_data3.state = data.state
    aggregated_data3.value = data.value
    
    aggregated_msg = aggregator_data()
    aggregated_msg.aggregated_data.append(aggregated_data3)
    
    pub.publish(aggregated_msg)
    rospy.loginfo(data)

def aggregator_node():
    rospy.init_node('aggregator_node',anonymous=True) 
    
    # Sub to the topics for temperature, humidity, and pressure data
    sub1 = rospy.Subscriber('temperature_data',sensor_readings,callback1) 
    sub3 = rospy.Subscriber('humidity_data',sensor_readings,callback2) 
    sub5= rospy.Subscriber('pressure_data',sensor_readings,callback3) 
    
    rospy.spin()


if __name__ == '__main__':
    pub = rospy.Publisher('aggregated_data',aggregator_data,queue_size=10)
    aggregator_node()