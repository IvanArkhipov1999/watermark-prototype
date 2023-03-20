#include <stdio.h>

int main()
{
  int a[200][200], b[200][200], c[200][200], i, j, k, v;
  for (i = 0; i < 200; i++)
  {
    for (j = 0; j < 200; j++)
    {
      a[i][j] = i * j;
    }
  }

  for (i = 0; i < 200; i++)
  {
    for (j = 0; j < 200; j++)
    {
      b[i][j] = i + j;
    }
  }

  for (v = 0; v < 2000; v++)
  {
    for(i = 0; i < 200; i++)
    {
        for(j = 0; j < 200; j++)
        {
      c[i][j] = 0;
      for(k = 0; k < 200; k++)
          c[i][j] += a[i][k] * b[k][j];

        }
    }
  }
  printf("%i\n", c[0][0]);  

  return 0;
}

