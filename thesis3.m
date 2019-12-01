% text(.5,.5,['$',latex(Pb_1),'$'],'interpreter','Latex','HorizontalAlignment','center','fontsize',20)
% single-homing and single-homing

% 一方歧视另一方不歧视
syms N M alpha1 alpha2 V_1 V_2 real
syms Sigma_pa1 Sigma_pa2 real
syms Sigma_xa Sigma_ya xb yb real
syms xai yaj Pa_1i Pa_2j Pb_1 Pb_2 real
syms ii jj positive
syms na_1 na_2 nb_1 nb_2 real
syms delta1 delta2 real
delta1 = 0;
delta2 = 0;
eq1 = 2*(alpha1+alpha2)*na_2 - alpha1 + 1 + Pb_1 - (2*na_1 + delta1);
eq2 = 2*(alpha1+alpha2)*na_1 - alpha2 + 1 + Pb_2 - (2*na_2 + delta2);
sol1 = solve(eq1, eq2, na_1, na_2);
na_1 = sol1.na_1;
na_2 = sol1.na_2;
nb_1 = simplify(subs(1-na_1));
nb_2 = simplify(subs(1-na_2));
pi_B = simplify(subs(Pb_1*nb_1 + Pb_2*nb_2));
eq3 = simplify(subs(diff(pi_B, Pb_1)));
eq4 = simplify(subs(diff(pi_B, Pb_2)));
sol2 = solve(eq3, eq4, Pb_1, Pb_2);
Pb_1 = sol2.Pb_1;
Pb_2 = sol2.Pb_2;
na_1 = simplify(subs(na_1));
na_2 = simplify(subs(na_2));
% [ii_temp1, params, conds] = solve(Pa_1i, ii, 'ReturnConditions', true);
% ii_temp1 = simplify(subs(ii_temp1));
% [ii_temp2, params2, conds2] = solve(xi-ii/n, ii, 'ReturnConditions', true);
% ii_temp2 = simplify(subs(ii_temp2));
% hh=simplify(subs(ii_temp2-ii_temp1));
% operator2 = 4 - m*n*(alpha1+alpha2)*(alpha1+alpha2);
% na1_true = 1/2 + (4*Pb_1 + (alpha1*alpha1-alpha2*alpha2)*m + 2*(alpha1+alpha2)*m*Pb_2 - 2*(alpha1-alpha2))/(2*operator2) - 1/(2*n);
% na2_true = 1/2 + (4*Pb_2 + (alpha2*alpha2-alpha1*alpha1)*n + 2*(alpha1+alpha2)*n*Pb_1 - 2*(alpha2-alpha1))/(2*operator2) - 1/(2*m);
% nb1_true = 1-na1_true;
% nb2_true = 1-na2_true;
% eq5 = nb1_true - Pb_1*2/operator2 - Pb_2*(alpha1+alpha2)*n/operator2;
% eq6 = nb2_true - Pb_2*2/operator2 - Pb_1*(alpha1+alpha2)*m/operator2;
% sol4 = solve(eq5, eq6, Pb_1, Pb_2);
% Pb_1 = sol4.Pb_1;
% Pb_2 = sol4.Pb_2;
% Pb_1 = simplify(subs(Pb_1));
% Pb_2 = simplify(subs(Pb_2));
% nb1_true = simplify(subs(nb1_true));
% nb2_true = simplify(subs(nb2_true));
% xi = simplify(subs(xi));
% yj = simplify(subs(yj));
% temp = simplify(subs(ya1-yb1));
% [V_2, params, conds] = solve(temp, V_2, 'ReturnConditions', true);
% V_2 = simplify(subs(V_2));

% 一方歧视另一方不歧视，双边市场均分成两段
% V_1 + alpha1*na_2 < 1/2 时


% 一方歧视另一方不歧视，两边市场全都没有竞争的情况
% operator = m*n*alpha1*alpha2-1;
% operator2 = alpha1*alpha2-1;
% eq1 = V_1 + alpha1*na_2 - na_1;
% eq2 = V_2 + alpha2*na_1 - na_2;
% eq3 = V_1 + alpha1*nb_2 - Pb_1 - nb_1;
% eq4 = V_2 + alpha2*nb_1 - Pb_2 - nb_2;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% eq5 = nb_1 + Pb_1/operator2 + Pb_2*alpha2/operator2;
% eq6 = nb_2 + Pb_2/operator2 + Pb_1*alpha1/operator2;
% sol2 = solve(eq5, eq6, Pb_1, Pb_2);
% Pb_1 = sol2.Pb_1;
% Pb_2 = sol2.Pb_2;
% Pa_1i = V_1 + alpha1*na_2 - ii/n;
% Pa_2j = V_2 + alpha2*na_1 - jj/m;
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% eq7 = na_1 + nb_1 - 1;
% [V_1_temp, ~, ~] = solve(eq7, V_1, 'ReturnConditions', true);
% V_1_temp = simplify(subs(V_1_temp));
% eq8 = na_2 + nb_2 - 1;
% [V_2_temp, params, conds] = solve(eq8, V_2, 'ReturnConditions', true);
% V_2_temp = simplify(subs(V_2_temp));
% sol3 = solve(eq7, eq8, V_1, V_2);
% V_1 = sol3.V_1;
% V_2 = sol3.V_2;
% Pb_1 = simplify(subs(Pb_1));
% Pb_2 = simplify(subs(Pb_2));
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));

