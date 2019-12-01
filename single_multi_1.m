% syms alpha1 alpha2 value1 value2 n m real
% syms pa1 pa2 pb1 pb2 real
% syms x1 ya1 yb1 real
% syms x y delta_1 delta_2 real
% operator = alpha1*alpha2-1;
% eq1 = delta_1 + x - 1 - (delta_2-1)/alpha2;
% eq2 = delta_2 + y - 1 - (delta_1-1)/alpha1;
% sol1 = solve(eq1, eq2, delta_1, delta_2);
% delta_1 = sol1.delta_1;
% delta_2 = sol1.delta_2;
% na1 = 1/2 + (delta_2-1)/(2*alpha2);
% na2 = 1/2 + (delta_1-1)/(2*alpha1);
% nb1 = simplify(subs(1-na1));
% nb2 = simplify(subs(1-na2));
% eq3 = nb1 + x/(2*operator) + y*alpha2/(2*operator);
% eq4 = nb2 + y/(2*operator) + x*alpha1/(2*operator);
% sol2 = solve(eq3, eq4, x, y);
% x = sol2.x;
% y = sol2.y;
% delta_1 = simplify(subs(delta_1));
% delta_2 = simplify(subs(delta_2));
% na1 = simplify(subs(na1));
% na2 = simplify(subs(na2));
% nb1 = simplify(subs(nb1));
% nb2 = simplify(subs(nb2));

% yb1 = sol1.yb1;
% x1 = simplify(subs(x1));
% ya1 = simplify(subs(ya1));
% yb1 = simplify(subs(yb1));
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