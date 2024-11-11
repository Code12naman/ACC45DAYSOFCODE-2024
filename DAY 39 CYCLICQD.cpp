#include <bits/stdc++.h>
using namespace std;

int main() {
	int a,b,c,d,t;
	cin>>t;
	while(t--){
	    cin>>a>>b>>c>>d;
	    if(a+c==180 || b+d==180){
	        cout<<"yes"<<endl;
	    }else{
	        cout<<"no"<<endl;
	    }
	}
	return 0;
}