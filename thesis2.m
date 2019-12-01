% text(.5,.5,['$',latex(pb1),'$'],'interpreter','Latex','HorizontalAlignment','center','fontsize',20)
syms n m alpha1 alpha2 V_1 V_2 real
syms Sigma_pa1 Sigma_pb1 Sigma_pa2 Sigma_pb2 real
syms Sigma_xa Sigma_ya Sigma_xb Sigma_yb real
syms Xa_i Ya_j Xb_i Yb_j Pa_1i Pa_2j Pb_1i Pb_2j real
syms ii jj real
% 两平台均实行价格歧视，平台之间没有竞争关系
% syms alpha1 alpha2 V_1 V_2 real
% syms pa1 pa2 pb1 pb2 real
% syms xa1 ya1 xb1 yb1 real
% operator = alpha1*alpha2-1;
% eq1 = V_1 + alpha1*ya1 - pa1 - xa1;
% eq2 = V_1 + alpha1*(1-yb1) - pb1 - (1-xb1);
% eq3 = V_2 + alpha2*xa1 - pa2 - ya1;
% eq4 = V_2 + alpha2*(1-xb1) - pb2 - (1-yb1);
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
% [V_2, params, conds] = solve(temp, V_2, 'ReturnConditions', true);
% V_2 = simplify(subs(V_2));

% syms n m alpha1 alpha2 V_1 V_2 real
% syms Pa_1i Pa_2j Pb_1i Pb_2j real
% syms ii jj real
% operator = n*m*alpha1*alpha2-1;
% xi = 1/2 - (Pa_1i-Pb_1i)/2;
% Ya_j = V_2 + alpha2/2 - Pa_2j;
% Yb_j = -V_2 - alpha2/2 + Pb_2j + 1;
% Sigma_pa1 = 1/4 - operator*3/4 - n*alpha2/4 + m*n*alpha2/4 - m*n*alpha2*(V_2+alpha2/2)/2;
% Sigma_pb1 = 1/4 - operator*3/4 - n*alpha2/4 + m*n*alpha2/4 - m*n*alpha2*(V_2+alpha2/2)/2;
% Sigma_pa2 = -m*(alpha1-alpha2)/4 + m*V_2/2 + 1/4 - m/4;
% Sigma_pb2 = -m*(alpha1-alpha2)/4 + m*V_2/2 + 1/4 - m/4;
% eq1 = xi - (ii-1)/n + Sigma_pa1*m*alpha1*alpha2/(2*operator) - Pa_1i/2 + Sigma_pa2*alpha2/(2*operator);
% eq2 = Ya_j - (jj-1)/m + Sigma_pa2*n*alpha1*alpha2/(2*operator) - Pa_2j + Sigma_pa1*alpha1/(2*operator);
% eq3 = ii/n - xi + Sigma_pb1*m*alpha1*alpha2/(2*operator) - Pb_1i/2 + Sigma_pb2*alpha2/(2*operator);
% eq4 = jj/m - Yb_j + Sigma_pb2*n*alpha1*alpha2/(2*operator) - Pb_2j + Sigma_pb1*alpha1/(2*operator);
% sol1 = solve(eq1, eq2, eq3, eq4, Pa_1i, Pa_2j, Pb_1i, Pb_2j);
% Pa_1i = sol1.Pa_1i;
% Pa_2j = sol1.Pa_2j;
% Pb_1i = sol1.Pb_1i;
% Pb_2j = sol1.Pb_2j;
% Pa_1i = simplify(subs(Pa_1i));
% Pa_2j = simplify(subs(Pa_2j));
% Pb_1i = simplify(subs(Pb_1i));
% Pb_2j = simplify(subs(Pb_2j));
% xi = simplify(subs(xi));
% Ya_j = simplify(subs(Ya_j));
% Yb_j = simplify(subs(Yb_j));
% temp = simplify(subs(Ya_j-Yb_j));
% [V_2, params, conds] = solve(temp, V_2, 'ReturnConditions', true);
% V_2 = simplify(subs(V_2));

