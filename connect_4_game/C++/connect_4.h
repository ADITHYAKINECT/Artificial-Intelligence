#ifndef CONNECT_4_H
#define CONNECT_4_H
#include<iostream>
#include<vector>
#include<bits/stdc++.h>
#include<string>
// #include <algorithm> 
#define columns 7
#define rows 6
#define AI "O"
#define User "X"
#define TIE "T"
using namespace std;

class connect_4
{
    private:
        
    public:
        connect_4(bool turn);
        string* board;
        string players[2];
        void play_game();
        bool turn;
        int position;
        bool valid;
        bool check_valid(int pos);
        void placement(int pos,bool turn);
        bool equal_4(string a, string b, string c, string d);
        string check_winner(string* m);
        string winner;
        int is_full(string* m);
        int minimax(string* m, int depth, string maximizingPlayer);
        void children(string* m,list<int>* l);
        int p_value,n_value;
        void display();
        void clear();
        ~connect_4();
};

#endif