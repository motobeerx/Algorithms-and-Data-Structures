#ifndef HERO_H_
#define HERO_H_

#include <string>
#include <iostream>
#include "dragon.h"
#include "troll.h"
using namespace std;

class Hero: public Unit {
	int scores;
public:
	static const int default_health = 100;
	static const int default_attackForce = 20;

	Hero(int health = default_health, int aForce = default_attackForce) :
			Unit(health, aForce), scores(0) {
	}
	void attack(Enemy &enemy) {

		string q = enemy.generateQuestion();

		std::cout << "question: " << q;
		int answer;
		std::cin >> answer;
		if (enemy.checkAnswer(answer)) {
			enemy.getDamage(attackForce);
			std::cout << "Hit you, dragon!" << std::endl;
		} else {
			getDamage(enemy.attackForce);
			std::cout << "Hero suffers..." << std::endl;
		}
	}

	int getScores() {
		return scores;
	}

	void addScores(int score_for_kill) {
		scores += score_for_kill;
	}
};

#endif /* HERO_H_ */
