#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>

using namespace std;

// ==========================================
// 1. CÁC HÀM SINH DÃY FIBONACCI
// ==========================================

// a. Thuật toán đệ quy (Recursive)
long long fibRecursive(int n) {
    if (n <= 0)
        return 0;

    if (n == 1)
        return 1;

    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

vector<long long> generateFibRecursive(int N) {
    vector<long long> result;

    for (int i = 0; i < N; i++) {
        result.push_back(fibRecursive(i));
    }

    return result;
}


// b. Thuật toán vòng lặp (Iterative)
vector<long long> generateFibIterative(int N) {
    if (N <= 0)
        return {};

    if (N == 1)
        return {0};

    vector<long long> result = {0, 1};

    for (int i = 2; i < N; i++) {
        result.push_back(result[i - 1] + result[i - 2]);
    }

    return result;
}


// ==========================================
// 2. HÀM ĐO LƯỜNG VÀ IN BÁO CÁO
// ==========================================

void measureSequentialTimes(int maxN) {

    cout << "BAO CAO THOI GIAN CHAY THUC TU 1 DEN "
         << maxN << " (Don vi: ms)\n\n";

    cout << left
         << setw(6) << "N"
         << " | "
         << setw(25) << "Vong lap (Iterative)"
         << " | "
         << "De quy (Recursive)"
         << endl;

    cout << string(60, '-') << endl;


    // Chạy N từ 1 đến maxN
    for (int N = 1; N <= maxN; N++) {

        // ----------------------------------
        // Đo thời gian Iterative
        // ----------------------------------

        auto startIterative = chrono::high_resolution_clock::now();

        generateFibIterative(N);

        auto endIterative = chrono::high_resolution_clock::now();

        double timeIterative =
            chrono::duration<double, milli>(
                endIterative - startIterative
            ).count();


        // ----------------------------------
        // Đo thời gian Recursive
        // ----------------------------------

        auto startRecursive = chrono::high_resolution_clock::now();

        generateFibRecursive(N);

        auto endRecursive = chrono::high_resolution_clock::now();

        double timeRecursive =
            chrono::duration<double, milli>(
                endRecursive - startRecursive
            ).count();


        // ----------------------------------
        // In kết quả
        // ----------------------------------

        cout << fixed << setprecision(4);

        cout << left
             << setw(6) << N
             << " | "
             << setw(25) << timeIterative
             << " | "
             << timeRecursive
             << endl;
    }

    cout << string(60, '-') << endl;

    cout << "Hoan thanh qua trinh do luong!" << endl;
}


// ==========================================
// 3. HÀM MAIN
// ==========================================

int main() {

    // Chạy thực tế từ N = 1 đến N = 40
    measureSequentialTimes(40);

    return 0;
}