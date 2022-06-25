import sys, json
import numpy as np
from PIL import Image 

#0 1 3 6 9

res = []
if len(sys.argv) > 1 :

    pic = Image.open(sys.argv[1])
    arr = np.array(pic)

    #h, w = pic.size

    i = 0
    for row in range(7):
        res.append([])
        for px in arr[row]:

            dp = 0
            if px[1] <= 110: dp = 4
            elif px[1] <= 161: dp = 3
            elif px[1] <= 196: dp = 2
            elif px[1] <= 233: dp = 1
            res[i].append(dp)
        i+=1
           
f = open("inp.json", "w")
json.dump(res, f)
f.close()
