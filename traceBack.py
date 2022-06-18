import traceback
try:
    raise Exception("This is the error message") 
except:
    with open("errorFile.txt","w") as f:
        f.write(traceback.format_exc())
        print("Traceback infor was written to the errorFile.txt")
    
