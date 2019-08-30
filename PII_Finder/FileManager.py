import os.path


class FileManager(object):
    COMPRESSED_EXT = ['zip', 'rar', 'tar', 'gzip', '7zip']

    def __init__(self):
        pass

    @staticmethod
    def open_file(file_path):
        if os.path.isfile(file_path):
            f = open(file_path, 'r')
            try:
                return f.readlines()
            except IOError:
                print(file_path + " IO error. Skipping...")
            except UnicodeDecodeError:
                print(file_path + " cannot be parsed. Skipping...")
            f.close()
        return None
