#ifndef UNIT_H_
#define UNIT_H_

class Unit {
protected:
	int health;
public:
	int attackForce;

	Unit(int start_health, int _attackForce) :
			health(start_health), attackForce(_attackForce) {
	}
	void getDamage(int damage) {
		health -= damage;
	}
	int getHealth() const {
		return health;
	}
	bool isAlive() const {
		return (health > 0);
	}
};

#endif /* UNIT_H_ */
