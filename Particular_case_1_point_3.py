import sympy as sp
# where s is alpha and t is beta
a, b, c, d, e, f, g, h, i, x, z, l, r, alpha, beta = sp.symbols('a b c d e f g h i x z l r alpha beta')

target = alpha + g*((r - d)/a)**2 + ((r - d)/a)*c

expanded = sp.expand(target)
sp.pretty_print(expanded)