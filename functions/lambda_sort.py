data = [{'name': 'Alice', 'age': 28}, {'name': 'Bob', 'age': 21}, {'name': 'Charlie', 'age': 35}]

sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)