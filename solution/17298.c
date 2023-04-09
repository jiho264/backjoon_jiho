#include <stdio.h>
int a[1000000] = {0};
int ans[1000000] = {0};
int stack[1000000] = {0};
int n, k, top = -1;
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &k);
        a[i] = k;
        ans[i] = -1;
    }

    for (int i = n - 1; i >= 0; i--)
    {
        while (top != -1 && stack[top] <= a[i])
            top--;
        if (top != -1)
            ans[i] = stack[top];
        stack[++top] = a[i];
    }

    for (int i = 0; i < n; i++)
        printf("%d ", ans[i]);
}