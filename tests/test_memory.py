from memory.memory import Memory
def test_get_set():
  memory=Memory()
  memory.set("name","Mufeed")
  assert memory.get("name")=="Mufeed"

