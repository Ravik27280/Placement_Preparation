#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,k;
    cin>>n>>k;
    int a[n];
    int count=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        if(a[i]==k){
        cout<<"searched";
        count++;
        break;
       }
    }
    if(count==0){
        cout<<"nope";
    }

}

