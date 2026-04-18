* Binary Tree Data Structure Code:


Class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None


root = Node(15)
secondNode = Node(35)
thirdNode = Node(40)
fourthNode = Node(3)
FifthNode = Node(6)
SixthNode = Node(5)
SeventhNode = Node(7)
EigthNode = Node(1)
NinthNode = Node(10)
TenthNode = Node(8)
EleventhNode = Node(41)


root.left = secondNode
root.right = thirdNode
root.left.left = fourthNode 
root.left.right = FifthNode
root.right.left = SixthNode
root.right.right = SeventhNode
root.left.left.left = EigthNode
root.left.left.right = NinthNode
root.right.left.left = TenthNode
root.right.left.right = EleventhNode



* Shell Sort Algorithm Code:


def shell_sort(arr):
    size = len(arr)
    gap = size // 2


    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


if __name__ == '__main__':
    list = [61, 9, 62, 83, 37, 80, 32, 45, 93]
    shell_sort(list)
    print(list)
