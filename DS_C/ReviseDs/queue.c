#include <stdio.h>
#include <stdlib.h>
#define size 100
int queue[100];
int front=-1;
int rear=-1;

int isempty()
{
      if(front==-1&&rear==-1)
      {
            return 1;
      }
      return 0;
}

int isfull()
{
      if(rear==size-1)
      {
            return 1;
      }
      return 0;
}
void enqueue(int data)
{
      
      if(isfull())
      {
            printf("\n Sorry Queue Overflow!!!!...First delete some data!!!");
            return;
      }
      
      else
      {
            rear++;
            if(front==-1)
            {
                  front=rear;
            }
            queue[rear]=data;
            cnt++;
      }
}

void dequeue()
{
      int flag=0;
      if(cnt<=0)
      {
            printf("\n Sorry Queue is Underflow!!!...First insert some data!!! ");
            return;
      }
      else
      {
            printf("\n This Number is deleted %d !!!!",queue[front]);
            front++;
            cnt--;
      }
}

void display()
{
      int i;
      if(isempty())
      {
            printf("\n Soory Queue is Underflow!!!...First insert some data!!! ");
      }
      else
      {
          printf("\n front= %d  rear = %d ",front,rear);
            printf("\n Queue elemnets are :");
            for(i=front;i<=rear;i++)
            {
                  printf("%5d",queue[i]);
            }
      }            
}

int main()
{
	int ch,data;
	while(1)
	{
		printf("\n********* Menu *********");
		printf("\n\t\t 1) Enqeue \n\t\t 2) Dequeue \n\t\t 3) Front \n\t\t 4) Display \n\t\t 5) Count");
		printf("\n\t\t\t Enter your Choice : ");
		scanf("%d",&ch);
		if(ch>5)
			break;
		printf("\n**************************************************************************\n");
		switch(ch)
		{
			case 1	:
					printf("\n\t\t Enter the data : ");
					scanf("%d",&data);
					enqueue(data);
					break;
			case 2	:
					data = dequeue();
					printf("\n\t\t %d",data, " is removed from queue !!!");	
					break;		
			case 3 :
					printf("\n\t\t %d %s",queue[front]);		
					printf(" is front of queue !!!");	
					break;		
			case 4 :		
					display();
					break;
			case 5 :
					printf("\n\t\t Count is : %d ",front+1);			
					break;
		}			

	}

	return 0;
}