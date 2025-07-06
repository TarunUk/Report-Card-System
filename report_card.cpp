#include <iostream>
#include <fstream>
using namespace std;

int main() {
    string name;
    int m1, m2, m3;

    cout << "Enter Student Name: ";
    getline(cin, name);

    cout << "Enter marks for 1st subjects: ";
    cin >> m1 ;
	cout << "Enter marks for 2nd subjects: ";
	cin >> m2;
	cout << "Enter marks for 3rd subjects: ";
	cin >> m3;

    ofstream file("student.txt");
    file << name << "\n" << m1 << "\n" << m2 << "\n" << m3;
    file.close();

    cout << "Data saved to student.txt\n";
    return 0;
}
