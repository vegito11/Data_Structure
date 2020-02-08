#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct List
{
	int data
	struct List* next;
};

struct graph
{
	int vertex;
	int edge;
	struct List *adj;
};

int main()
{
    int numcity,numroad,truck,repair;
    int from,to;
    scanf("%d%d%d%d",&numcity,&numroad,&truck,&repair);
    struct graph *g;
    struct List* tmp,*t;

    g=(struct graph*)malloc(sizeof(struct graph));

    g->vertex = numcity;
    g->edge = numroad;
    g->adj = (struct List*)malloc(sizeof(struct List)*g->vertex);

    // Initiallize All vertex
    for (int i = 0; i < g->vertex-1; ++i)
    {
    	g->adj[i]vertex=i;
    	g->adj[i]->next=NULL;
    }


    int count=0;

    // Creating graph
    for(int i = 0 ; i < numroad ; i++ )
    {
        scanf("%d%d",&from,&to);
        if(from==0)
        {
        	count++;
        }
        tmp = (struct List*)malloc(sizeof(struct List));
        tmp->vertex = to;
        tmp->next = NULL;
        t=g->adj[x];
        while(t->next!=null)
        {
        	t=t->next;
        }
        t->next=tmp;	

    }   
    return 0;
}