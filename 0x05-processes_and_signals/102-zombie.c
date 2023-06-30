#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creating an infinity loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}
/**
 * main - zombie process 5
 * Return: infinite zombies
 */
int main(void)
{
	pid_t idzombie;
	unsigned int j;

	for (j = 0; j < 5; j++)
	{
		idzombie = fork();
		if (idzombie == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", idzombie);
	}
	return (infinite_while());
}
