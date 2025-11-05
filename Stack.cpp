Implement stack as an abstract data type and use this ADT for conversion of infix expression to postfix, prefix and evaluation of postfix and prefix expression.

#include <iostream>
using namespace std;

#define SIZE 50

class Stack {
    char a[SIZE]; int top;
public:
    Stack() { top = -1; }
    void push(char x) { a[++top] = x; }
    char pop() { return a[top--]; }
    char peek() { return a[top]; }
    bool empty() { return top == -1; }
};

int prec(char c) {
    if (c=='^') return 3;
    if (c=='*'||c=='/') return 2;
    if (c=='+'||c=='-') return 1;
    return -1;
}

void reverse(char exp[]) {
    int n = 0; while (exp[n] != '\0') n++;
    for (int i = 0; i < n/2; i++) swap(exp[i], exp[n-i-1]);
}

void infixToPostfix(char in[], char post[]) {
    Stack s; int k = 0;
    for (int i = 0; in[i] != '\0'; i++) {
        char c = in[i];
        if ((c >= '0' && c <= '9') || (c >= 'A' && c <= 'Z'))
            post[k++] = c;
        else if (c == '(') s.push(c);
        else if (c == ')') {
            while (!s.empty() && s.peek() != '(')
                post[k++] = s.pop();
            s.pop();
        } else {
            while (!s.empty() && prec(c) <= prec(s.peek()))
                post[k++] = s.pop();
            s.push(c);
        }
    }
    while (!s.empty()) post[k++] = s.pop();
    post[k] = '\0';
}

void infixToPrefix(char in[], char pre[]) {
    reverse(in);
    for (int i = 0; in[i] != '\0'; i++) {
        if (in[i] == '(') in[i] = ')';
        else if (in[i] == ')') in[i] = '(';
    }
    infixToPostfix(in, pre);
    reverse(pre);
}

int evalPostfix(char exp[]) {
    int st[SIZE], top = -1;
    for (int i = 0; exp[i] != '\0'; i++) {
        char c = exp[i];
        if (c >= '0' && c <= '9') st[++top] = c - '0';
        else {
            int b = st[top--], a = st[top--];
            if (c=='+') st[++top]=a+b;
            else if (c=='-') st[++top]=a-b;
            else if (c=='*') st[++top]=a*b;
            else if (c=='/') st[++top]=a/b;
        }
    }
    return st[top];
}

int evalPrefix(char exp[]) {
    int st[SIZE], top = -1;
    reverse(exp);
    for (int i = 0; exp[i] != '\0'; i++) {
        char c = exp[i];
        if (c >= '0' && c <= '9') st[++top] = c - '0';
        else {
            int a = st[top--], b = st[top--];
            if (c=='+') st[++top]=a+b;
            else if (c=='-') st[++top]=a-b;
            else if (c=='*') st[++top]=a*b;
            else if (c=='/') st[++top]=a/b;
        }
    }
    return st[top];
}

int main() {
    char in[50], post[50], pre[50];
    cout << "Enter Infix: ";
    cin >> in;

    infixToPostfix(in, post);
    infixToPrefix(in, pre);

    cout << "Postfix: " << post << "\n";
    cout << "Prefix: " << pre << "\n";
    cout << "Postfix Eval: " << evalPostfix(post) << "\n";
    cout << "Prefix Eval: " << evalPrefix(pre) << "\n";
}


OUTPUT:
Enter Infix: 2+3*4
Postfix: 234*+
Prefix: +2*34
Postfix Eval: 14
Prefix Eval : 14

