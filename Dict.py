Dict = {"vocals": "Plant",
        "guitar": "Page"}
band2 = dict(vocals= "Plant", guitar="Page")
print(Dict) #{'vocals': 'Plant', 'guitar': 'Page'}
print(type(band2))
print(len(Dict))#2

#access item in dicts.
print(Dict["guitar"])#Page
print(band2.get("vocals"))#Plant

#list all keys
print(band2.keys())#dict_keys(['vocals', 'guitar'])
#list all values
print(Dict.values())#dict_values(['Plant', 'Page'])
#list of key-value pairs as tuples
print(band2.items())#dict_items([('vocals', 'Plant'), ('guitar', 'Page')])
#verify key is in list
print("vocals" in Dict)#True
print("triangle" not in Dict)
print("Plant" in Dict) # for values it is false

#change values
Dict["vocals"] = "Coverable"
Dict.update({"bass": "JPJ"})
print(Dict) #{'vocals': 'Coverable', 'guitar': 'Page', 'bass': 'JPJ'}

#Remove items
print(Dict.pop("bass")) #JPJ only key is removed
print(Dict) #{'vocals': 'Coverable', 'guitar': 'Page'}

Dict["drums"] = "Bonham" #{'vocals': 'Coverable', 'guitar': 'Page', 'drums': 'Bonham'}
print(Dict)
print(Dict.popitem()) #('drums', 'Bonham')
print(Dict)#{'vocals': 'Coverable', 'guitar': 'Page'}

#Delete and clear
Dict["drums"] = "Bonham"
del Dict["drums"]
print(Dict) #{'vocals': 'Coverable', 'guitar': 'Page'}
band2.clear()
print(band2) #{}

# #copy Dicts.
# band2 = Dict #Create a ref. same dicts.
# print("Badcopy")
# print(band2) #{'vocals': 'Coverable', 'guitar': 'Page'}
# band2["Movie"]  = "leo"
# print(Dict) #{'vocals': 'Coverable', 'guitar': 'Page', 'Movie': 'leo'}

band2 = Dict.copy()
band2["Movie"] = "Leo"
print("Good copy!")
print(Dict) #{'vocals': 'Coverable', 'guitar': 'Page'}
print(band2) #{'vocals': 'Coverable', 'guitar': 'Page', 'Movie': 'Leo'}

# or use Dict. constructor fn
band3 = dict(band2)
print("!Good copy")
print(band3) #{'vocals': 'Coverable', 'guitar': 'Page', 'Movie': 'Leo'}

#Nested dictionaries
member1 = {
    "name": "Plant", 
    "instrument": "vocals"
}
member2 = {
    "name": "Page", 
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2 
}
print(band) #{'member1': {'name': 'Plant', 'instrument': 'vocals'}, 'member2': {'name': 'Page', 'instrument': 'guitar'}}
print(band["member1"]["name"]) #Plant

