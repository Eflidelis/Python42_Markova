class Stack:
    __lst = list()

    def __init__(self):
        self.__lst = list()

    def __del__(self):
        pass

    def push_element(self, element):
        self.__lst.append(element)

    def pop_element(self):
        return self.__lst.pop()

    def top_element(self):
        return self.__lst[:-1]

    def count_elements(self):
        return len(self.__lst)

    def get_stack(self):
        return self.__lst

   def __getitem__(self, valera):
       return self.__container[valera]

   def __delitem__(self, key):
       self.__container.pop(key)


   def __setitem__(self, key, value):
       self.__container.append(value)

       

