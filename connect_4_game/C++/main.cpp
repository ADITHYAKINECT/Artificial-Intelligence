#include"connect_4.h"

int main(){
    cout<<"Enter 1 for first turn or else 0: ";
    bool turn;
    cin>> turn;
    connect_4* game = new connect_4(turn);
    game->play_game();
    delete game;
    return 0;
}