#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    int const FILAS = 3;
    int const COLUMNAS = 4;
    int f,c;
    int alumnos [FILAS][COLUMNAS];
    
    for(f=0; f < FILAS; f++)
    {
             for(c=0; c < COLUMNAS; c++)
             {
                      cout << "ingrese el elemento (" << f << "," << c << "): ";
                      cin >> alumnos[f][c];
             }
    }
    for (f=0; f < FILAS; f++)
    {
        cout << endl;
        for(c=0; c < COLUMNAS; c++)
        {
                 cout << setw(4) << alumnos[f][c];
        }
    }
    system("pause");
    return 0;
}
