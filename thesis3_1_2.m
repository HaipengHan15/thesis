% text(.5,.5,['$',latex(Pb_1),'$'],'interpreter','Latex','HorizontalAlignment','center','fontsize',25)
% single-homing and single-homing & multi-homing and single-homing
% group-1卖家，group-2买家
% 
% multi-homing and single-homing: Group-1 PD定价，Group-2统一定价
syms V_1 V_2 V alpha1 alpha2 t1 t2 t c1 c2 c positive
syms Pa_11 Pa_12 Pa_2 Pb_11 Pb_12 Pb_1 Pb_2 real
syms na_1 na_2 nb_1 nb_2 positve
syms CS_A1 CS_B1 CS_A2 CS_B2 CS SW real
t1 = 1;
t2 = 1;
c1 = 0;
c2 = 0;
V = 0;
eq1 = (V + alpha1*nb_2 - Pa_12 - Pb_12) + Pa_11 - t1*nb_1;
eq2 = (V + alpha1*na_2 - Pb_12 - Pa_12) + Pb_11 - t1*na_1;
eq3 = alpha2*na_1 - Pa_2 - t2*na_2 - (alpha2*nb_1 - Pb_2 - t2*nb_2);
eq4 = na_2 + nb_2 - 1;
sol1 = solve(eq1, eq2, eq3, eq4, na_1, nb_1, na_2, nb_2);
na_1 = sol1.na_1;
nb_1 = sol1.nb_1;
na_2 = sol1.na_2;
nb_2 = sol1.nb_2;
pi_A = simplify(subs(Pa_11*(1-nb_1) + Pa_12*(na_1+nb_1-1) + Pa_2*na_2 - c1*na_1 - c2*na_2));
pi_B = simplify(subs(Pb_11*(1-na_1) + Pb_12*(na_1+nb_1-1) + Pb_2*nb_2 - c1*nb_1 - c2*nb_2));
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 1
% normal subcase
% eq5 = simplify(subs(diff(pi_A, Pa_11)));
% eq6 = simplify(subs(diff(pi_A, Pa_12)));
% eq7 = simplify(subs(diff(pi_A, Pa_2)));
% eq8 = simplify(subs(diff(pi_B, Pb_11)));
% eq9 = simplify(subs(diff(pi_B, Pb_12)));
% eq10 = simplify(subs(diff(pi_B, Pb_2)));
% sol3 = solve(eq5, eq6, eq7, eq8, eq9, eq10, Pa_11, Pa_12, Pa_2, Pb_11, Pb_12, Pb_2);
% Pa_11 = sol3.Pa_11;
% Pa_12 = sol3.Pa_12;
% Pa_2 = sol3.Pa_2;
% Pb_11 = sol3.Pb_11;
% Pb_12 = sol3.Pb_12;
% Pb_2 = sol3.Pb_2;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2
% the subcase that na_1 = nb_1 = 1
sol2 = solve(na_1-1, Pa_12, 'ReturnConditions', true);
Pa_12 = sol2.Pa_12;
na_1 = simplify(subs(na_1));
na_2 = simplify(subs(na_2));
nb_1 = simplify(subs(nb_1));
nb_2 = simplify(subs(nb_2));
pi_A = simplify(subs(pi_A));
pi_B = simplify(subs(pi_B));
eq5 = simplify(subs(diff(pi_A, Pa_11)));
eq7 = simplify(subs(diff(pi_A, Pa_2)));
sol3 = solve(eq5, eq7, Pa_11, Pa_2);
Pa_11 = sol3.Pa_11;
Pa_2 = sol3.Pa_2;
Pa_12 = simplify(subs(Pa_12));
sol4 = solve(Pa_11-Pb_11, Pa_12-Pb_12, Pa_2-Pb_2, Pb_11, Pb_12, Pb_2);
Pb_11 = sol4.Pb_11;
Pb_12 = sol4.Pb_12;
Pb_2 = sol4.Pb_2;
Pa_11 = simplify(subs(Pa_11));
Pa_12 = simplify(subs(Pa_12));
Pa_2 = simplify(subs(Pa_2));
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 3
% the subcase that Pa_2 = Pb_2 = 0
% Pa_2 = 0;
% Pb_2 = 0;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% eq5 = simplify(subs(diff(pi_A, Pa_11)));
% eq6 = simplify(subs(diff(pi_A, Pa_12)));
% eq8 = simplify(subs(diff(pi_B, Pb_11)));
% eq9 = simplify(subs(diff(pi_B, Pb_12)));
% sol3 = solve(eq5, eq6, eq8, eq9, Pa_11, Pa_12, Pb_11, Pb_12);
% Pa_11 = sol3.Pa_11;
% Pa_12 = sol3.Pa_12;
% Pb_11 = sol3.Pb_11;
% Pb_12 = sol3.Pb_12;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 4
% the subcase that Pb_11 = Pb_12 (APD)
% Pb_11 = Pb_1;
% Pb_12 = Pb_1;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% eq5 = diff(pi_A, Pa_11);
% eq6 = diff(pi_A, Pa_12);
% eq7 = diff(pi_A, Pa_2);
% eq8 = diff(pi_B, Pb_1);
% eq9 = diff(pi_B, Pb_2);
% sol3 = solve(eq5, eq6, eq7, eq8, eq9, Pa_11, Pa_12, Pa_2, Pb_1, Pb_2);
% Pa_11 = sol3.Pa_11;
% Pa_12 = sol3.Pa_12;
% Pa_2 = sol3.Pa_2;
% Pb_1 = sol3.Pb_1;
% Pb_2 = sol3.Pb_2;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% end
na_1 = simplify(subs(na_1));
na_2 = simplify(subs(na_2));
nb_1 = simplify(subs(nb_1));
nb_2 = simplify(subs(nb_2));
pi_A = simplify(subs(pi_A));
pi_B = simplify(subs(pi_B));
CS_A1 = na_2*alpha1*na_1 - Pa_11*(1-nb_1) - Pa_12*(na_1+nb_1-1) - t1*int(t, t, 0, na_1);
CS_B1 = nb_2*alpha1*nb_1 - Pb_11*(1-na_1) - Pb_12*(na_1+nb_1-1) - t1*int(t, t, 0, nb_1);
CS_A2 = na_1*alpha2*na_2 - Pa_2*na_2 - t2*int(t, t, 0, na_2);
CS_B2 = nb_1*alpha2*nb_2 - Pb_2*nb_2 - t2*int(t, t, 0, nb_2);
CS = simplify(subs(V_1 + V_2 + V*(na_1 + nb_1 -1) + CS_A1 + CS_B1 + CS_A2 + CS_B2));
SW = simplify(subs(CS + pi_A + pi_B));
% 
% multi-homing and single-homing: 统一定价(NE)
% syms alpha1 alpha2 V_1 V_2 V t1 t2 c1 c2 c real
% syms Pa_1 Pa_2 Pb_1 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% syms CS1 CS2 CS SW t real
% t1 = 1;
% t2 = 1;
% c1 = 0;
% c2 = 0;
% V = 0;
% eq1 = V + alpha1*nb_2 - t1*nb_1 - Pb_1;
% eq2 = V + alpha1*na_2 - t1*na_1 - Pa_1;
% eq3 = alpha2*na_1 - Pa_2 - t2*na_2 - (alpha2*nb_1 - Pb_2 - t2*nb_2);
% eq4 = na_2 + nb_2 - 1;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% pi_A = simplify(subs(Pa_1*na_1 + Pa_2*na_2 - c1*na_1 - c2*na_2));
% pi_B = simplify(subs(Pb_1*nb_1 + Pb_2*nb_2 - c1*nb_1 - c2*nb_2));
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 1
% the normal subcase
% eq5 = simplify(subs(diff(pi_A, Pa_1)));
% eq6 = simplify(subs(diff(pi_A, Pa_2)));
% eq7 = simplify(subs(diff(pi_B, Pb_1)));
% eq8 = simplify(subs(diff(pi_B, Pb_2)));
% sol2 = solve(eq5, eq6, eq7, eq8, Pa_1, Pa_2, Pb_1, Pb_2);
% Pa_1 = sol2.Pa_1;
% Pa_2 = sol2.Pa_2;
% Pb_1 = sol2.Pb_1;
% Pb_2 = sol2.Pb_2;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2
% the subcase that na_1 = nb_1 = 1
% sol2 = solve(na_1-1, Pa_1, 'ReturnConditions', true);
% Pa_1 = sol2.Pa_1;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% eq6 = simplify(subs(diff(pi_A, Pa_2)));
% sol3 = solve(eq6, Pa_2, 'ReturnConditions', true);
% Pa_2 = sol3.Pa_2;
% Pa_1 = simplify(subs(Pa_1));
% sol4 = solve(Pa_1-Pb_1, Pa_2-Pb_2, Pb_1, Pb_2);
% Pb_1 = sol4.Pb_1;
% Pb_2 = sol4.Pb_2;
% Pa_1 = simplify(subs(Pa_1));
% Pa_2 = simplify(subs(Pa_2));
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 3
% the subcase that Pa_1 = Pb_1 = 0
% Pa_1 = 0;
% Pb_1 = 0;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% eq6 = simplify(subs(diff(pi_A, Pa_2)));
% eq8 = simplify(subs(diff(pi_B, Pb_2)));
% sol2 = solve(eq6, eq8, Pa_2, Pb_2);
% Pa_2 = sol2.Pa_2;
% Pb_2 = sol2.Pb_2;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 4
% the subcase that Pa_2 = Pb_2 = 0
% Pa_2 = 0;
% Pb_2 = 0;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% eq5 = simplify(subs(diff(pi_A, Pa_1)));
% eq7 = simplify(subs(diff(pi_B, Pb_1)));
% sol2 = solve(eq5, eq7, Pa_1, Pb_1, 'ReturnConditions', true);
% Pa_1 = sol2.Pa_1;
% Pb_1 = sol2.Pb_1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% end
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(Pa_1*na_1 + Pa_2*na_2));
% pi_B = simplify(subs(Pb_1*nb_1 + Pb_2*nb_2));
% CS_A1 = na_2*alpha1*na_1 - Pa_1*na_1 - t1*int(t, t, 0, na_1);
% CS_B1 = nb_2*alpha1*nb_1 - Pb_1*nb_1 - t1*int(t, t, 0, nb_1);
% CS_A2 = na_1*alpha2*na_2 - Pa_2*na_2 - t2*int(t, t, 0, na_2);
% CS_B2 = nb_1*alpha2*nb_2 - Pb_2*nb_2 - t2*int(t, t, 0, nb_2);
% CS = simplify(subs(V_1 + V_2 + V*(na_1 + nb_1 -1) + CS_A1 + CS_B1 + CS_A2 + CS_B2));
% SW = simplify(subs(CS + pi_A + pi_B));
% 
% single-homing and single-homing: 统一定价
% syms alpha1 alpha2 V_1 V_2 t1 t2 c1 c2 c real
% syms Pa_1 Pa_2 Pb_1 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% syms CS1 CS2 CS SW t real
% V_1 = 0;
% V_2 = 0;
% t1 = 1;
% t2 = 1;
% c1 = 0;
% c2 = 0;
% eq1 = alpha1*na_2 - Pa_1 - t1*na_1 - (alpha1*nb_2 - Pb_1 - t1*nb_1);
% eq2 = na_1 + nb_1 - 1;
% eq3 = alpha2*na_1 - Pa_2 - t2*na_2 - (alpha2*nb_1 - Pb_2 - t2*nb_2);
% eq4 = na_2 + nb_2 - 1;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% pi_A = simplify(subs(Pa_1*na_1 + Pa_2*na_2 - c1*na_1 - c2*na_2));
% pi_B = simplify(subs(Pb_1*nb_1 + Pb_2*nb_2 - c1*nb_1 - c2*nb_2));
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 1
% normal subcase
% eq5 = simplify(subs(diff(pi_A, Pa_1)));
% eq6 = simplify(subs(diff(pi_A, Pa_2)));
% eq7 = simplify(subs(diff(pi_B, Pb_1)));
% eq8 = simplify(subs(diff(pi_B, Pb_2)));
% sol2 = solve(eq5, eq6, eq7, eq8, Pa_1, Pa_2, Pb_1, Pb_2);
% Pa_1 = sol2.Pa_1;
% Pa_2 = sol2.Pa_2;
% Pb_1 = sol2.Pb_1;
% Pb_2 = sol2.Pb_2;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 2
% the subcase that Pa_1 = Pb_1 = 0
% Pa_1 = 0;
% Pb_1 = 0;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% eq6 = simplify(subs(diff(pi_A, Pa_2)));
% eq8 = simplify(subs(diff(pi_B, Pb_2)));
% sol2 = solve(eq6, eq8, Pa_2, Pb_2);
% Pa_2 = sol2.Pa_2;
% Pb_2 = sol2.Pb_2;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 3
% the subcase that Pa_2 = Pb_2 = 0 (the same to subcase 2)
% Pa_2 = 0;
% Pb_2 = 0;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% eq5 = simplify(subs(diff(pi_A, Pa_1)));
% eq7 = simplify(subs(diff(pi_B, Pb_1)));
% sol2 = solve(eq5, eq7, Pa_1, Pb_1);
% Pa_1 = sol2.Pa_1;
% Pb_1 = sol2.Pb_1;
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% end
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% CS1 = V_1 + 2*na_2*alpha1*na_1 - 2*Pa_1*na_1 - 2*t1*int(t, t, 0, na_1);
% CS2 = V_2 + 2*na_1*alpha2*na_2 - 2*Pa_2*na_2 - 2*t2*int(t, t, 0, na_2);
% SW = CS1 + CS2 + pi_A + pi_B;
% CS1 = simplify(subs(CS1));
% CS2 = simplify(subs(CS2));
% CS = simplify(subs(CS1 + CS2));
% SW = simplify(subs(SW));
% 
% syms alpha1 alpha2 t1 t2 t real
% syms Pa_1 Pa_2 Pb_1 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% syms p x1 x2 x3 x4 real
% t1 = t;
% t2 = t;
% temp = (alpha1^2 - 11*alpha1*t1 + 10*t1^2)/9 + (alpha1^2 + alpha2^2 + 6*alpha1*alpha2)/8;
% alpha2 = -t2*alpha1/(3*t1) + 4*t2/3;
% temp = simplify(subs(temp));