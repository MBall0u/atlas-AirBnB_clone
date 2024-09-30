#!/usr/bin/python3
"""

Don't know if I need documentation here
but just in case; this file marks a directory
as a python package.

"""

from models.file_storage import FileStorage

storage = FileStorage()
storage.reload()
