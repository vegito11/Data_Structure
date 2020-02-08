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

struct list* insert(struct list* start,int n)
{
	int ch,i,pos;
	struct list* tmp,*search;
	
	tmp=createNode();
	tmp->data=n;
	if(start==NULL)
	{		
	    start=tmp;
	    return tmp;
	}
	else
	{	
		tmp->next=start;
		start=tmp;
	}
	return  start;
}

void display(struct list* start)
{
	struct list *tmp;
	tmp=start;
	if(start == NULL)
	{
		printf("\n !!! List is Empty !!!! PLease Insert Some Data First !!!\n");
	}	
	else
	{
		printf("\n Number is  : ");
		while(tmp!=NULL)
		{
			printf("%d",tmp->data);
			tmp=tmp->next;
		}	
	}
	printf("\n");	
}
void count()
{
	 printf("\n Count of number of Nodes is : %d",cnt);      
}
struct list* addNumber(struct list* first,struct list* second,struct list* result)
{
	int div,rem,add;
	int carry=0;	
	struct list *tmp,*prev;
	tmp=createNode();
	while(first!=NULL)
	{		  
		  add =first->data+second->data;
		  rem = add%10;
		  carry= add/10;
		  tmp=createNode();
		  tmp->data=rem+div;
		  if(result==NULL)
		  {	
		  	result=tmp;
		  	prev=tmp;
		  }	
		  else
		  {
		  	prev->next = tmp;
		  	prev = tmp;
		  }	
		  first = first->next;
		  second = second->next;
	}
	if(carry!=0)	
	{
		tmp = createNode();
		tmp->data =carry;
		prev->next = tmp;
	}	
	return result;
}
struct list* reverse(struct list*);
int main(int argc, char const *argv[])
{
	 int ch,n1,n2;
	 int rem,cnt1=0,cnt2=0;
	 int tmp1,tmp2;
	 struct list *first=NULL;
	 struct list *second=NULL;
	 struct list* result =NULL;
	       printf("\n------------------------------------------------------------------");
	       printf("\n***********  Addition is  ************ :");
	       printf("\n\t\t Enter the First Number  :");
	       scanf("%d",&n1);
	       tmp1 = n1;
	       printf("\n\t\t Enter the Second Number :");
	       scanf("%d",&n2);
	       tmp2 = n2;

	       while(tmp1>0)
	       {
	       		rem = tmp1%10;
	       		//printf("%d\n",rem);
	       		first = insert(first,rem);
	       		cnt1++;
	       		tmp1 = tmp1/10;
	       }	
	       display(first);
	       while(tmp2>0)
	       {
	       		rem = tmp2%10;
	       		second = insert(second,rem);
	       		cnt2++;
	       		tmp2 = tmp2/10;
	       }	
	       display(second);
	       if(cnt2>cnt1)
	       {
	       		for(int i=1;i<=(cnt2-cnt1);i++)
	       		{
	       			first=insert(first,0);
	       		}	

	       }	
	       if(cnt1>cnt2)
	       {
	       		for(int i=1;i<=(cnt1-cnt2);i++)
	       		{
	       			second=insert(second,0);
	       		}	

	       }
	       first = reverse(first);
	       second =  reverse(second);
	       result = addNumber(first,second,result);
	       result = reverse(result);
	       display(result);
	printf("\n");
	return 0;
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
			current=next;
		}
		start=prev;	
	}	
	return start;
}