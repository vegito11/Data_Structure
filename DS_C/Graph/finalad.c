#include <stdio.h>
#include <stdlib.h>
#define MAX 10
struct listnode
{
    int vno;
    struct listnode* next;
};
 
struct list
{
    struct listnode *head;  
};
 
struct graph
{
    int V,E;
    struct list* array;
};
int vis[MAX];
struct listnode* addnode(int y)
{
      struct listnode*tmp=(struct listnode*)malloc(sizeof(struct listnode));
      tmp->next=NULL;
      tmp->vno=y;
      return tmp;
}

struct graph* creategraph()
{
    int i,x,y; 
    struct listnode*tmp; 
    struct graph* g = (struct graph*) malloc(sizeof(struct graph));
    printf("\n Enter the Vertex of graph : ");
    scanf("%d",&g->V);
    printf("\n Enter the Edges of graph  : ");
    scanf("%d",&g->E);
    g->array = (struct list*) malloc(g->V * sizeof(struct list));
    for (i = 0; i< g->V;i++)
            g->array[i].head = NULL;
    for(i=0;i<g->E;i++)
    {
            printf("\n Enter the connected (Starting vertex,Ending vertex) :");
            scanf("%d%d",&x,&y);
            tmp=addnode(y);      
            tmp->next=g->array[x].head;
            g->array[x].head=tmp;
            
            tmp=addnode(x);      
            tmp->next=g->array[y].head;
            g->array[y].head=tmp;
    }
 
    return g;
}

void display(struct graph *g)
{
      int i;
      for(i=0;i<g->V;i++)
      {
            printf("\n %dth :",i );
            struct listnode* t=g->array[i].head;
            while(t)
            {
                  printf("%3d",t->vno);
                  t=t->next;
            }
      }
}

void bfs(int st,struct graph* g)
{
      int q[g->V],front,rear,i;
      front=rear=-1;
      printf("%d",st);
      vis[st]=1;
      front++;
      rear++;
      q[rear]=st;
      while(front>=rear)
      {
            st=q[front];
            front++;
            for(i=0;i<g->V;i++)
            {
                  struct listnode* t=g->array[i].head;                  
                  while(t)
                  {
                              if(vis[t->vno]==0)
                              {
                                    rear++;
                                    q[rear]=t->vno;
                                    printf("%d",t->vno);
                                    vis[t->vno]==1;
                              }  
                              t=t->next;    
                  }                  
            }
      }
}
void dfs(int st,struct graph* g)
{
      int stk[g->V],top,i;
      top=-1;
//      printf("%d",st);
      vis[st]=1;
      top++;
      stk[top]=st;
      while(top!=-1)
      {
            st=stk[top];
            printf("%d",st);
            top++;
            for(i=0;i<g->V;i++)
            {
                  struct listnode* t=g->array[i].head;                  
                  while(t)
                  {
                              if(vis[t->vno]==0)
                              {
                                    top++;
                                    stk[top]=t->vno;
                                    vis[t->vno]==1;
                              }  
                              t=t->next;    
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
                              root=creategraph();
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
                              printf("\n List representation of Graph is As Follows :");                               
                              display(root);
            }
      }
      return 0;
}
