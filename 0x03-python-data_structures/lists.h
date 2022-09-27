#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

#define fi if
#define __local __attribute__((weak))

typedef unsigned int uint;

/**
 * enum rets - yes no values
 * @yes: 1
 * @no: 0
 */
enum rets
{
	no,
	yes
};

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;

