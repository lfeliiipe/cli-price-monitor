import sys

class Persist:
    def __init__(self, path):
        self._path = path
            
    def open_to(self, mode):
        try:
            file = open(self._path, mode)
        except FileNotFoundError:
            sys.exit(f"File not found in {self._path}")
        return file
