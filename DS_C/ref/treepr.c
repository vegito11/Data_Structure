#include<stdio.h>
#include<stdlib.h>

struct tree
{
      int data;
      struct tree*left,*right;
};

struct tree* createnode(int n)
{
      struct tree* tmp;
      tmp=(struct tree*)malloc(sizeof(struct tree));
      tmp->left=NULL;
      tmp->right=NULL;
      tmp->data=n;
      return tmp;
}
struct tree* insert(struct tree *root,int n)
{
      
      if(root==NULL)
      {
            root=createnode(n);
            return root;
      }
      else if(n<root->data)
      {
            root->left=insert(root->left,n);
      }
      else if(n>root->data)
      {
            root->right=insert(root->right,n);
      }
      return root;
}

void preorder(struct tree* root)
{
      if(root==NULL)
      {
            return ;
      }
      printf("%5d",root->data);
      preorder(root->left);
      preorder(root->right);
}

void inorder(struct tree* root)
{
      if(root==NULL)
      {
            return ;
      }
      inorder(root->left);
      printf("%5d",root->data);
      inorder(root->right);
}

void postorder(struct tree* root)
{
      if(root==NULL)
      {
            return ;
      }
      postorder(root->left);                //printf the left most node  then go to last nodes left empty so go to root data
      postorder(root->right);              //then back to n-1 node print n-1 node left and then right data back so on
      printf("%5d",root->data);
}
int  findmax(struct tree*root)
{
      struct tree* current;
      int maxi;
      current=root;
      while(current->right!=NULL)
      current=current->right;
      return current->data;
}
struct tree* delete(struct tree*root,int n)
{
      struct tree*tmp,t;
      if(root==NULL)
            printf("\n !!!!! NO such element exists !!!!");
      else if(n<root->data)
            root->left=delete(root->left,n);
      else if(n>root->data)
            root->right=delete(root->right,n);
      else
      {
            if(root->left&&root->right)
            {
                  root->data=findmax(root->left);               //here root is location which we want to delete
                  delete(root->left,root->data);               //delete replaced number
            }
            else
            {
                  tmp=root;
                  if(root->left==NULL&&root->right==NULL)
                  {
                        free (tmp);
                        tmp=NULL;
                  }      
                  else if(root->right=NULL)
                        root=root->left;
                  else if(root->left=NULL)
                        root=root->right;
            }
      }
      return root;
}
int main()
{
      struct tree* root=NULL;
      int n;      
      int ch,che;
      while(1)
      {
            printf("\n\n******** Enter your choice********* :\n\t 1. INSERT \n\t 2. DELETE \n\t 3. TRAVERSAL \n\t 4. COUNT \n\t 5. EXIT");
            printf("\n Enter Your Choice :...");
            scanf("%d",&ch);
            if(ch>4)
            break;
            switch(ch)
            {
                  case 1 :
                         printf("\n Enter data to be insert :");
                         scanf("%d",&n);
                         root=insert(root,n);
                         break;
                  case 2 :
                         printf("\n Enter Number to be delete :");
                         scanf("%d",&n);
                         delete(root,n);
                         break;      
                  case 3 :
                         if(root==NULL)
                         printf("\n !!!!!!TREE is Empty!!!!!!!");
                         else
                         {
                               printf("\n\n\t******** Enter your choice********* :\n\t 1. Preorder \n\t 2. Postorder \n\t 3. Inorder \n\t ");
                               printf("\n Enter Your Choice :...");
                               scanf("%d",&che);
                               switch(che)
                               {
                                    case 1:
                                          printf("\n Preorder traversal is :");
                                          preorder(root);
                                          break;
                                    case 2:
                                          printf("\n Preorder traversal is :");
                                          postorder(root);
                                          break;
                                    case 3:
                                          printf("\n Preorder traversal is :");
                                          inorder(root);
                                          break;
                               }      
                         }
                         break;      
                  case 4 :
                        //count();
                        break;
                  
            }
      
      }
      return 0 ;
}            
