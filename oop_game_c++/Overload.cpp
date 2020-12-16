#include <sstream>
#include <cstdlib>
#include <list>

#include "hero.h"

using namespace std;

void showHealth(const Hero &hero, const Dragon &enemy) {
	cout << "Hero health: " << hero.getHealth() << ", Dragon health: "
			<< enemy.getHealth() << endl;
}

list<Enemy*> generateDragonList() {
	list<Enemy*> competitors;
	competitors.push_back(new GreenDragon());
	competitors.push_back(new RedDragon());
	competitors.push_back(new BlackDragon());
	competitors.push_back(new NorthTroll());

	return competitors;
}

bool playGame(Hero &hero, list<Enemy*> &enemies) {
	bool gameOver = false;

	for (list<Enemy*>::iterator enemy = enemies.begin(); enemy != enemies.end();
			enemy++) {
		cout << "You have met a new beast. " << (*enemy)->type() << ". Fight!"
				<< endl;

		while ((*enemy)->isAlive() && hero.isAlive()) {
			hero.attack(**enemy);
		}
		if (!hero.isAlive()) {
			gameOver = true;
			break;
		} else // dragon was killed!
		{
			hero.addScores(Enemy::c_killScores);
			cout << "Ough! You have killed a dragon!" << endl;
		}
	}
	return gameOver;
}

int main() {
	Hero hero;
	list<Enemy*> enemies = generateDragonList();
	bool gameResult = playGame(hero, enemies);

	if (gameResult) {
		cout << "Game over! Your score is: " << hero.getScores() << endl;
	} else {
		cout << "You win! Your score is: " << hero.getScores() << endl;
	}
	for (list<Enemy*>::iterator dragon = enemies.begin();
			dragon != enemies.end(); dragon++) {
		delete *dragon;
	}

	return 0;
}

