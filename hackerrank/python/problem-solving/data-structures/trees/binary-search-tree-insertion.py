   def insertion(self, cur, val):
        if not cur:
            cur = Node(val)
        elif cur.info > val:
            cur.left = self.insertion(cur.left, val)
        else:
            cur.right = self.insertion(cur.right, val)

        return cur

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.insertion(self.root, val)
