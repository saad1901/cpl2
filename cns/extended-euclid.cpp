#include <iostream>
using namespace std;
int main(){
    int a,b;
    cout<<"Enter a: ";
    cin>>a;
    cout<<"Enter b: ";
    cin>>b;
    int r1,r2,s1,s2,t1,t2,r,s,t,k;
    s1=t2=1;
    s2=t1=0;
    r1=a;
    r2=b;
    
    while(r2>0){
        int q= r1/r2;
        r=r1-(q*r2);
        r1=r2;
        r2=r;

        s=s1-(q*s2);
        s1=s2;
        s2=s;

        t=t1-(q*t2);
        t1=t2;
        t2=t;
    }
    cout<<"r1: "<<r1<<endl;
    s=s1;
    t=t1;
    k=s*a+t*b;
    cout<<"k: "<<k;
}