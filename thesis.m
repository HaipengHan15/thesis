% text(.5,.5,['$',latex(pb1),'$'],'interpreter','Latex','HorizontalAlignment','center','fontsize',20)

%1 两平台统一定价，平台之间没有竞争关系
syms alpha1 alpha2 V_1 V_2 real
syms Pa_1 Pb_1 Pa_2 Pb_2 real
syms na_1 na_2 nb_1 nb_2 real
eq1 = V_1 + alpha1*na_2 - Pa_1 - na_1;
eq2 = V_2 + alpha2*na_1 - Pa_2 - na_2;
sol1 = solve(eq1, eq2, na_1, na_2);
na_1 = sol1.na_1;
na_2 = sol1.na_2;
eq3 = na_1 + Pa_1*diff(na_1, Pa_1) + Pa_2*diff(na_2, Pa_1);
eq4 = na_2 + Pa_2*diff(na_2, Pa_2) + Pa_1*diff(na_1, Pa_2);
sol2 = solve(eq3, eq4, Pa_1, Pa_2);
Pa_1 = sol2.Pa_1;
Pa_2 = sol2.Pa_2;
na_1 = simplify(subs(na_1));
na_2 = simplify(subs(na_2));
eq3 = na_1 - 1/2;
eq4 = na_2 - 1/2;
% sol2 = solve(eq3, eq4, V_1, V_2);
% V_1 = sol2.V_1;
% V_2 = sol2.V_2;
[V_1, params, conds] = solve(eq3, V_1, 'ReturnConditions', true);
na_1 = simplify(subs(na_1));
na_2 = simplify(subs(na_2));
Pa_1 = simplify(subs(Pa_1));
Pa_2 = simplify(subs(Pa_2));

%2 Group-1分成两段价格歧视，Group-2统一定价
% syms alpha1 alpha2 V_1 V_2 real
% syms Pa_1 Pb_1 Pa_2 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% syms x_11 x_12 Pa_11 Pa_12 real
% eq1 = V_1 + alpha1*na_2 - Pa_11 - x_11;
% eq2 = V_1 + alpha1*na_2 - Pa_12 - x_12;
% eq3 = V_2 + alpha2*na_1 - Pa_2 - na_2;
% eq4 = x_11 + x_12 - 1/2 - na_1;
% sol2_1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, x_11, x_12);
% na_1 = sol2_1.na_1;
% na_2 = sol2_1.na_2;
% x_11 = sol2_1.x_11;
% x_12 = sol2_1.x_12;
% eq5 = x_11 + Pa_11*diff(x_11, Pa_11) + Pa_12*diff(x_12, Pa_11) + Pa_2*diff(na_2, Pa_11);
% eq6 = x_12-1/2 + Pa_12*diff(x_12, Pa_12) + Pa_11*diff(x_11, Pa_12) + Pa_2*diff(na_2, Pa_12);
% eq7 = na_2 + Pa_2*diff(na_2, Pa_2) + Pa_11*diff(x_11, Pa_2) + Pa_12*diff(x_12, Pa_2);
% sol2_2 = solve(eq5, eq6, eq7, Pa_11, Pa_12, Pa_2);
% Pa_11 = sol2_2.Pa_11;
% Pa_12 = sol2_2.Pa_12;
% Pa_2 = sol2_2.Pa_2;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% x_11 = simplify(subs(x_11));
% x_12 = simplify(subs(x_12));
% test = simplify(subs(x_12+x_11-1/2));
% test2 = simplify(subs(Pa_11-Pa_12));
% pi_2 = x_11*Pa_11 + (x_12-1/2)*Pa_12 + na_2*Pa_2;
% pi_2 = simplify(subs(pi_2));
% temp = simplify(subs(pi_2-pi_1));
% [V_1, params, conds] = solve(temp, V_1, 'ReturnConditions', true);
% V_1 = simplify(subs(V_1));
% x_12 = simplify(subs(x_12));
% 由此可以证明，当x_12>1/2时，平台是应该将价格降低到负值以吸引观众的，即Pa_12<0
% temp = simplify(subs(V_1+alpha1*na_2));
% x_11 = simplify(subs(x_11));
% pi_1 = x_11*Pa_11 + (x_12-1/2)*Pa_12;
% pi_1 = simplify(subs(pi_1));

