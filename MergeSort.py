Problem Statement: You are given a list of online orders, each with an estimated delivery time in minutes. Write a program to sort these orders using the Merge Sort algorithm so the delivery system can prioritize quicker deliveries first.

# Merge Sort Function for list of tuples (order_id, delivery_time)
def merge_sort_orders(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_orders(L)
        merge_sort_orders(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][1] < R[j][1]:  # sort by delivery time
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1; k += 1

# ------------------- Main Program -------------------
orders = []
n = int(input("Enter number of orders: "))
for _ in range(n):
    order_id = input("Enter Order ID: ")
    time = int(input("Enter estimated delivery time (minutes): "))
    orders.append((order_id, time))

# Display original orders
print("\nOriginal Orders:")
for oid, t in orders:
    print(f"{oid} : {t} min")

# Sort orders
merge_sort_orders(orders)

# Display sorted orders
print("\nSorted Orders (quicker deliveries first):")
for oid, t in orders:
    print(f"{oid} : {t} min")

OUTPUT:
Enter number of orders: 5
Enter Order ID: O101
Enter estimated delivery time (minutes): 45
Enter Order ID: O102
Enter estimated delivery time (minutes): 30
Enter Order ID: O103
Enter estimated delivery time (minutes): 60
Enter Order ID: O104
Enter estimated delivery time (minutes): 25
Enter Order ID: O105
Enter estimated delivery time (minutes): 50

Original Orders:
O101 : 45 min
O102 : 30 min
O103 : 60 min
O104 : 25 min
O105 : 50 min

Sorted Orders (quicker deliveries first):
O104 : 25 min
O102 : 30 min
O101 : 45 min
O105 : 50 min
O103 : 60 min
                                                    OR
