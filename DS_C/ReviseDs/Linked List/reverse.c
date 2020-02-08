//gcc ll1.c  -lm
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
struct list
{
	int data;
	struct list *next;
};
struct list* createNode()
{
	struct list *tmp;
	tmp = (struct list*)malloc(sizeof(struct list));
	tmp->next = NULL;
	return tmp;
}
int cnt=0;

struct list* insert(struct list* start, int n)
{
	int ch,i,pos;
	struct list* tmp,*search;
	
	tmp=createNode();
	if(start==NULL)
	{
		tmp->data=n;
	    start=tmp;
	    cnt++;
	    return start;
	}
	else
	{	
		tmp->data=n;
		search = start;
		while(search->next!=NULL)
		{
			search = search->next;
		}	
		search->next=tmp;		
	}
	cnt++;
	return start;
}
struct list* reverse(struct list* start)
{
	struct list* next,*prev,*current;
	if(start==NULL || start->next==NULL)
	{
		return start;
	}
	else
	{
		prev=NULL;
		next=NULL;
		current=start;
		while(current!=NULL)
		{
			next = current->next;
			current->next=prev;
			prev = current;
			//printf("\n\t\t data is : %5d",prev->data);
			current=next;
		}
		start=prev;	
	}	
	return start;
}

void dis(struct list *start)
{
	struct list *tmp;
	tmp=start;
	if(start == NULL)
	{
		printf("\n !!! List is Empty !!!! PLease Insert Some Data First !!!\n");
	}	
	else
	{
		printf("\n Linked List Data is  :\t");
		while(tmp!=NULL)
		{
			printf("%5d",tmp->data);
			tmp=tmp->next;
		}	
	}
	printf("\n");	
}
void count()
{
	 printf("\n Count of number of Nodes is : %d",cnt);      
}

int main(int argc, char const *argv[])
{
	 int ch,n;
	 struct list *start=NULL;
	 while(1)
	 {
	       printf("\n------------------------------------------------------------------");
	       printf("\n******** Enter your choice********* :");
	       printf("\n\t 1) Insert \n\t 2) Reverse \n\t 3) Display \n\t 4) Count:%d \n\t 5) Exit",cnt);
	       printf("\t\t Enter Your Choice : ");
	       scanf("%d",&ch);
	       if(ch>4)
	       break;
	       switch(ch)
	       {
	             case 1:
	                   printf("\t\t\t\tEnter number to be insert :");
	                   scanf("%d",&n);
	                   start =  insert(start,n);
	                   break;
	             case 2:
	                   start = reverse(start);
	                   printf("\n ................  Reverse Successfully ............  ");
	                   break;      
	             case 3:
	                   dis(start);
	                   break;      
	             case 4:
	                   count();

	       }
	}       
	printf("\n");
	return 0;
}