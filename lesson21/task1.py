class MyOpenFile:
    file_counter = 0
    file_types_enabled = ['jpg', 'png', 'txt', 'py']
    file_types = {key: 0 for key in file_types_enabled}
    file_types['other'] = 0

    def open_file(self, file, mode='r', add_str=None):
        file_ext = file.split('.')[-1]
        if file_ext in MyOpenFile.file_types_enabled:
            if file_ext in MyOpenFile.file_types.keys():
                MyOpenFile.file_types.update({file_ext: MyOpenFile.file_types[file_ext] + 1})
                print(MyOpenFile.file_types)
        else:
            MyOpenFile.file_types['other'] += 1
            raise TypeError('The type of file is not enabled.')

        if mode == 'r':
            with open(file, mode) as f:
                f.readlines()
        elif mode == 'w':
            with open(file, 'w') as f:
                f.write(add_str)
        elif mode == 'a':
            with open(file, 'a') as f:
                f.write(add_str)
        else:
            raise Exception("The mode you have chosen is wrong. Use only one of the mode: 'r', 'w', 'a'.")
        return f

    @classmethod
    def get_num_of_usage(cls):
        return cls.file_counter

    @classmethod
    def get_num_of_usage_types(cls, type):
        for key in MyOpenFile.file_types.keys():
            if type == key:
                value = MyOpenFile.file_types[type]
                return value
        else:
            print('This type is not valuable.')

    def __enter__(self):
        MyOpenFile.file_counter += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Closing file. Quantity of closings is : {self.file_counter}.')
        return None
