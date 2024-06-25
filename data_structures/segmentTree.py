# this data structure realizes operation of calculating sum of array[i], array[i+1], ... , array[j] elements
# in O(log n) time complexity

class SegmentTreeArraySum:
    def __init__(self, array) -> None:
        arrayLen = len(array)
        numberOfLeaves = 1
        while numberOfLeaves < arrayLen:
            numberOfLeaves <<= 1                # same as numberofleaves *= 2

        self.firstLeafIdx = numberOfLeaves - 1
        self.segmentTree = [0 for _ in range(2*numberOfLeaves - 1)]

        # copy values from original array and update tree O(n log n)
        for i in range(arrayLen):
            self.update(i, array[i])

    def update(self, idx, val):
        idx += self.firstLeafIdx
        difference = val - self.segmentTree[idx]
        self.segmentTree[idx] = val

        while 0 < idx:
            idx = (idx - 1) // 2
            self.segmentTree[idx] += difference

    def get_sum(self, beg, end):
        def inner(currentNode, nodeBeg, nodeEnd):
            if end < nodeBeg or nodeEnd < beg:
                return 0
            if beg <= nodeBeg and nodeEnd <= end:
                return self.segmentTree[currentNode]
            
            mid = (nodeBeg + nodeEnd) // 2
            left = 2*currentNode + 1
            right = 2*currentNode + 2
            return inner(left, nodeBeg, mid) + inner(right, mid + 1, nodeEnd)
        return inner(0, 0, self.firstLeafIdx)
    
    #########################
    # visualization purpose #
    #########################

    def print_layers(self):
        layer = 0
        firstElementOnLayer = 0
        while firstElementOnLayer < len(self.segmentTree):
            print(f"layer {layer}:")
            for i in range(firstElementOnLayer, 2*firstElementOnLayer + 1):
                print(self.segmentTree[i], end=" ")
            layer += 1
            firstElementOnLayer = 2*firstElementOnLayer + 1
            print()


    def __repr__(self) -> str:
        return f"SegTree({self.segmentTree})"

def test_array_sum(array, beg, end):
    global testCnt
    testCnt += 1
    print(f"\n\n######## test {testCnt} ########\n\n")
    segTree = SegmentTreeArraySum(array)
    print(segTree)
    segTree.print_layers()
    print()
    print(f"sum of array[{i}], ... ,array[{j}]:")
    print(" - segTree sum:", segTree.get_sum(beg, end))
    print(" - correct sum:", sum(array[beg:end+1]))

if __name__ == "__main__":
    testCnt = 0
    array = [1,5,3,7]
    i = 1
    j = 3
    test_array_sum(array, i, j)

    array = [1,5,3,7,7,4,3,1,2,3,8]
    i = 2
    j = 7
    test_array_sum(array, i, j)

    print("\n\n######## update test ########\n\n")
    array = [1,5,3,7]
    segTree = SegmentTreeArraySum(array)
    print(segTree)
    segTree.print_layers()
    i = 1
    j = 3
    print(f"sum of array[{i}], ... ,array[{j}]: {segTree.get_sum(i, j)}")
    segTree.update(3, 2)
    print("\nafter update:\n")
    print(segTree)
    segTree.print_layers()
    print(f"sum of array[{i}], ... ,array[{j}]: {segTree.get_sum(i, j)}")
