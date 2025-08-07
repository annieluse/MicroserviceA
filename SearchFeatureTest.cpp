#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){

    string user_input;

    cout << "Please enter the video game you wish to search for: " << endl;
    getline(cin, user_input);

    //Indirect communication - process execution 
    string command = "python3 SearchFeature.py \"" + user_input + "\"";
    system(command.c_str());

    return 0;

}