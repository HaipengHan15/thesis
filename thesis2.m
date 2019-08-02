% syms alpha1 alpha2 value1 value2 real
% syms pa1 pa2 pb1 pb2 real
% syms xa1 ya1 xb1 yb1 real
% operator = alpha1*alpha2-1;
% eq1 = value1 + alpha1*ya1 - pa1 - xa1;
% eq2 = value1 + alpha1*(1-yb1) - pb1 - (1-xb1);
% eq3 = value2 + alpha2*xa1 - pa2 - ya1;
% eq4 = value2 + alpha2*(1-xb1) - pb2 - (1-yb1);
% sol1 = solve(eq1, eq2, eq3, eq4, xa1, ya1, xb1, yb1);
% xa1 = sol1.xa1;
% ya1 = sol1.ya1;
% xb1 = sol1.xb1;
% yb1 = sol1.yb1;
% xa1 = simplify(subs(xa1));
% ya1 = simplify(subs(ya1));
% xb1 = simplify(subs(xb1));
% yb1 = simplify(subs(yb1));
% eq5 = xa1 + pa1/operator + pa2*alpha2/operator;
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
% xa1 = simplify(subs(xa1));
% ya1 = simplify(subs(ya1));
% xb1 = simplify(subs(xb1));
% yb1 = simplify(subs(yb1));
% temp = simplify(subs(ya1-yb1));
% [value2, params, conds] = solve(temp, value2, 'ReturnConditions', true);
% value2 = simplify(subs(value2));

% syms n m alpha1 alpha2 value1 value2 real
% syms pa1i pa2j pb1i pb2j real
% syms i1 j1 real
% operator = n*m*alpha1*alpha2-1;
% xi = 1/2 - (pa1i-pb1i)/2;
% yaj = value2 + alpha2/2 - pa2j;
% ybj = -value2 - alpha2/2 + pb2j + 1;
% sum_pa1 = 1/4 - operator*3/4 - n*alpha2/4 + m*n*alpha2/4 - m*n*alpha2*(value2+alpha2/2)/2;
% sum_pb1 = 1/4 - operator*3/4 - n*alpha2/4 + m*n*alpha2/4 - m*n*alpha2*(value2+alpha2/2)/2;
% sum_pa2 = -m*(alpha1-alpha2)/4 + m*value2/2 + 1/4 - m/4;
% sum_pb2 = -m*(alpha1-alpha2)/4 + m*value2/2 + 1/4 - m/4;
% eq1 = xi - (i1-1)/n + sum_pa1*m*alpha1*alpha2/(2*operator) - pa1i/2 + sum_pa2*alpha2/(2*operator);
% eq2 = yaj - (j1-1)/m + sum_pa2*n*alpha1*alpha2/(2*operator) - pa2j + sum_pa1*alpha1/(2*operator);
% eq3 = i1/n - xi + sum_pb1*m*alpha1*alpha2/(2*operator) - pb1i/2 + sum_pb2*alpha2/(2*operator);
% eq4 = j1/m - ybj + sum_pb2*n*alpha1*alpha2/(2*operator) - pb2j + sum_pb1*alpha1/(2*operator);
% sol1 = solve(eq1, eq2, eq3, eq4, pa1i, pa2j, pb1i, pb2j);
% pa1i = sol1.pa1i;
% pa2j = sol1.pa2j;
% pb1i = sol1.pb1i;
% pb2j = sol1.pb2j;
% pa1i = simplify(subs(pa1i));
% pa2j = simplify(subs(pa2j));
% pb1i = simplify(subs(pb1i));
% pb2j = simplify(subs(pb2j));
% xi = simplify(subs(xi));
% yaj = simplify(subs(yaj));
% ybj = simplify(subs(ybj));
% temp = simplify(subs(yaj-ybj));
% [value2, params, conds] = solve(temp, value2, 'ReturnConditions', true);
% value2 = simplify(subs(value2));

