class ListNode:
    def __init__(self, key: int, val: int) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.previous = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lp = ListNode(0, 0)
        self.rp = ListNode(0, 0)
        self.hash_map = {}
        self.lp.next = self.rp
        self.rp.previous = self.lp

    def remove(self, node):
        prev_node = node.previous
        next_node = node.next
        prev_node.next = next_node
        next_node.previous = prev_node

    def insert(self, node):
        mru = self.rp.previous
        mru.next = node
        self.rp.previous = node
        node.next = self.rp
        node.previous = mru

    def get(self, key: int) -> int:
        current_node = self.hash_map.get(key)
        if current_node:
            self.remove(current_node)
            self.insert(current_node)
            return current_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        current_node = self.hash_map.get(key)
        if current_node:
            current_node.val = value
            self.remove(current_node)
            self.insert(current_node)
        else:
            new_node = ListNode(key, value)
            self.insert(new_node)
            self.hash_map[key] = new_node
            if len(self.hash_map) > self.capacity:
                del self.hash_map[self.lp.next.key]
                self.remove(self.lp.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
