import pytest



class TestUser:
   
   async def test_me(self, client, login):
      res = await client.get("/api/auth/me")
      assert res.status_code == 200
      assert "email" in res.json()

   async def test_delete(self, client, login):
      res = await client.delete("/api/auth/logout")
      assert res.status_code == 200
      assert "message" in res.json()

   async def test_refresh_token(self, client, login):
      res = await client.post("/api/auth/refresh")
      assert res.status_code == 200
      assert res.json()['message'] == "access token refreshed successfully"
   