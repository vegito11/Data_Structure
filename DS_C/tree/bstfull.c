#include<stdio.h>
#include<stdlib.h>

struct node 
{
      int data;
      struct node *left,*right; 
};
struct node* createnode()
{
      struct node*tmp=(struct node* )malloc(sizeof(struct node));      
      tmp->left=NULL;
      tmp->right=NULL;
      return tmp;
}

struct node* insert(struct node* root,int n)
{
      struct node *tmp;
      if(root==NULL)
      {
          //  printf("enter");
            root=createnode();
            root->data=n;
            return root;
      }
      else if(n<=root->data)
      {
           // printf("enter1");
            root->left=insert(root->left,n);
      }
      else if(n>root->data)
      {
          //  printf("enter2");
            root->right=insert(root->right,n);
      }
      return root;
}

void preorder(struct node*root)
{
      if(root!=NULL)
      {
            printf("%3d",root->data);
            preorder(root->left);
            preorder(root->right);
      }
}
void inorder(struct node*root)
{
      if(root!=NULL)
      {
            inorder(root->left);
            printf("%3d",root->data);
            inorder(root->right);
      }
}
void postorder(struct node*root)
{
      if(root!=NULL)
      {
            postorder(root->left);
            postorder(root->right);
            printf("%3d",root->data);
      }
}
int max(struct node* root)
{
      struct node* current;
      int maxi;
      while(current->right!=NULL)
      current=current->right;
      return current->data;
}
struct node* delete(struct node* root,int n)
{
      struct node*tmp;
      if(root==NULL)
      printf("\n No such element exit :");
      else if(n<root->data)
                  root->left=delete(root->left,n);
      else if(n>root->data)
                  root->right=delete(root->right,n);
            else
            {
                  if(root->left&&root->right)
                  {
                        
                        root->data=max(root->left);
                        root->left=delete(root->left,root->data);
                  }
                  else                        
                  {    
                        tmp=root;
                        if(root->left==NULL&root->right==NULL)
                        {
                              free(tmp);
                        }
                        else if(root->left==NULL)
                          root=root->right;
                        else if(root->right==NULL)
                          root=root->left;
                          free(tmp);
                  }                          
            }
      return root;
}

int main()
{
      struct node* root=NULL;
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
                               printf("\n\n\t******** Traversal Option********* :\n\t 1. Preorder \n\t 2. Postorder \n\t 3. Inorder \n\t ");
                               printf("\n\t\t Enter Your Traversal : ");
                               scanf("%d",&che);
                               switch(che)
                               {
                                    case 1:
                                          printf("\n Preorder traversal is :");
                                          preorder(root);
                                          break;
                                    case 2:
                                          printf("\n Postorder traversal is :");
                                          postorder(root);
                                          break;
                                    case 3:
                                          printf("\n Inorder traversal is :");
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
