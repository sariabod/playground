import pandas as pd
import pathlib
import sys
import uuid
import shutil

df = pd.read_csv('data/train.csv')

# sometime remove new whal
#df = df[df['Id']!='new_whale']

f = open("data/labels.csv","a")
f.write("name,label\n")

#let make dir structure
for label in df['Id'].unique():

     newdf = df[df['Id']==label]
     # used for pickles if needed
     #uf = str(uuid.uuid4())
     # split into new train/val dataframes
     train = newdf.sample(frac=0.8)
     valid = newdf.drop(train.index)


     if len(valid) < 1:
         train = newdf

     else:
          path = "data/valid.cropped/{}".format(label)
          pathlib.Path(path).mkdir(parents=True, exist_ok=True)
          for k, v in valid.iterrows():
               file = v[0]
               label = v[1]
               # copy the file from raw to appropriate directories (you can move is space is an issue)
               shutil.copy("data/raw.cropped/{}".format(file), "data/valid.cropped/{}/{}".format(label,file))
               f.write("valid.cropped/{}/{},{}\n".format(label,file,label))
               # save pickles for later reference if needed
               # valid.to_pickle("data/pickles/valid_{}".format(uf))

     path = "data/train.cropped/{}".format(label)
     pathlib.Path(path).mkdir(parents=True, exist_ok=True)
     for k, v in train.iterrows():
          file = v[0]
          label = v[1]
          # copy the file from raw to appropriate directories (you can move is space is an issue)
          shutil.copy("data/raw.cropped/{}".format(file), "data/train.cropped/{}/{}".format(label,file))
          f.write("train.cropped/{}/{},{}\n".format(label,file,label))
          # save pickles for later reference if needed
          # train.to_pickle("data/pickles/train_{}".format(uf))
     



f.close()


