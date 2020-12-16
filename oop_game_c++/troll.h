#ifndef TROLL_H_
#define TROLL_H_
#include "enemy.h"
#include <bitset>
#include <string>

class Troll: public Enemy {
public:

	Troll(string clan, int start_health, int _attackForce) :
			Enemy(start_health, _attackForce, clan) {
	}
	virtual ~Troll() {

	}
};

class NorthTroll: public Troll {
	static const int c_northTrollHealth = 40;
	static const int c_northTrollAttackForce = 100;
public:

	NorthTroll() :
			Troll("North Troll", c_northTrollHealth, c_northTrollAttackForce) {
	}

	~NorthTroll() {
	}

	string generateQuestion() {
		int number = 1 + rand() % 100;
		string bit_number = bitset<32>(number).to_string();
		stringstream question;
		question << bit_number << " in decimal: ";
		my_answer = number;
		return question.str();
	}
};

#endif /* TROLL_H_ */
