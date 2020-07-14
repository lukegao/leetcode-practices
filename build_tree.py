

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s = ''
        if root is None:
            return s + 'a '

        s += f"{root.val} "

        s += self.serialize(root.left)
        s += self.serialize(root.right)
        return s

    def build(self, val_list):
        if len(val_list) == 0:
            return None

        val = val_list[0]
        val_list.pop(0)

        if val is 'a':
            return None
        else:
            val = int(val)

        node = TreeNode(val)
        node.left = self.build(val_list)
        node.right = self.build(val_list)

        print(node.val)

        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dl = data.split()

        print(dl)

        node = self.build(dl)
        return node


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()

    s = codec.serialize(root)
    print(s)

    node = codec.deserialize(s)
