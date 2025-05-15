from Stack import Stack

if __name__ == "__main__":
    stack = Stack()

    print(stack.get_stack())

    print("количество элементов стека: ", stack.count_elements())
    print("верхний элемент стека:", stack.top_element())

    while True:
        push_element = int(input("введите число для заполнения стека"))
        stack.push_element(push_element)
        print("текущее количество элементов стека: ", stack.count_elements())

        pop_element = stack.pop_element()
        print("текущее количество элементов стека: ", stack.count_elements())
        print("верхний элемент стека:", stack.top_element())

if __name__ == "__main__":
    main()