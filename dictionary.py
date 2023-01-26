# MyDict ={
#     "name":"nikhil","age":"20", "gender": 'male',
#     "anotherDict":{"harry_potter":"j.k  rowling" , "inception": "Christopher Nolan"}
# }
# print(MyDict["age"]) 
# print(MyDict["name"]) 
# print(MyDict["gender"]) 
# print(MyDict["anotherDict" ]["harry_potter"])
# print(MyDict)

# print("******************************************************************************************")

# # dictionary methods
# print(MyDict.keys())#print all the keys in the dictionary
# print(type(MyDict.keys()))
# print(list(MyDict.keys()))#print all the keys in the dictionary in list format
# print(list(MyDict.values()))#print all the keys in the dictionary
# print(MyDict.items())#print all the list of (key,value)pairs in the dictionary

# print("******************************************************************************************")
# #update dictionary
# updateDict={
#     "profession":"developer", "salary":"45K" , "allowance":"20K"
# }
# #update dictionary method
# MyDict.update(updateDict) #update the dictionary by adding key value pairs from updateDict
# print(MyDict)


# print(MyDict.get("name")) #print value associated to the key name
# print(MyDict["harry"])  #print value associated to the key name

# print(MyDict["name2"]) # returns error as name2 is not any key in the dictionary
# print(MyDict.get("name2")) #returns none as name2 is not present in the dictionary










