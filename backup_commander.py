#! /usr/bin/env python3

# Adapted from the simple commander demo examples on 
# https://github.com/ros-planning/navigation2/blob/galactic/nav2_simple_commander/nav2_simple_commander/demo_security.py

from copy import deepcopy
import sys
import time
import stretch_body.robot
from geometry_msgs.msg import PoseStamped
from stretch_nav2.robot_navigator import BasicNavigator, TaskResult
import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from rclpy.action import ActionClient
from control_msgs.action import FollowJointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from sensor_msgs.msg import JointState


"""
Basic security route patrol demo. In this demonstration, we use the D435i camera
mounted on the robot to relay the camera feed back to us that can be monitored
using RViz.
"""

def do_basic_routine(robot):
    print("Moving Lift to 0.55m...")
    robot.lift.move_to(0.55)
    robot.push_command()
    robot.lift.wait_until_at_setpoint()
    time.sleep(7)
    print("Moving Lift to 1.05m...")
    robot.lift.move_to(1.05)
    robot.push_command()
    robot.lift.wait_until_at_setpoint()
    time.sleep(7)
    for i in range(1,5):
      print("Round: ", i)
      status = robot.get_status()
      print("Current Orientation: ", status['pimu']['imu']['my'])
      print("Rotating Base by 90°...")
      robot.base.rotate_by(np.pi / 2)
      robot.push_command()
      robot.base.wait_until_at_setpoint
      time.sleep(7)
      status = robot.get_status()
      print("Orientation after Rotation: ", status['pimu']['imu']['my'])
      status = robot.get_status()
      lift_pos_m = status['lift']['pos']
      print("Lift Position: ", lift_pos_m)
      i+=1


def main():
    rclpy.init()
    robot = stretch_body.robot.Robot()
    navigator = BasicNavigator()
    robot.home()
    # Security route, probably read in from a file for a real application
    # from either a map or drive and repeat.
    security_route = [[-0.086442, 0.131],[1.2386, 0.88525],[1.165, 2.6624]]
    status = robot.get_status()
    #print("------ Status: ------", status)
    # Set our demo's initial pose
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = -0.086442
    initial_pose.pose.position.y = 0.131
    initial_pose.pose.orientation.z = 0.0049257
    initial_pose.pose.orientation.w = 0.99999
    navigator.get_logger().info('PoseStamped: ' + str(initial_pose))
    navigator.setInitialPose(initial_pose)

    posdata = []
    
    # Wait for navigation to fully activate
    navigator.waitUntilNav2Active()
    # Do security route until dead
    while rclpy.ok():
        # Send our route
        route_poses = []
        pose = PoseStamped()
        # Receive current joint states
        #robot.joint_state
        pose.header.frame_id = 'map'
        pose.header.stamp = navigator.get_clock().now().to_msg()
        pose.pose.orientation.w = 1.0
        for pt in security_route[1:]:
            pose.pose.position.x = pt[0]
            pose.pose.position.y = pt[1]
            route_poses.append(deepcopy(pose))
            posdata.append(pose.pose)
        
        nav_start = navigator.get_clock().now()
        navigator.followWaypoints(route_poses)
        
        # Do something during our route (e.x. AI detection on camera images for anomalies)

        # Simply print ETA for the demonstation
        i = 0
        while not navigator.isTaskComplete():
            print("starting")
            i += 1
            feedback = navigator.getFeedback()
            if feedback and i % 5 == 0:
            #if feedback:
                navigator.get_logger().info('Executing current waypoint: ' +
                    str(feedback.current_waypoint + 1) + '/' + str(len(route_poses)))
                
                for i in range(1,5):
                    navigator.spin(spin_dist=1.57, time_allowance=3)
                    navigator.waypoint_pause_duration()

                navigator.get_logger().info("-------------Spin done-------------")
               
                #print('--- Move Arm out ---')
         

                
                #print('--- Move Arm in ---')
                now = navigator.get_clock().now()
                # Some navigation timeout to demo cancellation
                if now - nav_start > Duration(seconds=.0):
                    navigator.cancelTask() 
                    
            #do_basic_routine(robot)
        print("----- Routine finished -----")
             
        # If at end of route, reverse the route to restart
        #navigator.goToPose(initial_pose)
        
        security_route.reverse()

        result = navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            navigator.get_logger().info('Route complete! Restarting...')
        elif result == TaskResult.CANCELED:
            navigator.get_logger().info('Security route was canceled, exiting.')
            rclpy.shutdown()
        elif result == TaskResult.FAILED:
            navigator.get_logger().info('Security route failed! Restarting from other side...')


        navigator.get_logger().info("posdata: " + str(posdata))
    print('------ Done with Security Route ------')
    rclpy.shutdown()


if __name__ == '__main__':
    main()