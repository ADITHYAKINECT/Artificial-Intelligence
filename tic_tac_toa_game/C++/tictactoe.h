#ifndef TICTACTOE_H
#define TICTACTOE_H

#include<vector>
#include<string>
#include<bits/stdc++.h>
#include<iostream>
using namespace std;

struct point{
    int x;
    int y;
};

class TicTactoe
{
    private:
        string* board;
        string player[2];
        int x,y;
        bool turn;
        string winner;
        
        bool equal3(string a,string b,string c);
        string check_winner(string* m);
        void pos(vector<point*> *positions);
        void deep_copy(string *a,string *b);
        bool is_full();
        point minimax(string* m,int depth,bool turn);
        void next_turn(bool turn);
        void clear();
        void display();
        
    public:
        TicTactoe();
        void play_game(bool turn);
        ~TicTactoe();
};

#endif