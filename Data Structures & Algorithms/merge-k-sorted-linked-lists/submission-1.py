class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.merge_list(list1, list2))
            lists = merged
        return lists[0]

    def merge_list(self, ptr1, ptr2):
        dummy = ListNode()
        tail = dummy
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next
        tail.next = ptr1 or ptr2
        return dummy.next