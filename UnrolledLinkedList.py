from typing import Optional, Callable, Any
from copy import deepcopy


class Node:
    def __init__(self):
        self.array = []
        self.next = None
        self.len = 0

    def __len__(self):
        return self.len


class Iter(object):
    def __init__(self, ull):
        self.ull = ull
        self.iter_n = 0

    def __next__(self):
        if self.iter_n < self.ull.len:
            value = self.ull.access_member(self.iter_n)
            self.iter_n += 1
            return value
        else:
            raise StopIteration()


class UnrolledLinkedList:
    """
    Initialize unrolled linked list structure
    and define related methods.
    """

    def __init__(self, max_cap=50) -> None:
        self.node_cap = max_cap
        self.len = 0
        self.head = None
        self.tail = None
        self.halfl = max_cap // 2

    def __str__(self):
        """
        String serialization method.
        :return:
        """
        if self.len == 0:
            return "empty"
        else:
            string = "{"
            node = self.head
            while node is not None:
                string += "["
                for i in range(0, len(node)):
                    string += str(node.array[i])
                    if i + 1 < len(node):
                        string += ", "
                string += "]"
                if node.next is not None:
                    string += ", "
                node = node.next
            string += "}"
            return string

    def __eq__(self, other):
        if not isinstance(other, UnrolledLinkedList):
            return NotImplemented
        elif self.node_cap != other.node_cap:
            return False
        elif self.len != other.len:
            return False
        elif str(self) != str(other):
            return False
        return True

    def __iter__(self) -> Iter:
        '''
        Get an iterator
        :return: an object of class Iter
        '''
        return Iter(self)

    def access_member(self, n):
        if n < 0 or n >= self.len:
            raise ValueError("invalid index")
        else:
            cur_node = self.head
            while n >= cur_node.len:
                n = n - cur_node.len
                cur_node = cur_node.next
            return cur_node.array[n]


def cons(li, value):
    """
    Add a new element by value
    :param li: the list
    :param value: An element to be added
    :return:
    """
    if li.node_cap <= 0:
        raise ValueError("invalid capability")
    cop = deepcopy(li)
    if cop.head is None:
        cop.head = Node()
        cop.head.array.append(value)
        cop.head.len += 1
        cop.tail = cop.head
    elif cop.tail.len < cop.node_cap:
        cop.tail.array.append(value)
        cop.tail.len += 1
    else:
        new_node = Node()
        middle = cop.halfl
        new_node.array = cop.tail.array[middle:]
        new_node.len = middle
        cop.tail.array = cop.tail.array[:middle]
        cop.tail.len = cop.node_cap - cop.halfl
        cop.tail.next = new_node
        cop.tail = new_node
        cop.tail.array.append(value)
        cop.tail.len += 1
    cop.len = cop.len + 1
    return cop


def remove(li, value):
    """
    Remove all elements of the specific value in the list.
    :param li: the list
    :param value: the element to be removed
    :return: a new list after remove the element
    """
    cop = deepcopy(li)
    cur_node = cop.head
    if cur_node is None:
        return "The unrolled linked list is empty."
    elif not member(li, value):
        assert not member(li, value), "Element is not in the list"
    else:
        while cur_node is not None:
            for i in range(len(cur_node)):
                if value == cur_node.array[i]:
                    if len(cur_node) > cop.halfl or cur_node.next is None:
                        for j in range(i, len(cur_node) - 1):
                            cur_node.array[j] = cur_node.array[j + 1]
                        cur_node.len -= 1
                        cop.len = cop.len - 1
                    else:
                        if len(cur_node.next) > cop.halfl:
                            for j in range(i, len(cur_node) - 1):
                                cur_node.array[j] = cur_node.array[j + 1]
                            cur_node.array[len(cur_node) - 1] = cur_node.next[0]
                            for k in range(0, len(cur_node.next) - 1):
                                cur_node.array[k] = cur_node.array[k + 1]
                            cur_node.next.len -= 1
                            cop.len = cop.len - 1
                        else:
                            for k in range(0, len(cur_node.next) - 1):
                                cur_node.array.append(cur_node.next.array[k])
                                cur_node.len += 1
                            for j in range(i, len(cur_node) - 1):
                                cur_node.array[j] = cur_node.array[j + 1]
                            cur_node.len -= 1
                            cop.len = cop.len - 1
                            cur_node.next = cur_node.next.next
            cur_node = cur_node.next
        return cop


