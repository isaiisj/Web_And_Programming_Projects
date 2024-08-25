#include<iostream>
using namespace std;

int main()
{
    int codigo = 5;
    switch(codigo)
    {
        case 2: // la variable codigo toma un valor/*
             cout << "Es de america" << endl;
             break;
        case 3:
             cout << "Es de europa" << endl;
             break;
        case 4:
             cout << "Es de asia" << endl;
             break;
        default://por defecto/*
                cout << "Indefinido" << endl;
    }
    system("pause");
    return 0;
}
