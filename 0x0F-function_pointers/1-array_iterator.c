#include <stdio.h>
#include "function_pointers.h"

/**
 * array_iterator - execute function given as a parameter
 * @array: - array to execute function
 * @size: - size of the array
 * @action: - a pointer to the function you need to use
 *
 * Return: Nothing.
 */
void array_iterator(int *array, size_t size, void (*action)(int))
{
		size_t i;

	if (array && action)
	{
		for (i = 0; i < size; i++)
		{
			action(array[i]);
		}
	}
}
