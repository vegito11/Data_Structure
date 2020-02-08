//gcc ll1.c  -lm
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
typedef struct list
{
	int data;
	struct list *next;
}node;
struct list* createNode()
{
	struct list *tmp;
	tmp = (struct list*)malloc(sizeof(struct list));
	tmp->next = NULL;
	return tmp;
}
int cnt=0;

struct list* makeaLoop(struct list* start)
{
	struct list* tmp,*third;
	tmp=start;
	int var=0;
	while(tmp->next!=NULL)
	{		
		tmp=tmp->next;
	}
	third =start;
	while(var<cnt/2)
	{
		third = third->next;
		var++;
	}	
	tmp->next=third;
	return start;	

}

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
	int var=0;
	if(start == NULL)
	{
		printf("\n !!! List is Empty !!!! PLease Insert Some Data First !!!\n");
	}	
	else
	{
		printf("\n Linked List Data is  :\t");
		while(tmp!=NULL && var<cnt+9)
		{
			printf("%5d",tmp->data);
			tmp=tmp->next;
			var++;
		}	
	}
	printf("\n");	
}
node* checkLoop(node *start)
{
	node* slow,*fast;
	slow=fast=start;
	while(slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if(slow==fast)
			return slow;
	}	
	return NULL; 
}
node* startOfloop(node* start,node *slow)
{
	node* tmp=start;
	while(slow!=tmp)
	{
		slow=slow->next;
		tmp=tmp->next;
	}
	return slow;	
}
void count()
{
	 printf("\n Count of number of Nodes is : %d",cnt);      
}
node* removeLoop(node *start,node* position)
{
	int cnt=0;
	node *tmp=start;
	while(tmp)
	{
		if(tmp->next==position && cnt==0)
			cnt++;
		else if(tmp->next==position && cnt!=0)
		{	
			tmp->next=NULL;
			return start;
		}	
		tmp=tmp->next;

	}	
	return start;
}
int main(int argc, char const *argv[])
{
	 int ch,n;
	 struct list *start=NULL;
	 struct list *third=NULL;
	 int flg=0;
	 struct list *position;
	 while(1)
	 {
	       printf("\n------------------------------------------------------------------");
	       printf("\n******** Enter your choice********* :");
	       printf("\n\t 1) Insert \n\t 2) Find LOOP \n\t 3) Display \n\t 4) Remove Loop \n\t 5) Exit");
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
	                   start = makeaLoop(start);
	                   dis(start);
	                   if(position=checkLoop(start))
	                   {		                   		
	                   	  printf("\n\t Given Linked List have Loop ");
	                   	  position = startOfloop(start,position);
	                   	  printf("\n\t Node where Loop Started Is :%d",position->data);
	                   	  flg=1;

	                   }  
	                   	else
	                   		printf("\n Given Linked List Doesn't have Loop : %p ",(void*)position);
	                   break;      
	             case 3:
	                   dis(start);
	                   break;      
	             case 4:
	              		if(flg==1)
	              		{	
	              			removeLoop(start,position);
	              			flg=0;
	              		}
	              		else
	              			printf("\n !!! No LOOP Exits !!!");
	              		break;	      
	             case 5:
	                   count();

	       }
	}       
	printf("\n");
	return 0;
}