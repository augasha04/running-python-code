#print ("Hello World! Pass this test, please.")
def test_app_py_exists(path):
    assert(path.exists("lib/app.py"))