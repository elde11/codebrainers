#hexcolor(255, 99, 71) => "#FF6347"  (Tomato)
#hexcolor(184, 134, 11) => "#B8860B"  (DarkGoldenrod)
#hexcolor(189, 183, 107) => "#BDB76B"  (DarkKhaki)
#hexcolor(0, 0, 205) => "#0000CD"  (MediumBlue)
# jasność koloru też 0 .... 255 , wikipedia tabela kolorów


# import tabelki z wikipedii ? 




def hexcolor (red, green, blue):
    red = hex(red)
    green = hex(green)
    blue = hex(blue)
    hexcode = "#" + red[2:] + green[2:] + blue[2:]

    return hexcode
print("To jest barwa:")