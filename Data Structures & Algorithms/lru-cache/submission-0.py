class Node:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # key -> Node(value)
        self.cache = {} 
        # dummy left, right node
        self.left = Node(None, None, None, None)
        self.right = Node(None, None, None, None)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # connect node.prev, node.next
            self.remove(node)
            # node.prev.next = node.next
            # node.next.prev = node.prev

            # move node to right
            self.insert(node)
            # node.prev = self.right.prev
            # self.right.prev.next = node
            # node.next = self.right
            # self.right.prev = node
            return node.value
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else: 
            node = Node(key, value, None, None)
            self.insert(node)
            self.cache[key] = node

        if len(self.cache) > self.capacity:
            # remove left most node
            node_to_del = self.left.next
            self.remove(node_to_del)
            # delete key from cache
            del self.cache[node_to_del.key]
    
    def insert(self, node):
        # insert node to right most
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        # unlink node and connect its prev, next
        node.prev.next = node.next
        node.next.prev = node.prev
        

        
