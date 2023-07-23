import turtle as t
t.speed(0)

def koch(t, n):
    """ Draws a Koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

def snowflake(t, n):
    """ Draws a Snowflake (a triangle with a Koch curve for each side). """
    for i in range(3):
        koch(t, n)
        t.rt(120)

snowflake(t, 400)
t.mainloop()
