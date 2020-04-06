class Reader:

    def read(self, file_input_name):
        f = open(file_input_name, 'r')
        lines = f.readlines()
        clean_lines = [line.replace("\n", "") for line in lines]
        f.close()
        return clean_lines

