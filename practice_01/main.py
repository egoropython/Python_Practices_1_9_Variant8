def read_durations():
    """Запрашивает длительность тренировок и проверяет ввод."""
    while True:
        try:
            count = int(input("Введите количество тренировок: "))
            if count <= 0:
                print("Ошибка: количество должно быть больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число.")

    durations = []
    for i in range(count):
        while True:
            try:
                duration = float(input(f"Продолжительность тренировки {i + 1} (мин): "))
                if duration <= 0:
                    print("Ошибка: длительность должна быть больше нуля.")
                    continue
                durations.append(duration)
                break
            except ValueError:
                print("Ошибка: введите число.")
    return durations


def calculate_total(durations):
    return sum(durations)


def calculate_average(durations):
    return calculate_total(durations) / len(durations)


def count_over_hour(durations):
    return sum(1 for value in durations if value > 60)


def calculate_under_30_percent(durations):
    return sum(1 for value in durations if value < 30) / len(durations) * 100


def main():
    durations = read_durations()
    print("\n===== Анализ тренировок =====")
    print(f"Суммарная продолжительность: {calculate_total(durations):.2f} мин.")
    print(f"Средняя продолжительность: {calculate_average(durations):.2f} мин.")
    print(f"Самая длинная тренировка: {max(durations):.2f} мин.")
    print(f"Тренировок более часа: {count_over_hour(durations)}")
    print(f"Тренировок менее 30 минут: {calculate_under_30_percent(durations):.2f}%")


if __name__ == "__main__":
    main()
