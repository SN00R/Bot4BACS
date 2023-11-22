import pandas as pd
#dfpath = "/home/hello-robot/Bot4BACS/test.csv"
dfpath = "ObjectDetection/labels_my-project-name_2023-10-25-07-08-39.csv"
col=["sec", "nanosec", "frame_id", "child_frame_id", "trans_x", "trans_y", "trans_z", "rot_x", "rot_y", "rot_z", "rot_w"]
df = pd.read_csv("/home/hello-robot/Bot4BACS/test.csv", header=None, names=col)
#df.columns(col)
print(df)
