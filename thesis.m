% text(.5,.5,['$',latex(pb1),'$'],'interpreter','Latex','HorizontalAlignment','center','fontsize',20)
% 
% 1 两平台统一定价，平台之间没有竞争关系
% syms alpha1 alpha2 V_1 V_2 real
% syms Pa_1 Pb_1 Pa_2 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% eq1 = V_1 + alpha1*na_2 - Pa_1 - na_1;
% eq2 = V_2 + alpha2*na_1 - Pa_2 - na_2;
% sol1 = solve(eq1, eq2, na_1, na_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% pi_A = Pa_1*na_1 + Pa_2*na_2;
% eq3 = simplify(subs(diff(pi_A, Pa_1)));
% eq4 = simplify(subs(diff(pi_A, Pa_2)));
% sol2 = solve(eq3, eq4, Pa_1, Pa_2);
% Pa_1 = sol2.Pa_1;
% Pa_2 = sol2.Pa_2;
% 
% 1 两平台统一定价，group-1有竞争关系
% syms alpha1 alpha2 V_1 V_2 real
% syms Pa_1 Pb_1 Pa_2 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% eq1 = alpha1*na_2 - Pa_1 - na_1 - (alpha1*nb_2 - Pb_1 - nb_1);
% eq2 = V_2 + alpha2*na_1 - Pa_2 - na_2;
% eq3 = V_2 + alpha2*nb_1 - Pb_2 - nb_2;
% eq4 = na_1 + nb_1 - 1;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% pi_A = Pa_1*na_1 + Pa_2*na_2;
% pi_B = Pb_1*nb_1 + Pb_2*nb_2;
% eq3 = simplify(subs(diff(pi_A, Pa_1)));
% eq4 = simplify(subs(diff(pi_A, Pa_2)));
% eq5 = simplify(subs(diff(pi_B, Pb_1)));
% eq6 = simplify(subs(diff(pi_B, Pb_2)));
% sol2 = solve(eq3, eq4, eq5, eq6, Pa_1, Pa_2, Pb_1, Pb_2);
% Pa_1 = sol2.Pa_1;
% Pa_2 = sol2.Pa_2;
% Pb_1 = sol2.Pb_1;
% Pb_2 = sol2.Pb_2;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_A = simplify(subs(pi_A));
% pi_B = simplify(subs(pi_B));
% 
% APD
% syms alpha1 alpha2 V_1 V_2 N M real
% syms Pa_1 Pb_1 Pa_2 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% two-side APD for N>1, M>1
% eq1 = (alpha1+2*alpha2)*na_2 - 2*na_1 - 1/N - (alpha1*nb_2 - Pb_1 - 1);
% eq2 = (alpha2+2*alpha1)*na_1 - 2*na_2 - 1/M - (alpha2*nb_1 - Pb_2 - 1);
% N>1, M=1
% eq1 = (alpha1+2*alpha2)*na_2 - 2*na_1 - 1/N - (alpha1*nb_2 - Pb_1 - 1);
% eq2 = (alpha2+2*alpha1)*na_1 - 4*na_2 - (alpha2*nb_1 - Pb_2 - 1);
% eq3 = na_1 + nb_1 - 1;
% eq4 = na_2 + nb_2 - 1;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% pi_B = Pb_1*nb_1 + Pb_2*nb_2;
% eq3 = simplify(subs(diff(pi_B, Pb_1)));
% eq4 = simplify(subs(diff(pi_B, Pb_2)));
% sol2 = solve(eq3, eq4, Pb_1, Pb_2);
% Pb_1 = sol2.Pb_1;
% Pb_2 = sol2.Pb_2;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_B = simplify(subs(pi_B));
% N>1, M=1
% eq1 = (alpha1+2*alpha2)*na_2 - 2*na_1 - 1/N - (alpha1*nb_2 - Pb_1 - 1);
% eq2 = (alpha2+2*alpha1)*na_1 - 3*na_2 - ((alpha2+2*alpha1)*nb_1 - 3*nb_2);
% eq3 = na_1 + nb_1 - 1;
% eq4 = na_2 + nb_2 - 1;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% Pb_2 = 2*nb_2 - 2*alpha1*nb_1;
% pi_B = Pb_1*nb_1 + Pb_2*nb_2;
% eq3 = simplify(subs(diff(pi_B, Pb_1)));
% sol2 = solve(eq3, Pb_1, 'ReturnConditions', true);
% Pb_1 = sol2.Pb_1;
% Pb_2 = simplify(subs(Pb_2));
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_B = simplify(subs(pi_B));
% 
% 3 A平台完全价格歧视，B平台在Group-1上统一定价
% syms alpha1 alpha2 V_1 V_2 N M real
% syms Pa_1 Pb_1 Pa_2 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% eq1 = alpha1*na_2 + 2*alpha2*na_2 - na_1 - (alpha1*nb_2 - Pb_1 - nb_1);
% eq2 = alpha2*na_1 + 2*alpha1*na_1 - na_2 - (alpha2*nb_1 - 2*alpha1*nb_1 - nb_2);
% eq3 = na_1 + nb_1 - 1;
% eq4 = na_2 + nb_2 - 1;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% temp = alpha2*nb_1 - alpha2*na_1 - 2*alpha1*na_1 + 1;
% pi_B = simplify(subs(Pb_1*nb_1 + (temp-2*alpha1*nb_1)*nb_2/2));
% eq3 = diff(pi_B, Pb_1);
% sol2 = solve(eq3, Pb_1, 'ReturnConditions', true);
% Pb_1 = sol2.Pb_1;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_B = simplify(subs(pi_B));
% 
% 4 A平台完全价格歧视，B平台统一定价
% syms alpha1 alpha2 V_1 V_2 N M real
% syms Pa_1 Pb_1 Pa_2 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 real
% eq1 = alpha1*na_2 + 2*alpha2*na_2 - na_1 - (alpha1*nb_2 - Pb_1 - nb_1);
% eq2 = alpha2*na_1 + 2*alpha1*na_1 - na_2 - (alpha2*nb_1 - Pb_2 - nb_2);
% eq3 = na_1 + nb_1 - 1;
% eq4 = na_2 + nb_2 - 1;
% sol1 = solve(eq1, eq2, eq3, eq4, na_1, na_2, nb_1, nb_2);
% na_1 = sol1.na_1;
% na_2 = sol1.na_2;
% nb_1 = sol1.nb_1;
% nb_2 = sol1.nb_2;
% pi_B = simplify(subs(Pb_1*nb_1 + Pb_2*nb_2));
% eq3 = diff(pi_B, Pb_1);
% eq4 = diff(pi_B, Pb_2);
% sol2 = solve(eq3, eq4, Pb_1, Pb_2, 'ReturnConditions', true);
% Pb_1 = sol2.Pb_1;
% Pb_2 = sol2.Pb_2;
% na_1 = simplify(subs(na_1));
% na_2 = simplify(subs(na_2));
% nb_1 = simplify(subs(nb_1));
% nb_2 = simplify(subs(nb_2));
% pi_B = simplify(subs(pi_B));
% 
% 5 temp
% syms alpha1 alpha2 V_1 V_2 N M real
% syms Pa_1 Pb_1 Pa_2 Pb_2 real
% syms na_1 na_2 nb_1 nb_2 na1_t na2_t real
% profits = zeros(6, 500); % 6行，第一行Pb_1，第二行Pb_2，第三行na_1，第四行na_2
% alpha1 = 0.3;
% alpha2 = 0.4;
% profits(1, 1) = 1 - alpha2;
% profits(2, 1) = 1 - alpha1;
% profits(3, 1) = 1/2;
% profits(4, 1) = 1/2;
% profits(5, 1) = 1;
% profits(6, 1) = 1;
% for NM=2:length(profits)
%     N = NM;
%     M = NM;
%     for i=ceil(N/2 + 1/2):N
%         flag = 0;
%         for j=ceil(M/2 + 1/2):M
%             eq1 = (2*alpha1+4*alpha2)*na2_t-2*na1_t-1/N -(alpha1-2*(1-na1_t)/i+2*alpha2-1);
%             eq2 = (2*alpha2+4*alpha1)*na1_t-2*na2_t-1/M -(alpha2-2*(1-na2_t)/j+2*alpha1-1);
%             sol1 = solve(eq1, eq2, na1_t, na2_t);
%             temp1 = eval(vpa(sol1.na1_t));
%             temp2 = eval(vpa(sol1.na2_t));
%             for k=1:length(temp1(:))
%                 if temp1(k) >= 0.5 && temp1(k) <=1
%                     temp1 = temp1(k);
%                     break;
%                 end
%             end
%             for l=1:length(temp2(:))
%                 if temp2(l) >= 0.5 && temp2(l) <=1
%                     temp2 = temp2(l);
%                     break;
%                 end
%             end
%             i_exp = (floor(N*temp1 - 1/2)+2);
%             j_exp = (floor(M*temp2 - 1/2)+2);
%             if isempty(temp1) || isempty(temp2)
%                 continue;
%             elseif i<=i_exp && j>j_exp
%                 break
%             elseif i==i_exp && j==j_exp
%                 flag = 1;
%                 break
%             elseif i>i_exp
%                 flag = 2;
%                 break
%             end
%         end
%         if flag==1
%             na_1 = temp1;
%             na_2 = temp2;
%             profits(1, NM) = 2*(1-na_1)/i - 2*(1-na_2)*alpha2; % Pb_1
%             profits(2, NM) = 2*(1-na_2)/j - 2*(1-na_1)*alpha1; % Pb_2
%             profits(3, NM) = na_1;
%             profits(4, NM) = na_2;
%             profits(5, NM) = i;
%             profits(6, NM) = j;
%             fprintf(1,'%g\n',NM);
%             break
%         elseif flag==2
%             profits(1, NM) = i;
%             profits(2, NM) = j;
%             fprintf(1,'%g\n',-1);
%             break;
%         end
%     end
% end
% 
% for NM=50:50
%     N = NM;
%     M = NM;
%     flag = 0;
%     i=27;
%     j=27;
%     na1_t = 26.5/N;
%     na2_t = 12.5/M;
%     eq1 = (2*alpha1+4*alpha2)*na2_t-2*na1_t-1/N -(alpha1-2*(1-na1_t)/i+2*alpha2-1);
%     eq2 = (2*alpha2+4*alpha1)*na1_t-2*na2_t-1/M -(alpha2-2*(1-na2_t)/j+2*alpha1-1);
%     sol1 = solve(eq2, na2_t, 'ReturnConditions', true);
%     temp1 = eval(vpa(sol1.na1_t));
%     temp2 = eval(vpa(sol1.na2_t));
%     temp1 = na1_t;
%     temp2 = na2_t;
%     eq1 = (2*alpha1+4*alpha2)*na2_t-2*na1_t-1/N -(alpha1-2*(1-na1_t)/i+2*alpha2-1);
%     eq2 = (2*alpha2+4*alpha1)*na1_t-2*na2_t-1/M -(alpha2-2*(1-na2_t)/j+2*alpha1-1);
%     sol1 = solve(eq1, eq2, na1_t, na2_t);
%     temp1 = eval(vpa(sol1.na1_t));
%     temp2 = eval(vpa(sol1.na2_t));
%     for k=1:length(temp1(:))
%         if temp1(k) >= 0.5 && temp1(k) <=1
%             temp1 = temp1(k);
%             break;
%         end
%     end
%     for l=1:length(temp2(:))
%         if temp2(l) >= 0.5 && temp2(l) <=1
%             temp2 = temp2(l);
%             break;
%         end
%     end
%     i_exp = (floor(N*temp1 - 1/2)+2);
%     j_exp = (floor(M*temp2 - 1/2)+2);
%     if isempty(temp1) || isempty(temp2)
%         continue;
%     elseif i<=i_exp && j>j_exp
%     elseif i==i_exp && j==j_exp
%         flag = 1;
%     elseif i>i_exp
%         flag = 2;
%     end
%     Pb_1 = (alpha1 - 1 - 2*(alpha1+alpha2)*temp2 + 2*temp1 + 1/N);
%     Pb_2 = (alpha2 - 1 - 2*(alpha1+alpha2)*temp1 + 2*temp2 + 1/M);
%     profits(1, NM) = Pb_1;
%     profits(2, NM) = Pb_2;
%     profits(3, NM) = temp1; % na_1
%     profits(4, NM) = temp2; % na_2
%     fprintf(1,'%g\n',-1);
% end
% profits_table = array2table(profits, 'RowNames', {'Pb_1', 'Pb_2', 'na_1', 'na_2', 'n', 'm'});
% writetable(profits_table, 'C:\Users\HanHaipeng\Desktop\result4.csv');
% 6 temp
% syms alpha1 alpha2 V_1 V_2 N M real
% syms Pa_1 Pb_1 Pa_2 real
% syms na_1 na_2 nb_1 nb_2 na1_t na2_t real
% profits = zeros(5, 500); % 5行，第一行Pb_1，第二行na_1，第三行na_2
% alpha1 = 0.2;
% alpha2 = 0.3;
% profits(1, 1) = 1 - alpha2;
% profits(2, 1) = 1/2;
% profits(3, 1) = 1/2;
% profits(4, 1) = 1;
% profits(5, 1) = 1;
% for NM=2:length(profits)
%     N = NM;
%     M = NM;
%     for i=ceil(N/2)+1:N
%         flag = 0;
%         eq1 = (2*alpha1+4*alpha2)*na2_t-2*na1_t-1/N -(alpha1-2*(1-na1_t)/i+2*alpha2-1);
%         eq2 = (2*alpha2+4*alpha1)*na1_t-2*na2_t -(alpha2+2*alpha1-1);
%         sol1 = solve(eq1, eq2, na1_t, na2_t);
%         temp1 = eval(vpa(sol1.na1_t));
%         temp2 = eval(vpa(sol1.na2_t));
%         for k=1:length(temp1(:))
%             if temp1(k) >= 0.5 && temp1(k) <=1
%                 temp1 = temp1(k);
%                 break;
%             end
%         end
%         for l=1:length(temp2(:))
%             if temp2(l) >= 0.5 && temp2(l) <=1
%                 temp2 = temp2(l);
%                 break;
%             end
%         end
%         i_exp = (floor(N*temp1 - 1/2)+2);
%         j_exp = (floor(M*temp2 - 1)+3);
%         if isempty(temp1) || isempty(temp2)
%             continue;
%         elseif i==i_exp
%             flag = 1;
%             break
%         elseif i>i_exp
%             flag = 2;
%             break
%         end
%     end
%     if flag==1
%         na_1 = temp1;
%         na_2 = temp2;
%         profits(1, NM) = 2*(1-na_1)/i - 2*(1-na_2)*alpha2; % Pb_1
%         profits(2, NM) = na_1;
%         profits(3, NM) = na_2;
%         profits(4, NM) = i;
%         profits(5, NM) = j_exp;
%         fprintf(1,'%g\n',NM);
%     elseif flag==2
%         profits(1, NM) = i;
%         profits(2, NM) = j_exp;
%         fprintf(1,'%g\n',-1);
%     end
% end
% 
% for NM=81:81
%     N = NM;
%     M = NM;
%     flag = 0;
%     i=42;
%     na1_t = 26.5/N;
%     na2_t = 12.5/M;
%     eq1 = (2*alpha1+4*alpha2)*na2_t-2*na1_t-1/N -(alpha1-2*(1-na1_t)/i+2*alpha2-1);
%     eq2 = (2*alpha2+4*alpha1)*na1_t-2*na2_t -(alpha2+2*alpha1-1);
%     sol1 = solve(eq2, na2_t, 'ReturnConditions', true);
%     temp1 = eval(vpa(sol1.na1_t));
%     temp2 = eval(vpa(sol1.na2_t));
%     temp1 = na1_t;
%     temp2 = na2_t;
%     eq1 = (2*alpha1+4*alpha2)*na2_t-2*na1_t-1/N -(alpha1-2*(1-na1_t)/i+2*alpha2-1);
%     eq2 = (2*alpha2+4*alpha1)*na1_t-2*na2_t -(alpha2+2*alpha1-1);
%     sol1 = solve(eq1, eq2, na1_t, na2_t);
%     temp1 = eval(vpa(sol1.na1_t));
%     temp2 = eval(vpa(sol1.na2_t));
%     for k=1:length(temp1(:))
%         if temp1(k) >= 0.5 && temp1(k) <=1
%             temp1 = temp1(k);
%             break;
%         end
%     end
%     for l=1:length(temp2(:))
%         if temp2(l) >= 0.5 && temp2(l) <=1
%             temp2 = temp2(l);
%             break;
%         end
%     end
%     i_exp = (floor(N*temp1 - 1/2)+2);
%     j_exp = (floor(M*temp2 - 1)+3);
%     if isempty(temp1) || isempty(temp2)
%         continue;
%     elseif i==i_exp
%         flag = 1;
%     elseif i>i_exp
%         flag = 2;
%     end
%     Pb_1 = (alpha1 - 1 - 2*(alpha1+alpha2)*temp2 + 2*temp1 + 1/N);
%     profits(1, NM) = Pb_1;
%     profits(2, NM) = temp1; % na_1
%     profits(3, NM) = temp2; % na_2
%     profits(4, NM) = i;
%     profits(5, NM) = j_exp;
%     fprintf(1,'%g\n',-1);
% end
% profits_table = array2table(profits, 'RowNames', {'Pb_1', 'na_1', 'na_2', 'n', 'm'});
% writetable(profits_table, 'C:\Users\HanHaipeng\Desktop\result21.csv');
% 7 estimate
syms alpha1 alpha2 V_1 V_2 N M n m real
syms Pa_1 Pb_1 Pa_2 real
syms na_1 na_2 nb_1 nb_2 na1_t na2_t real
% n = 1; 
% m = 1; 
eq1 = (2*alpha1+4*alpha2)*na2_t-2*na1_t-1/N -alpha1+2*(1-na1_t)/n-2*alpha2+1;
eq2 = (2*alpha2+4*alpha1)*na1_t-2*na2_t-1/M -alpha2+2*(1-na2_t)/m-2*alpha1+1;
% eq1 = (2*alpha1+4*alpha2)*na2_t-2*na1_t-1/N -alpha1+1/n-2*alpha2+1;
% eq2 = (2*alpha2+4*alpha1)*na1_t-2*na2_t-1/M -alpha2+1/m-2*alpha1+1;
sol1 = solve(eq1, eq2, na1_t, na2_t);
na_1 = sol1.na1_t;
na_2 = sol1.na2_t;
temp1 = diff(na_1, N);
temp2 = diff(na_2, M);
temp1 = simplify(subs(temp1));
temp2 = simplify(subs(temp2));
% Pb_1 = 2*(1-na_1)/n - 2*na_2*alpha2;
% Pb_2 = 2*(1-na_2)/m - 2*na_1*alpha1;
% profit_B = Pb_1*(1-na_1) + Pb_2*(1-na_2);
% sol2 = solve(profit_B, N, na1_t, na2_t);