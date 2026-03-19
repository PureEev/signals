import itertools

def generate_simplex_matrix(m):
    """
    Генерирует порождающую матрицу Симплексного кода порядка m.
    (Она же - проверочная матрица кода Хэмминга).
    Столбцы матрицы - это все возможные ненулевые двоичные векторы длины m.
    """
    columns = []
    for i in range(1, 2**m):
        col = [int(x) for x in bin(i)[2:].zfill(m)]
        columns.append(col)
    
    G = [[columns[j][i] for j in range(len(columns))] for i in range(m)]
    return G

def encode_message(v, G):
    """
    Умножает информационный вектор v на порождающую матрицу G по модулю 2.
    Возвращает кодовое слово.
    """
    codeword = []
    for col_idx in range(len(G[0])):
        bit_sum = sum(v[row_idx] * G[row_idx][col_idx] for row_idx in range(len(v)))
        codeword.append(bit_sum % 2) 
    return codeword

def example_task_2():
    """
    Решение Задачи 2 с использованием написанных функций.
    """
    print("=" * 60)
    print("ПРИМЕР: ЗАДАЧА 2 (Симплекс-код длины 7, m=3)")
    print("=" * 60)
    
    m = 3
    H_task = [
        [0, 0, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1]
    ]
    
    print("Порождающая матрица G (проверочная матрица H из условия):")
    for row in H_task:
        print(row)
        
    print("\nПроверяем все возможные кодовые слова c = v*H (mod 2):")
    print(f"{'Сообщение v':<15} | {'Кодовое слово c':<25} | {'Вес (кол-во 1)'}")
    print("-" * 60)
    
    all_messages = list(itertools.product([0, 1], repeat=m))
    
    for v_tuple in all_messages:
        v = list(v_tuple)
        c = encode_message(v, H_task)
        weight = sum(c)
        
        print(f"{str(v):<15} | {str(c):<25} | {weight}")
        

if __name__ == "__main__":
    example_task_2()