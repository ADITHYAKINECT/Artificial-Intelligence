#include"connect_4.h"

connect_4::connect_4(bool turn){
    players[0] = AI;
    players[1] = User;
    this->turn = turn;
    board = new string[rows*columns];
    clear();
    display();
}

void connect_4::clear(){
    for(int i=0;i<rows;i++){
        for (int j = 0; j < columns; j++){
            board[columns * i + j] = "_";
        }
    }
}

void connect_4::display(){
    for(int i=0;i<rows;i++){
        for (int j = 0; j < columns; j++){
            cout << board[columns * i + j] << ' ';
        }
        cout <<"\n";
    }
}

void d(string* m){
    for(int i=0;i<rows;i++){
        for (int j = 0; j < columns; j++){
            cout << m[columns * i + j] << ' ';
        }
        cout <<"\n";
    }
}

// returns 0 if the board is full

int connect_4::is_full(string* m){
    return count(m, m + rows * columns, "_");   
}

bool connect_4::check_valid(int pos){
    return ( pos >= 0 && pos < columns );
}
 
bool connect_4::equal_4(string a, string b, string c, string d){
    return ( (a == b) && (b==c) && (c==d) && (a!="_") );
}

string connect_4::check_winner(string* m){
    winner = "\0";
    // check for horizontal steak of four
    for(int i = 0; i < rows;i++){ 
        for (int j = 0; j < columns - 3; j++){
            int cell_id = i * columns + j;
            if( equal_4(m[cell_id],m[cell_id+1],m[cell_id+2],m[cell_id+3]) ){
                winner = m[cell_id];
            }
        }
    }
    // check for vertical steak of four
    for (int i = 0; i < columns; i++){
        for (int j = 0; j < rows - 3; j++){
            int cell_id = j * columns + i;
            if( equal_4(m[cell_id],m[cell_id + columns],
            m[cell_id + 2*columns],m[cell_id + 3*columns]) ){
                winner = m[cell_id];
            }
        }
    }
    // check for negative diagonal steak of four
    for(int i=0; i < rows - 3; i++){
        for(int j=0; j < columns - 3; j++){
            int cell_id = columns * i + j;
            if( equal_4(m[cell_id],m[cell_id+8],m[cell_id+16],m[cell_id+24]) ){
                winner = m[cell_id];
            }
        }
    }
    // check for positive diagonal steak of four
    for(int i=3; i < rows; i++){
        for(int j=0; j < columns-3; j++){
            int cell_id = columns * i + j;
            if( equal_4(m[cell_id],m[cell_id-6],m[cell_id-12],m[cell_id-18]) ){
                winner = m[cell_id];
            }
        }
    } 

    if(is_full(&m[0]) == 0 && winner == "\0"){winner = TIE;}   
    return winner;  
}

void connect_4::placement(int pos,bool turn){
    if(board[pos] != "_"){
        cout<<"Column is full!, please select another column"<<"\n";
        return;
    }
    else{
        for(int i=0;i<rows;i++){
            if(board[columns * (rows-i-1) + pos] == "_"){
                board[columns * (rows-i-1) + pos] = players[turn];
                return;
            }
        }
    }     
}

void connect_4::children(string* m,list<int>* l){
    for(int i = 0;i < columns; i++){
        for (int j = rows - 1; j >= 0; j--){
            int cell_id = columns * j + i;
            if(m[cell_id]=="_"){
                l->push_back(cell_id);
                break;
            }
            else{
                l->remove(cell_id);
            }   
        }
    }
}

int connect_4::minimax(string* m, int depth, string maximizing_player){

    list<int> child_positions;
    list<int>::iterator cit;
    string* child = new string[rows*columns]; ;
    int child_pos;
    string local_winner = check_winner(&m[0]);
    
    if( depth == 0 || (is_full(&m[0]) == 0) ||  local_winner !="\0"){
        if ( local_winner == AI ){return 100000;}
        else if( local_winner == AI ){return -100000;}
        else if ( local_winner == TIE ){return 0;}
        // handle case when depth = 0
    }

    children(&m[0],&child_positions);

    if (maximizing_player == AI){
        p_value = INT_MIN;
        for (cit = child_positions.begin(); cit != child_positions.end(); cit++){
            copy(m->begin(),m->end(),child);
            child[(*cit)] = AI;
            n_value = minimax(&child[0],depth-1,User);
            if(n_value > p_value){
                p_value = n_value;
                child_pos = (*cit);
            }
        }
        return child_pos;
    }

    else{   
        p_value = INT_MAX;
        for (cit = child_positions.begin(); cit != child_positions.end(); cit++){
            copy(m->begin(),m->end(),child);
            child[(*cit)] = User;
            n_value = minimax(&child[0],depth-1,AI);
            if(n_value < p_value){
                p_value = n_value;
                child_pos = (*cit);
            }
        }
        return child_pos;
    }
}

void connect_4::play_game(){
    while (is_full(&board[0])){
        string win = check_winner(&board[0]);
        cout<<win<<"\n";
        // list<int> child_positions;
        // list<int>::iterator cit;
        // children(&board[0],&child_positions);
        // for(cit = child_positions.begin(); cit != child_positions.end(); cit++){
        //     cout<<(*cit)<<" ";
        // }
        cout<<"\n";
        if( win != "\0"){
            cout << win << "\n";
            break;
        }
        else{
            if(!turn){
                cout<<"Enter a number between 0 to 6: "<<"\n";
                cin >> position;
                if(check_valid(position)){
                    placement(position,!turn);
                    turn = !turn;
                } 
            }
            else if(turn){
                // cout<<"Enter a number between 0 to 6: "<<"\n";
                // cin >> position;
                // if(check_valid(position)){
                //     placement(position,!turn);
                //     turn = !turn;
                // }
                position = minimax(&board[0],1,AI);
                board[position] = AI;
                turn = !turn;
            }
            display();
        }
    }
}    

connect_4::~connect_4(){
    cout<<"Have a nice day!"<<endl;
}