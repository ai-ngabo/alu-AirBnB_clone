from models.engine.file_storage import FileStorage

storage = FileStorage()  # Create an instance of FileStorage
storage.reload()  # Load existing data from file.json
