import os, sys


PATH = os.path.dirname(os.path.abspath(__file__))
if PATH not in sys.path:
        sys.path.insert(0, PATH)


from sgvisuals import app as application
