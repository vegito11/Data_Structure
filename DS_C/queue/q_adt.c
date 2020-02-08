#include<stdio.h>
#include<stdlib.h>
struct queue
{
      int data;
      struct queue *link;
};
struct queue *start=NULL;

void ENQUEUE()
{     
      int no;
      struct queue *tmp,*t;
      tmp=(struct queue*)malloc(sizeof(struct queue*));
      printf("\n Enter no to be insert : ");
      scanf("%d",&no);
      tmp->data=no;
      tmp->link=NULL;
      if(start==NULL)
      {
            start=tmp;
      }
      else
      {
            t=start;
            while(t->link!=NULL)
            {
                  t=t->link;
            }
            t->link=tmp;
      }
}

void DEQUEUE()
{
      struct queue* tmp;
      if(start==NULL)
      {
            printf("\n List is empty !!!!Please insert some data!!!!");
            return;
      }
      else
      {
            tmp=start;
            start=start->link;
            printf("\n %d This no is deleted from Queue!!!!!!!!",tmp->data);
            free(tmp);
      }
}

void dis()
{
      struct queue* tmp;
      if(start==NULL)
      {
            printf("\n List is empty !!!!Please insert some data!!!!");
            return;
      }
      else
      {
            tmp=start;
            while(tmp!=NULL)
            {
                  printf("%5d",tmp->data);
                  tmp=tmp->link;
            }
      }      
}

int main()
{
      int ch;
      //cnt=0;
      while(1)
      {
            printf("\n\n******** Enter your choice********* :\n\t 1. ENQUEUE \n\t 2. DEQUEUE \n\t 3. DISPLAY \n\t 4. EXIT");
            printf("\n Enter Your Choice :...");
            scanf("%d",&ch);
            if(ch>3)
            break;
            switch(ch)
            {
                  case 1:
                        ENQUEUE();
                        break;
                  case 2:
                        DEQUEUE();
                        break;      
                  case 3:
                        dis();
                        break;      
            }
     }       
      return 0;
}

