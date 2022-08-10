# 707 - Design Linked List
# https://leetcode.com/problems/design-linked-list/


class Solution:

    # list the methods to be run against the test cases
    implementations = ["test_case_helper"]

    class MyLinkedList:
        class ListNode:
            def __init__(self, val):
                """Time: O(1)"""
                self.val = val
                self.next = None

        def __init__(self):
            """Time: O(1)"""
            self.prehead = self.ListNode("prehead")
            self.size = 0

        def get(self, index: int) -> int:
            """Time: O(n)"""
            # validate index
            if index < 0 or index >= self.size:
                return -1

            # traverse list up to desired node
            cur = self.prehead.next
            for _ in range(index):
                cur = cur.next
            return cur.val

        def addAtIndex(self, index: int, val: int) -> None:
            """Time: O(n)"""
            # validate index
            if index < 0 or index > self.size:
                return

            # find predecessor of node to be added
            pred = self.prehead
            for _ in range(index):
                pred = pred.next

            # insert new node after predecessor
            new = self.ListNode(val)
            new.next = pred.next
            pred.next = new
            self.size += 1

        def addAtHead(self, val: int) -> None:
            """Time: O(1)"""
            self.addAtIndex(0, val)

        def addAtTail(self, val: int) -> None:
            """Time: O(n)"""
            self.addAtIndex(self.size, val)

        def deleteAtIndex(self, index: int) -> None:
            """Time: O(n)"""
            # validate index
            if index < 0 or index >= self.size:
                return

            # find predecessor of node to be deleted
            pred = self.prehead
            for _ in range(index):
                pred = pred.next

            # delete node
            pred.next = pred.next.next
            self.size -= 1

    def test_case_helper(self, commands: list[str], args: list) -> list:
        """
        This function will execute the commands and collect the outputs used
        to evaluate the implementation of the LinkedList class
        """

        # first command is to initiate a LinkedList
        obj = self.MyLinkedList()
        outputs = [None]

        # execute remaining commands
        for i, command in enumerate(commands[1:]):
            func = getattr(obj, command)
            out = func(*args[i + 1])
            outputs.append(out)

        return outputs


# =============================== DRIVER CODE ================================

