#include "crushit.h"
#include "mydefs.h"

bool initialise(state *s, const char *str)
{
    // printf("<----------initialise is working.---------->\n");
    //   varify parameter
    if (s == NULL || str == NULL)
    {
        // printf("initialise return: In invalid parameter.\n");
        return false;
    }
    /*
    先把str当成文件名去找文件
    if能打开文件
        把文件内容copy到一个字符串里
    if不能打开文件
        就把str当成字符串
    */

    // init board and str_for_board
    for (int i = 0; i < MAXROWS; i++)
    {
        for (int j = 0; j < WIDTH; j++)
        {
            s->board[i][j] = '.';
        }
        s->board[i][WIDTH] = '\0';
    }
    // printf("board after init:\n");
    // print_board(s);
    int str_len = strlen(str);
    char str_for_board[MAXROWS * WIDTH + 1] = {0};
    for (int i = 0; i < str_len; i++)
    {
        str_for_board[i] = str[i];
    }
    // printf("str_for_board:  %s\nstr:            %s\n", str_for_board, str);

    // verify string formate
    // check length
    if (str_len > MAXROWS * WIDTH || str_len % WIDTH != 0)
    {
        // printf("initialise return: str is in invalid length.\n");
        return false;
    }
    // check alpha
    for (int i = 0; i < str_len; i++)
    {
        if (!isalpha(str_for_board[i]))
        {
            // printf("initialise return: str is not all alpha.\n");
            return false;
        }
    }
    // use str to fill the board properly
    int str_index = 0;
    for (int i = 0; i < MAXROWS; i++)
    {
        for (int j = 0; j < WIDTH; j++)
        {
            if (str_index < str_len)
            {
                s->board[i][j] = str_for_board[str_index];
                str_index++;
            }
        }
    }
    dropblocks(s);
    // printf("board after fill:\n");
    // print_board(s);
    return true;
}
bool dropblocks(state *s)
{
    // printf("<----------dropblocks is working.---------->\n");
    for (int i = 0; i < WIDTH; i++)
    {
        for (int j = MAXROWS - 1; j >= 0; j--)
        {
            // search each col bottom up
            if (s->board[j][i] == '.')
            {
                // once find an dot, search up for the nearst letter
                bool need_drop = true; // set a stop sign
                // printf("current tile is [%c], need_drop = %d", s->board[j][i], need_drop);
                for (int letter_above_dot = j - 1; letter_above_dot >= 0; letter_above_dot--)
                {
                    if (s->board[letter_above_dot][i] != '.' && need_drop == true)
                    {
                        // printf("s->board[letter_above_empt:     %d][i:%d] is a tile need drop:  %c.\n", letter_above_dot, i, s->board[letter_above_dot][i]);
                        // printf("s->board[j:                    %d][i:%d] is a empty tile:      %c.\n", j, i, s->board[j][i]);
                        // use nearst letter to fill the dot
                        s->board[j][i] = s->board[letter_above_dot][i];
                        s->board[letter_above_dot][i] = '.';
                        need_drop = false;
                        // printf("need_drop: %d\n", need_drop);
                        // printf("board after [%d] drop:\n", letter_above_dot);
                        // print_board(s);
                    }
                }
            }
        }
    }
    // printf("board after drop:\n");
    // print_board(s);
    return true;
}
bool tostring(const state *s, char *str)
{
    // printf("<----------tostring is working.---------->\n");
    // printf("board for tostring:\n");
    // create an empty row for compare
    char empty_row[WIDTH + 1];
    for (int i = 0; i < WIDTH; i++)
    {
        empty_row[i] = '.';
        // printf("empty_row[%d]=%c\n",i, empty_row[i]);
    }
    empty_row[WIDTH] = '\0';
    // printf("empty_row:%s\n", empty_row);

    //  compare each row top to bottom to find the first not all dot one
    bool is_empty_row = true; // set a sign
    int start_tostring_row;
    for (int i = 0; i < MAXROWS && is_empty_row; i++)
    {
        // printf("each row before find !is_empty_row: [%d] %s\n", i, s->board[i]); // print each row before find !is_empty_row
        if (strcmp(s->board[i], empty_row) != 0) // 《在判断相等的时候，究竟在比较什么东西？》
        {
            is_empty_row = false;
        }
        start_tostring_row = i;
        // printf("!is_empty_row: [%d] %s\n", start_tostring_row, s->board[start_tostring_row]); // print !is_empty_row
    }
    // printf("           start_tostring_row is [%d]:%s\n", start_tostring_row, s->board[start_tostring_row]);
    // to string start at this current row [start_tostring_row] to MAXROWS
    str[0] = '\0'; // prepare str for strcat()
    for (int i = start_tostring_row; i < MAXROWS; i++)
    {
        strcat(str, s->board[i]);
    }
    // print_board(s);
    // printf("str after tostring %s\n", str);
    return true;
}
bool matches(state *s)
{
    // printf("<----------matches is working.---------->\n");
    // prepare a match_result_matrix(2Darray) to compare with s->board
    // 1:matched,0:!matched
    int match_result_matrix[HEIGHT][WIDTH];
    for (int i = 0; i < HEIGHT; i++)
    {
        for (int j = 0; j < WIDTH; j++)
        {
            match_result_matrix[i][j] = 0;
        }
    }
    int INVISIBLE_HEIGHT = MAXROWS - HEIGHT;
    // round 1: search by row
    for (int i = (MAXROWS - HEIGHT); i < MAXROWS; i++)
    {
        // find_match(s->board[i], match_result_matrix[i - (MAXROWS - HEIGHT)]);
        for (int j = 0; j < WIDTH; j++)
        {
            if (j == 0) // current_tile is at the start
            {
                if ((s->board[i][j] == s->board[i][j + 1]) &&
                    (s->board[i][j] == s->board[i][j + 2]))
                {
                    match_result_matrix[i - INVISIBLE_HEIGHT][j] =
                        match_result_matrix[i - INVISIBLE_HEIGHT][j + 1] =
                            match_result_matrix[i - INVISIBLE_HEIGHT][j + 2] = 1;
                }
            }
            else if (0 < j && j < (WIDTH - 1)) // current_tile is in the middle
            {
                if ((s->board[i][j] == s->board[i][j - 1]) &&
                    (s->board[i][j] == s->board[i][j + 1]))
                {
                    match_result_matrix[i - INVISIBLE_HEIGHT][j] =
                        match_result_matrix[i - INVISIBLE_HEIGHT][j - 1] =
                            match_result_matrix[i - INVISIBLE_HEIGHT][j + 1] = 1;
                }
            }
            else if (j == (WIDTH - 1)) // current_tile is at the end
            {
                if ((s->board[i][j] == s->board[i][j - 2]) &&
                    (s->board[i][j] == s->board[i][j - 1]))
                {
                    match_result_matrix[i - INVISIBLE_HEIGHT][j] =
                        match_result_matrix[i - INVISIBLE_HEIGHT][j - 1] =
                            match_result_matrix[i - INVISIBLE_HEIGHT][j - 2] = 1;
                }
            }
            if (i == (MAXROWS - HEIGHT))
            {
                if (s->board[i][j] == s->board[i + 1][j] &&
                    s->board[i][j] == s->board[i + 2][j])
                {
                    match_result_matrix[i - INVISIBLE_HEIGHT][j] =
                        match_result_matrix[i - INVISIBLE_HEIGHT + 1][j] =
                            match_result_matrix[i - INVISIBLE_HEIGHT + 2][j] = 1;
                }
            }
            else if ((MAXROWS - HEIGHT) < i && i < (MAXROWS - 1)) //"i <= (MAXROWS - 2)"或许是更好的选择
            {
                if (s->board[i][j] == s->board[i - 1][j] &&
                    s->board[i][j] == s->board[i + 1][j])
                {
                    match_result_matrix[i - INVISIBLE_HEIGHT][j] =
                        match_result_matrix[i - INVISIBLE_HEIGHT - 1][j] =
                            match_result_matrix[i - INVISIBLE_HEIGHT + 1][j] = 1;
                }
            }
            else if (i == (MAXROWS - 1))
            {
                if (s->board[i][j] == s->board[i - 1][j] &&
                    s->board[i][j] == s->board[i - 2][j])
                {
                    match_result_matrix[i - INVISIBLE_HEIGHT][j] =
                        match_result_matrix[i - INVISIBLE_HEIGHT - 1][j] =
                            match_result_matrix[i - INVISIBLE_HEIGHT - 2][j] = 1;
                }
            }
        }
    }
    // round 2: search by col
    // for (int i = (MAXROWS - HEIGHT); i < MAXROWS; i++)
    // {
    //     // find_match(s->board[i], match_result_matrix[i - (MAXROWS - HEIGHT)]);
    //     for (int j = 0; j < WIDTH; j++)
    //     {
    //         if (i == (MAXROWS - HEIGHT))
    //         {
    //             if (s->board[i][j] == s->board[i + 1][j] &&
    //                 s->board[i][j] == s->board[i + 2][j])
    //             {
    //                 match_result_matrix[i - INVISIBLE_HEIGHT][j] =
    //                     match_result_matrix[i - INVISIBLE_HEIGHT + 1][j] =
    //                         match_result_matrix[i - INVISIBLE_HEIGHT + 2][j] = 1;
    //             }
    //         }
    //         else if ((MAXROWS - HEIGHT) < i && i < (MAXROWS - 1)) //"i <= (MAXROWS - 2)"或许是更好的选择
    //         {
    //             if (s->board[i][j] == s->board[i - 1][j] &&
    //                 s->board[i][j] == s->board[i + 1][j])
    //             {
    //                 match_result_matrix[i - INVISIBLE_HEIGHT][j] =
    //                     match_result_matrix[i - INVISIBLE_HEIGHT - 1][j] =
    //                         match_result_matrix[i - INVISIBLE_HEIGHT + 1][j] = 1;
    //             }
    //         }
    //         else if (i == (MAXROWS - 1))
    //         {
    //             if (s->board[i][j] == s->board[i - 1][j] &&
    //                 s->board[i][j] == s->board[i - 2][j])
    //             {
    //                 match_result_matrix[i - INVISIBLE_HEIGHT][j] =
    //                     match_result_matrix[i - INVISIBLE_HEIGHT - 1][j] =
    //                         match_result_matrix[i - INVISIBLE_HEIGHT - 2][j] = 1;
    //             }
    //         }
    //     }
    // }

    for (int i = 0; i < HEIGHT; i++)
    {
        for (int j = 0; j < WIDTH; j++)
        {
            if (match_result_matrix[i][j])
            {
                s->board[i + INVISIBLE_HEIGHT][j] = '.';
            }
        }
    }

    // printf("board after matches():\n");
    // print_board(s);
    return true;
}

// print board for check
void print_board(state *s)
{
    for (int i = 0; i < MAXROWS; i++)
    {
        printf("               ");
        for (int j = 0; j < WIDTH; j++)
        {
            printf("%c", s->board[i][j]);
        }
        printf("    [%d]", i);
        printf("\n");
    }
}
void test(void)
{
}
