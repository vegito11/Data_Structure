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
int length(struct list *start)
{
	int cnt=0;
	while(start!=NULL)
	{	
		start = start->next;
		cnt++;
	}	  
	return cnt;
}
int isGreater(int one,int two)
{
	if(one>two)
		return 1;
	return 0;
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
	if(start == NULL)
	{
		printf("\n !!! List is Empty !!!! PLease Insert Some Data First !!!\n");
	}	
	else
	{		
		while(tmp!=NULL)
		{
			printf("%5d",tmp->data);
			tmp=tmp->next;
		}	
	}
	printf("\n");	
}
int isPalindrome(struct list* first,struct list* second)
{
	while(first)
	{
		if(first->data!=second->data)
			return 0;	
		first=first->next;
		second=second->next;
	}	
	return 1;
}
struct list* split(struct list *root)
{
	 struct list *slow,*fast;		 	
	 slow=root;
	 fast=root;
	 struct list *second;
	 second=NULL;

	 if(root==NULL || root->next ==NULL)
	 	return root;
	 /*  In Search of Middle*/
	 while(1)
	 {
	 	fast = fast->next->next;
	 	/*
			slow			 	 	s                   s
			10 20 30 40 	  	10 20 30 40   		10 20 30 40 NULL
			fast					  f                          f
	 	*/	  
	 	
	 	/* even Length*/
	 	if(fast==NULL)
	 	{
	 		//printf("\n Middle  Data is : %d",slow->data);	
	 		second=slow->next;
	 		slow->next=NULL;	 		
	 		break;
	 	}	
	 	/*
			slow			 	 	s                       s
			10 20 30 40  50	  	10 20 30 40  50 		10 20 30 40 50
			fast					  f                              f
	 	*/	  
	 	/*   Odd length*/
	 	if(fast->next==NULL)
	 	{
	 	//	printf("\n Middle  Data is : %d",slow->data);	
	 		second = slow->next->next;	
	 		slow->next = NULL;		
	 		break;
	 	}	
	 	slow = slow->next;
	 	//printf("\n Data is : %d",slow->data);
	 }
	 //reverse(second);
	 //dis(second);	
	 return second;
}

int main(int argc, char const *argv[])
{
	 int ch,n;
	 int cnt2=0,cnt1=0;
	 int flg=0;
	 struct list *first=NULL;
	 //struct list *second=NULL;
	 struct list *result=NULL;
	 while(1)
	 {
	       printf("\n------------------------------------------------------------------");
	       printf("\n******** Enter your choice********* :");
	       printf("\n\t 1) Insert  \n\t 2) Palindrome Check \n\t 3) Display \n\t 4) Exit");
	       printf("\t\t Enter Your Choice : ");
	       scanf("%d",&ch);
	       if(ch>4)
	       break;
	       switch(ch)
	       {
	             case 1:
	                   if(cnt1==0)
	                   {
		                   first =  insert(first,10);
		                   first =  insert(first,20);
		                   first =  insert(first,30);
		                   first =  insert(first,40);
		                   first =  insert(first,70);
		                   first =  insert(first,40);
		                   first =  insert(first,30);
		                   first =  insert(first,20);
		                   //first =  insert(first,10);
		                   cnt1++;
		                   break;
		                }  
	                   printf("\t\t\t\tEnter number to be insert :");
	                   scanf("%d",&n);
	                   first =  insert(first,n);
	                   break;
	             case 2:
	                   result = split(first);
	                   result = reverse(result);
	                   if(isPalindrome(first,result))
	                   	printf("\n\t\t ......Given String is Palindrome ....");
	                   	else
	                   	printf("\n\t\t !!!!!! Given String is NOT Palindrome !!!! ");
	                   //dis(result);
	                   break;
	             case 3:	        	                   
	                   dis(first);

	                   printf("\n");	
	                   break;      

	       }
	}       
	printf("\n");
	return 0;
}