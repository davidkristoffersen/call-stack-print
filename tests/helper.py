def run_tests(glob={}):
    for key, val in glob.items():
        if callable(val) and str(val)[:9] == "<function" and not key == "run":
            val()
