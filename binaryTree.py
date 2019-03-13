import queue
class Node:
	def __init__(self,data=0):
		self.data = data
		self.left=None
		self.right=None
class BinaryTree:
	def __init__(self,root=None):
		self.root=root
	def levelOrder(self):
		result=[]
		if not self.root:
			return 
		q=queue.Queue()
		q.put(self.root)
		while not q.empty():
			node = q.get()
			result.append(node.data)
			if node.left:
				q.put(node.left)
			if node.right:
				q.put(node.right)
		return result
	def numberOfNode(self,root):
		if not root:
			return 0
		return self.numberOfNode(root.left) + self.numberOfNode(root.right) + 1
	def numberOfNode_itr(self,root):
		num=0
		if not root:
			return num
		q=queue.Queue()
		q.put(root)
		while not q.empty():
			node=q.get()
			#print(node.data)
			num=num+1
			if node.left:
				q.put(node.left)
			if node.right:
				q.put(node.right)
		return num
	def heightRec(self,root):
		if not root:
			return 0
		return max(self.heightRec(root.left),self.heightRec(root.right))+1
	def heightItr(self,root):
		if not root:
			return 0
		q=queue.Queue()
		q.put([root,1])
		depth=0
		while not q.empty():
			node,depth = q.get()
			tmp=depth
			if node.left:
				depth=depth+1
				q.put([node.left,depth])
			if node.right:
				if tmp==depth:
					depth=depth+1
				q.put([node.right,depth])
		return depth
	def zigzag(self,root):
		result=[]
		if not root:
			return
		stack=[]
		stack.append(root)
		lrFlag=False
		while len(stack) > 0:
			node = stack.pop()
			result.append(node.data)
			if not lrFlag:
				if node.left:
					stack.append(node.left)
				if node.right:
					stack.append(node.right)
				lrFlag=True
			else:
				if node.right:
					stack.append(node.right)
				if node.left:
					stack.append(node.left)
				lrFlag=False
		return result
	def leafNum(self,root):
		if not root:
			return 0
		if not root.left and not root.right:
			return 1
		return self.leafNum(root.left) + self.leafNum(root.right)
	def singleChild(self,root):
		if not root:
			return 0
		#print (root.data)
		if ((not root.left and root.right) or (not root.right and root.left)):
			return self.singleChild(root.left) + self.singleChild(root.right)+1
		return self.singleChild(root.left) + self.singleChild(root.right)
	def bothChild(self,root):
		if not root:
			return 0
		if (root.left and root.right):
			return self.bothChild(root.left) + self.bothChild(root.right) +1
		return self.bothChild(root.left) + self.bothChild(root.right)
			
if __name__=='__main__':
	fst=Node(1)
	snd=Node(2)
	fst.left=snd
	thrd=Node(3)
	fst.right=thrd
	frth=Node(4)
	fth=Node(5)
	sth=Node(6)
	svn=Node(7)
	eght=Node(8)
	nth=Node(9)
	snd.left=frth
	snd.right=fth
	thrd.left=sth
	thrd.right=svn
	fth.right=eght
	svn.left=nth
	nth.left=Node(10)
	nth.right=Node(12)
	nth.left.right=Node(11)
	tree=BinaryTree(fst)
	result=tree.levelOrder()
	print("printing levelOrder")
	print(result)
	print("printing number of node")
	num=tree.numberOfNode(tree.root)
	print(num)
	print("printing number of node by itr")
	num=tree.numberOfNode_itr(tree.root)
	print(num)
	print("printing heigth of tree by rec")
	num=tree.heightRec(tree.root)
	print(num)
	print("printing heigth of tree by itr")
	num=tree.heightItr(tree.root)
	print(num)
	print("printing hzigzag travarsal")
	num=tree.zigzag(tree.root)
	print(num)
	print("printing num of leafs recirsion")
	num=tree.leafNum(tree.root)
	print(num)
	print("printing single child recirsion")
	num=tree.singleChild(tree.root)
	print(num)
	print("printing both child recirsion")
	num=tree.bothChild(tree.root)
	print(num)
	