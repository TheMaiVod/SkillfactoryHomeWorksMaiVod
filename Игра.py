def initialize_board():
    """
    Инициализирует пустое игровое поле 3x3.
    Каждая ячейка содержит '-', что означает "пусто".
    """
    return [['-' for _ in range(3)] for _ in range(3)]


def print_board(board):
    """
    Выводит текущее состояние игрового поля в консоль.
    
    Формат вывода:
      0 1 2
    0 X - O
    1 - X -
    2 O - X
    
    где X и O - символы игроков, '-' - пустая ячейка
    """
    print("\n  0 1 2")  # заголовок столбцов
    for i in range(3):
        row_display = f"{i} "  # номер строки
        for j in range(3):
            row_display += board[i][j] + " "
        print(row_display)
    print()  # пустая строка для читаемости


def get_player_move(board, player_symbol):
    """
    Запрашивает у игрока координаты хода и проверяет их корректность.
    """
    while True:
        try:
            # Получаем ввод от пользователя
            input_str = input(f"Игрок {player_symbol}, введите координаты (строка столбец): ")
            
            # Проверяем, что введены два числа
            coords = input_str.split()
            if len(coords) != 2:
                print("Ошибка: нужно ввести ДВА числа через пробел!")
                continue
            
            row, col = int(coords[0]), int(coords[1])
            
            # Проверяем, что координаты в пределах поля
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Ошибка: координаты должны быть от 0 до 2!")
                continue
            
            # Проверяем, что ячейка свободна
            if board[row][col] != '-':
                print("Ошибка: эта ячейка уже занята!")
                continue
            
            return row, col
            
        except ValueError:
            print("Ошибка: вводите только числа!")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


def check_win(board, player_symbol):
    """
    Проверяет, выиграл ли указанный игрок.
    
    Проверяет все возможные выигрышные комбинации:
    1. Горизонтальные линии
    2. Вертикальные линии
    3. Диагонали
    
    Args:
        board: игровое поле
        player_symbol: символ игрока для проверки
    
    Returns:
        True если игрок выиграл, иначе False
    """
    # Проверка горизонтальных линий
    for i in range(3):
        if all(board[i][j] == player_symbol for j in range(3)):
            return True
    
    # Проверка вертикальных линий
    for j in range(3):
        if all(board[i][j] == player_symbol for i in range(3)):
            return True
    
    # Проверка диагоналей
    if all(board[i][i] == player_symbol for i in range(3)):
        return True
    if all(board[i][2-i] == player_symbol for i in range(3)):
        return True
    
    return False


def check_draw(board):
    """
    Проверяет, является ли текущая ситуация ничьей.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True


def play_game():

    print("=" * 40)
    print("       КРЕСТИКИ-НОЛИКИ")
    print("=" * 40)
    print("\nПравила:")
    print("1. Игроки ходят по очереди")
    print("2. X ходит первым")
    print("3. Вводите координаты: номер строки и номер столбца")
    print("   Например: '1 2' для второй строки, третьего столбца")
    print("4. Координаты от 0 до 2")
    print("=" * 40)
    
    # Инициализация игрового поля
    board = initialize_board()
    current_player = 'X'
    move_count = 0
    
    print("\nНачальное поле:")
    print_board(board)
    
    # Главный игровой цикл
    while True:
        # Получаем ход текущего игрока
        row, col = get_player_move(board, current_player)
        
        # Выполняем ход
        board[row][col] = current_player
        move_count += 1
        
        print(f"\nХод {move_count}:")
        print_board(board)
        
        # Проверяем победу текущего игрока
        if check_win(board, current_player):
            print("=" * 40)
            print(f"ПОБЕДА! Игрок {current_player} выиграл!")
            print("=" * 40)
            break
        
        # Проверяем ничью
        if check_draw(board):
            print("=" * 40)
            print("НИЧЬЯ! Все ячейки заполнены.")
            print("=" * 40)
            break
        
        # Передаем ход другому игроку
        current_player = 'O' if current_player == 'X' else 'X'
    
    # Предложение сыграть еще раз
    play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
    if play_again in ['да', 'д', 'yes', 'y']:
        play_game()
    else:
        print("\nСпасибо за игру! До свидания!")



# Точка входа в программу
if __name__ == "__main__":
    """
Запуск игры
    """
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nИгра прервана пользователем.")
