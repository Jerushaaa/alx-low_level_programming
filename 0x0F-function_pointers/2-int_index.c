#include <stdio.h>
#include "function_pointers.h"

/**
 * int_index - searches for an integer
 * @array: array to serch through
 * @size: is the number of elements in the array
 * @cmp: is a pointer to the function to be used to compare values
 *
 * Return: -1 if no element matches and if size <= 0
 */
int int_index(int *array, int size, int (*cmp)(int))
{
		int i, r;

	if (size > 0 && array && cmp)
	{
		for (i = 0; i < size; i++)
		{
			r = cmp(array[i]);
			if (r)
				break;
		}
		if (i < size)
			return (i);
	}
	return (-1);
}