% 两平台均实行价格歧视，平台之间没有竞争关系
operator = m*n*alpha1*alpha2-1;
eq1 = n*V_1 + n*alpha1*Sigma_ya - alpha1*n*(m-1)/2 - Sigma_pa1 - Sigma_xa;
eq2 = n*V_1 - n*alpha1*Sigma_yb + alpha1*n*(m+1)/2 - Sigma_pb1 - n + Sigma_xb;
eq3 = m*V_2 + m*alpha2*Sigma_xa - alpha2*m*(n-1)/2 - Sigma_pa2 - Sigma_ya;
eq4 = m*V_2 - m*alpha2*Sigma_xb + alpha2*m*(n+1)/2 - Sigma_pb2 - m + Sigma_yb;
sol1 = solve(eq1, eq2, eq3, eq4, Sigma_xa, Sigma_ya, Sigma_xb, Sigma_yb);
Sigma_xa = sol1.Sigma_xa;
Sigma_ya = sol1.Sigma_ya;
Sigma_xb = sol1.Sigma_xb;
Sigma_yb = sol1.Sigma_yb;
eq5 = V_1 + alpha1*Sigma_ya - alpha1*(m-1)/2 - Pa_1i - Xa_i;
eq6 = V_1 - alpha1*Sigma_yb + alpha1*(m+1)/2 - Pb_1i - 1 + Xb_i;
eq7 = V_2 + alpha2*Sigma_xa - alpha2*(n-1)/2 - Pa_2j - Ya_j;
eq8 = V_2 - alpha2*Sigma_xb + alpha2*(n+1)/2 - Pb_2j - 1 + Yb_j;
sol2 = solve(eq6, eq5, eq7, eq8, Xa_i, Xb_i, Ya_j, Yb_j);
Xa_i = sol2.Xa_i;
Xb_i = sol2.Xb_i;
Ya_j = sol2.Ya_j;
Yb_j = sol2.Yb_j;
eq9 = Sigma_xa - (n-1)/2 + Sigma_pa1/operator + Sigma_pa2*n*alpha2/operator;
eq10 = Sigma_ya - (m-1)/2 + Sigma_pa2/operator + Sigma_pa1*m*alpha1/operator;
eq11 = (n+1)/2 - Sigma_xb + Sigma_pb1/operator + Sigma_pb2*n*alpha2/operator;
eq12 = (m+1)/2 - Sigma_yb + Sigma_pb2/operator + Sigma_pb1*m*alpha1/operator;
sol3 = solve(eq9, eq10, eq11, eq12, Sigma_pa1, Sigma_pa2, Sigma_pb1, Sigma_pb2);
Sigma_pa1 = sol3.Sigma_pa1;
Sigma_pa2 = sol3.Sigma_pa2;
Sigma_pb1 = sol3.Sigma_pb1;
Sigma_pb2 = sol3.Sigma_pb2;
Xa_i = simplify(subs(Xa_i));
Xb_i = simplify(subs(Xb_i));
Ya_j = simplify(subs(Ya_j));
Yb_j = simplify(subs(Yb_j));
eq13 = Xa_i - (ii-1)/n + Sigma_pa1*m*alpha1*alpha2/operator - Pa_1i + Sigma_pa2*alpha2/operator;
eq14 = Ya_j - (jj-1)/m + Sigma_pa2*n*alpha1*alpha2/operator - Pa_2j + Sigma_pa1*alpha1/operator;
eq15 = ii/n - Xb_i + Sigma_pb1*m*alpha1*alpha2/operator - Pb_1i + Sigma_pb2*alpha2/operator;
eq16 = jj/m - Yb_j + Sigma_pb2*n*alpha1*alpha2/operator - Pb_2j + Sigma_pb1*alpha1/operator;
sol4 = solve(eq13, eq14, eq15, eq16, Pa_1i, Pa_2j, Pb_1i, Pb_2j);
Pa_1i = sol4.Pa_1i;
Pa_2j = sol4.Pa_2j;
Pb_1i = sol4.Pb_1i;
Pb_2j = sol4.Pb_2j;
Pa_1i = simplify(subs(Pa_1i));
Pa_2j = simplify(subs(Pa_2j));
Pb_1i = simplify(subs(Pb_1i));
Pb_2j = simplify(subs(Pb_2j));
Xa_i = simplify(subs(Xa_i));
Xb_i = simplify(subs(Xb_i));
Ya_j = simplify(subs(Ya_j));
Yb_j = simplify(subs(Yb_j));
temp = simplify(subs(Ya_j-Yb_j));
[V_2, params, conds] = solve(temp, V_2, 'ReturnConditions', true);
V_2 = simplify(subs(V_2));