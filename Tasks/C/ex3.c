#include <stdio.h>
#include <stdbool.h> // booleans lib

int main() {

    // comments section
    /* another way to represent a comment line */

    /* 
    variable = reusable container for a value.
               behaves as if it were the values it contains.

     int = whole numbers (4 bytes in modern systems)
     float = single-precision decimal number (4 bytes)
     double = double-precision decimal number (8 bytes)
     char = single character (1 byte)
     char[] = array of characters (size varies)
     bool = true or false (1 byte, requires <stdbool.h>)

    Format specifier = Special tokens that begin with a % symbol,
    followed by a character that specifies the data type
    and optional modifiers (width, precision, flags).
    They control how data is displayed or interpreted.
    */


    int age = 25;                   // %d "integer or decimal numbers"
    int year = 2025;                
    int quantity = 3;

    float gpa = 5.6; // -> gpa is grade point average
    float price = 1.99;             // %f  "float numbers"

    double pi = 3.14159265358979;   // %lf "longfloat" BUT %f works too
    double e  = 2.71828182845904;

    char symbol = 'S';               // %c "single symbol"
    char grade[] = "MM";             // %s "string" a array of caracters
    char name[] = "PWD";

    bool isOnline = false;            // %d "booleans"
    /* false = 0 and true = 1 */

    printf("You are %d years old \n", age);
    printf("The year is %d, is the %c year \n", year, symbol);
    printf("I'm buying %d products, thats costs %.2f each \n", quantity, price);
    printf("Your gpa is %.1f, this means that your actual grade is %s  \n", gpa, grade);
    printf("The value os pi is %.14lf and the value of e is %.14lf \n", pi, e);

    if(isOnline){
        printf("The user %s is Online", name);
    }
    else{
        printf("The user %s is Offline", name);
    }

    return 0;
}