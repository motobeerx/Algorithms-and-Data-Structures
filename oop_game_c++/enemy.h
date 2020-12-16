#ifndef ENEMY_H_
#define ENEMY_H_

#include "unit.h"
#include <iostream>
using namespace std;

class Enemy: public Unit {
protected:
	int my_answer;
	string my_type;
public:
	static const int c_killScores = 100;

	Enemy(int start_health, int _attackForce, string type) :
			Unit(start_health, _attackForce), my_type(type) {

	}
	virtual ~Enemy() {

	}

	virtual string generateQuestion() = 0;

	bool checkAnswer(int answer) const {
		return answer == my_answer;
	}
	string type() const {
		return my_type;
	}

};

#endif