% 一边市场有竞争，另一边市场没竞争的情况
% eq1 = V_1 + alpha1*na_2 - na_1;
% eq2 = na_2 + nb_2 - 1;
% eq3 = V_1 + alpha1*nb_2 - Pb_1 - nb_1;
% eq4 = alpha2*na_1 - na_2 - alpha2*nb_1 + Pb_2 + nb_2;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% eq5 = nb_1 + Pb_1*diff(nb_1, Pb_1) + Pb_2*diff(nb_2, Pb_1);
% eq6 = nb_2 + Pb_2*diff(nb_2, Pb_2) + Pb_1*diff(nb_1, Pb_2);
% sol2 = solve(eq5, eq6, Pb_1, Pb_2);
% Pb_1 = simplify(subs(sol2.Pb_1));
% Pb_2 = simplify(subs(sol2.Pb_2));
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% eq7 = na_1 + nb_1 - 1;
% [V_1_temp, ~, ~] = solve(eq7, V_1, 'ReturnConditions', true);
% V_1_temp = simplify(subs(V_1_temp));

% xb = simplify(subs(xb));
% yb = simplify(subs(yb));
% eq11 = xai - (i1-1)/n + Sigma_pa1*m*alpha1*alpha2/operator - Pa_1i + Sigma_pa2*alpha2/operator;
% eq12 = yaj - (j1-1)/m + Sigma_pa2*n*alpha1*alpha2/operator - Pa_2j + Sigma_pa1*alpha1/operator;
% sol4 = solve(eq11, eq12, Pa_1i, Pa_2j);
% Pa_1i = sol4.Pa_1i;
% Pa_2j = sol4.Pa_2j;
% Pa_1i = simplify(subs(Pa_1i));
% Pa_2j = simplify(subs(Pa_2j));
% xai = simplify(subs(xai));
% yaj = simplify(subs(yaj));
% n=2;
% i1=2;
% m=2;
% j1=2;
% xai = simplify(subs(xai));
% temp = simplify(subs(xai-xb));
% [V_1, params, conds] = solve(temp, V_1, 'ReturnConditions', true);
% V_1 = simplify(subs(V_1));
% xai = simplify(subs(xai));
% xb = simplify(subs(xb));
% yaj = simplify(subs(yaj));
% yb = simplify(subs(yb));
% Pa_1i = simplify(subs(Pa_1i));
% Pa_2j = simplify(subs(Pa_2j));
% Pb_1 = simplify(subs(Pb_1));
% Pb_2 = simplify(subs(Pb_2));
% temp = simplify(subs(yaj-yb));
% [V_2, params, conds] = solve(temp, V_2, 'ReturnConditions', true);
% V_2 = simplify(subs(V_2));
% xai = simplify(subs(xai));
% xb = simplify(subs(xb));
% yaj = simplify(subs(yaj));
% yb = simplify(subs(yb));
% Pa_1i = simplify(subs(Pa_1i));
% Pa_2j = simplify(subs(Pa_2j));
% Pb_1 = simplify(subs(Pb_1));
% Pb_2 = simplify(subs(Pb_2));

% single-homing and single-homing: 只有一侧企业，分情况讨论，情况1-1
% syms h g real
% eq1 = V_1 + alpha1*na_2 - Pa_1i - na_1;
% eq2 = V_2 + alpha2*na_1 - Pa_2j - na_2;
% eq3 = -h + Pa_1i + alpha2*na_2;
% eq4 = -g + Pa_2j + alpha1*na_1;
% sol1 = solve(eq1, eq2, eq3, eq4, h, g, na_1, na_2);
% g = sol1.g;
% h = sol1.h;
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% i1 = simplify(subs(na_1-h));
% j1 = simplify(subs(na_2-g));
% i1 = -(n*(- V_1*alpha2^2 - V_2*alpha2 + V_1 + V_2*alpha1))/(alpha1*alpha2 - 1);
% j1 = -(m*(- V_2*alpha1^2 - V_1*alpha1 + V_2 + V_1*alpha2))/(alpha1*alpha2 - 1);
% eq5 = i1*alpha1*diff(na_2, Pa_1i) + h + Pa_1i*diff(na_1, Pa_1i) + j1*alpha2*diff(na_1, Pa_1i) + Pa_2j*diff(na_2, Pa_1i);
% eq6 = j1*alpha2*diff(na_1, Pa_2j) + g + Pa_2j*diff(na_2, Pa_2j) + i1*alpha1*diff(na_2, Pa_2j) + Pa_1i*diff(na_1, Pa_2j);
% sol2 = solve(eq5, eq6, Pa_1i, Pa_2j);
% Pa_1i = sol2.Pa_1i;
% Pa_2j = sol2.Pa_2j;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% i1 = simplify(subs(i1));
% j1 = simplify(subs(j1));