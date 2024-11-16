#include "mydefs.h"

bool file2str(const char *fname, char *str)
{
   // verigfy file not empty
   if (fname == NULL || str == NULL)
   {
      return false;
   }

   FILE *file_for_str;
   char current_char;
   int index = 0;

   // open file for read
   file_for_str = fopen(fname, "r");
   if (file_for_str == NULL)
   {
      return false;
   }

   // swift file content to str
   while ((current_char = fgetc(file_for_str)) != EOF)
   {
      if (current_char != '\n' && current_char != '\r')
      {
         // file content should only have alpha letter
         if (current_char != '-' && !isupper((unsigned char)current_char))
         {
            fclose(file_for_str);
            return false;
         }
         str[index++] = current_char;
      }
      else
      {
         str[index++] = '-';
      }
   }
   str[index] = '\0';
   fclose(file_for_str);

   // remove extra '-' at the end of str
   int str_tail = strlen(str) - 1;
   while (str_tail >= 0 && str[str_tail] == '-')
   {
      str[str_tail] = '\0';
      str_tail--;
   }

   // verify str formate
   if (prepare_str_for_state(str) == false)
   {
      return false;
   }

   return true;
}

state *str2state(const char *str)
{
   // allocate memory for state
   state *new_state = (state *)malloc(sizeof(state));
   if (new_state == NULL)
   {
      return NULL;
   }

   // allocate memory for board
   new_state->tail_index = 0;
   board *board_from_file = &(new_state->board_list[0]);
   memset(board_from_file->tiles, 0, sizeof(board_from_file->tiles));
   board_from_file->self_index = 0;
   board_from_file->parent_index = -1;

   // init hawk
   board_from_file->hawk_tile = str[0];

   // init board
   int break_line = 0;
   int length = strlen(str);
   int i = TILE_ROW_START;
   int row;
   int col;
   int is_last_row = 0;
   for (row = 0; row < BRDSZ && i < length && !is_last_row; row++)
   {
      for (col = 0; col < BRDSZ && break_line == 0; col++)
      {
         if (str[i] == '-')
         {
            break_line = 1;
         }
         else
         {
            board_from_file->tiles[row][col] = str[i];
            if (board_from_file->tiles[row][0] == '\0')
            {
               is_last_row = 1;
            }
            i++;
         }
      }
      break_line = 0;
      i++;
   }
   new_state->filled_width = strlen(board_from_file->tiles[0]);
   new_state->filled_height = row;

   return new_state;
}

int solve(state *s, bool verbose)
{
   int solution_cnt = -1;
   int solved = 0; // loop termination conditions
   int current_board_index = 0;
   do
   {
      board *current_board = &s->board_list[current_board_index];
      solved = (!create_child_boards(s, current_board)); // santi: saperat it->check solved+create child
      if (!solved)
      {
         current_board_index++;
      }
   } while (!solved && current_board_index <= s->tail_index && current_board_index <= MAXBRDS);

   if (solved)
   {
      solution_cnt = 0;
      board *current_step = &s->board_list[current_board_index];
      int solution_list[CNT_LS_LEN];
      memset(solution_list, 0, sizeof(CNT_LS_LEN));
      if (current_step->self_index != 0)
      {
         while (current_step->parent_index >= 0)
         {
            solution_list[solution_cnt] = current_step->self_index;
            solution_cnt++;
            current_step = &s->board_list[current_step->parent_index];
         }
      }
      if (verbose)
      {
         print_board_tiles(s, s->board_list[0].self_index);
         printf("\n");
         for (int i = (solution_cnt - 1); i >= 0; i--)
         {
            print_board_tiles(s, solution_list[i]);
            printf("\n");
         }
      }
   }
   return solution_cnt;
}

void test(void)
{
   char str[BRDSZ * BRDSZ + BRDSZ + 2];

   // Test 1 passed: Standard format
   strcpy(str, "A-ABC-ABC-ABC");
   assert(prepare_str_for_state(str) == true);

   // Test 2 passed: Unequal row widths
   strcpy(str, "A-ABC-AB-ABC");
   assert(prepare_str_for_state(str) == false);

   // Test 3 passed: Non-uppercase characters
   strcpy(str, "A-ABC-abc-ABC");
   assert(prepare_str_for_state(str) == false);

   // Test 4 passed: Missing Hawk tile
   strcpy(str, "-ABC-ABC-ABC");
   assert(prepare_str_for_state(str) == false);

   // Test 5 passed: Too many rows
   strcpy(str, "A-B-B-B-B-B-B-B");
   assert(prepare_str_for_state(str) == false);

   // Test 6 passed: Row too wide
   strcpy(str, "A-ABCDEFGH-ABC");
   assert(prepare_str_for_state(str) == false);

   // Test 7 passed: Empty string
   strcpy(str, "");
   assert(prepare_str_for_state(str) == false);

   // Test 8 passed: Only Hawk tile
   strcpy(str, "A-");
   assert(prepare_str_for_state(str) == false);

   // Test 9 passed: Wrong separator
   strcpy(str, "A ABC-ABC-ABC");
   assert(prepare_str_for_state(str) == false);
}

