#include <stdio.h>
#include <stdlib.h>
struct node
{
	int data;
	struct node* left;
	struct node* right;
};
struct node* createNode()
{
	struct node* tmp;
	tmp = (struct node*)malloc(sizeof(struct node*));
	tmp->left=NULL;
	tmp->right=NULL;
	return tmp;
}
int stack[100];
int top=0;
void push(int data)
{
	if(top+1 ==100)
	{
		printf("\n !!! Stack is Full !!!!");
	}	
	stack[top++] = data;
}
int pop()
{
	int tmp;
	if(top==-1)
	{
		return -1;
	}	
	else
		return stack[top--];
	return tmp;
}
struct node* insert(struct node* root,int data)
{
	struct node* tmp;
	if(root==NULL)
	{
	    //  printf("enter");
	      root=createNode();
	      root->data=data;
	      return root;
	}
	else if(root->data>data)
		root->left = insert(root->left,data);
	else if(root->data<=data)
	{	
		root->right = insert(root->right,data);
	}	
	return root;
}
void inorder(struct node* root)
{
	if(root!=NULL)
	{
		inorder(root->left);
		printf("%5d",root->data);
		inorder(root->right);		
	}	

}
void preorder(struct node* root)
{
	if(root!=NULL)
	{	
		printf("%5d",root->data);
		preorder(root->left);
		preorder(root->right);
	
	}	

}
void postorder(struct node* root)
{
	if(root!=NULL)
	{		
		postorder(root->left);
		postorder(root->right);
		printf("%5d",root->data);
	}	

}
void leveOrder(struct node* root)
{
	while()
}
int main(int argc, char const *argv[])
{
	int i,cnt,ch,n;
	struct node* root = NULL;
	while(1)	
	{
		printf("\n********* Menu *********");
		printf("\n\t\t 1) Add Node \n\t\t 2) Inorder \n\t\t 3) Preorder \n\t\t 4) PostOrder \n\t\t 5) Delete ");
		printf("\n\t\t\t Enter your Choice : ");
		scanf("%d",&ch);
		printf("\n**************************************************************************\n");
		switch(ch)
		{
			case 1:
					insert(root,10);
					printf("\n Enter the Data to Insert :");
					scanf("%d",&n);
					root = insert(root,n);
					root = insert(root,8);
					root = insert(root,4);
					root = insert(root,9);
					root = insert(root,21);
					root = insert(root,58);
					break;
			case 2:
			      	printf("\n Inorder Traversal Of given Tree is  :");	
			      	inorder(root);
			      	break;		
			case 3:
			      	printf("\n PreOrder Traversal Of given Tree is  :");	
			      	preorder(root);
			      	break;		
			case 4:
			      	printf("\n Postorder Traversal Of given Tree is  :");	
			      	postorder(root);
			      	break;		
		}

	}	
	return 0;
}