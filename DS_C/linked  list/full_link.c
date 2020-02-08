//insert node at nth location of the list/*
/*

            _________                     ___________
            |   |   |                     |     |    |
            |___|___| ---              |--|_____|____|
                         |             ----------          
                         |      ____________    | 
                         |      |     |    |    |
                          ------|_____|____|----
                            
*/
#include<stdlib.h>
#include<stdio.h>

struct node
{
      int data;
      struct node *link;
};
struct node* start=NULL;
struct node* createnode()
{
      struct node* tmp;
      tmp=(struct node*)malloc(sizeof(struct node*));
      return tmp;
}

void insert(int pos)
{
      struct node* tmp,*search;
      int n,i;
      tmp=createnode();
      printf("\n Enter number to be insert :");
      scanf("%d",&n);
      tmp->data=n;
      tmp->link=NULL;
      if(pos==1)
      {
            tmp->link=start;
            start=tmp;
            return;
      }
            search=start;
            for(i=1;i<pos-1;i++)//actually i=n-2 explain below
            {
                  search=search->link;//to get n-1 node 
            }
            tmp->link=search->link; //In new node link store the adress of nth node
            search->link=tmp; //store adress of new node in nth location
      
}               

void delete(int pos)
{
      
      struct node* tmp,*search;
      int n,i;
      tmp=start;
      if(pos==1)
      {
            start=tmp->link;
            free(tmp);
            return;
      }
            search=start;
            for(i=1;i<pos-1;i++)
            {
                  search=search->link;//to get n-1 node 
            }
            tmp=search->link; //point to the nth node means it become nth node
            search->link=tmp->link;//n-1th node point to n+1 th node
            free(tmp); 
}

void dis()
{
            struct node* tmp1;
            tmp1=start;
            printf("\n List is : ");
            while(tmp1!=NULL)
            {
                  printf("%3d",tmp1->data);
                  tmp1=tmp1->link;
            }
}               

int main()
{
      int ch,pos;
      //cnt=0;
      while(1)
      {
            printf("\n\n******** Enter your choice********* :");
            printf("\n\t 1. INSERT \n\t 2. DELETE \n\t 3. DISPLAY \n\t 4. EXIT");
            printf("\n Enter Your Choice :...");
            scanf("%d",&ch);
            if(ch>3)
            break;
            switch(ch)
            {
                  case 1:
                        printf("\t\t Enter the location at which you want to insert node :");      
                        scanf("%d",&pos);
                        insert(pos);
                        break;
                  case 2:
                        printf("\t\t Enter the location of the node which you want to delete :"); 
                        scanf("%d",&pos);
                        delete(pos);
                        break;      
                  case 3:
                        dis();
                        break;      
            }
     }       
      return 0;
}



/*           
  while (!n-2)means  3   and tmp is at n-1 location and point to the nth location
      tmp=tmp->nxt          
                       1            2          3            4              5   
                 __________   _________   _________    _________    ____________
                 |    |    |   |   |   |   |   |   |    |   |   |   |     |     |
                 |____|____|   |___|___|   |___|___|    |___|___|   |_____|_____|

                                    1~         2~           3~          
*/









