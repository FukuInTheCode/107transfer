#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>

std::string generateExpression(int length) {
    std::string expression;
    for (int i = 0; i < length; ++i) {
        expression += std::to_string(rand() % 9 + 1);
        if (i < length - 1)
            expression += "*";
    }
    return expression;
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " num_expressions_to_generate max_length_of_each_expression\n";
        return 1;
    }

    int numExpressions = std::atoi(argv[1]);
    int maxLength = std::atoi(argv[2]);

    std::srand(std::time(nullptr));

    std::cout << "./107transfer \"";
    for (int i = 0; i < numExpressions; ++i) {
        int length = rand() % maxLength + 1;
        std::cout << generateExpression(length);
        if (i < numExpressions - 1)
            std::cout << "\" \"";
    }
    std::cout << "\"" << std::endl;

    return 0;
}