/* Many of other functions, as required */

bool create_child_boards(state *s, board *parent) // return flags means 3 things: [0]no child/[-1]find solusion/[child number]return
{
   int pushable_flag[BRDSZ]; // init pushable_flag
   memset(pushable_flag, 0, sizeof(pushable_flag));
   if (!(find_pushable_col(s, parent, pushable_flag))) // cannot find pushable column
   {
      return false; // create candidate faild -> solved
   }

   for (int i = 0; i < s->filled_width; i++)
   {
      // create candidate succeed
      if (pushable_flag[i] == 1)
      {
         board candidate_board;
         memset(candidate_board.tiles, 0, sizeof(candidate_board.tiles));
         candidate_board.hawk_tile = parent->hawk_tile;
         memcpy(candidate_board.tiles, parent->tiles, sizeof(parent->tiles));
         candidate_board.parent_index = parent->self_index;
         push_hawk(&candidate_board, i, s);
         if (board_unique_check(s, &candidate_board) && s->tail_index < (MAXBRDS - 1))
         {
            // have unique candidate --> add into list
            s->tail_index++;
            board_insert(&(s->board_list[s->tail_index]), candidate_board);
            s->board_list[s->tail_index].self_index = s->tail_index;
         }
      }
   }
   return true; // not solved: impossible or next loop
}

void push_hawk(board *candidate_board, int column_to_push, state *s)
{
   char new_hawk_tile = '\0';
   for (int row = (s->filled_height - 1); row > 0; row--)
   {
      if (row == (s->filled_height - 1))
      {
         new_hawk_tile = candidate_board->tiles[row][column_to_push];
      }
      candidate_board->tiles[row][column_to_push] = candidate_board->tiles[row - 1][column_to_push];
   }
   candidate_board->tiles[0][column_to_push] = candidate_board->hawk_tile;
   candidate_board->hawk_tile = new_hawk_tile;
}

bool find_pushable_col(state *s, board *board, int *col_state_list)
{
   int found = 0;
   for (int col = 0; col < s->filled_width; col++)
   {
      for (int row = 0; row < s->filled_height; row++)
      {
         // compare every char in same column with the first char in the column
         if (board->tiles[0][col] != board->tiles[row][col])
         {
            col_state_list[col] = 1;
            found++;
         }
      }
   }
   if (found > 0)
   {
      return true;
   }
   else
   {
      return false;
   }
}

bool board_unique_check(state *s, board *candidate_board)
{
   int is_unique = 1;
   for (int i = 0; i < s->tail_index; i++)
   {
      if (check_2boards_same(candidate_board, &(s->board_list[i])))
      {
         is_unique = 0;
      }
   }
   if (!is_unique)
   {
      return false;
   }

   return true;
}

bool check_2boards_same(board *board_A, board *board_B)
{
   if (memcmp(board_A->tiles, board_B->tiles, sizeof(board_A->tiles)) == 0)
   {
      return true;
   }
   return false;
}

void board_insert(board *board_dest, board board_src)
{
   memcpy(board_dest->tiles, board_src.tiles, sizeof(board_src.tiles));
   // copy hawk_tile
   board_dest->hawk_tile = board_src.hawk_tile;
   // copy parent_index
   board_dest->parent_index = board_src.parent_index;
}

bool prepare_str_for_state(char *str)
{
   if (str == NULL)
   {
      return false;
   }

   // check Hawk tile
   if (strlen(str) < 3 || !isupper((unsigned char)str[0]) || str[1] != '-')
   {
      return false;
   }

   int str_len = strlen(str);
   int teil_row_start = TILE_ROW_START;
   int curr_row_width = 0;
   int prev_row_width = 0;
   int row_count = 0;

   for (int i = teil_row_start; i < str_len; i++)
   {
      // check char
      if (str[i] != '-' && !isupper((unsigned char)str[i]))
      {
         return false;
      }

      if (str[i] != '-')
      {
         curr_row_width++;
      }
      else
      {
         // check width <= maxmun_width
         if (curr_row_width == 0 || curr_row_width > BRDSZ)
         {
            return false;
         }

         // check each row have same width
         if (prev_row_width != 0 && curr_row_width != prev_row_width)
         {
            return false;
         }

         prev_row_width = curr_row_width;
         curr_row_width = 0;
         row_count++;
      }
   }

   // remove endiing '-'
   if (curr_row_width > 0)
   {
      if (curr_row_width > BRDSZ ||
          (prev_row_width != 0 && curr_row_width != prev_row_width))
      {
         return false;
      }
      row_count++;
   }

   // check height <= maxmun
   if (row_count > BRDSZ)
   {
      return false;
   }
   return true;
}

void print_board_tiles(state *s, int board_index)
{
   for (int row = 0; row < s->filled_height; row++)
   {
      for (int col = 0; col < s->filled_height; col++)
      {
         printf("%c", s->board_list[board_index].tiles[row][col]);
      }
      printf("\n");
   }
}
