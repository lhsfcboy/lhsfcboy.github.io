#pragma once

/* Put anything you like here, but
   certainly your 'state' structure
   to hold your board e.g.
*/
#define MAXROWS 20
#define WIDTH 5
#define HEIGHT 6
struct st
{
   char board[MAXROWS][WIDTH + 1];//add a tile for '\0'
};
typedef struct st state;

void print_board(state *s);
