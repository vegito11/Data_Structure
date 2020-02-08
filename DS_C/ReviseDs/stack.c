#include <stdio.h>
#include <stdlib.h>
int stack[100];
int top=-1;
void push(int data)
{
	top++;
	if(top==100)
	{
		printf("\n !!! Stack is Full !!!!");
	}	
	stack[top] = data;
}
int pop()
{
	int tmp;
	if(top==-1)
	{
		return -1;
	}	
	else
		return stack[top--];
	return tmp;
}
void display()
{
	printf("\n Stack Elements are :");
	for (int i = top; i >=0; i--)
	{
		printf("\n\t %4d",stack[i]);
	}
}
int main()
{
	int ch,data;
	while(1)
	{
		printf("\n********* Menu *********");
		printf("\n\t\t 1) Push \n\t\t 2) Pop \n\t\t 3) Top \n\t\t 4) Display \n\t\t 5) Count");
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
					push(data);
					break;
			case 2	:
					data = pop();
					if(data==-1)
					{	
						printf("\n\t\t !!!!! Stack Is Empty   !!!!");
						break;
					}	

					printf("\n\t\t %d %s",data, " is removed from stack !!!");	
					break;		
			case 3 :
					printf("\n\t\t %d %s",stack[top], " is Top of stack !!!");		
					break;		
			case 4 :		
					display();
					break;
			case 5 :
					printf("\n\t\t Count is : %d ",top+1);			
					break;
		}			

	}

	return 0;
}