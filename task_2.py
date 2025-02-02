import turtle
import math

def draw_branch(t, length, level):
    """Рекурсивно малює фрактальне дерево Піфагора."""
    if level == 0:
        return

    # Малюємо основну лінію (стовбур)
    t.forward(length)

    # Зберігаємо поточне положення
    x, y = t.pos()
    angle = t.heading()

    # Обчислюємо довжину нових гілок
    new_length = length / math.sqrt(2)

    # Малюємо ліву гілку
    t.left(45)
    draw_branch(t, new_length, level - 1)

    # Повертаємося назад
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

    # Малюємо праву гілку
    t.right(45)
    draw_branch(t, new_length, level - 1)

    # Повертаємося назад
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()

def draw_pythagoras_tree(level):
    """Функція ініціалізації полотна та запуску малювання"""
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.color("brown")

    # Початкова позиція
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)

    # Виконуємо рекурсивне малювання
    draw_branch(t, 150, level)

    # Завершення
    turtle.done()

if __name__ == "__main__":
    recursion_level = int(input("Введіть рівень рекурсії (рекомендується 7-12): "))
    draw_pythagoras_tree(recursion_level)
