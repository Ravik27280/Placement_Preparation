#include<bits/stdc++.h>
using namespace std;
int binarysearch(int a[],int l,int r,int x){
    if (r >= l) {
     int mid = l + (r - l) / 2;

     if (a[mid] == x)
     return x;

     if (a[mid] > x)
     return binarysearch(a, l, mid - 1, x);

     return binarysearch(a, mid + 1, r, x);

    }
    return -1;
}
int main(){
    int n,x;
    cin>>n>>x;
    int a[n];
    for(int i=0;i<=n;i++){
        cin>>a[i];
    }
    sort(a,a+n);
    cout<<binarysearch(a,0,n-1,x);
}