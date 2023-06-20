import sympy as sp
a, b, c, d, e, f, g, h, i, x, z, l, r, alpha, beta = sp.symbols('a b c d e f g h i x z l r alpha beta')

x_component = (-d + r)/a
z_component = d/c

# Finding the eigenvalues
jacobian_00 = -2*a*x_component - c*z_component - r - d - l
jacobian_01 = -c*x_component
jacobian_10 = z_component*(-i)
jacobian_11 = alpha - 2*e*z + beta*x - g*x**2

product_0 = jacobian_00 * jacobian_11
product_1 = jacobian_10 * jacobian_01

solution = sp.solve(product_0 - product_1, l)
result_0  = solution[0]
sp.pretty_print(result_0)