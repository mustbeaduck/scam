import sys, json, os
from datetime import datetime, timedelta

FILENAME= str(datetime.now().timestamp())
MODE = False


def fill_the_cell( date, depth ):
    
    global MODE

    for i in range(depth):
        #make a change
        if MODE:
            MODE = False
            os.system("chmod +x " + FILENAME) 
        else:
            os.system("chmod -x " + FILENAME) 
            MODE = True
        #add a commit
        os.system("git add . && git commit -am\".\" --date " + date.strftime("%Y-%m-%d")+" --quiet")
    


#get a timestamp from user input date
if ( len(sys.argv) > 2 ):

    #set up the file
    f = open(FILENAME, "w")
    f.close()
    #os.system("chmod +x " + FILENAME) 

    date = datetime.strptime(sys.argv[2], "%d %m %Y")
    print("date: ", date)

    #print("starting date: ", date)

    #parse json input file with pixelmap
    """
        i could catch exceptions but its not
        like im going to do anything about them
    """
    inp = open(sys.argv[1])
    pic = json.load(inp)
    inp.close()

    #go through the list incrementng day by day
    for i in range(len(pic[0])):
        for j in range(len(pic)):
            if pic[j][i] > 0:
                fill_the_cell(date, pic[j][i])
            date += timedelta(days = 1)
    
    #print("end date:", date)
    os.system("git push && rm " + FILENAME)
    
