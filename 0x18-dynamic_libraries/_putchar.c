#include "main.h"
#include <unistd.h>

/**
 * _putchar - write characters
 * @c: The character to print
 *
 * Return: on success one.
 * on error -1 is returned
 */
int _putchar(char c)
{
	return (write(1, &c, 1));
}
