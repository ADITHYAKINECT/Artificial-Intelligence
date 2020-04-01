#include "tictactoe.h"
#define rows 3
#define columns 3

TicTactoe::TicTactoe(){
    player[0] = "X";
    player[1] = "O";
    board = new string[rows*columns];
    clear();
}

bool TicTactoe::equal3(string a, string b, string c){
    if ((a == b) && (b == c) && (a != "_")){
        return true;
    }
    else{
        return false;
    }
}

string TicTactoe::check_winner(string *m){
    winner = "\0";
    for (int i = 0; i < rows; i++){
        if (equal3(m[3 * i], m[3 * i + 1], m[3 * i + 2])){
            winner = m[3 * i];
        }
    }
    for (int i = 0; i < columns; i++){
        if (equal3(m[i], m[i + 3], m[i + 6])){
            winner = m[i];
        }
    }
    if (equal3(m[0], m[4], m[8])){
        winner = m[0];
    }
    if (equal3(m[2], m[4], m[6])){
        winner = m[2];
    }
    if (is_full()){
        winner = "T";
    }
    return winner;
}

void TicTactoe::pos(vector<point*> *positions){
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < columns; j++){
            if (board[columns * i + j] == "_"){
                point *p = new point();
                p->x = i;
                p->y = j;
                positions->push_back(p);
            }
        }
    }
}

void TicTactoe::deep_copy(string *a,string *b){
    for (int i = 0; i < rows*columns; i++){
            a[i] = b[i];
        }
}

bool TicTactoe::is_full(){
    int no_of_empty = 0;
    for (int i = 0; i < rows * columns; i++){
        if (board[i] == "_"){
            no_of_empty++;
        }
    }
    return (no_of_empty == 0);
}

point TicTactoe::minimax(string* m,int depth,bool turn){
  string winner = check_winner(&m[0]);  
  int pvalue,nvalue,a,b;
  vector<point*> p;
  vector<point*>::iterator it;
  point child_position;
    
  if( is_full() || winner != "\0" || depth == 0){
      point reward;
      if (winner == player[0]){
          reward.x = 10;
          reward.y = 0;
      }
      else if (winner == player[0]){
          reward.x = -10;
          reward.y = 0;
      }
      else if (winner == "T"){
          reward.x = 0;
          reward.y = 0;
      }
      return reward;
  }
  
  else if (turn){
      pvalue = -10000;
      pos(&p);
      for(it = p.begin();it!=p.end();it++){  
        a = (*it)->x;
        b = (*it)->y;
        string* temp = new string[rows*columns];
        deep_copy(&temp[0],&m[0]);
        temp[rows * a + b] = player[0];
        nvalue = minimax(&temp[0],depth-1,0).x;
        if(nvalue > pvalue){
            pvalue = nvalue;
            child_position.x = a;
            child_position.y = b;
        }   
    }
        return child_position;
  }

  else{
      pvalue = 10000;
      pos(&p);
      for(it = p.begin();it!=p.end();it++){  
        a = (*it)->x;
        b = (*it)->y;
        string* temp = new string[rows*columns];
        deep_copy(&temp[0],&m[0]);
        temp[rows * a + b] = player[1];
        nvalue = minimax(&temp[0],depth-1,1).x;
        if(nvalue < pvalue){
            pvalue = nvalue;
            child_position.x = a;
            child_position.y = b;
        }      
    }
        return child_position;
  }
}

void TicTactoe::next_turn(bool turn){
    cout << player[turn] << " player's turn\n";
    if (turn == 0){
        point position = minimax(&board[0],5,1);
        x = position.x;
        y = position.y;
    }
    else{
        while (1){
            cout << "Enter the X position: ";
            cin >> x;
            cout << "Enter the Y position: ";
            cin >> y;
            if (board[x * columns + y] == "_"){
                break;
            }else{
                cout << x << ' ' << y << +" is occupied\n";
                cout << player[turn] << " player's turn\n";
                display();
            }
        }
    }
    board[x * columns + y] = player[turn];
    display();
}

void TicTactoe::play_game(bool turn){
    cout << "Game Started"<< "\n";
    while (true){
        string result = check_winner(&board[0]);
        if (result != "\0"){
            if (result == player[0] || result == player[1]){
                cout << "and the winner is " << result << '\n';
            }
            else{
                cout << "The game is Tie\n";
            }
            break;
        }
        else{
            next_turn(turn);
            turn = (turn + 1) % 2;
        }
    }
}

void TicTactoe::clear(){
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < columns; j++){
            board[columns * i + j] = "_";
        }
    }
}

void TicTactoe::display(){
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < columns; j++){
            cout << board[columns * i + j] << " ";
        }
        cout << endl;
    }
    cout << "\n";
}

TicTactoe::~TicTactoe(){
    cout << "Game object deleted\n";
}

