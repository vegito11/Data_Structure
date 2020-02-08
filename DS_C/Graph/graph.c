#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int jun,del,edge;
    int min,d,cnt;
    scanf("%d",&jun);
    scanf("%d",&del);
    scanf("%d",&edge);
    int x,y;
    int q[jun];
    for(int i=0;i<jun;i++)
    {
        q[i]=0;
    }    

    struct graph
    {
      int vertex;
      int **a;    
      int time;  
    }g;
    g.a=(int**)malloc(sizeof(int*)*jun);
    for(int i=0;i<jun;i++)
    {
        g.a[i]=(int*)malloc(sizeof(int)*jun);
        for(int j=0;j<jun;j++)
        {    
            if(i!=j)
            {    
                g.a[i][j]=5000;
            }    
            else
                g.a[i][j]=0;
        }    
    }    
    
    for(int i=0;i<edge;i++)
    {
        scanf("%d%d%d",&x,&y,&g.time);
            if( g.a[x-1][y-1] > g.time)
            {
                g.a[x-1][y-1] = g.time;
                g.a[y-1][x-1]=g.time;
            }    
        //g.a[x-1][y-1]=g.time;
        //g.a[y-1][x-1]=g.time;
    }    
    ///*
    //  Display Graph
    for(int i=0;i<jun;i++)
    {
        for (int j = 0; j < jun; ++j)
        {
            printf("%7d",g.a[i][j]);
        }
        printf("\n");
    }// */   
    // Now find the min time
   
    q[0]=1;
    
    int cal,extrapath;
    d=0;
    cnt=0;
    //printf("\nq[0]%5d\n",q[0]);
    while(cnt<jun)
    {
        min=6000;
        for (int j = 0; j < jun; j++)
        {
            if(j==d)
                continue;
            
            cal=g.a[0][d]+g.a[d][j];
            
           // printf("\ncal:%6d cal2 :%6d min :%6d",cal,g.a[0][j],min);
            if(cal!=0 && cal%del==0 && (j!=jun-1))
                cal=cal+del;
            else if(cal!=0 && (j!=jun-1))
            {
                extrapath=cal/del;
                if(extrapath%2==1)
                {
                    cal=cal+del*(extrapath%del+1)-cal;
                }    
            }    
            
            if(cal<=g.a[0][j])
            {
                g.a[0][j]=cal;
                if(min>g.a[0][j] && q[j]==0)
                {
                    min=g.a[0][j];
                    d=j;
                }
            }

        }
       // printf("\n Node :%d",d);
        q[d]=1;
        cnt++;
        
    } 
   ///*         // Display Graph Once Again
    printf("\n\n\t *****Finally*** \n\n ");
     for(int i=0;i<jun;i++)
     {
         for (int j = 0; j < jun; ++j)
         {
             printf("%7d",g.a[i][j]);
         }
         printf("\n");
     }       
   // */
    printf("%d",g.a[0][jun-1]);
    return 0;
}