#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a[n];
    int min=999;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
   for(int i=0;i<n;i++){
       if(a[i]<min){
           min=a[i];
       }
   }
   cout<<min;
}