#pragma once

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <assert.h>
#include <stdbool.h>

#define BRDSZ 6
#define MAXBRDS 200000
// #define FIRST_TILE 2
#define HAWK_ROW_END 1
#define TILE_ROW_START 2
#define CNT_LS_LEN 20//to init solution_list

typedef struct
{
    char tiles[BRDSZ][BRDSZ + 1];
    char hawk_tile;
    int parent_index;
    int self_index;
} board;

typedef struct
{
    board board_list[MAXBRDS];
    int tail_index;
    int filled_width;
    int filled_height;
} state;

#include "md.h"

bool create_child_boards(state *s, board *parent);
void push_hawk(board *candidate_board, int column_to_push, state *s);
bool find_pushable_col(state *s, board *board, int *col_state_list);
bool board_unique_check(state *s, board *candidate_board);
void board_insert(board *board_dest, board board_src);
bool check_2boards_same(board *board_A, board *board_B);
bool prepare_str_for_state(char *str);
void print_board_tiles(state *s,int board_index);
