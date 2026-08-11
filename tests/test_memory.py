from memory.memory import Memory
def test_get_set():
  memory=Memory()
  memory.set("name","Mufeed")
  assert memory.get("name")=="Mufeed"
def test_delete():
  memory=Memory()
  memory.set("Name","Mufeed")
  memory.delete("Name")
  assert memory.get("Name") is None
