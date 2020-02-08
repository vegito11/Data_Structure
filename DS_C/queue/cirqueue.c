#include<stdio.h>
#define size 3
int front=-1,rear=-1;

void ENQUEUE(int a[])
{
      int data;
      
      if(front==(rear+1)%(size))
      {
            printf("\n Sorry QUEUE Overflow!!!!...First delete some data!!!");
      }
      
      else
      {
            rear=(rear+1)%(size);
            printf("\n Enter the Number :");
            scanf("%d",&data);
            if(front==-1)
            {
                  front=rear;
            }
            a[rear]=data;
      }
}

void DEQUEUE(int a[])
{
     
      if(front==rear)
      {
            if(rear == -1)
            {                  
                  printf("\n Soory QUEUE is Underflow!!!...First insert some data!!! ");
            }
            else
            {
                  printf("\n This Number is deleted %d !!!!",a[front]);
                  front=rear=-1;
            }
            
      }
      else
      {
            printf("\n This Number is deleted %d !!!!",a[front]);
            front=(front+1)%(size);
      }
}

void dis(int a[])
{
      int i;
      if(front==-1)
      {
            printf("\n Soory QUEUE is Underflow!!!...First insert some data!!! ");
      }
      else if(front<=rear)
      {
            printf("\n f = %d r = %d",front,rear);
            printf("\n Array elemnets are :");
            for(i=front;i<=rear;i++)
            {
                  printf("%3d",a[i]);
            }
      }  
      else if(front>=rear)
      {
            printf("\nvb f = %d r = %d",front,rear);
            printf("\n Array elemnets are :");
            do
            {
                  printf("%3d",a[front]);
                  front=(front+1)%size;
            }while(front!=(rear+1)%size);
            
      }          
}

int main()
{
      int a[size],ch;
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
                        ENQUEUE(a);
                        break;
                  case 2:
                        DEQUEUE(a);
                        break;      
                  case 3:
                        dis(a);
                        break;      
            }
     }       
      return 0;
}

/*output
******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter the Number :11


******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter the Number :22


******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter the Number :33


******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...3

 f = 0 r = 2
 Array elemnets are : 11 22 33

******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...2

 This Number is deleted 11 !!!!

******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...2

 This Number is deleted 22 !!!!

******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...2

 This Number is deleted 33 !!!!

******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...2

 Soory QUEUE is Underflow!!!...First insert some data!!! 

******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter the Number :11


******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter the Number :22


******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...1

 Enter the Number :33


******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...3

 f = 0 r = 2
 Array elemnets are : 11 22 33

******** Enter your choice********* :
	 1. ENQUEUE 
	 2. DEQUEUE 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...^C



*/
