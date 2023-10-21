#!/usr/bin/env python3
""" This is the package initialization """
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Deserialize the data
storage.reload()
