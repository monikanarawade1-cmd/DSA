Implement binary search tree and perform following operations:
a) Insert (Handle insertion of duplicate entry) 
b) Delete 
c) Search 
d) Display tree (Traversal) 
e) Display - Depth of tree 
f) Display - Mirror image 
g) Create a copy 
h) Display all parent nodes with their child nodes 
i) Display leaf nodes 
j) Display tree level wise

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert (ignore duplicates)
    def insert(self, root, val):
        if not root:
            return Node(val)
        if val < root.data:
            root.left = self.insert(root.left, val)
        elif val > root.data:
            root.right = self.insert(root.right, val)
        else:
            print("Duplicate ignored!")
        return root

    def insert_val(self, val):
        self.root = self.insert(self.root, val)

    # Delete
    def delete(self, root, val):
        if not root: return None
        if val < root.data:
            root.left = self.delete(root.left, val)
        elif val > root.data:
            root.right = self.delete(root.right, val)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def delete_val(self, val):
        self.root = self.delete(self.root, val)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    # Search
    def search(self, root, val):
        if not root: return False
        if root.data == val: return True
        return self.search(root.left, val) if val < root.data else self.search(root.right, val)

    def search_val(self, val):
        print("Found" if self.search(self.root, val) else "Not Found")

    # Inorder Traversal
    def inorder(self, root):
        return self.inorder(root.left) + [root.data] + self.inorder(root.right) if root else []

    # Depth of tree
    def depth(self, root):
        return 1 + max(self.depth(root.left), self.depth(root.right)) if root else 0

    # Mirror image
    def mirror(self, root):
        if not root: return None
        mirrored = Node(root.data)
        mirrored.left = self.mirror(root.right)
        mirrored.right = self.mirror(root.left)
        return mirrored

    # Copy tree
    def copy_tree(self, root):
        if not root: return None
        new_root = Node(root.data)
        new_root.left = self.copy_tree(root.left)
        new_root.right = self.copy_tree(root.right)
        return new_root

    # Parents with their children
    def show_parents(self, root):
        if root:
            if root.left: print(f"Parent {root.data} -> Left {root.left.data}")
            if root.right: print(f"Parent {root.data} -> Right {root.right.data}")
            self.show_parents(root.left)
            self.show_parents(root.right)

    # Leaf nodes
    def show_leaves(self, root):
        if root:
            if not root.left and not root.right: print(root.data, end=" ")
            self.show_leaves(root.left)
            self.show_leaves(root.right)

    # Level-wise display
    def level_order(self):
        if not self.root: return
        q = [self.root]
        while q:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        print()

# ---- Menu Driven Example ----
bst = BST()
while True:
    print("\n1.Insert 2.Delete 3.Search 4.Display 5.Depth 6.Mirror 7.Copy 8.Parents 9.Leaves 10.Level 11.Exit")
    choice = int(input("Choice: "))
    if choice == 1: bst.insert_val(int(input("Value: ")))
    elif choice == 2: bst.delete_val(int(input("Value: ")))
    elif choice == 3: bst.search_val(int(input("Value: ")))
    elif choice == 4: print("Inorder:", bst.inorder(bst.root))
    elif choice == 5: print("Depth:", bst.depth(bst.root))
    elif choice == 6: print("Mirror Inorder:", bst.inorder(bst.mirror(bst.root)))
    elif choice == 7: print("Copy Inorder:", bst.inorder(bst.copy_tree(bst.root)))
    elif choice == 8: bst.show_parents(bst.root)
    elif choice == 9: print("Leaf nodes:", end=" "); bst.show_leaves(bst.root); print()
    elif choice == 10: print("Level Order:"); bst.level_order()
    elif choice == 11: break


OUTPUT:
1.Insert 2.Delete 3.Search 4.Display 5.Depth 6.Mirror 7.Copy 8.Parents 9.Leaves 10.Level 11.Exit
Choice: 1
Value: 50
1.Insert 2.Delete 3.Search 4.Display 5.Depth 6.Mirror 7.Copy 8.Parents 9.Leaves 10.Level 11.Exit
Choice: 1
Value: 30
1.Insert 2.Delete 3.Search 4.Display 5.Depth 6.Mirror 7.Copy 8.Parents 9.Leaves 10.Level 11.Exit
Choice: 1
Value: 70
1.Insert 2.Delete 3.Search 4.Display 5.Depth 6.Mirror 7.Copy 8.Parents 9.Leaves 10.Level 11.Exit
Choice: 1
Value: 20
1.Insert 2.Delete 3.Search 4.Display 5.Depth 6.Mirror 7.Copy 8.Parents 9.Leaves 10.Level 11.Exit
Choice: 1
Value: 40
1.Insert 2.Delete 3.Search 4.Display 5.Depth 6.Mirror 7.Copy 8.Parents 9.Leaves 10.Level 11.Exit
Choice: 4
Inorder: [20, 30, 40, 50, 70]

Choice: 3
Value: 40
Found

Choice: 3
Value: 90
Not Found

Choice: 5
Depth: 3

Choice: 6
Mirror Inorder: [70, 50, 40, 30, 20]

Choice: 7
Copy Inorder: [20, 30, 40, 50, 70]

Choice: 8
Parent 50 -> Left 30
Parent 50 -> Right 70
Parent 30 -> Left 20
Parent 30 -> Right 40

Choice: 9
Leaf nodes: 20 40 70 

Choice: 10
Level Order:
50 30 70 20 40 

Choice: 11
