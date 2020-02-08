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
	      
	printf("\n\t\t ------------ To Insert At : -----------");
	printf("\n\t\t\t 1 . Beginning \n\t\t\t 2 . Middle \n\t\t\t 3 . END");
	printf("\n\t\t\t 4 . Location ");
	printf("\t\t Your Choice : ");
	scanf("%d",&ch);
	printf("\t\t\t\tEnter number to be insert :");
	scanf("%d",&n);
	tmp->data=n;
	printf("\n\t\t-----------------------------------");

	if(ch>4)
		return;
	switch(ch)
	{
		case 1 :
				tmp->next=start;
				start = tmp;
				break;
		case 2 :
				/* Insert At the End of Count is One*/
				if(cnt==1)
				{
					start->next=tmp;
					cnt++;
					return;
				}	
				pos=ceil(cnt/2);
				/*
						1 	 	2   3   4   5         = 5/2  = 3
						1  	 	2   3   4             = 4 /2 = 2+1 
						start  
						pos = 3 
						i = 1    
							pos = 2

				*/
				if(cnt%2==0)
					pos+=1;
				search = start;
				for (int i = 1; i < pos-1; ++i) // 
				{
					search = search->next;
					printf("%d\n",i);
				}

				tmp->next = search->next;
				search->next = tmp;
				break;		
		case 4 :
				printf("\n\t\t\t Enter the Position :");
				scanf("%d",&pos);
				/* Enter At END */
				if(pos==cnt+1)
				{
					search  = start;
					while(search->next!=NULL)
					{
						search = search->next;
					}	
					search->next=tmp;
				}	
				/* Enter A Start */
				else if (pos==1)
				{
					tmp->next=start;
					start = tmp;
				}
				
				/* If Posiotion is Valid*/
				else if(pos<=cnt)
				{
					search = start;
					for(int i = 1; i <pos-1 ; ++i)
					{
						search = search->next;  //n-1 node
					}	
					tmp->next = search->next;
					search->next = tmp;
				}	
				/*If Position is Invalid */
				else
				{
					printf("\n !!!! PLEASE Enter the Valid Position !!!!");
					return;
				}	

				break;		
		case 3 :	
				search  = start;
				while(search->next!=NULL)
				{
					search = search->next;
				}	
				search->next=tmp;
				break;
	}
	cnt++;
}
void delete()
{
	struct list* tmp,*search,*last;
	int ch,n,i,pos;
	if(start==NULL)
	{
	      printf("\n Sorry LIST is Empty !!!!!! First Insert some Data :)");
	      return;
	}
	
	printf("\n\t\t DELETE Node From : ");
	printf("\n\t\t\t 1 . Beginning \n\t\t\t 2 . Middle \n\t\t\t 3 . END \n\t\t\t 4 . Location ");
	printf("\t Your Choice : ");
	scanf("%d",&ch);
	switch(ch)
	{
		case 1 :
				if(start->next==NULL)	
				{
					printf("%d is deleted From List\n",start->data);
					free(start);
					start = NULL;
				}
				else
				{
					tmp=start;
					start = start->next;
					printf("%d is deleted From List\n",tmp->data);
					free(tmp);
					tmp=NULL;
				}	
				break;
		case 2 :		
				if(cnt==1)
				{
					free(start);
					start = NULL;
				}	
				pos=ceil(cnt/2);
				if(cnt%2==0)
					pos+=1;
				search = start;
				for (int i = 1; i < pos-1; ++i) // 
				{
					search = search->next;		 // n-1 node		
				}
				tmp=search->next;
				search->next = tmp->next;
				printf("%d is deleted From List\n",tmp->data);
				free(tmp);

				break;
		case 4 :
				printf("\n\t\t\t Enter the Position :");
				scanf("%d",&pos);
				/* Delete At END */
				if(pos==cnt)
				{
					search  = start;
					while(search->next!=NULL)
					{
						last=search;
						search = search->next;
					}	
					last->next=NULL;
					printf("%d is deleted From List\n",search->data);
					free(search);
				}	
				/* Delete A Start */
				else if (pos==1)
				{
					tmp=start;
					start = start->next;
					printf("%d is deleted From List\n",tmp->data);
					free(tmp);
				}
				
				/* If Position is Valid*/
				else if(pos<cnt)
				{
					search = start;
					for(int i = 1; i <pos-1 ; ++i)
					{
						search = search->next;  //n-1 node
					}	
					tmp=search->next;
					search->next = tmp->next;
					printf("%d is deleted From List\n",tmp->data);
					free(tmp);

				}	
				/*If Position is Invalid */
				else
				{
					printf("\n !!!! PLEASE Enter the Valid Position !!!!");
					return;
				}	

				break;		
		case 3 :	
                   search=start;
                   while(search->next!=NULL)
                   {
                         last=search;            //point to last-1 node i.e is future last
                         search=search->next;
                   }
                   tmp=search;
                   last->next=NULL;
                   printf("\n %d Number is Deleted from list !!!!!!",tmp->data);
                   free(tmp);
                   tmp=NULL;
				break;
						
	}
	cnt--;
	


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
	       printf("\n\t 1.INSERT \n\t 2.DELETE\n\t 3.DISPLAY \n\t 4.COUNT:%d \n\t 5.EXIT",cnt);
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
	                   delete();
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