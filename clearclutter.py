# using os module

import os
if (not os.path.exists("Data")):
    os.mkdir("Data")
for i in range(0,6):
    if (not os.path.exists("Data")):
        os.mkdir(f"Data/{i+1}") # to create a folder from 1 to 6 no
    # os.rmdir(f"Data/6") # it will remove or delete the 6 no folder 

oldfname=["Data/1/BTAS10501 EO.pdf","Data/1/BTCO13502 WT.pdf","Data/1/BTIT13501 DMBI.pdf","Data/1/BTIT13502 CNS.pdf","Data/1/BTIT14501 SE.pdf","Data/1/BTIT15501 IOE-1.pdf"]
newfname=["Data/1/1.pdf","Data/1/2.pdf","Data/1/3.pdf","Data/1/4.pdf","Data/1/5.pdf","Data/1/6.pdf"]
for i in range(len(oldfname)):
    os.rename(oldfname[i],newfname[i])