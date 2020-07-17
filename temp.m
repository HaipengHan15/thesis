% text(.5,.5,['$',latex(pb1),'$'],'interpreter','Latex','HorizontalAlignment','center','fontsize',20)
% 
% 5 temp
syms N real
syms P_1 P_2 real
syms na_1 nb_1 real
% profits = zeros(4, 500); % 2行，第一行P_2，第二行pi_2，第三行d_2，第四行m
% profits(1, 1) = 1;
% profits(2, 1) = 1/2;
% profits(3, 1) = 1/2;
% profits(4, 1) = 1;
% for N=2:length(profits)
%     if mod(N, 2) == 0
%         profits(1, N) = 2/N - 6/(N*N + 6*N);
%         profits(4, N) = 1 + N/2;
%     else
%         profits(1, N) = 2/N - 8/(N*N + 5*N);
%         profits(4, N) = 1 + (N+1)/2;
%     end
%     profits(3, N) = 1/2 + 1/(2*N) - profits(1, N)/2;
%     profits(2, N) = profits(3, N) * profits(1, N);
% end
% profits_table = array2table(profits);
% writetable(profits_table, 'C:\Users\HanHaipeng\Desktop\temp.csv');
% N is even
% P_2 = 2/N - 6/(N*N + 4*N);
% na_1 = (P_2+1)/2 - 1/(2*N);
% nb_1 = 1-na_1;
% na_1 = simplify(subs(na_1));
% nb_1 = simplify(subs(nb_1));
% pi_2 = simplify(subs(nb_1 * P_2));
% h1 = (na_1 - 1/2 + 1/(2*N))/2 + 1/(2*N);
% h2 = (na_1 - 1/2 + 1/(2*N))/2;
% temp1 = (1+P_2)/N * (N/2 - 1) - (N-2)/(4*N) + h1*h1*2 + h2*h2*2;
% temp1 = simplify(subs(temp1));
% N is odd
P_2 = 2/N - 8/(N*N + 5*N);
na_1 = (P_2+1)/2 - 1/(2*N);
nb_1 = 1-na_1;
na_1 = simplify(subs(na_1));
nb_1 = simplify(subs(nb_1));
pi_2 = simplify(subs(nb_1 * P_2));
h1 = (na_1 - 1/2)/2 + 1/(2*N);
h2 = (na_1 - 1/2)/2;
temp1 = (1+P_2)/N * (N - 1)/2 - (N*N-1)/(4*N*N) + h1*h1*2 + h2*h2*2;
temp1 = simplify(subs(temp1));