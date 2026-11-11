#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[10];
    char input[100];

    printf("===== BUFFER OVERFLOW ATTACK =====\n");

    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);

    // Remove newline character
    input[strcspn(input, "\n")] = '\0';

    // Check buffer size
    if (strlen(input) >= sizeof(buffer))
    {
        printf("\nBuffer Overflow Condition Detected!\n");
        printf("Input size exceeds buffer capacity.\n");
    }
    else
    {
        strcpy(buffer, input);

        printf("\nInput stored successfully.\n");
        printf("Buffer Content: %s\n", buffer);
    }

    return 0;
}

