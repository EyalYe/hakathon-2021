import json

def get_status(id):
    return "full"
    pass


def update(id,newStatus):
    with open(r'C:\Users\dango\Desktop\DataBase.json', "r+") as file:
        data = json.load(file)
            
        print(data["services"][id]["name"])
        data["services"][id]["name"] = newStatus
        print(data)
        file.seek(0)
        json.dump(data,file,indent = 4)


def append(new_data):
    with open(r'C:\Users\dango\Desktop\OnlyFull.json', "r+") as file:         
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["services"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended





def onlyFullUpdate():
    
        
    with open(r'C:\Users\dango\Desktop\DataBase.json', "r+") as file:
        data = json.load(file)
        
        for i in range(len(data["services"])):
            if (data["services"][i]["name"] ==  "full"):
                print("Damnnnn",i)
                append(data["services"][i])


