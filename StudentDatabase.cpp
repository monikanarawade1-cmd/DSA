Design a program to maintain a student database that performs the following tasks:
 1. Add and store student details (ID, Name, CGPA) using dynamically allocated memory. 
2. Expand the student list using realloc() as new entries are added.
3. Implement Linear Search and Binary Search to find student records by ID. 
4. Implement at least two Sorting Algorithms (Bubble Sort, Selection Sort, or Insertion Sort) to sort student records by: Name (Alphabetically) CGPA (Ascending/Descending) 5. Analyze and compare the performance of search operations before and after sorting


S
#include <iostream>
using namespace std;

struct Student {
    int id;
    string name;
    float cgpa;
};

void add(Student *&s, int &n) {
    Student *t = new Student[n + 1];
    for (int i = 0; i < n; i++) t[i] = s[i];
    cout << "ID: "; cin >> t[n].id;
    cout << "Name: "; cin.ignore(); getline(cin, t[n].name);
    cout << "CGPA: "; cin >> t[n].cgpa;
    delete[] s; s = t; n++;
}

void show(Student *s, int n) {
    cout << "\nID\tName\tCGPA\n";
    for (int i = 0; i < n; i++)
        cout << s[i].id << "\t" << s[i].name << "\t" << s[i].cgpa << endl;
}

void bubbleName(Student *s, int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (s[j].name > s[j + 1].name) {
                Student temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
}

void selectCGPA(Student *s, int n, bool asc = true) {
    for (int i = 0; i < n - 1; i++) {
        int k = i;
        for (int j = i + 1; j < n; j++)
            if ((asc && s[j].cgpa < s[k].cgpa) || (!asc && s[j].cgpa > s[k].cgpa))
                k = j;
        Student temp = s[i];
        s[i] = s[k];
        s[k] = temp;
    }
}

int linear(Student *s, int n, int id) {
    for (int i = 0; i < n; i++) if (s[i].id == id) return i;
    return -1;
}

void sortByID(Student *s, int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (s[j].id > s[j + 1].id) {
                Student temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
}

int binary(Student *s, int n, int id) {
    int l = 0, h = n - 1;
    while (l <= h) {
        int m = (l + h) / 2;
        if (s[m].id == id) return m;
        if (s[m].id < id) l = m + 1; else h = m - 1;
    }
    return -1;
}

int main() {
    Student *s = nullptr; int n = 0, ch;
    do {
        cout << "\n1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: ";
        cin >> ch;
        if (ch == 1) add(s, n);
        else if (ch == 2) show(s, n);
        else if (ch == 3) bubbleName(s, n);
        else if (ch == 4) { int o; cout << "1.Asc 2.Desc: "; cin >> o; selectCGPA(s, n, o == 1); }
        else if (ch == 5) {
            int id; cout << "Enter ID: "; cin >> id;
            int i = linear(s, n, id); cout << "Linear: " << (i == -1 ? "Not Found" : s[i].name) << endl;
            sortByID(s, n);
            i = binary(s, n, id); cout << "Binary: " << (i == -1 ? "Not Found" : s[i].name) << endl;
        }
    } while (ch != 6);
    delete[] s;
}

OUTPUT:
1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 1
ID: 101
Name: Rahul
CGPA: 8.7

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 1
ID: 103
Name: Priya
CGPA: 9.1

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 1
ID: 102
Name: Aman
CGPA: 7.8

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 2

ID      Name    CGPA
101     Rahul   8.7
103     Priya   9.1
102     Aman    7.8

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 3
✅ Sorted by Name (Alphabetically)

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 2

ID      Name    CGPA
102     Aman    7.8
103     Priya   9.1
101     Rahul   8.7

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 4
1.Asc 2.Desc: 2
✅ Sorted by CGPA (Descending)

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 2

ID      Name    CGPA
103     Priya   9.1
101     Rahul   8.7
102     Aman    7.8

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 5
Enter ID: 101
Linear: Rahul
Binary: Rahul

1.Add 2.Show 3.SortName 4.SortCGPA 5.Search 6.Exit: 6
