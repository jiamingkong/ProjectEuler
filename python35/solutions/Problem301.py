'''
The main idea is describe in this page:

https://en.wikipedia.org/wiki/Nim

So the key here is to figure out a fast way to calculate the Nim-sum. The easiest brute force solution is of course to loop through 2^30 which is about 1b numbers, and find out all those (1n, 2n, 3n) such that 1n^2n^3n == 0. Took 65 seconds on a moderate computer.

But that is just not funny at all.

Now let me solve it paper and pencil:


3n = 2n + n. In binary, 3n will be the n shifted 1 bit and add itself. Now the requirement is n^2n^3n == 0:

so n^2n == 3n:
so n&2n == 0:

so n doesn't have consecutive 1s in its bit form.





'''

from Utilities.fibonacci import fibonacci

print(fibonacci(32))
