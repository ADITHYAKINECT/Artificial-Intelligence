#include"tictactoe.h"

void playGame(bool player_turn){
    TicTactoe* game = new TicTactoe();
    game->play_game(player_turn);
    delete game;
}

int main(){
    bool player_turn;
    cout<<"Enter 1 for first move or else 0: ";
    cin>> player_turn;
    playGame(player_turn);
    return 0;
}