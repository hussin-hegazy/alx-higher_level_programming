#include "lists.h"

/**
 * reverse_linked_list - Reverses a linked list
 * @first_node: Pointer to the first node in the list
 *
 * Return: Pointer to the first node in the reversed list
 */
void reverse_linked_list(listint_t **first_node)
{
	listint_t *previous = NULL;
	listint_t *current = *first_node;
	listint_t *next_node = NULL;

	while (current)
	{
		next_node = current->next;
		current->next = previous;
		previous = current;
		current = next_node;
	}

	*first_node = previous;
}

/**
 * check_palindrome - Checks if a linked list is a palindrome
 * @first_node: Double pointer to the linked list
 *
 * Return: 1 if it is a palindrome, 0 if not
 */
int check_palindrome(listint_t **first_node)
{
	listint_t *slow_ptr = *first_node, *fast_ptr = *first_node, *temp_ptr = *first_node, *duplicate = NULL;

	if (*first_node == NULL || (*first_node)->next == NULL)
		return (1);

	while (1)
	{
		fast_ptr = fast_ptr->next->next;
		if (!fast_ptr)
		{
			duplicate = slow_ptr->next;
			break;
		}
		if (!fast_ptr->next)
		{
			duplicate = slow_ptr->next->next;
			break;
		}
		slow_ptr = slow_ptr->next;
	}

	reverse_linked_list(&duplicate);

	while (duplicate && temp_ptr)
	{
		if (temp_ptr->n == duplicate->n)
		{
			duplicate = duplicate->next;
			temp_ptr = temp_ptr->next;
		}
		else
			return (0);
	}

	if (!duplicate)
		return (1);

	return (0);
}
