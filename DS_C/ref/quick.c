#include<stdio.h>
#define SIZE 5

void quick(int a[],int size, int beg,int end,int *loc)
{
      int left,right,tmp;
      left=beg;
      right=end;
      *loc=beg;               //location to be compare wrt list is divided in two part
      printf("erro");
      step2:      
            while(a[*loc]<a[right] && right!=*loc)
            {
                  right--;
            }
            if(*loc==right)
            return ;
            if(a[*loc]>a[right])
            {
                  tmp=a[*loc];
                  a[*loc]=a[right];
                  a[right]=a[*loc];
            }
            goto step3;                        //until left == loc or right ==loc loop traverse in both directiom
      step3 :
            while(a[*loc]>a[left] && left!=*loc)
            {
                  left++;
            }            
            if(*loc==left)
            return ;
            if(a[*loc]<a[left])
            {
                  tmp=a[*loc];
                  a[*loc]=a[left];
                  a[left]=a[*loc];
            }
            goto step2;
            
}     

void quicksort(int a[],int n)
{
      int top,*loc;
      int lower[n],upper[n],beg,end;
      top=-1;
      if(n>1)
      {
            top++;
            lower[top]=0;
            upper[top]=n-1;
      }
      
      printf("\n##sort##");
      while(top!=-1)
      {
            beg=lower[top];
            end=upper[top];
            top--;
            quick(a,SIZE,beg,end,loc);
            if(beg>*loc-1)                 //at least two elemnet in left array
            {
                  top++;
                  lower[top]=beg;
                  upper[top]=*loc-1;
            }
            if(*loc+1>end)                 //at least two element in right array
            {
                  top++;
                  lower[top]=*loc+1;
                  upper[top]=end;
            }
      }
}

int main()
{
      
      int a[SIZE],i,j,tmp,n;
      printf("\n Enter the elment in array :");
      n=SIZE;      
      for(i=0;i<SIZE;i++)
      {
            scanf("%d",&a[i]);
      }
      printf("\n The element in array before sorting :");
      for(i=0;i<SIZE;i++)
      {
            printf("%4d",a[i]);
      }
      quicksort(a,n);
      printf("\n The element in array After sorting :");
      for(i=0;i<SIZE;i++)
      {
            printf("%4d",a[i]);
      }
      
      return 0;
}

