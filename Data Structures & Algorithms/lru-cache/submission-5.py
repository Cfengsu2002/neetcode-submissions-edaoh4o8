class Node:
    def __init__(self, value=-1, key=-1):
        self.value=value
        self.key=key
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.L=Node()
        self.R=Node()
        self.L.next=self.R
        self.R.prev=self.L
        self.capacity=capacity
        self.listnodes={}
    def get(self, key: int) -> int:
        if key not in self.listnodes:
            return -1
        else:
            self.update(key, self.listnodes[key].value)
            return self.listnodes[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.listnodes:
            self.update(key, value)
            return
        node=Node(value, key)
        self.L.next.prev=node
        node.next=self.L.next
        self.L.next=node
        node.prev=self.L
        self.listnodes[key]=node
        if(len(self.listnodes)>self.capacity):
            key=self.listnodes[self.R.prev.key]
            self.listnodes[key.key].prev.next=self.listnodes[key.key].next
            self.listnodes[key.key].next.prev=self.listnodes[key.key].prev
            del self.listnodes[key.key]
        return

    def update(self, key, value):
        node=self.listnodes[key]
        node.prev.next=node.next
        node.next.prev=node.prev
        self.L.next.prev=node
        node.next=self.L.next
        node.prev=self.L
        self.L.next=node
        node.value=value
