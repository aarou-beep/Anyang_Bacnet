from fastapi.testclient import TestClient 
from fastapi import FastAPI

app = FastAPI()

client = TestClient(app) 

def test_read_tasks():
      res = client.get("/tasks") 
      assert res.status_code == 200


      