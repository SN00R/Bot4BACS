import stretch_body.robot
import numpy as np
import time
from threading import Thread

robot = stretch_body.robot.Robot()
start_time = time.time()

print("Start!")
if robot.startup() == False:
    robot.startup()
    #print('robot startup')

status = robot.get_status()
robotdata = []

def background_loop():
    for i in range(1000):
    # while do_basic_routine(robot=robot)==True:
        current_lift =  robot.get_status()['lift']['pos']
        current_base_orientation = robot.get_status()['pimu']['imu']['my']
        current_base_x = robot.get_status()['pimu']
        #print(current_base_orientation)
        print(current_base_x)
        print(current_lift)
        robotdata.append(current_lift)
        time.sleep(0.5)

print('begin routine') 

def point_routine():
    print("Moving Lift to 0.25m...")
    robot.lift.move_to(0.25)
    robot.push_command()
    robot.lift.wait_until_at_setpoint()
    time.sleep(5)
    print("Moving Lift to 0.65m...")
    robot.lift.move_to(0.65)
    robot.push_command()
    robot.lift.wait_until_at_setpoint()
    time.sleep(5)
    print("Moving Lift to 1.05m...")
    robot.lift.move_to(1.05)
    robot.push_command()
    robot.lift.wait_until_at_setpoint()
    time.sleep(5)
    for i in range(1,5):
      print("Round: ", i)
      status = robot.get_status()
      print("Rotating Base by 90°...")
      robot.base.rotate_by(np.pi / 2)
      robot.push_command()
      robot.base.wait_until_at_setpoint
      time.sleep(5)
    print("Finished Point Sensing Routine")


#robot.lift.home()
position= []
#print("--------status: ", status)
#print(robot.start_event_loop)
def do_basic_routine():
    position.append(0)
    print("Start Sensing Routine at Position 0")
    point_routine()
    print("Moving to  Position 1")
    robot.base.translate_by(0.5)
    robot.push_command()
    robot.base.wait_until_at_setpoint()
    position.append(1)
    time.sleep(1)
    print("Start Sensing Routine at Position 1")
    point_routine()
    print("Move back to Position 0")
    robot.base.translate_by(-0.5)
    robot.push_command()
    robot.base.wait_until_at_setpoint()
    position.append(1)
    print("----- Routine finished -----")


b = Thread(target=background_loop)
f = Thread(target=do_basic_routine)
b.start()
f.start()


try:
    while True:
        time.sleep(1)
        print('processing...')  
        if time.time() - start_time > 8000:
            print("Process stopped after: ", (time.time() - start_time)/60, "mins")
            print("exiting...")
            print('------ BREAK ------ exiting after time limit...')
            break

except KeyboardInterrupt:
    print("Process stopped after: ", (time.time() - start_time)/60, "mins")
    print("exiting...")
    print('------ BREAK ------ exiting after interrupt...')
    print("Process stopped after: ", (time.time() - start_time)/60, "mins")
    print("exiting...")

#do_basic_routine(robot)

print("---------------",robotdata)
# backup data
df = pd.DataFrame(rawdata, columns=['Time', 'Amb','Obj', 'Temp', 'Humid', 'CO2', 'Elapsed', 'LightFront', 'LightTop'])
print("collected data", rawdata)
df['Time'] = pd.to_datetime(df.loc[:,'Time'])

#print("DF: ", df)

df.to_csv("/home/hello-robot/Bot4BACS/Sensoring/serial_finalsetup_test.csv", index=False)