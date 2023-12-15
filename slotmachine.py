import random
MAX_LINES =3
MAX_BET=20
MIN_BET=1

ROWS=3
COLS=3

symbol_count = {
    "$" :2,
    "!": 4,
    "*": 6,
    "&": 8
}
symbol_value = {
    "$" :5,
    "!": 4,
    "*": 3,
    "&": 2
}
#https://www.youtube.com/watch?v=th4OBktqK1I (38:22)
#print("current bugs: can't bet more than 20 on each line regardless of balance")

def chek_winnings (columns, lines, bet, values):
    winnings=0
    winning_lines = []
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings+= values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ") #")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("amount must be bewtween 1-"+str(MAX_LINES))
        else:
            print("Please enter a number")
    return lines
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be bewtween ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet = bet * lines
        if total_bet > balance:
         print("dont bet more than your balance")
        else:
          break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = chek_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"You won on lines:", *winning_lines)
main()