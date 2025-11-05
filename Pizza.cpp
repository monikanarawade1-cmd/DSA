Pizza Parlor accepting maximum M orders. Orders are served in first come first served basis. Order once placed cannot be cancelled. Write C++ program to simulate the system using circular queue using array.


#include <iostream>
using namespace std;

#define MAX 5   // Maximum number of orders

class PizzaParlor {
    int order[MAX];
    int front, rear;
public:
    PizzaParlor() { front = rear = -1; }

    bool isFull()  { return (front == 0 && rear == MAX - 1) || (front == rear + 1); }
    bool isEmpty() { return front == -1; }

    void placeOrder(int id) {
        if (isFull()) {
            cout << "No more orders can be placed! (Queue Full)\n";
            return;
        }
        if (isEmpty()) front = 0;
        rear = (rear + 1) % MAX;
        order[rear] = id;
        cout << "Order " << id << " placed successfully.\n";
    }

    void serveOrder() {
        if (isEmpty()) {
            cout << "No orders to serve! (Queue Empty)\n";
            return;
        }
        cout << "Order " << order[front] << " served.\n";
        if (front == rear) front = rear = -1;
        else front = (front + 1) % MAX;
    }

    void display() {
        if (isEmpty()) {
            cout << "No pending orders.\n";
            return;
        }
        cout << "Pending Orders: ";
        int i = front;
        while (true) {
            cout << order[i] << " ";
            if (i == rear) break;
            i = (i + 1) % MAX;
        }
        cout << endl;
    }
};

int main() {
    PizzaParlor p;
    int choice, id;

    do {
        cout << "\n--- Pizza Parlor ---\n";
        cout << "1. Place Order\n2. Serve Order\n3. Display Orders\n4. Exit\nEnter choice: ";
        cin >> choice;

        switch (choice) {
        case 1:
            cout << "Enter Order ID: ";
            cin >> id;
            p.placeOrder(id);
            break;
        case 2:
            p.serveOrder();
            break;
        case 3:
            p.display();
            break;
        case 4:
            cout << "Thank you! Visit again.\n";
            break;
        default:
            cout << "Invalid choice.\n";
        }
    } while (choice != 4);
}

OUTPUT:
--- Pizza Parlor ---
1. Place Order
2. Serve Order
3. Display Orders
4. Exit
Enter choice: 1
Enter Order ID: 101
Order 101 placed successfully.

Enter choice: 1
Enter Order ID: 102
Order 102 placed successfully.

Enter choice: 3
Pending Orders: 101 102

Enter choice: 2
Order 101 served.

Enter choice: 3
Pending Orders: 102
