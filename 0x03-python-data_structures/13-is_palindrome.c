#include "lists.h"

/**
 * is_palindrome - to check if linked list is a palindrome.
 * @head: pointer to pointer to head
 * Return: 
*/


int is_palindrome(listint_t **head)
{
    char *temp;
    
    if (head == NULL || *head == NULL)
    {
        return 0;

    }
    temp = head->next;

    printf("%s", temp);
    return 0;
}
