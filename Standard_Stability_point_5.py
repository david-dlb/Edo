import sympy as sp
a, b, c, d, e, f, g, h, i, x, z, l = sp.symbols('a b c d e f g h i x z l')

x_component = a*e + c*(g*h - i) - (a**2*e**2 - 2*a*c*e*(2*b*g - g*h + i) + c**2*(4*e*f*g + (g*h - i)**2) + 4*c*d*e*g)**(1/2)

z_component = ((a*b - d) - a*x_component)/c

# Finding the eigenvalues
jacobian_00 = -2*a*x_component - c*z_component - a*b - d - l
jacobian_01 = -c*x_component
jacobian_10 = z_component*(g*h - 2*g*x_component - i)
jacobian_11 = e*f - 2*e*z_component - g*x_component**2 + (g*h - i)*x_component - l

product_0 = jacobian_00 * jacobian_11
product_1 = jacobian_10 * jacobian_01

solution = sp.solve(product_0 - product_1, l)
result_0  = solution[0]
result_1 = solution[1]
sp.pretty_print(result_0)