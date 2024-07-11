def tic_tac_toe_winner(board):
    # Sprawdź poziome, pionowe i przekątne linie
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
            return board[i * 3]  # Wygrana w poziomie
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return board[i]  # Wygrana w pionie

    if board[0] == board[4] == board[8] != ' ':
        return board[0]  # Wygrana na przekątnej (od lewej góry do prawej dolnej)
    if board[2] == board[4] == board[6] != ' ':
        return board[2]  # Wygrana na przekątnej (od prawej góry do lewej dolnej)

    return None  # Brak wygranej

# Przykład użycia:
plansza = "XOX OXO XOX"
wynik = tic_tac_toe_winner(plansza)
if wynik:
    print(f"Wygrał gracz {wynik}")
else:
    print("Nie można tego rozstrzygnąć.")

def test_tic_tac_toe_winner():
    assert tic_tac_toe_winner("XXX XXX XXX") == "o"
    assert tic_tac_toe_winner("XOX XOO XXO") == "X"

test_tic_tac_toe_winner() 