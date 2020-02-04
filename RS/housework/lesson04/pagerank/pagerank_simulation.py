import numpy as np
m = np.array([[0, 1/2, 1, 0],
			[1/3, 0, 0, 1/2],
			[1/3, 0, 0, 1/2],
			[1/3, 1/2, 0, 0]])
m_leak = np.array([[0, 0, 0, 1/2],
				   [0, 0, 0, 1/2],
				   [0, 1, 0, 0],
				   [0, 0, 1, 0]])

m_sink = np.array([[0, 0, 0, 0],
				   [1/2, 0, 0, 1],
				   [0, 1, 1, 0],
				   [1/2, 0, 0, 0]])

w = np.array([1/4, 1/4, 1/4, 1/4])

def work(m, w):
    for i in range(100):
        w = np.dot(m, w)
        print(w)


def random_work(m, w, n):
    d = 0.85
    for i in range(100):
        w = (1 - d)/n + d * np.dot(m, w)
        print(w)

# work(m, w)
# work(m_leak, w)
random_work(m_leak, w, 4)
