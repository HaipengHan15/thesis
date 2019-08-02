syms alpha1 alpha2 value1 value2 real
syms pa1 pa2 pb1 pb2 real
syms x1 ya1 yb1 real
operator = alpha1*alpha2-1;
eq1 = alpha1*(ya1+yb1) - (pa1-pb1) - alpha1 + 1 - 2*x1;
eq2 = value2 + alpha2*x1 - pa2 - ya1;
eq3 = value2 + alpha2*(1-x1) - pb2 - (1-yb1);
sol1 = solve(eq1, eq2, eq3, x1, ya1, yb1);
x1 = sol1.x1;
ya1 = sol1.ya1;
yb1 = sol1.yb1;
x1 = simplify(subs(x1));
ya1 = simplify(subs(ya1));
yb1 = simplify(subs(yb1));
% eq5 = x1 + pa1/operator + pa2*alpha2/operator;
% eq6 = ya1 + pa2/operator + pa1*alpha1/operator;
% eq7 = 1-xb1 + pb1/operator + pb2*alpha2/operator;
% eq8 = 1-yb1 + pb2/operator + pb1*alpha1/operator;
% sol2 = solve(eq5, eq6, eq7, eq8, pa1, pa2, pb1, pb2);
% pa1 = sol2.pa1;
% pa2 = sol2.pa2;
% pb1 = sol2.pb1;
% pb2 = sol2.pb2;
% pa1 = simplify(subs(pa1));
% pa2 = simplify(subs(pa2));
% pb1 = simplify(subs(pb1));
% pb2 = simplify(subs(pb2));
% x1 = simplify(subs(x1));
% ya1 = simplify(subs(ya1));
% xb1 = simplify(subs(xb1));
% yb1 = simplify(subs(yb1));
% temp = simplify(subs(ya1-yb1));
% [value2, params, conds] = solve(temp, value2, 'ReturnConditions', true);
% value2 = simplify(subs(value2));