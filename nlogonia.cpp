#include <iostream>
using namespace std;
int main() {
	int casas;
	int divisa_x, divisa_y;
	int casa_x, casa_y;

	cin >> divisa_x >> divisa_y;
	for (int numero_casa=0; numero_casa < casas; numero_casa++) {
		cin >> casa_x >> casa_y;
		cout << casa_x << " " << casa_y << "\n";
	}
	return 0;
}

