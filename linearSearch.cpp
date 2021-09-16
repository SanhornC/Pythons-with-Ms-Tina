#include<iostream>
#include<vector>
using namespace std;
int arr = {0,0,0,0,0,0}, target = 0;
void linearSearch(arr, target){
	vector<int> vec;
	for (int i=0; i<arr.size(); i++){
		if (arr[i] == target)
			vec.push_back(i);
	}
	
	for (int num: vec)
		cout << num << " ";
}

int main(){
	arr2 = {1,2, 3, 4, 5, 6};
	cout << linearSearch(arr2,6) << endl; 


}
