class BSTNode:
    def __init__(self, distancia=None, ciudad1=None, ciudad2=None):
        self.left = None
        self.right = None
        self.distancia = distancia
        self.ciudad1 = ciudad1
        self.ciudad2 = ciudad2

    def insert(self, distancia, ciudad1, ciudad2):
        if not self.distancia:
            self.distancia = distancia
            self.ciudad1 = ciudad1
            self.ciudad2 = ciudad2
            return
        if self.distancia == distancia:
            return
        if distancia < self.distancia:
            if self.left:
                self.left.insert(distancia, ciudad1, ciudad2)
                return
            self.left = BSTNode(distancia, ciudad1, ciudad2)
            return

        if distancia > self.distancia:
            if self.right:
                self.right.insert(distancia, ciudad1, ciudad2)
                return
            self.right = BSTNode(distancia, ciudad1, ciudad2)
            return

    def inorder_traversal(self):
        result = []
        if self.left:
            result += self.left.inorder_traversal()
        result.append((self.distancia, self.ciudad1, self.ciudad2))
        if self.right:
            result += self.right.inorder_traversal()
        return result
