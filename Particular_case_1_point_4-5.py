import sympy as sp
a, b, c, d, e, f, g, h, i, x, z, l, r, alpha, beta = sp.symbols('a b c d e f g h i x z l r alpha beta')

z_component = (r - d - a*x) / c
x_component = z_component*(alpha - e*z_component - g*x**2 + c*x)

x_equation_solution = sp.solve(x_component, x)
x_solution_0 = x_equation_solution[0]
z_solution_0 = sp.expand(r - a * x_solution_0) / c
x_solution_1 = x_equation_solution[1]
z_solution_1 = sp.expand(r - a * x_solution_1) / c

sp.printing.pretty_print(x_solution_0)
sp.printing.pretty_print(z_solution_0)
sp.printing.pretty_print(x_solution_1)
sp.printing.pretty_print(z_solution_1)