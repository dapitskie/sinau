#include <iostream>
using namespace std;

int biaya(int jantan, int betina) {
    int harga_bebek;
    int total_bebek = jantan + betina;
    
    if (total_bebek < 10) {
        harga_bebek = 100000;
    } else if (total_bebek <= 50) {
        harga_bebek = 75000;
    } else {
        harga_bebek = 50000;
    }

    return harga_bebek * total_bebek;
}

int main() {
    int jantan[4] = {0, 10, 50, 60};
    int betina[4] = {7, 80, 9, 40};

    for (int i = 0; i < 4; i++) {
        int biaya_jantan = biaya(jantan[i], 0);
        int biaya_betina = biaya(betina[i], 0);

        cout << biaya_jantan + biaya_betina << endl;
    }
}
