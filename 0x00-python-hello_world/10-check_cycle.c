#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 *check_cycle - Enter point
 *@list:list
 *Return: 0 suc 1 fil
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
