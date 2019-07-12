import numpy as np
import tensorflow as tf
import sympy


def A_profit_i(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, i):
    # i从零开始
    operater = N * M * alpha1 * alpha2
    A_price1_changed = A_price1.copy()
    A_price1_changed[i] = 0
    B_sum_price1 = np.sum(B_price1)
    B_sum_price2 = np.sum(B_price2)
    A_sum_price1 = np.sum(A_price1_changed)
    A_sum_price2 = np.sum(A_price2)
    if 0.5 + alpha1 * (alpha2 * M * (A_sum_price1 - B_sum_price1) +
                       A_sum_price2 - B_sum_price2) / (2 * operater) + 0.5 * B_price1[i] - i / N <= 0:
        return 0
    average = (operater + alpha1 * (
        alpha2 * M * (A_sum_price1 - B_sum_price1) +
        A_sum_price2 - B_sum_price2) + B_price1[i] * operater -
        operater * (2 * i + 1) / N) / (operater - alpha1 * alpha2 * M)
    sigma = abs(operater / (2 * N * (alpha1 * alpha2 * M - operater)))
    A_price1_i = tf.Variable(tf.truncated_normal(
        shape=[1], mean=average, stddev=sigma))
    loss = -1 * (
        0.5 * A_price1_i + alpha1 * (A_sum_price1 + A_price1_i) *
        (alpha2 * M * (A_sum_price1 + A_price1_i - B_sum_price1)) / (2 * operater)
        - 0.5 * (A_price1_i * A_price1_i) + 0.5 * A_price1_i * B_price1[i]
        - A_price1_i * i / N + alpha2 * A_sum_price2 *
        (A_sum_price1 + A_price1_i - B_sum_price1) / (2 * operater))
    train_op = tf.train.AdamOptimizer(1e-4).minimize(loss)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for k in range(5000):
            xs, loss_show = sess.run([A_price1_i, loss])
            A_price1_changed[i] = xs
            A_n1 = A_n(N, M, alpha1, alpha2, A_price1_changed,
                       A_price2, B_price1, B_price2, 1)
            # if (A_n1 >= 0).all() and (A_n1 <= 1 / N).all():
            _ = sess.run(train_op)
            print(k, loss_show, xs, A_n1[i])
'''            A_price1_changed[i] = xs
            A_n1 = A_n(N, M, alpha1, alpha2, A_price1_changed,
                       A_price2, B_price1, B_price2, 1)
            A_n2 = A_n(N, M, alpha1, alpha2, A_price1_changed,
                       A_price2, B_price1, B_price2, 2)'''


def A_n(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, group):
    B_sum_price1 = np.sum(B_price1)
    B_sum_price2 = np.sum(B_price2)
    A_sum_price1 = np.sum(A_price1)
    A_sum_price2 = np.sum(A_price2)
    operater = N * M * alpha1 * alpha2
    if(group == 1):
        # 用户群体1
        result = np.zeros(N)
        operater1 = alpha1 * (alpha2 * M * (A_sum_price1 - B_sum_price1)
                              + A_sum_price2 - B_sum_price2) / (2 * operater)
        for i in range(N):
            result[i] = 0.5 + operater1 - 0.5 * \
                (A_price1[i] - B_price1[i]) - i / N
            if result[i] < i / N:
                result[i] = i / N
            if result[i] > (i + 1) / N:
                result[i] = (i + 1) / N
    else:
        # 用户群体2
        result = np.zeros(M)
        operater1 = alpha2 * (alpha1 * N * (A_sum_price2 - B_sum_price2)
                              + A_sum_price1 - B_sum_price1) / (2 * operater)
        for j in range(M):
            result[j] = 0.5 * alpha2 + operater1 - A_price2[j] - j / N
            if result[j] < j / M:
                result[j] = j / M
            if result[j] > (j + 1) / M:
                result[j] = (j + 1) / M
    return result


N = 5
M = 5
A_price1 = np.ones(N)
A_price2 = np.ones(M)
B_price1 = np.ones(N)
B_price2 = np.ones(M)
a1 = 0.01
a2 = 2
A_profit_i(N, M, a1, a2, A_price1, A_price2, B_price1, B_price2, N - 1)
