#include <iostream>
using namespace std;

class car{
    public:
        int x;
        void set();
        void display();
    private:
        int y;
};

void car::set() {
    x = 1.0;
    y = 2.0;
}

void car::display() {
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
}

int main() {
    car a;
    a.set();
    a.display();
    return 0;
}
