#include <iostream>
#include <stdlib.h>
#include <thread>

#ifndef _WIN32
#include <openssl/rand.h>
#include <cstring>
#include <memory>
#else
#include <windows.h>
#include <Wincrypt.h>
#endif

#define MAX_ARG_LEN 256
#define MAX 100
#define MIN 1

using namespace std;

#ifndef _WIN32
int rand_int() {
    unsigned char * rand_msg = new unsigned char[4];
    int rc = RAND_bytes(rand_msg, 4);
    if(rc == 0) {
        cerr << "crypto: failed." << endl;
        exit(EXIT_FAILURE);
    }
    int x = (rand_msg[3] << 24) | (rand_msg[2] << 16) | (rand_msg[1] << 8) | (rand_msg[0]); 
    free(rand_msg);
    return x;
}
#else
int rand_int() {
    int x = -1;
    HCRYPTPROV hCryptProv;
    BYTE pbData[4];
    if (CryptAcquireContext(&hCryptProv, NULL, "Microsoft Base Cryptographic Provider v1.0", PROV_RSA_FULL, CRYPT_VERIFYCONTEXT)) {
        if (CryptGenRandom(hCryptProv,4,pbData)) {
            x = (pbData[3] << 24) | (pbData[2] << 16) | (pbData[1] << 8) | (pbData[0]); 
            // delete rand_msg;
        }
    }
    if(x == -1) {
        cerr << "crypto: failed." << endl;
        exit(EXIT_FAILURE);
    }
    return x;
}
#endif

class Player {
  private:
    string name;        
    int wins;       
  public:   
    Player(string n) {
        name = n;
        wins = 0;
    }         
    int get_wins(){
        return wins;
    }
    void incr_wins(){
        wins++;
    }
    string get_name(){
        return name;
    }
    
};

int safe_atoi(char * arg) {
	char * tmp;
	if(!(tmp = new char[MAX_ARG_LEN])) {
		perror("new");
		exit(EXIT_FAILURE);
	}
	strncpy(tmp, arg, MAX_ARG_LEN);
	int z = atoi(tmp);
	free(tmp);
	return z;
}

int rand_int_in_range(int min, int max) {
	int r = rand_int();
	if(r < 0) {
		r = r * -1;
	}
    return min + ( r % ( max - min + 1 ) );
}

string arg_copy(char * arg) {
	char * tmp = new char[MAX_ARG_LEN];
	strncpy(tmp, arg, MAX_ARG_LEN);
	string ret(tmp);
	free(tmp);
	return ret;
}

int play_round(Player ** players, int winning) {
	int losing = 1 - winning;
    int w_roll = rand_int_in_range(MIN, MAX);
    cout << "\t" << players[winning]->get_name() << " (the current winner) rolled a " << w_roll << endl;
    bool game_over = false;
    while(!game_over) {
        int new_roll = rand_int_in_range(MIN, MAX);
        cout << "\t" << players[losing]->get_name() << " (the current loser) rolled a " << new_roll << endl;
        if(new_roll < w_roll) {
            int tmp = winning;
            winning = losing;
            losing = tmp;
            w_roll = new_roll;
        } else {
            players[winning]->incr_wins();
            game_over = true;
        } 
    }
    cout << "\t" << players[winning]->get_name() << " Wins!" << std::endl;    
	cout << endl;
	return winning;
}

int main(int argc, char ** argv) {
	if(argc != 4) {
		cerr << "Usage: " << argv[0] << " <name1> <name2> <rounds>" << endl;
		exit(EXIT_FAILURE);
	}
	
	Player ** players = new Player*[2];
	players[0] = new Player(arg_copy(argv[1]));
	players[1] = new Player(arg_copy(argv[2]));
    int rounds = safe_atoi(argv[3]);
    int winning = rand_int_in_range(MIN, MAX) % 2;

    cout << "Starting randomly with " << players[winning]->get_name() << "." << endl;
    for(int i = 0; i < rounds; i++) {
    	cout << "Round " << i << ":" << endl;
    	winning = play_round(players, winning);
    }

    for(int i = 0; i < 2; i++) {
    	cout << players[i]->get_name() << " has " << players[i]->get_wins() << " wins." << endl;
	}
}
