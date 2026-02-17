import pytest



class TestTasks:

    async def test_create_task(self, client, login):
       res = await client.post("/api/tasks/", json={"title":"test task", "description":"test", "status":"pending", "date":"2026-10-10"})
       assert res.status_code == 200
       assert res.json()['status'] == "pending"
       task_id = res.json()['id']
       res2 = await client.delete(f"/api/tasks/{task_id}/")
       assert res2.status_code == 200


    async def test_edit_task(self, client, login):
       task = await client.post("/api/tasks/", json={"title":"test task", "description":"test", "status":"pending", "date":"2026-10-10"})
       task_id = task.json()['id']
       res = await client.patch(f"/api/tasks/{task_id}/", json={"title":"title changed", "description":"test patch", "status":'completed', "date":"2026-02-18"})
       assert res.status_code == 200
       assert res.json()['title'] == 'title changed'
       assert res.json()['description'] == 'test patch'
       await client.delete(f"/api/tasks/{task_id}/")


    async def test_get_task_by_id(self, client, login):
       task = await client.post("/api/tasks/", json={"title":"test task", "description":"test", "status":"pending", "date":"2026-10-10"})
       task_id = task.json()['id']
       res = await client.get(f"/api/tasks/{task_id}/")
       assert res.status_code == 200
       assert res.json()['title'] == 'test task'
       await client.delete(f"/api/tasks/{task_id}/")
    

    async def test_search_task(self, client, login):
       task = await client.post("/api/tasks/", json={"title":"test task", "description":"test", "status":"pending", "date":"2026-10-10"})
       task_id = task.json()['id']
       res = await client.get("/api/tasks/search", params={'status':'pending', 'title':'test task'})
       assert res.status_code == 200
       assert res.json()[0]['title'] == 'test task'
       await client.delete(f"/api/tasks/{task_id}/")
