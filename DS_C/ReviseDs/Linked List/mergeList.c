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
//10 50 70 98
// 20 34 60 112
// 10 20 34 50 60 70 98 112
struct list* merge(struct list *first,struct list *second,struct list *result)
{
	 struct list* tmp,*start;		 	
	 if(first==NULL) 
	 	return second;
	 if( second==NULL)
	 	return first;

	 if(first->data<second->data)
	 {
	 	result = first;
	 	start=first;
	 	first=first->next;
	 }	
	 else
	 {
	 	result = second;
	 	start=second;
	 	second = second->next;
	 }	
	 while(first && second)
	 {
	 	if(first->data <=second->data)
	 	{
	 		result->next = first;
	 		result = first;
	 		first = first->next;
	 	}	
	 	if(first->data > second->data)
	 	{
	 		result->next = second;
	 		result = second;
	 		second = second->next;
	 	}	
	 }
	 if(first==NULL)	
	 	result->next = second;
	 else
	 	result->next = first;

	 return start;
}

int main(int argc, char const *argv[])
{
	 int ch,n;
	 int cnt2=0,cnt1=0;
	 int flg=0;
	 struct list *first=NULL;
	 struct list *second=NULL;
	 struct list *result=NULL;
	 while(1)
	 {
	       printf("\n------------------------------------------------------------------");
	       printf("\n******** Enter your choice********* :");
	       printf("\n\t 1) Insert 1 \n\t 2) Insert 2 \n\t 3) Display \n\t 4) merge \n\t 5) Exit");
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
		                   first =  insert(first,50);
		                   first =  insert(first,90);
		                   first =  insert(first,100);
		                   cnt1++;
		                   break;
		                }  
		                if(flg==1)
		                	break;
	                   printf("\t\t\t\tEnter number to be insert :");
	                   scanf("%d",&n);
	                   first =  insert(first,n);
	                   break;
	             case 2:
	                   if(cnt2==0)
	                   {
		                   second =  insert(second,20);
		                   second =  insert(second,30);
		                   second =  insert(second,40);
		                   second =  insert(second,60);
		                   cnt2++;
		                   break;
		                }
		                if(flg==1)  
		                	break;
	                   printf("\t\t\t\tEnter number to be insert :");
	                   scanf("%d",&n);
	                   second =  insert(second,n);
	                   break;
	             case 3:
	                   printf("\n Linked List 1 Data is  :\t");
	                   dis(first);
	                   printf("\n Linked List 2 Data is  :\t");
	                   dis(second);
	                   printf("\n");	
	                   break;      
	             case 4:
	                   flg=1;
	                   result = merge(first,second,result);
	                   printf("\n Merge List Data is  :\t");
	                   dis(result);
	                   break;

	       }
	}       
	printf("\n");
	return 0;
}