syms n m alpha1 alpha2 value1 value2 real
syms sum_pa1 sum_pb1 sum_pa2 sum_pb2 real
syms xa ya xb yb real
syms xai yaj xbi ybj pa1i pa2j pb1i pb2j real
syms i1 j1 positive
operator = m*n*alpha1*alpha2-1;
eq1 = n*value1 + n*alpha1*ya - alpha1*n*(m-1)/2 - sum_pa1 - xa;
eq2 = n*value1 - n*alpha1*yb + alpha1*n*(m+1)/2 - sum_pb1 - n + xb;
eq3 = m*value2 + m*alpha2*xa - alpha2*m*(n-1)/2 - sum_pa2 - ya;
eq4 = m*value2 - m*alpha2*xb + alpha2*m*(n+1)/2 - sum_pb2 - m + yb;
sol1 = solve(eq1, eq2, eq3, eq4, xa, ya, xb, yb);
xa = sol1.xa;
ya = sol1.ya;
xb = sol1.xb;
yb = sol1.yb;
eq5 = value1 + alpha1*ya - alpha1*(m-1)/2 - pa1i - xai;
eq6 = value1 - alpha1*yb + alpha1*(m+1)/2 - pb1i - 1 + xbi;
eq7 = value2 + alpha2*xa - alpha2*(n-1)/2 - pa2j - yaj;
eq8 = value2 - alpha2*xb + alpha2*(n+1)/2 - pb2j - 1 + ybj;
sol2 = solve(eq6, eq5, eq7, eq8, xai, xbi, yaj, ybj);
xai = sol2.xai;
xbi = sol2.xbi;
yaj = sol2.yaj;
ybj = sol2.ybj;
% eq9 = xa - (n-1)/2 + sum_pa1/operator + sum_pa2*n*alpha2/operator;
% eq10 = ya - (m-1)/2 + sum_pa2/operator + sum_pa1*m*alpha1/operator;
% eq11 = (n+1)/2 - xb + sum_pb1/operator + sum_pb2*n*alpha2/operator;
% eq12 = (m+1)/2 - yb + sum_pb2/operator + sum_pb1*m*alpha1/operator;
% sol3 = solve(eq9, eq10, eq11, eq12, sum_pa1, sum_pa2, sum_pb1, sum_pb2);
% sum_pa1 = sol3.sum_pa1;
% sum_pa2 = sol3.sum_pa2;
% sum_pb1 = sol3.sum_pb1;
% sum_pb2 = sol3.sum_pb2;
% xai = simplify(subs(xai));
% xbi = simplify(subs(xbi));
% yaj = simplify(subs(yaj));
% ybj = simplify(subs(ybj));
% eq13 = xai - (i1-1)/n + sum_pa1*m*alpha1*alpha2/operator - pa1i + sum_pa2*alpha2/operator;
% eq14 = yaj - (j1-1)/m + sum_pa2*n*alpha1*alpha2/operator - pa2j + sum_pa1*alpha1/operator;
% eq15 = i1/n - xbi + sum_pb1*m*alpha1*alpha2/operator - pb1i + sum_pb2*alpha2/operator;
% eq16 = j1/m - ybj + sum_pb2*n*alpha1*alpha2/operator - pb2j + sum_pb1*alpha1/operator;
% sol4 = solve(eq13, eq14, eq15, eq16, pa1i, pa2j, pb1i, pb2j);
% pa1i = sol4.pa1i;
% pa2j = sol4.pa2j;
% pb1i = sol4.pb1i;
% pb2j = sol4.pb2j;
% pa1i = simplify(subs(pa1i));
% pa2j = simplify(subs(pa2j));
% pb1i = simplify(subs(pb1i));
% pb2j = simplify(subs(pb2j));
% xai = simplify(subs(xai));
% xbi = simplify(subs(xbi));
% yaj = simplify(subs(yaj));
% ybj = simplify(subs(ybj));
% temp = simplify(subs(yaj-ybj));
% [value2, params, conds] = solve(temp, value2, 'ReturnConditions', true);
% value2 = simplify(subs(value2));