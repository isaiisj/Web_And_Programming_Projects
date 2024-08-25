#include<iostream>
using namespace std;

int main()
{
    double numero;
    double sumatorio;
    int n;
    int i;
    for(n = 1; n <= 3; n = n +1){
          sumatorio = 0;
          cout << "notas del alumno numero" << n << endl;
          for(i = 1; i <= 4; i = i +1){
                cin >> numero;
                sumatorio += numero;
          }
          cout << "promedio del alumno " << n << ": " << (sumatorio / 4) << endl;
    }
    system("pause");
    return 0;
}
