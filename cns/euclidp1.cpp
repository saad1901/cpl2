//Euclid's Algorithm
#include <iostream>
using namespace std;

int find_gcd(int a, int b)
{
    float r;
    while(b>0){
        r=a%b;
        a=b;
        b=r;
    }
    return a;
}
int main(){
    int a,b;
    cout<<"Enter a: ";
    cin>>a;
    cout<<"Enter b: ";
    cin>>b;
    cout<<"The gcd(a,b) is: "<<find_gcd(a,b);
}