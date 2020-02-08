#include<stdio.h>
#define size 3
int rear=-1,front=-1;
int cnt=0;

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
void enqueue(int a[])
{
      int data;
      if(isfull())
      {
            printf("\n Sorry Queue Overflow!!!!...First delete some data!!!");
            return;
      }
      
      else
      {
            printf("\n Enter the Number :");
            scanf("%d",&data);
            rear++;
            if(front==-1)
            {
                  front=rear;
            }
            a[rear]=data;
            cnt++;
      }
}

void dequeue(int a[])
{
      int flag=0;
      if(cnt<=0)
      {
            printf("\n Sorry Queue is Underflow!!!...First insert some data!!! ");
            return;
      }
      else
      {
            printf("\n This Number is deleted %d !!!!",a[front]);
            front++;
            cnt--;
      }
}

void dis(int a[])
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
                  printf("%5d",a[i]);
            }
      }            
}


int main()
{
      int a[size],ch;
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
                        enqueue(a);
                        break;
                  case 2:
                        dequeue(a);
                        break;      
                  case 3:
                        dis(a);
                        break;      
            }
     }       
      return 0;
}

/*output


*/
