def zeros_list(flower_bed : str) -> list:
    count_zero = 0
    result = []

    if "1" in flower_bed and "0" in flower_bed:
        for place in flower_bed:
            if place == "0":
                count_zero += 1
            elif place == "1":
                result.append(count_zero)
                count_zero = 0
    elif "1" in flower_bed and "0" not in flower_bed:
        result = [0]
    elif "1" not in flower_bed and "0" in flower_bed:
        result = [len(flower_bed)]

    return result


flower_bed = input("Введите строку из нулей и единиц: ")
zeros = zeros_list(flower_bed)
if flower_bed[0] == "0":
    zeros[0] += 1
if flower_bed[-1] == "0":
    zeros[-1] += 1

if "1" in flower_bed and "0" not in flower_bed:
    print("Вам некуда сажать цветы")
else:
    max_flowers = max(zeros) - 2
    print(f"Вы можете посадить максимальную группу из {max_flowers} цветов")