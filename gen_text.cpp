// пример, как это использовать:
#include <iostream>
#include <random> // для std::mt19937
#include <ctime>  // для std::time
using namespace std;
#include <vector>
#include <bitset>

int toBinary(const int n)
{
    return n % 2;
}

vector<int> Bin_vector(const vector<int>& v){
    vector<int> vector_second;

    for (int iter : v)
    {
        vector_second.push_back(toBinary(iter));
    }
    return vector_second;
}

vector<int> Generation_numbers(){
    vector<int>  vector_first;

    // Инициализируем наш вихрь Мерсенна случайным начальным значением на основе часов
    mt19937 mersenne{ static_cast<std::mt19937::result_type>(std::time(nullptr)) };

    // Создаем многоразовый генератор случайных чисел,
    //  который равномерно генерирует числа от 1 до 6
    uniform_int_distribution die{ 1, 5000 };

    cout << "Cлучайная последовательность 10-ой формы:\n";
    // Распечатываем пачку случайных чисел
    for (int count{ 1 }; count <= 128; ++count)
    {
      cout << die(mersenne) ; // здесь генерируем результат броска кубика
      vector_first.push_back(die(mersenne));
    }
    return Bin_vector(vector_first);
}

int main() {
    vector<int>  vector_finish = Generation_numbers();
    cout << "\nБинарная случайная последовательность:\n";
    for(int n : vector_finish)
        cout << n;
    cout << "\nРазмер бинарной случайной последовательности:\n";
    cout << vector_finish.size();
    //запись в файл
    ofstream fout("gen_binary_text.txt");
    for (int i : vector_finish)
    {
        fout << i;
    }
    fout.close();

    return 0;
}




