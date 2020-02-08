#include<stdio.h>
#include<stdlib.h>
#define MAX 10
struct graph
{
      int V,E;
      int **matri;
};
int vis[MAX];
struct graph* adjmatrix()
{
      int v,e,i,j;
      struct graph*g;
      g=(struct graph*)malloc(sizeof(struct graph));
      printf("\n Enter the Number of Vetices  : ");
      scanf("%d",&g->V);
      printf("\n Enter the Number of Edges    : ");
      scanf("%d",&g->E);
      g->matri=malloc(sizeof(int*)*(g->V));
      for(i=0;i<g->V;i++)
      {
            g->matri[i]=malloc(sizeof(int)*(g->V));            
            for(j=0;j<g->V;j++)
            {
                  g->matri[i][j]=0;
            }
      }
      for(i=0;i<g->E;i++)
      {
            printf("\n Enter the starting and ending point of edge (v,e) :");
            scanf("%d%d",&v,&e);
            g->matri[v][e]=1;
            g->matri[e][v]=1;
      }
      return g;
      printf("\n");
}
void display(struct graph*g)
{
      int i,j;
      printf("\n\t");
      for(i=0;i<g->V;i++)
      {
            for(j=0;j<g->V;j++)
            {
                  printf("%4d",g->matri[i][j]);
            }
            printf("\n\t");
      }
}
void bfs(int st,struct graph *g)
{
      int i,que[g->V];
      int front,rear;
      front=rear=-1;
      printf("%3d",st);      
      vis[st]=1;
      front++;
      rear++;
      que[rear]=st;
      while(front<=rear)
      {
            st=que[front];
            front++;
            for(i=0;i<g->V;i++)
            {
                  if(g->matri[st][i]==1 && vis[i]==0)
                  {
                        rear++;
                        que[rear]=i;
                        printf("%3d",i);
                        vis[i]=1;
                  }
            }
      }
}
void dfs(int st,struct graph *g)
{
      int i,stk[g->V];
      int top;
      top=-1;
//      printf("%3d",st);      
      vis[st]=1;
      top++;
      stk[top]=st;
      while(top!=-1)
      {
            st=stk[top];
            printf("%3d",st);
            top--;
            for(i=0;i<g->V;i++)
            {
                  if(g->matri[st][i]==1 && vis[i]==0)
                  {
                        top++;
                        stk[top]=i;
                        vis[i]=1;
                  }
            }
      }

}
int main()
{
      struct graph*root;
      int ch,st,che,i;
      while(1)
      {
            printf("\n MENU \n\t 1 . insert graph \n\t 2 . Traverse graph \n\t 3 . Display \n\t 4 . EXIT ");
            printf("\t Enter your Choice : ");
            scanf("%d",&ch);
            if(ch>3)
            break;
            switch(ch)
            {
                  case 1:
                              root=adjmatrix();
                              break;
                  case 2:
                              printf("\n\t MENU \n\t\t 1 . BFS \n\t\t 2 . DFS ");
                              printf("\t Enter your Choice : ");
                              scanf("%d",&che);
                              switch(che)
                              {
                                    case 1:
                                                for(i=0;i<MAX;i++)
                                                vis[i]=0;
                                                printf("\n Enter the starting node adress :");
                                                scanf("%d",&st);
                                                printf("\n DFS Traversal is : ");
                                                bfs(st,root);                  
                                                break;
                                    case 2: 
                                                for(i=0;i<MAX;i++)
                                                vis[i]=0;
                                                printf("\n Enter the starting node adress :");
                                                scanf("%d",&st);
                                                printf("\n BFS Traversal is : ");
                                                dfs(st,root);
                                                break;           
                              }                                                                  
                              break;
                  case 3: 
                              printf("\n Matrix representation of Grapg is As Follows :");                               
                              display(root);
            }
      }
      return 0;
}
