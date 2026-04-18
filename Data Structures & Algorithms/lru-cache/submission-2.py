class Node:
    def __init__(self, key=-1, val=-1):
        self.val=val
        self.prev=None
        self.next=None
        self.key=key
class LRUCache:
    def __init__(self, capacity: int):
        self.key_value={}
        self.capacity=capacity
        self.tail=Node()
        self.head=Node()
        self.tail.prev=self.head
        self.head.next=self.tail
        self.cur_capacity=0
    def get(self, key: int) -> int:
        if(key not in self.key_value):
            return -1 
        else:
            self.update_front(key)
            print(self.key_value[key].val)
            return self.key_value[key].val
    def put(self, key: int, value: int) -> None:
        if(self.cur_capacity==self.capacity and key not in self.key_value):
            self.cur_capacity-=1
            self.delete_last_node()
        if(key in self.key_value):
            self.update_front(key)
            self.key_value[key].val=value
            return 
        update_node=Node(key, value)
        head_next=self.head.next
        head_next.prev=update_node
        update_node.next=head_next
        self.head.next=update_node
        update_node.prev=self.head
        self.key_value[key]=update_node
        self.cur_capacity+=1
    def update_front(self, key):
        update_node=self.key_value[key]
        update_node.prev.next=update_node.next
        update_node.next.prev=update_node.prev
        head_next=self.head.next
        head_next.prev=update_node
        update_node.next=head_next
        self.head.next=update_node
        update_node.prev=self.head
    def delete_last_node(self):
        delete_node=self.tail.prev
        del self.key_value[delete_node.key]
        delete_node.prev.next=self.tail
        self.tail.prev=delete_node.prev

