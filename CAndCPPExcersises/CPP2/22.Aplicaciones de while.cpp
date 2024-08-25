#include<iostream>
using namespace std;

int main()
{
    double sumatorio = 0;
    double n;
    int i = 0;
    cin >> n; 
    while(n >= 0){
            sumatorio += n;
            i ++;
            cin >> n;
    }
    cout << "promedio :" << (sumatorio / i) << endl;
    system("pause");
    return 0;
}
