import stars




def draw_letter(letter):
    if letter == "L":
        stars.vertical(5)
        stars.horizontal(7)
    elif letter == "E":
        stars.horizontal(6)
        stars.vertical(2)
        stars.horizontal(6)
        stars.vertical(2)
        stars.horizontal(6)


draw_letter("L")
draw_letter("E")