#include<iostream>
using namespace std;

void calcular_temperaturas(double, double& , double&);

int main()
{
    double centi, fahren, kelvin;
    centi = 25;
    calcular_temperaturas(centi, fahren, kelvin);
    cout << centi << " grados centigrados " << endl;
    cout << fahren << " grados fahrenheit " << endl;
    cout << kelvin << " grados kelvin " << endl;
    system("pause");
    return 0;
}
void calcular_temperaturas(double centi, double& fahren, double& kelvin)
{
     fahren = 1.8 * centi + 32;
     kelvin = centi + 273.15;
}
