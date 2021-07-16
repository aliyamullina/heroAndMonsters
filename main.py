import random
import sys
from typing import Tuple

# Счетчик поверженных героем чудовищ:
monster_counter = 0

# У рыцаря изначально не менее 10 жизней и сила удара не менее 10.
# Текущее состояние здоровье героя:
hp = 10

# Текущая сила удара героя:
attack = 10


def game() -> None:
    """Главная функция, запустив которую начнется игра."""
    print(
        'Текстовая игра "Герой и чудовища". Введи 1, чтобы начать! Или 2, чтобы выйти из игры.'
    )
    answer = getInput()
    if answer in "1":
        hero_hp = hp
        hero_attack = attack
        m_counter = monster_counter
        win_count = 10
        print(
            "Ты — рыцарь в фантастической стране. Задача — победить",
            win_count,
            "чудовищ, чтобы спасти королевство от "
            "нападения и тем самым выиграть игру!",
        )
        while m_counter < win_count:
            # Рандомно вывести события из monsters(), swords(), apples()
            events = [monsters, apples, swords]
            current_event = random.choices(events, weights=[0.4, 0.4, 0.2])[0]

            if current_event == apples:
                hero_hp = apples(hero_hp)
            elif current_event == swords:
                hero_attack = swords(hero_attack)
            else:
                hero_hp, hero_attack, m_counter = monsters(
                    hero_hp, hero_attack, m_counter
                )
                print("Твой счет", m_counter, "из", win_count)

            # При победе в игре, на экран должна быть выведена любая строка,
            # в которой присутствует слово ПОБЕДА
            # При победе над 10 чудовищами, выводится сообщение "ПОБЕДА!" (или что-то другое на ваш выбор)
            # и происходит завершение программы.
            if m_counter == win_count:
                print("ПОБЕДА")
                print("Ты победил всех чудовищ!")
                sys.exit()

            # Выводится сообщение «ПОРАЖЕНИЕ! игра окончена» и происходит завершение программы.
            # При поражении в игре, на экран должна быть выведена любая строка,
            # в которой присутствует слово ПОРАЖЕНИЕ
            if hero_hp == 0:
                print("ПОРАЖЕНИЕ")
                print("Игра окончена!")
                sys.exit()
    else:
        print("С возвращением в реальный мир!")


def monsters(x: int, y: int, z: int) -> Tuple[int, int, int]:
    """Монстры.

    :param x: жизнь героя
    :param y: сила атаки героя
    :param z: число атакованных монстров
    :return: x, y, z
    :rtype: int
    """
    # Перед тем как дать игроку выбор драться с чудовищем или убежать, на экран должна быть выведена любая строка,
    # в которой присутствует слово БОЙ.
    # В этой же строке первое встреченное число будет обозначать число жизней чудовища, а второе - его силу удара.

    # Количество жизней чудовищ
    monster_hp = random.randint(1, 10)

    # Силы атаки чудовищ
    monster_attack = random.randint(1, 10)

    # Сражение с чудовищем:
    print("БОЙ")
    print(
        "На горизонте чудовище с",
        monster_hp,
        "жизнями и с силой атаки",
        monster_attack,
        ". У тебя жизнь:",
        x,
        "и сила атаки:",
        y,
    )

    # Действия
    print("РЕШАЙСЯ! 1 - сражаться, 2 - убежать, чтобы набраться сил")
    answer = getInput()
    if answer in "1":
        print("СРАЖЕНИЕ!")
        # Если у чудовища жизней меньше, чем сила удара героя — то победа.
        # И при этом атака чудовища меньше, чем количество оставшихся жизней героя — победа,
        # но жизни снимаются.
        # В случае сражения рыцарь побеждает, если число его атаки превосходит число жизней чудовища.
        # При этом чудовище отнимает у рыцаря число жизней, соответствующее его атаке.
        if y >= monster_hp and x > monster_attack:
            x = x - monster_attack
            z = z + 1
            print("УСПЕХ! В бою твоя жизнь сократилась до", x)
            return x, y, z
        else:
            # На горизонте чудовище с 10 жизнями и с силой атаки 10 .
            # У тебя жизнь: 18 и сила атаки: 6

            # БОЙ! На горизонте чудовище с 5 жизнями и с силой атаки 9 .
            # У тебя жизнь: 9 и сила атаки: 10

            # БОЙ! На горизонте чудовище с 3 жизнями и с силой атаки 10 .
            # У тебя жизнь: 8 и сила атаки: 14

            # БОЙ! На горизонте чудовище с 5 жизнями и с силой атаки 1 .
            # У тебя жизнь: 15 и сила атаки: 4

            # Если чудовище сильнее рыцаря, то есть,
            # если сила атаки чудовища превосходит количество жизней рыцаря — рыцарь умирает

            # Все атаки (и героя и чудовища) происходят одновременно.
            # Если в одном ходу произошла и победа над последним чудовищем и смерть героя - то игра проиграна.

            # Если у чудовища больше сила удара, чем жизней у героя — то поражение.
            x = 0
            return x, y, z

    else:
        print("Фух! Удалось убежать!")
        return x, y, z


def swords(x: int) -> int:
    """Мечи.

    :return: x
    :rtype: int
    :type x: int
    """
    # Перед тем как дать игроку выбор взять меч или пройти мимо него,
    # на экран должна быть выведена любая строка, в которой присутствует слово МЕЧ,
    # а также число обозначающее его силу атаки
    # Должен быть новый меч со случайной силой атаки
    # При взятии нового меча сила атаки рыцаря принимается равной силе атаки нового подобранного меча

    # Силы атаки мечей
    sword_attack = random.randint(1, 15)

    # Нахождение меча
    print("МЕЧ")
    print("Найден меч с силой атаки", sword_attack, "Старый меч", x)

    # Действия
    print("1 - взять меч себе (выбросив старый), 2 - пройти мимо меча")
    answer = getInput()
    if answer in "1":
        x = sword_attack
        print("Новый меч в ножнах! Новая сила атаки:", x)
        return x
    else:
        print("Проходишь мимо меча...")
        return x


def apples(x: int) -> int:
    """Яблочки.

    :return: x
    :rtype: int
    :type x: int
    """
    # При обнаружении яблочка — рыцарь съедает его,
    # и узнаёт насколько он увеличил количество жизней и чему теперь равно его количество жизней.
    # В случае нахождения яблочка игроку не даётся выбора действия.
    # количество жизней, которое даёт яблочко
    # Должно быть увеличивающее случайное число здоровья яблочко
    apple_hp = random.randint(1, 5)
    x = x + apple_hp
    print("СЪЕДЕНО ЯБЛОЧКО! Количество жизней увеличилось на", apple_hp, "и равно", x)
    return x


def getInput() -> str:
    """Ввод игрока.

    :return: answer
    :rtype: str
    """
    print("Введи цифру 1 или 2")
    while True:
        answer = input()
        if answer in ("1", "2"):
            return answer
        print("Действие не распознано. Введи еще раз 1 или 2")


# if __name__ == "__main__":
#     game()
game()
