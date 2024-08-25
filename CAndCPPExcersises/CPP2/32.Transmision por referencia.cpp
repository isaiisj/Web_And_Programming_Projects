#include<iostream>
using namespace std;

void convertir_a_radianes(double&);

int main()
{
    double angulo = 360;
    cout << " El valor del angulo en grado es: " << angulo << endl;
    convertir_a_radianes(angulo);
    cout << " El valor del angulo en radianes es: " << angulo << endl;
    system("pause");
    return 0;
}
void convertir_a_radianes(double& x)
{
     x = x * 3.141592 / 180;
}
