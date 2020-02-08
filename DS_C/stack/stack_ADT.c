//stack adt
#include<stdio.h>
#include<stdlib.h>

struct node
{
      int data;
      struct node* link;
};
struct node* start=NULL;

struct node* createnode()
{
      struct node* tmp1;
      tmp1=(struct node*)malloc(sizeof(struct node*));
      return tmp1;
}

void push()
{
      int n;
      struct node* tmp,*search;
      tmp=createnode();
      printf("\n Enter data to be Pushed :");
      scanf("%d",&n);
      tmp->data=n;
      tmp->link=NULL;
      if(start==NULL)
      {
            start=tmp;
            return;
      }
      else
      {
            tmp->link=start;
            start=tmp;     
      }
}

void pop()
{
      struct node* tmp,*search;
      tmp=start;
      if(start==NULL)
      {
            printf("\n List is empty !!!!Please insert some data!!!!");
            return;
      }
      start=start->link;
      printf("\n %d Number is deleted from the list",tmp->data);
      free(tmp);
}

void dis()
{
      struct node* tmp;
      tmp=start;
      if(start==NULL)
      {
            printf("\n List is empty !!!!Please insert some data!!!!");
            return;
      }
      printf("\n List is :");
      while(tmp!=NULL)
      {
            printf("\n%3d",tmp->data);
            tmp=tmp->link;
      }
}

int main()
{
      int ch,pos;
      //cnt=0;
      while(1)
      {
            printf("\n\n******** Enter your choice********* :\n\t 1. PUSH \n\t 2. POP \n\t 3. DISPLAY \n\t 4. EXIT");
            printf("\n Enter Your Choice :...");
            scanf("%d",&ch);
            if(ch>3)
            break;
            switch(ch)
            {
                  case 1:
                        push();
                        break;
                  case 2:
                        pop();
                        break;      
                  case 3:
                        dis();
                        break;      
            }
     }       
      return 0;
}

/* output :

******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter data to be Pushed :44


******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter data to be Pushed :33


******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter data to be Pushed :22


******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter data to be Pushed :11


******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...3

 List is :
 11
 22
 33
 44

******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...2

 11 Number is deleted from the list

******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...3

 List is :
 22
 33
 44

******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...
*/
