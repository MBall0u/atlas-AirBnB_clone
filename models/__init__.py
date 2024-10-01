#!/usr/bin/python3
"""

Don't know if I need documentation here
but just in case; this file marks a directory
as a python package.

"""

import models.engine.file_storage as f

storage = f.FileStorage()
storage.reload()
