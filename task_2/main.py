def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

        return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    except ValueError:
        print("Неправильний формат даних у файлі.")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)