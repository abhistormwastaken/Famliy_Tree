
import json
 
# Opening JSON file
json_file= open('D:\FamilyTree\data\data.json') 
data = json.load(json_file)
d = data["data"]
def find_node_house_no(name,age,d):
    for i in d:
        if i["Name"]==name and i["Age"]==age:
            return i["House Number"]
def find_all_member(house_no,d):
    ans = []
    for i in d:
        if i["House Number"]==str(house_no):
            ans.append(i)
    return ans
def find_family(data,name):
    # list dict containing {name,relation}
    lst = [{"name":name,"relation":"self"}]
    curr = None
    for i in data:
        if i["Name"]==name:
            curr = i
            break
    att = list(i.keys())[1]
    if att == "Father Name":
        lst.append({"name":i[att],"relation":"parent"})
    else:
        lst.append({"name":i[att],"relation":"Spouse"})
    for i in data:
        try:
            if i["Father Name"]==name:
                curr = i
                break
        except:
            continue
    lst.append({"name":i["Name"],"relation":"Child"})
    return lst
def driver(name,age,d):
    house_no = find_node_house_no(name, age, d)
    famliy = find_all_member(house_no,d)
    rel_tree = find_family(d, name)
    return rel_tree
# export 
def Driver(name,age):
    return driver(name,age,d)


