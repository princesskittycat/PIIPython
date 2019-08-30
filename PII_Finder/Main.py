import os

from FileManager import FileManager
from RegexValidator import RegexValidator

rootDir = 'C:\\users\\amandal\\Documents\\PIIPython\\'

if __name__ == '__main__':
    validator = RegexValidator()
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            absoute_path = os.path.join(dirName, fname)
            split_path = absoute_path.split('.')
            if len(split_path) > 1:
                if split_path[-1] in FileManager.COMPRESSED_EXT:
                    print(absoute_path + " is compressed... =/")
                else:
                    file_lines = FileManager.open_file(absoute_path)
                    i = 1
                    if file_lines is not None:
                        for line in file_lines:
                            key = validator.find_match(line)
                            if key is not None:
                                print("Match line " + str(i) + " on " + absoute_path + " for " + key)
                            i += 1

    print("\nDONE!!! =D")