def length(li):
    """
    Get the size of unrolled linked list
    :param li: the unrolled linked list
    """
    return li.len


def member(li, value):
    """
    Checks whether the given value is a member.
    :param li: the unrolled linked list
    :param value: The given value
    :return: True if the value is a member, otherwise False
    """
    if li.head is None:
        return False
    else:
        mem_value = False
        node = li.head
        while node is not None:
            if value in node.array:
                mem_value = True
                break
            else:
                node = node.next
        return mem_value


def reverse(li):
    """
    Reverse the unrolled linked list.
    :return: a new reversed list
    """
    new_list = UnrolledLinkedList()
    node = li.head
    iter_array = []
    while node is not None:
        iter_array += node.array
        node = node.next
    for element in reversed(iter_array):
        new_list = cons(new_list, element)
        new_list.len += 1
    return new_list


def to_list(li):
    """
    Convert an Unrolled linked list to a list
    :return:
    """
    node = li.head
    iter_array = []
    while node is not None:
        iter_array += node.array
        node = node.next
    return iter_array


def from_list(lst):
    """
    Convert to an unrolled linked list from a list
    :param lst: A list need to be converted.
    :return:
    """
    l = UnrolledLinkedList()
    for element in lst:
        new_list = cons(l, element)
        new_list.len += 1
    return l


def find(li, predicate):
    """
    Whether the list has specific element by specific predicate.
    :param li: An unrolled linked list.
    :param predicate: Specified predicate.
    :return: True if the list has element that fits the predicate
    """
    if li.head is None:
        return "The unrolled linked list is empty."
    else:
        current = li.head
        while current is not None:
            for i in range(len(current.array)):
                if predicate(current.array[i]):
                    return True
            current = current.next
        return False


def filter(li, predicate):
    """
    Filter data that meet specified predicate
    :param li: An unrolled linked list.
    :param predicate: Specified predicate
    :return: a new list contains the elements that fits
    """
    if li.head is None:
        return "The unrolled linked list is empty."
    else:
        x = UnrolledLinkedList()
        current = li.head
        while current is not None:
            for i in current.array:
                if predicate(i):
                    cons(x, i)
            current = current.next
        return x


def map(li, func: Optional[Callable[..., Any]] = None):
    """
    Apply a specific function to all elements.
    :param li: An unrolled linked list.
    :param func: Specified function
    :return:
    """
    cop = deepcopy(li)
    if func is None:
        return cop
    if li.head is None:
        return cop
    current = cop.head
    while current is not None:
        for i in range(len(current.array)):
            current.array[i] = func(current.array[i])
        current = current.next
    return cop


def reduce(li, func: Optional[Callable[..., Any]], ini):
    """
    Reduce process elements and build a value by the function.
    :param func: Specified function
    :return: The result of process
    """
    if func is None:
        return
    else:
        current = li.head
        value = ini
        while current is not None:
            for i in range(len(current.array)):
                value = func(value, current.array[i])
            current = current.next
        return value


def iterator(lst):
    """
    Convert the unrolled linked list to an iterator object.
    """
    cur = lst.head
    i = 0

    def foo():
        nonlocal cur
        nonlocal i
        if cur is None:
            raise StopIteration
        else:
            if i < cur.len:
                value = cur.array[i]
            else:
                i = 0
                cur = cur.next
                value = cur.array[i]
        return value

    return foo


def empty(li):
    li.head = None
    return li


def concat(li, ull):
    """
    Concat two unrolled linked lists.
    :param li: An unrolled linked list
    :param ull: Another unrolled linked list
    :return:
    """
    cop1 = deepcopy(li)
    cop2 = deepcopy(ull)
    current = cop2.head
    while current is not None:
        for i in range(len(current.array)):
            cop1 = cons(cop1, current.array[i])
        current = current.next
    return cop1
