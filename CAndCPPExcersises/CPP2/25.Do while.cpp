#include<iostream>
using namespace std;

int main()
{
    int num;
    do
    {
        cout << "Introduzca un numero del 1 al 10; " << endl;
        cin >> num;
       }
    while(num < 1 || num > 10);
    cout << "El numero ingresado es " << num << endl;
    system("pause");
    return 0;
}
//teorema de demorgan/*
