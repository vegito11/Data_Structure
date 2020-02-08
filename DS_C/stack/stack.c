#include<stdio.h>
#define size 10
int top=-1;
void push(int a[])
{
      int data;
      
      if(top==size)
      {
            printf("\n Sorry Array Overflow!!!!...First delete some data!!!");
      }
      
      else
      {
            top++;
            printf("\n Enter the Number :");
            scanf("%d",&data);
            a[top]=data;
            
  //          cnt++;
      }
}

void pop(int a[])
{
      if(top==-1)
      {
            printf("\n Soory Array is Underflow!!!...First insert some data!!! ");
      }
      else
      {
            printf("\n This Number is deleted %d !!!!",a[top]);
            top--;
//            cnt--;        
            
      }
}

void dis(int a[])
{
      int i;
      if(top==-1)
      {
            printf("\n Soory Array is Underflow!!!...First insert some data!!! ");
      }
      else
      {
            printf("\n Array elemnets are :");
            for(i=0;i<=top;i++)
            {
                  printf("\n%3d",a[i]);
            }
      }            
}

int main()
{
      int a[size],ch;
      //cnt=0;
      while(1)
      {
            printf("\n\n******** Enter your choice********* :\n\t 1. PUSH \n\t 2. POP \n\t 3. DISPLAY \n\t 4. EXIT");
            printf("\n Enter Your Choice :...");
            scanf("%d",&ch);
            if(ch>3)
            break;
            switch(ch)
            {
                  case 1:
                        push(a);
                        break;
                  case 2:
                        pop(a);
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
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...2

 This Number is deleted 22 !!!!

******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...3

 Array elemnets are : 11

******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...2

 This Number is deleted 11 !!!!

******** Enter your choice********* :
	 1. PUSH 
	 2. POP 
	 3. DISPLAY 
	 4. EXIT
 Enter Your Choice :...2

 Soory Array is empty!!!...First insert some data!!! 

*/
