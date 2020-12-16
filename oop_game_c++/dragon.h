#ifndef DRAGON_H_
#define DRAGON_H_

#include <string>
#include <sstream>
#include "enemy.h"
using namespace std;

class Dragon: public Enemy {
public:
	Dragon(string color, int start_health, int _attackForce) :
			Enemy(start_health, _attackForce, color) {
	}
	virtual ~Dragon() {

	}

};

class GreenDragon: public Dragon {
	static const int c_greenDragonHealth = 20;
	static const int c_greenDragonAttackForce = 5;
public:

	GreenDragon() :
			Dragon("Green Dragon", c_greenDragonHealth,
					c_greenDragonAttackForce) {
	}

	~GreenDragon() {
		//delete this;
	}

	string generateQuestion() {
		int left = 1 + rand() % 100;
		int right = 1 + rand() % 100;

		stringstream question;
		question << left << " + " << right << ": ";
		my_answer = left + right;
		return question.str();
	}
};

class RedDragon: public Dragon {
	static const int c_redDragonHealth = 20;
	static const int c_redDragonAttackForce = 10;
public:
	RedDragon() :
			Dragon("Red Dragon", c_redDragonHealth, c_redDragonAttackForce) {

	}

	~RedDragon() {
		//delete this;
	}

	string generateQuestion() {
		int left = 1 + rand() % 100;
		int right = 1 + rand() % 100;

		stringstream question;
		question << left << " - " << right << ": ";
		my_answer = left - right;
		return question.str();
	}

};

class BlackDragon: public Dragon {
	static const int c_blackDragonHealth = 20;
	static const int c_blackDragonAttackForce = 20;
public:
	BlackDragon() :
			Dragon("Black Dragon", c_blackDragonHealth,
					c_blackDragonAttackForce) {

	}

	~BlackDragon() {
	}

	string generateQuestion() {
		int left = 1 + rand() % 100;
		int right = 1 + rand() % 100;

		stringstream question;
		question << left << " * " << right << ": ";
		my_answer = left * right;
		return question.str();
	}

};

#endif /* DRAGON_H_ */
