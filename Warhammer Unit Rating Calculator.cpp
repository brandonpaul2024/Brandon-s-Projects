#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;
using std::cout;
using std::cin;

int main()
{
	int userchoice;
	string modelname;
	int points;
	int toughness;
	int armorsave;
	int invulnsave;
	int rangestrg;
	int model;
	int woundcount;
	int range;
	int damage;
	int movement;
	int bonuspoints;
	int score;
	int tscore;
	int ascore;
	int wscore;
	int iscore;
	int rscore;
	int rascore;
	int dscore;
	int mscore;
	int extrascore;
	int totalscore;
	int fly = 30;
	int twinlinked = 30;
	int devastingwounds = 20;
	int sustainedhits = 15;
	int lethalhits = 15;
	int feelnopain = 20;
	int fightfirst =25;
	int none = 0;





	cout << "Rating scale for entries.\n";
	cout << "Grade A range = Excellent.\n";
	cout << "Grade B range = Good.\n";
	cout << "Grade C range = Average.\n";
	cout << "Grade D range = Poor.\n";
	cout << "Enter the name of unit/model name.\n";
	cin >> modelname;
	cout << "Enter point cost for unit.\n";
	cin >> points;

	cout << "Enter the toughness of the unit.\n";
	cin >> toughness;
	if (toughness >= 12)
	{
		cout << "Grade A on toughness rating.\n";
		tscore = 55;
	}
	else if (toughness <= 11 && toughness >= 10)
	{
		cout << "Grade A- on toughness rating.\n";
		tscore = 50;
	}
	else if (toughness == 9)
	{
		cout << "Grade B+ on toughness rating.\n";
		tscore = 45;
	}
	else if (toughness <= 8 && toughness >= 7)
	{
		cout << "Grade B on toughness rating.\n";
		tscore = 40;
	}
	else if (toughness == 6)
	{
		cout << "Grade B- on toughness rating.\n";
		tscore = 35;
	}
	else if (toughness == 5)
	{
		cout << "Grade C+ on toughness rating.\n";
		tscore = 30;
	}
	else if (toughness == 4)
	{
		cout << "Grade C on toughness rating.\n";
		tscore = 25;
	}
	else if (toughness <= 3)
	{
		cout << "Grade D on toughness rating.\n";
		tscore = 10;
	}

	cout << "Enter the armor save of the unit.\n";
	cin >> armorsave;
	if (armorsave <= 2)
	{
		cout << "Grade A on armor rating.\n";
		ascore = 55;
	}
	else if (armorsave == 3)
	{
		cout << "Grade B on armor rating.\n";
		ascore = 40;
	}
	else if (armorsave == 4)
	{
		cout << "Grade C on armor rating.\n";
		ascore = 25;
	}
	else if (armorsave == 5)
	{
		cout << "Grade D on armor rating.\n";
		ascore = 10;
	}
	else if (armorsave >= 6)
	{
		cout << "Grade F on armor rating.\n";
		ascore = 0;
	}

	cout << "Enter the wound count of the model.\n";
	cin >> woundcount;
	if (woundcount >= 24)
	{
		cout << "Grade A+ on wound count.\n";
		wscore = 60;
	}
	else if (woundcount <= 23 && woundcount >= 18)
	{
		cout << "Grade A on wound count.\n";
		wscore = 55;
	}
	else if (woundcount <= 17 && woundcount >= 13)
	{
		cout << "Grade B+ on wound count.\n";
		wscore = 45;
	}
	else if (woundcount <= 12 && woundcount >= 8)
	{
		cout << "Grade B on wound count.\n";
		wscore = 40;
	}
	else if (woundcount <= 7 && woundcount >= 5)
	{
		cout << "Grade C+ on wound count.\n";
		wscore = 30;
	}
	else if (woundcount <= 4 && woundcount >= 3)
	{
		cout << "Grade C on wound\n";
		wscore = 25;
	}
	else if (woundcount < 2)
	{
		cout << "Grade D on wound\n";
		wscore = 10;
	}


	cout << "Enter the invulnerable save of the unit.\n";
	cin >> invulnsave;
	if (invulnsave == 0)
	{
		cout << "Grade F on invulnerable rating.\n";
		iscore = 0;
	}
	else if (invulnsave <= 3)
	{
		cout << "Grade A+ on invulnerable rating.\n";
		iscore = 60;
	}
	else if (invulnsave == 4)
	{
		cout << "Grade A on invulnerable rating.\n";
		iscore = 55;
	}
	else if (invulnsave == 5)
	{
		cout << "Grade C on invulnerable rating.\n";
		iscore = 25;
	}
	else if (invulnsave == 6)
	{
		cout << "Grade D on invulnerable rating.\n";
		iscore = 10;
	}
	else if (invulnsave >= 7)
	{
		cout << "Grade F on invulnerable rating.\n";
		iscore = 0;
	}

	cout << "Enter the stregnth characteristic of the main range weapon.\n";
	cin >> rangestrg;
	if (rangestrg >= 12)
	{
		cout << "Grade A+ on ranged weapons strength.\n";
		rscore = 60;
	}
	else if (rangestrg < 11 && rangestrg >= 10)
	{
		cout << "Grade A on ranged weapons strength.\n";
		rscore = 55;
	}
	else if (rangestrg <= 9 && rangestrg >= 8)
	{
		cout << "Grade B on Ranged weapons strength.\n";
		rscore = 40;
	}
	else if (rangestrg <= 7 && rangestrg >= 5)
	{
		cout << "Grade C+ on Ranged weapons strength.\n";
		rscore = 30;
	}
	else if (rangestrg == 4)
	{
		cout << "Grade C on Ranged weapons strength.\n";
		rscore = 25;
	}
	else if (rangestrg <= 3)
	{
		cout << "Grade F on Ranged weapons strength.\n";
		rscore = 0;
	}

	cout << "Enter Range for primary weapon\n";
	cin >> range;
	if (range >= 36)
	{
		cout << "Grade A on weapon range.\n";
		rascore = 55;
	}
	else if (range <= 35 && range >= 24)
	{
		cout << "Grade B on weapon range.\n";
		rascore = 40;
	}
	else if (range <= 23 && range >= 18)
	{
		cout << "Grade C on weapon range.\n";
		rascore = 25;
	}
	else if (range <= 17 && range >= 12)
	{
		cout << "Grade D on weapon range.\n";
		rascore = 10;
	}
	else if (range <= 11)
	{
		cout << "Grade F on weapon range.\n";
		rascore = 0;
	}

	cout << "Enter damage output of main weapon. If D6 enter 66. If D3 enter 33.\n";
	cin >> damage;
	if (damage >= 6 && damage < 30)
	{
		cout << "Grade A on damage output.\n";
		dscore = 55;
	}
	else if (damage >= 3 && damage <= 5)
	{
		cout << "Grade B on damage output.\n";
		dscore = 40;
	}
	else if (damage == 66)
	{
		cout << "Grade B- on damage output.\n";
		dscore = 35;
	}
	else if (damage == 2)
	{
		cout << "Grade C on damage output.\n";
		dscore = 25;
	}
	else if (damage == 33)
	{
		cout << "Grade C on damage output.\n";
		dscore = 25;
	}
	else if (damage == 1)
	{
		cout << "Grade D on damage output.\n";
		dscore = 10;
	}

	cout << "Enter the units movement.\n";
	cin >> movement;
	if (movement > 14)
	{
		cout << "Grade A+ on movement.\n";
		mscore = 60;
	}
	else if (movement <= 13 && movement >= 12)
	{
		cout << "Grade A on movement.\n";
		mscore = 55;
	}
	else if (movement <= 11 && movement >= 10)
	{
		cout << "Grade B+ on movement.\n";
		mscore = 45;
	}
	else if (movement <= 9 && movement >= 8)
	{
		cout << "Grade B on movement.\n";
		mscore = 40;
	}
	else if (movement <= 7 && movement >= 6)
	{
		cout << "Grade C on movement.\n";
		mscore = 25;
	}
	else if (movement == 5)
	{
		cout << "Grade C- on movement.\n";
		mscore = 20;
	}
	else if (movement < 4)
	{
		cout << "Grade F on movement.\n";
		mscore = 0;
	}

	cout << "Enter in select keywords from list below.\n";
	cout << "fly, twinlinked, devastatingwounds, sustainedhits, lethalhits, feelnopain, fightfirst, or none. \n";
	cin >> userchoice;
	if (userchoice == fly)
	{
		extrascore = 30;
	}
	else if (userchoice == twinlinked)
	{
		extrascore = 30;
	}
	else if (userchoice == devastingwounds)
	{
		extrascore = 20;
	}
	else if (userchoice == sustainedhits)
	{
		extrascore = 15;
	}
	else if (userchoice == lethalhits)
	{
		extrascore = 15;
	}
	else if (userchoice == feelnopain)
	{
		extrascore = 20;
	}
	else if (userchoice == fightfirst)
	{
		extrascore = 25;
	}
	else if (userchoice == none)
	{
		extrascore = 0;
	}
	else if (userchoice != fly, twinlinked, devastingwounds, sustainedhits, lethalhits, feelnopain, fightfirst, none)
	{
		extrascore == 0;
		cout << "Please write one of the keywords above exactly." << userchoice << std::endl;
	}
	{
		totalscore = extrascore + tscore + ascore + wscore + iscore + rscore + rascore + dscore + mscore;
	}
	cout << "Total Score is....";
	cout << totalscore << "\n";
	if (totalscore >= 400)
	{
		cout << modelname;
		cout << " overall score is an A.";
	}
	else if (totalscore >= 280 && totalscore <= 399)
	{
		cout << modelname; 
		cout << " overall score is a B.";
	}
	else if (totalscore >= 160 && totalscore <= 279)
	{
		cout << modelname; 
		cout << " overall score is a C.";
	}
	else if (totalscore >= 40 && totalscore <= 159)
	{
		cout << modelname; 
		cout << " overall score is a D.";
	}
	else if (totalscore <= 39)
	{
		cout << modelname; 
		cout << " overall score is an F.";
	}
	
	
	return 0;
}