if __name__ == "__main__":

    from class_print_tests import PrintTests as PT

    # enter test cases: ['description', [inputs], expected_result]
    test_cases = [
        [
            "Example 1",
            [
                [
                    "MyLinkedList",
                    "addAtHead",
                    "addAtTail",
                    "addAtIndex",
                    "get",
                    "deleteAtIndex",
                    "get",
                ],
                [[], [1], [3], [1, 2], [1], [1], [1]],
            ],
            [None, None, None, None, 2, None, 3],
        ],
        [
            "Example 2",
            [
                [
                    "MyLinkedList",
                    "get",
                    "deleteAtIndex",
                    "deleteAtIndex",
                    "addAtIndex",
                    "addAtIndex",
                    "addAtHead",
                    "addAtIndex",
                ],
                [[], [1], [0], [1], [2, 1], [0, 0], [1], [3, 3]],
            ],
            [None, -1, None, None, None, None, None, None],
        ],
        [
            "More Complex",
            [
                [
                    "MyLinkedList",
                    "addAtHead",
                    "addAtHead",
                    "addAtHead",
                    "addAtIndex",
                    "deleteAtIndex",
                    "addAtHead",
                    "addAtTail",
                    "get",
                    "addAtHead",
                    "addAtIndex",
                    "addAtHead",
                ],
                [
                    [],
                    [7],
                    [2],
                    [1],
                    [3, 0],
                    [2],
                    [6],
                    [4],
                    [4],
                    [4],
                    [5, 0],
                    [6],
                ],
            ],
            [
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                4,
                None,
                None,
                None,
            ],
        ],
        [
            "Most Complex",
            [
                [
                    "MyLinkedList",
                    "addAtHead",
                    "addAtTail",
                    "addAtTail",
                    "get",
                    "get",
                    "addAtTail",
                    "addAtIndex",
                    "addAtHead",
                    "addAtHead",
                    "addAtTail",
                    "addAtTail",
                    "addAtTail",
                    "addAtTail",
                    "get",
                    "addAtHead",
                    "addAtHead",
                    "addAtIndex",
                    "addAtIndex",
                    "addAtHead",
                    "addAtTail",
                    "deleteAtIndex",
                    "addAtHead",
                    "addAtHead",
                    "addAtIndex",
                    "addAtTail",
                    "get",
                    "addAtIndex",
                    "addAtTail",
                    "addAtHead",
                    "addAtHead",
                    "addAtIndex",
                    "addAtTail",
                    "addAtHead",
                    "addAtHead",
                    "get",
                    "deleteAtIndex",
                    "addAtTail",
                    "addAtTail",
                    "addAtHead",
                    "addAtTail",
                    "get",
                    "deleteAtIndex",
                    "addAtTail",
                    "addAtHead",
                    "addAtTail",
                    "deleteAtIndex",
                    "addAtTail",
                    "deleteAtIndex",
                    "addAtIndex",
                    "deleteAtIndex",
                    "addAtTail",
                    "addAtHead",
                    "addAtIndex",
                    "addAtHead",
                    "addAtHead",
                    "get",
                    "addAtHead",
                    "get",
                    "addAtHead",
                    "deleteAtIndex",
                    "get",
                    "addAtHead",
                    "addAtTail",
                    "get",
                    "addAtHead",
                    "get",
                    "addAtTail",
                    "get",
                    "addAtTail",
                    "addAtHead",
                    "addAtIndex",
                    "addAtIndex",
                    "addAtHead",
                    "addAtHead",
                    "deleteAtIndex",
                    "get",
                    "addAtHead",
                    "addAtIndex",
                    "addAtTail",
                    "get",
                    "addAtIndex",
                    "get",
                    "addAtIndex",
                    "get",
                    "addAtIndex",
                    "addAtIndex",
                    "addAtHead",
                    "addAtHead",
                    "addAtTail",
                    "addAtIndex",
                    "get",
                    "addAtHead",
                    "addAtTail",
                    "addAtTail",
                    "addAtHead",
                    "get",
                    "addAtTail",
                    "addAtHead",
                    "addAtTail",
                    "get",
                    "addAtIndex",
                ],
                [
                    [],
                    [84],
                    [2],
                    [39],
                    [3],
                    [1],
                    [42],
                    [1, 80],
                    [14],
                    [1],
                    [53],
                    [98],
                    [19],
                    [12],
                    [2],
                    [16],
                    [33],
                    [4, 17],
                    [6, 8],
                    [37],
                    [43],
                    [11],
                    [80],
                    [31],
                    [13, 23],
                    [17],
                    [4],
                    [10, 0],
                    [21],
                    [73],
                    [22],
                    [24, 37],
                    [14],
                    [97],
                    [8],
                    [6],
                    [17],
                    [50],
                    [28],
                    [76],
                    [79],
                    [18],
                    [30],
                    [5],
                    [9],
                    [83],
                    [3],
                    [40],
                    [26],
                    [20, 90],
                    [30],
                    [40],
                    [56],
                    [15, 23],
                    [51],
                    [21],
                    [26],
                    [83],
                    [30],
                    [12],
                    [8],
                    [4],
                    [20],
                    [45],
                    [10],
                    [56],
                    [18],
                    [33],
                    [2],
                    [70],
                    [57],
                    [31, 24],
                    [16, 92],
                    [40],
                    [23],
                    [26],
                    [1],
                    [92],
                    [3, 78],
                    [42],
                    [18],
                    [39, 9],
                    [13],
                    [33, 17],
                    [51],
                    [18, 95],
                    [18, 33],
                    [80],
                    [21],
                    [7],
                    [17, 46],
                    [33],
                    [60],
                    [26],
                    [4],
                    [9],
                    [45],
                    [38],
                    [95],
                    [78],
                    [54],
                    [42, 86],
                ],
            ],
            [
                None,
                None,
                None,
                None,
                -1,
                2,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                84,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                16,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                37,
                None,
                None,
                None,
                None,
                None,
                23,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                19,
                None,
                17,
                None,
                None,
                56,
                None,
                None,
                31,
                None,
                17,
                None,
                12,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                40,
                None,
                None,
                None,
                37,
                None,
                76,
                None,
                42,
                None,
                None,
                None,
                None,
                None,
                None,
                80,
                None,
                None,
                None,
                None,
                43,
                None,
                None,
                None,
                40,
                None,
            ],
        ],
    ]

    # run test cases and print results using PrintTests class
    pt = PT(Solution(), test_cases)
    pt.run()
