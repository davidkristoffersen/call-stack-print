create_tests = '''
for key, val in globals().copy().items():
    if callable(val) and str(val)[:9] == "<function":
        exec("test_" + key + " = lambda: " + key + "()", globals())
'''

run_tests = '''
for key, val in globals().copy().items():
    if len(key) > 5 and key[:5] == "test_":
        val()
'''
