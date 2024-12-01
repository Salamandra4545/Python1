def find_oldest_parallel(students):
    for i in range(len(students) - 1, -1, -1):
        if students[i] > 120:
            return i + 5
    return None


def insert_zero_columns(matrix, k):
    for row in matrix:
        row.insert(k, 0)
        row.insert(k + 2, 0)
    return matrix


def swap_min_max(lst):
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
    return lst


def to_set(data):
    if isinstance(data, str):
        data = map(int, data.split())
    return set(data), len(set(data))


def sales_summary(sales):
    from collections import defaultdict
    customers = defaultdict(lambda: defaultdict(int))
    for sale in sales:
        customer, product, quantity = sale.split()
        customers[customer][product] += int(quantity)
    result = {}
    for customer in sorted(customers.keys()):
        result[customer] = dict(sorted(customers[customer].items()))
    return result


if __name__ == "__main__":
    students = [100, 130, 90, 150, 110, 140, 160]
    print("Самая старшая параллель с более чем 120 учащимися:", find_oldest_parallel(students))

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print("Матрица после вставки столбцов:", insert_zero_columns(matrix, k))

    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Список после обмена минимального и максимального элементов:", swap_min_max(lst))

    data = "1 2 3 4 5 6 7 8 9"
    print("Множество и его мощность:", to_set(data))

    sales = ["Ivanov apple 10", "Petrov banana 5", "Ivanov banana 2", "Sidorov apple 5"]
    print("Сводка продаж:", sales_summary(sales))