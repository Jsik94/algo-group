#include <stdio.h>
#include <string.h>

#define MAX_LEN 252

int main() {
    char alpha;
    char str[MAX_LEN];

    while (1) {
        alpha = getchar(); // 문자 입력
        getchar(); // 공백 제거

        if (alpha == '#')  // 종료 조건
            return 0;

        fgets(str, sizeof(str), stdin); // 문자열 입력
        str[strcspn(str, "\n")] = '\0'; // 개행 문자 제거

        int result = 0;
        char lower = (alpha >= 'A' && alpha <= 'Z') ? alpha + 32 : alpha;
        char upper = (alpha >= 'a' && alpha <= 'z') ? alpha - 32 : alpha;

        for (int i = 0; i < strlen(str); i++) { // `sizeof(str)` → `strlen(str)`로 변경
            if (str[i] == alpha || str[i] == lower || str[i] == upper)
                result++;
        }

        printf("%c %d\n", alpha, result);
    }

    return 0;
}
