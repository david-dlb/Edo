import sympy as sp
a, b, c, d, e, f, g, h, i, x, z, l, r, alpha, beta = sp.symbols('a b c d e f g h i x z l r alpha beta')

target = e*f + ((a*b - d)/a)*(-i)

expanded = sp.expand(target)
sp.pretty_print(expanded)