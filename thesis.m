syms n m N M alpha1 alpha2 positive
operator = alpha1*alpha2*N*M-1;
coefficient_matrix = [n*M*alpha1*alpha2/operator-1 -n*M*alpha1*alpha2/(2*operator) n*(alpha1+alpha2)/(2*operator) -n*alpha1/(2*operator);...
    -n*M*alpha1*alpha2/(2*operator) n*M*alpha1*alpha2/operator-1 -n*alpha1/(2*operator) n*(alpha1+alpha2)/(2*operator);...
    m*(alpha1+alpha2)/(2*operator) -m*alpha2/(2*operator) m*N*alpha1*alpha2/operator-1 -m*N*alpha1*alpha2/(2*operator);...
    -m*alpha2/(2*operator) m*(alpha1+alpha2)/(2*operator) -m*N*alpha1*alpha2/(2*operator) m*N*alpha1*alpha2/operator-1];
inv_matrix = inv(coefficient_matrix);
result_matrix = [-n/2+(n-1)*n/(2*N);n/2-(n+1)*n/(2*N);-m/2+(m-1)*m/(2*M);m/2-(m+1)*m/(2*M)];
result = inv_matrix * result_matrix; %#ok<*MINV>
temp = [M*alpha1*alpha2/operator -M*alpha1*alpha2/(2*operator) (alpha1+alpha2)/(2*operator) -alpha1/(2*operator)];
p_A_1n = 0.5 + temp*result - (n-1)/N;