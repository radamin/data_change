import csv


def show_data():
    with open("book.csv", "r", encoding='utf=8') as f:
        for i in csv.reader(f):
            print(*i)


def add_data():
    fio = input("Введите ФИО: ")
    num_phone = input("Введите номер телефона: ")
    with open("book.csv", "a", encoding='utf=8', newline="") as f:
        wr = csv.writer(f)
        wr.writerow([fio, "|", num_phone])


def find_data():
    data = input("Введите данные для поиска: ")
    with open('book.csv', 'r', encoding='utf-8') as f:
        tel = f.read()
    print(search(tel, data).replace(",", " "))


def search(book: str, info: str) -> str:
    book = book.split("\n")
    return "\n".join([post for post in book if info in post])


def del_data():
    bill = []
    with open('book.csv', 'r', encoding='utf-8') as f:
        for i, k in enumerate(csv.reader(f), start=1):
            print(i, *k)
            bill.append(k)
        var = int(input("Номер строки: "))
        if var < 1 or var > len(bill):
            print("Нет такой строки")
            return
        bill.pop(var - 1)
    with open('book.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerows(bill)


def change():
    bill = []
    with open('book.csv', 'r', encoding='utf-8') as f:
        for i, k in enumerate(csv.reader(f), start=1):
            bill.append(k)
        var = int(input("Номер строки: "))
        if var < 1 or var > len(bill):
            print("Нет такой строки")
            return
        bill[var - 1] = [input("ФИО: "), "|", input("Номер телефона: ")]
    with open('book.csv', 'w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerows(bill)