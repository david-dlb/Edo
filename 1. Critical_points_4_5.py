import sympy as sp
a, b, c, d, e, f, g, h, i, x, z, l = sp.symbols('a b c d e f g h i x z l')

z_component = (a*b - d - a*x) / c
x_component = z_component*(e*(f - z_component) + g*x*(h - x) - i*x)

x_equation_solution = sp.solve(x_component, x)
x_solution_0 = x_equation_solution[0]
x_solution_1 = x_equation_solution[1]

sp.printing.pretty_print(x_solution_0)
sp.printing.pretty_print(x_solution_1)