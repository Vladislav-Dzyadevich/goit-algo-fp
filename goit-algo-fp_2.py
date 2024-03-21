import turtle

def draw_tree(trunk_length, level):
    if level == 0:
        return
    turtle.forward(trunk_length)
    turtle.left(45)
    draw_tree(0.6 * trunk_length, level - 1)
    turtle.right(90)
    draw_tree(0.6 * trunk_length, level - 1)
    turtle.left(45)
    turtle.backward(trunk_length)

def main():
    turtle.speed(0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    
    # Запит у користувача для введення рівня рекурсії
    level = int(input("Введіть рівень рекурсії (ціле число): "))
    
    draw_tree(150, level)
    turtle.mainloop()

if __name__ == "__main__":
    main()
