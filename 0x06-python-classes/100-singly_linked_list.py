#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value, None)
        else:
            pointer = self.__head
            while pointer is not None:
                if value < pointer.data:
                    break
                prev_node = pointer
                pointer = pointer.next_node

            new_node = Node(value, pointer)
            if pointer == self.__head:
                self.__head = new_node
            else:
                prev_node.next_node = new_node

    def __str__(self):
        str_list = []
        new_str = ""
        pointer = self.__head

        while pointer is not None:
            str_list.append(str(pointer.data) + "\n")
            pointer = pointer.next_node
        new_str = new_str.join(str_list)
        return new_str[:-1]
