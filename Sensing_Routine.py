# Backup script of the sensing routine based on the simple commander feature of Nav2
# The script is already on the robot saved under simple_commander_demo.py in the stretch_nav2 folder 
# The Sensing routine will be launched with 'ros2 launch stretch_nav2 demo_security.launch.py' while providing a map path   

#! /usr/bin/env python3

# Adapted from the simple commander demo examples on 
# https://github.com/ros-planning/navigation2/blob/galactic/nav2_simple_commander/nav2_simple_commander/demo_security.py

from copy import deepcopy

from geometry_msgs.msg import PoseStamped
from stretch_nav2.robot_navigator import BasicNavigator, TaskResult

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration

import pandas as pd
import csv


def main():
    rclpy.init()

    navigator = BasicNavigator()

    # Type in here the position data
    security_route = [
        [0.054, -0.0413],   # initial position
        [1.16, 0.68],       # first position in routine
        [0.49, -2.47]]      # second position in routine
    currposdata = []
    headerdata = ["msg"]

    # Set our demo's initial pose 
    # When saving the position data of the initial position also copy the orientation data of this position
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()

    # leave these values as it is
    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0

    # Type the determined orientation here
    initial_pose.pose.orientation.z = -0.113    
    initial_pose.pose.orientation.w = 0.994
    navigator.setInitialPose(initial_pose)
    
    # Wait for navigation to fully activate
    navigator.waitUntilNav2Active()

    # Do security route until process is finished or killed
    while rclpy.ok():
        # Feed our positions into the route
        route_poses = []
        pose = PoseStamped()
        pose.header.frame_id = 'map'
        pose.header.stamp = navigator.get_clock().now().to_msg()
        pose.pose.orientation.w = 1.0
        for pt in security_route[1:]:
            pose.pose.position.x = pt[0]
            pose.pose.position.y = pt[1]
            route_poses.append(deepcopy(pose))
        
        nav_start = navigator.get_clock().now()

        # There are different ways in the Simpler Commander API to follow a route. 
        # Since we want the robot to go all positions and then directly back to the initial position instead of reversing the route, I chose to go with the goToPose() command
        #navigator.followWaypoints(route_poses)

        # Go to first pose 
        navigator.goToPose(route_poses[0])
        # Do something during our route (e.x. AI detection on camera images for anomalies)
        # Simply print ETA for the demonstation
        i = 0
        while not navigator.isTaskComplete():
            i = i + 1
            feedback = navigator.getFeedback()
            if feedback and i % 4 == 0:
                #navigator.get_logger().info('Executing current waypoint: ' + str(feedback.current_waypoint + 1) + '/' + str(len(route_poses)))
                #print('...... current pose: ' + '{0:.0f}'.format(PoseStamped.from_msg(feedback.current_pose)))
                #navigator.get_logger().info('----- Current Pose: ' + str(feedback.current_pose))

                # I tried to extract the position data of the robot for every point it reaches since simultaneous recording of the overall movement was not possible yet in ROS2
                # Also, the df "pos" was supposed to be saved as an csv. This idea was not further used as it was a long process to structure and extract the desired information from the bulky ROS message samples.
                # It is better to use rosbag once it is available properly for ROS2

                pos = feedback.current_pose
                currposdata.append(pos)         
                now = navigator.get_clock().now()
                
        # Once the first point is reached, navigate to the second point
        
        result = navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            navigator.get_logger().info('Arrived at first measurement point: ' + str(route_poses[0])+
            ' next point is: ' + str(route_poses[1]))
            navigator.goToPose(route_poses[1])
            i = 0
            while not navigator.isTaskComplete():
                i = i + 1
                feedback = navigator.getFeedback()
                if feedback and i % 4 == 0:
                    #navigator.get_logger().info('Executing current waypoint: ' + str(feedback.current_waypoint + 1) + '/' + str(len(route_poses)))
                    #print('...... current pose: ' + '{0:.0f}'.format(PoseStamped.from_msg(feedback.current_pose)))
                    #navigator.get_logger().info('----- Current Pose: ' + str(feedback.current_pose))
                    pos = feedback.current_pose
                    currposdata.append(pos)
            
            # Once the second posiiton is achieved, go back to the initial position 

            result = navigator.getResult()
            if result == TaskResult.SUCCEEDED:
                navigator.get_logger().info('Arrived at first measurement point: ' + str(route_poses[0])+
                ' next point is: ' + str(initial_pose))
                navigator.goToPose(initial_pose)
                i = 0
                while not navigator.isTaskComplete():
                    i = i + 1
                    feedback = navigator.getFeedback()
                    if feedback and i % 4 == 0:
                        #navigator.get_logger().info('Executing current waypoint: ' + str(feedback.current_waypoint + 1) + '/' + str(len(route_poses)))
                        #print('...... current pose: ' + '{0:.0f}'.format(PoseStamped.from_msg(feedback.current_pose)))
                        #navigator.get_logger().info('----- Current Pose: ' + str(feedback.current_pose))
                        pos = feedback.current_pose
                        currposdata.append(pos)
                
                # Once back to the initial position, end the process.
                         
                result = navigator.getResult()
                if result == TaskResult.SUCCEEDED:
                    navigator.get_logger().info('----Finished')
                    rclpy.shutdown()
        
        # Exemplatory alternatives if the first position is not reached, 
                    
        elif result == TaskResult.CANCELED:
            navigator.get_logger().info('Security route was canceled, exiting.')
            navigator.goToPose(initial_pose)
            rclpy.shutdown()
        elif result == TaskResult.FAILED:
            navigator.get_logger().info('Security route failed! Restarting from other side...')
            rclpy.shutdown()
        while not navigator.isTaskComplete():
            pass

    rclpy.shutdown()


if __name__ == '__main__':
    main()