%3 Group-1分成多段价格歧视，Group-2统一定价
% syms alpha1 alpha2 V_1 V_2 N i1 real
% syms Pa_1i Pa_2 real
% syms na_1 na_2 real
% syms x_1i real
% eq1 = V_1 + (alpha1+alpha2)*na_2 - (na_1 + 1/(2*N));
% eq2 = V_2 + (alpha1+alpha2)*na_1 - 2*na_2;
% sol1 = solve(eq1, eq2, na_1, na_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% Pa_2 = simplify(subs(V_2 + alpha2*na_1 - na_2));
% temp = simplify(subs(V_1 + alpha1*na_2 - i1/N));
% temp2 = simplify(subs((i1-1)/N + 1/(2*N) + (na_1 - (i1-1)/N - 1/(2*N))/2));
% temp3 = simplify(subs((i1-1)/N + (na_1 - (i1-2)/N - 1/(2*N))/2));
% eq3 = na_1 - 1/2;
% eq4 = na_2 - 1/2;
% sol2 = solve(eq3, eq4, V_1, V_2);
% V_1 = sol2.V_1;
% V_2 = sol2.V_2;
% [V_1, params, conds] = solve(eq3, V_1, 'ReturnConditions', true);
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% temp = simplify(subs(V_1+alpha1*na_2));
% x_11 = simplify(subs(x_11));
% pi_1 = x_11*Pa_11 + (x_12-1/2)*Pa_12;
% pi_1 = simplify(subs(pi_1));

%4 两平台统一定价，group-2有竞争关系
% eq5 = V_1 + alpha1*na_2 - Pa_1 - na_1;
% eq6 = V_1 + alpha1*nb_2 - Pb_1 - nb_1;
% eq7 = alpha2*na_1 - Pa_2 - na_2 - (alpha2*nb_1 - Pb_2 - nb_2);
% eq8 = na_2 + nb_2 - 1;
% sol3 = solve(eq5, eq6, eq7, eq8, na_1, na_2, nb_1, nb_2);
% na_1 = sol3.na_1;
% na_2 = sol3.na_2;
% nb_1 = sol3.nb_1;
% nb_2 = sol3.nb_2;
% eq9 = na_1 + Pa_1*diff(na_1, Pa_1) + Pa_2*diff(na_2, Pa_1);
% eq10 = na_2 + Pa_2*diff(na_2, Pa_2) + Pa_1*diff(na_1, Pa_2);
% eq11 = nb_1 + Pb_1*diff(nb_1, Pb_1) + Pb_2*diff(nb_2, Pb_1);
% eq12 = nb_2 + Pb_2*diff(nb_2, Pb_2) + Pb_1*diff(nb_1, Pb_2);
% sol4 = solve(eq9, eq10, eq11, eq12, Pa_1, Pa_2, Pb_1, Pb_2);
% Pa_1 = sol4.Pa_1;
% Pa_2 = sol4.Pa_2;
% Pb_1 = sol4.Pb_1;
% Pb_2 = sol4.Pb_2;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% temp = simplify(subs(ya1-yb1));
% [value2, params, conds] = solve(temp, value2, 'ReturnConditions', true);
% value2 = simplify(subs(value2));

%5 两平台价格歧视，双边市场均没有竞争关系
% syms alpha1 alpha2 V_1 V_2 real
% syms Pa_1 Pb_1 Pa_2 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% syms x_11 x_12 Pa_11 Pa_12 M N real
% na_1 = -((alpha1+alpha2)*(V_2 - 1/(2*M)) + (V_1 - 1/(2*N)))/((alpha1+alpha2)^2 - 1);
% na_2 = -((alpha1+alpha2)*(V_1 - 1/(2*N)) + (V_2 - 1/(2*M)))/((alpha1+alpha2)^2 - 1);
% eq5_1 = na_1 - 1/2;
% eq5_2 = na_2 - 1/2;
% sol5_1 = solve(eq5_1, eq5_2, V_1, V_2);
% V_1 = sol5_1.V_1;
% V_2 = sol5_1.V_2;
% [V_2, params, conds] = solve(eq5_2, V_2, 'ReturnConditions', true);
% V_2 = simplify(subs(V_2));
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% % 计算两平台接壤时的倒数前两个区域的定价
% Pa_2 = V_1 + alpha1*na_2 - 1/2 + 1/(4*N);
% Pa_1 = V_1 + alpha1*na_2 - 1/2 - 1/(4*N);
% Pa_2 = simplify(subs(Pa_2));
% Pa_1 = simplify(subs(Pa_1));