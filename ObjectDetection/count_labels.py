import pandas as pd

df = pd.read_csv("/Users/noor/Bot4BACS/ObjectDetection/labels_my-project-name_2023-11-08-11-04-35.csv")

labels = {"Radiator","Knob_Radiator", "Light_Switch"}
#print(labels)
#print(df["label_name"])
counter = 0
num_labels = []

selected = df[df.label_name == "Light_Switch"]
print(selected)
#num_labels.append(len(selected))
print(len(selected))


""" for label in labels: 
    selected = df[df.label_name == label]
    num_labels.append(len(selected))
    print(len(selected))
          
print(labels)          
print(num_labels) """