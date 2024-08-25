#include<iostream>
using namespace std;

int numero = 12;

int main()
{
    int numero = 100;
    cout << " El numero es: " << numero << endl;
    cout << " El numero es: " << ::numero << endl;
    system("pause");
    return 0;
}
