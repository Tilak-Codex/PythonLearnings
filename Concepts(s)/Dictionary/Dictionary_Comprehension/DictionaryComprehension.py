#dicntionary={key: expression for (key,value) in iterable if}

w={"Newyork":"sunny","canada":"sunny","alaska":"cold","newjersey":"cold"}

w_sunny={key:value for (key,value) in w.items() if value=="sunny"}

print(w_sunny)
