class MaxSum {
	public static void main(String[] args)
	{
		TreeNode root = createTree();
		TreeSum maxSum = findMaxSum(root);
		System.out.println(Math.max(maxSum.maxSumBetweenTwoNodes, maxSum.maxSumFromRootToLeaf));
	}

	private static class TreeNode
	{
	        private int data;
        	private TreeNode left;
	        private TreeNode right;

	        public int getData()
        	{
	            return data;
        	}

	        public TreeNode getLeft()
        	{
	            return left;
        	}

	        public TreeNode getRight()
        	{
	            return right;
        	}

	        public TreeNode(int data)
        	{
	            this.data = data;
        	    left = null;
	            right = null;
        	}

	        public void setLeft(TreeNode left)
        	{
	            this.left = left;
        	}

	        public void setRight(TreeNode right)
        	{
	            this.right = right;
        	}
	}

	private static TreeNode createTree()
	{
	        TreeNode root = new TreeNode(75);
        	root.setLeft(new TreeNode(95));
	        root.setRight(new TreeNode(64));

        	root.getLeft().setLeft(new TreeNode(17));
	        root.getLeft().setRight(new TreeNode(47));

        	return root;
	}

	private static class TreeSum
	{
        	private int maxSumBetweenTwoNodes;
	        private int maxSumFromRootToLeaf;

        	public TreeSum(int maxSumBetweenTwoNodes, int maxSumFromRootToLeaf)
	        {
        		this.maxSumBetweenTwoNodes = maxSumBetweenTwoNodes;
			this.maxSumFromRootToLeaf = maxSumFromRootToLeaf;
		}
	}

	private static TreeSum findMaxSum(TreeNode root)
	{
		if (root == null)
		{
        		return new TreeSum(0, 0);
		}
	        TreeSum leftTreeSum = findMaxSum(root.getLeft());
        	TreeSum rightTreeSum = findMaxSum(root.getRight());
	        int maxSumBetweenTwoNodesOfChildren = Math.max(leftTreeSum.maxSumBetweenTwoNodes, rightTreeSum.maxSumBetweenTwoNodes);

		maxSumBetweenTwoNodesOfChildren = Math.max(maxSumBetweenTwoNodesOfChildren, leftTreeSum.maxSumFromRootToLeaf
                        + rightTreeSum.maxSumFromRootToLeaf + root.getData());

	        int maxSumFromRootToLeaf = leftTreeSum.maxSumFromRootToLeaf > rightTreeSum.maxSumFromRootToLeaf
                        ? leftTreeSum.maxSumFromRootToLeaf + root.getData()
                        : rightTreeSum.maxSumFromRootToLeaf + root.data;

		return new TreeSum(maxSumBetweenTwoNodesOfChildren, maxSumFromRootToLeaf);
	}
}
