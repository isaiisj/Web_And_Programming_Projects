#include<iostream>
#include<iomanip> //input output manipulacion para manipular los flujos de salida
using namespace std;

int main()
{
    double numero = 78524.2684;
    cout.precision(5);//manipulador de salida metodo cout
    cout << numero << endl;// manipuladores de salida:setfill,setw,setprecision,scientific,showpos,boolalpha,fixed,setiosflag
    system("pause");
}
