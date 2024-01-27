import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def create_snowflake(t, order, size):
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    order = int(input("Enter the recursion level (e.g., 0, 1, 2, ...): "))
    size = 300

    create_snowflake(t, order, size)

    screen.mainloop()

if __name__ == "__main__":
    main()

    