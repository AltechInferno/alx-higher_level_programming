#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;
	while (next = current->next)
	{
		current->next = prev;
		prev = current;
		current = next;
	}
	current->next = prev;
	*head = current;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	dup = slow->next;
	reverse_listint(&dup);
	while (dup && temp)
	{
		if (temp->n != dup->n)
			return (0);
		dup = dup->next;
		temp = temp->next;
	}
	return (1);
}
