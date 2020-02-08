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
struct list *start=NULL;
int cnt=0;

void insert()
{
	int ch,n,i,pos;
	struct list* tmp,*search;
	
	tmp=createNode();
	if(start==NULL)
	{
		printf("\t\t\t\tEnter number to be insert :");
		scanf("%d",&n);
		tmp->data=n;
	    start=tmp;
	    cnt++;
	    return;
	}
	else
	{	
		printf("\t\t\t\tEnter number to be insert :");
		scanf("%d",&n);
		tmp->data=n;
		search = start;
		while(search->next!=NULL)
		{
			search = search->next;
		}	
		search->next=tmp;		
	}
	cnt++;
}
void evenOrodd()
{
	struct list* next,*prev,*current;
	if(start==NULL)
	{
		return ;
	}
	else
	{
		current=start;
		while(1)
		{
			if(current==NULL)
			{	
				printf("\n !!!! Length Of Linked List is Even !!!");				
				break;
			}	
			if(current->next==NULL)	
			{			
				printf("\n !!!! Length Of Linked List is ODD !!!");
				break;
			}	
			current=current->next->next;
			//printf("%5d",current->data);
		}

	}	

}
void dis()
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
	 while(1)
	 {
	       printf("\n------------------------------------------------------------------");
	       printf("\n******** Enter your choice********* :");
	       printf("\n\t 1) Insert \n\t 2) Length \n\t 3) Display \n\t 4) Count:%d \n\t 5) Exit",cnt);
	       printf("\t\t Enter Your Choice : ");
	       scanf("%d",&ch);
	       if(ch>4)
	       break;
	       switch(ch)
	       {
	             case 1:
	                   insert();
	                   break;
	             case 2:
	                   evenOrodd();
	                   break;      
	             case 3:
	                   dis();
	                   break;      
	             case 4:
	                   count();

	       }
	}       
	printf("\n");
	return 0;
}