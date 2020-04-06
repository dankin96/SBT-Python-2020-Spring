class Writer:

    def write(self, file_name, str):
        f = open(file_name, "w")
        f.write(str)
        f.close()