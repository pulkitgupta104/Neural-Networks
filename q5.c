#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int S[5][12] = {{1,1,1,1,-1,1,1,1,1,1,-1,1},
				   {1,1,1,1,1,1,1,-1,1,1,1,1},
				   {1,1,1,1,-1,-1,1,-1,-1,1,1,1},
				   {1,1,1,1,-1,1,1,-1,1,1,1,1},
				   {1,1,1,1,1,1,1,-1,-1,1,1,1}	};
	int S_T[12][5], sum=0, W[12][12];
	for (int i = 0; i < 12; ++i)
		for (int j = 0; j < 5; ++j)
			S_T[i][j] = S[j][i];
	
	for (int i = 0; i < 12; ++i)
		for (int j = 0; j < 12; ++j)
		{
			for (int k = 0; k < 5; ++k)
				sum += S_T[i][k] * S[k][j];
			W[i][j] = sum;
			sum = 0;
		}

	for (int i = 0; i < 12; ++i)
	{
		for (int j = 0; j < 12; ++j)
			printf("%d\t", W[i][j]);
		printf("\n");
	}
	return 0;
}