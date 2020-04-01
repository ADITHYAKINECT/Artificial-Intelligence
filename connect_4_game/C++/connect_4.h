#ifndef CONNECT_4_H
#define CONNECT_4_H
#include<iostream>
#include<vector>
#include<bits/stdc++.h>
#include<string>
#define columns 7
#define rows 6
#define AI "O"
#define User "X"
#define TIE "T"
#define start_address(x) &x[0]

using namespace std;

class connect_4
{
    private:
        string* board;
        string players[2];
        bool turn;
        int position;
        bool valid;
        string winner;
        int p_value,n_value;

        void clear();
        void display(string* m);
        int is_full(string* m);
        bool check_valid(int pos);
        bool equal_4(string a, string b, string c, string d);
        string check_winner(string* m);
        void placement(int pos,bool turn);
        void children(string* m,list<int>* l);
        int minimax(string* m, int depth, string maximizingPlayer);
        int evaluation(string* m);
        int count_steaks(string* m,int no_of_steaks,string playerID);
        
    public:
        connect_4(bool turn);
        void play_game();
        ~connect_4();
};

#endif