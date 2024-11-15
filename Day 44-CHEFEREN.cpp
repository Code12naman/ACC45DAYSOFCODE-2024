#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	
	while(t--){
	    int A,B,n,sum=0;
	    cin>>n>>A>>B;
	    for(int i=1;i<=n;i++){
	        if(i%2==0){
	            sum+=A;
	        }else{
	            sum+=B;
	        }
	    }
	    cout<<sum<<endl;
	    }
	return 0;
}

