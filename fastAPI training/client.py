import requests 


url = "http://127.0.0.1:8000/tasks"

#GET requests 
response = requests.get(url)
print(response.status_code)
print(response.json())



#POST requests 

task = {"id": 1, "name": "Buy milk",
        "id": 2, "name": "Walk dog"}
response = requests.post(url, json=task)
print(response.json())


# PUT and delete 
#update 
requests.put(
    url, 
    json = {"id": 1, "name": "Buy milk","done": True}
    )

#delete 
requests.delete(url, json={"id": 1}) 


for task in requests.get(url).json():
    print(f"{task['id']}: {task['name']} ({'done' if task['done'] else 'pending'})")