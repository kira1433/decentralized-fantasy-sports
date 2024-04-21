import hashlib

class Node:
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val

class MerkleTree:
    def __init__(self, trans):
        self.root = None
        self.createTree(trans)

    @staticmethod
    def hash(val):
        return hashlib.sha256(val.encode('utf-8')).hexdigest()

    def createTree(self, trans):
        leafArray = []
        for i in trans:
            leafArray.append(i)

        if len(trans) % 2 != 0:
            leafArray.append(leafArray[-1])  # important, would mess up without copy

        self.root = self.rec_build(leafArray)

    def rec_build(self, leafArray):
        if len(leafArray) % 2 != 0:
            leafArray.append(leafArray[-1])

        if len(leafArray) == 2:
            return Node(left=leafArray[0], right=leafArray[1], val=MerkleTree.hash(leafArray[0].transaction_hash + leafArray[1].transaction_hash))

        left = self.rec_build(leafArray[len(leafArray) // 2:])
        right = self.rec_build(leafArray[:len(leafArray) // 2])
        value = self.hash(left.val + right.val)
        return Node(left, right, value)

    def getRoot(self):
        return self.root.val