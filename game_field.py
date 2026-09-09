"""
game_field.py
=============
ניהול לוח המשחק ברמת הלוגיקה (שורות ועמודות, בלי פיקסלים).

הלוח מיוצג ע"י מטריצה בגודל BOARD_ROWS x BOARD_COLS.
כל תא הוא אחד מ: consts.EMPTY / consts.MINE / consts.FLAG.
החייל *אינו* נשמר במטריצה - הוא מנוהל במודול soldier, וכך הציור
והלוגיקה של החייל לא מתערבבים עם הלוח.
"""

import random

import consts

# המטריצה עצמה. נבנית מחדש בכל קריאה ל-build().
matrix = []

# רשימת הפינות השמאליות (row, col) של המוקשים, לשימוש הציור במצב החשיפה.
mines = []


def build():
    """בונה לוח חדש: מטריצה ריקה, דגל בפינה הימנית-תחתונה, ומוקשים אקראיים."""
    global matrix, mines
    matrix = [[consts.EMPTY for _ in range(consts.BOARD_COLS)]
              for _ in range(consts.BOARD_ROWS)]
    mines = []
    _place_flag()
    _scatter_mines()


# ---------------------------------------------------------------------------
# דגל
# ---------------------------------------------------------------------------
def flag_top_left():
    """(row, col) של הפינה השמאלית-עליונה של הדגל.
    מחושב מגודל הלוח פחות גודל הדגל - אין כאן מספר קבוע."""
    return (consts.BOARD_ROWS - consts.FLAG_ROWS,
            consts.BOARD_COLS - consts.FLAG_COLS)


def _place_flag():
    """מסמן את משבצות הדגל במטריצה."""
    top, left = flag_top_left()
    for row in range(top, top + consts.FLAG_ROWS):
        for col in range(left, left + consts.FLAG_COLS):
            matrix[row][col] = consts.FLAG


# ---------------------------------------------------------------------------
# מוקשים
# ---------------------------------------------------------------------------
def _scatter_mines():
    """מפזר MINES_COUNT מוקשים במיקומים אקראיים חוקיים."""
    placed = 0
    while placed < consts.MINES_COUNT:
        row = random.randint(0, consts.BOARD_ROWS - consts.MINE_ROWS)
        # שהמוקש בן שלוש המשבצות ייכנס בתוך הלוח
        col = random.randint(0, consts.BOARD_COLS - consts.MINE_COLS)
        if _can_place_mine(row, col):
            _put_mine(row, col)
            placed += 1


def _can_place_mine(row, col):
    """בודק שאפשר להניח מוקש שפינתו השמאלית ב-(row, col):
    לא על הדגל, לא על פינת ההתחלה של החייל, ולא צמוד למוקש קיים."""
    # לא לחפוף את ריבוע ההתחלה של החייל - אחרת הפסד כבר בפריים הראשון
    if row < consts.SOLDIER_ROWS and col < consts.SOLDIER_COLS:
        return False

    # לבדוק את טווח המוקש עצמו + רווח MINE_GAP מכל צד
    left = max(0, col - consts.MINE_GAP)
    right = min(consts.BOARD_COLS - 1, col + consts.MINE_COLS - 1 + consts.MINE_GAP)
    for check_col in range(left, right + 1):
        if matrix[row][check_col] != consts.EMPTY:
            return False
    return True


def _put_mine(row, col):
    """מסמן את שלוש משבצות המוקש ומוסיף אותו לרשימת המוקשים."""
    for i in range(consts.MINE_COLS):
        matrix[row][col + i] = consts.MINE
    mines.append((row, col))


# ---------------------------------------------------------------------------
# בדיקות התנגשות - מקבלות רשימת משבצות ומחזירות תשובה בוליאנית
# ---------------------------------------------------------------------------
def any_cell_has(cells, marker):
    """האם לפחות אחת מהמשבצות ברשימה מסומנת ב-marker הנתון."""
    return any(matrix[row][col] == marker for row, col in cells)


def touches_flag(cells):
    """האם אחת מהמשבצות נוגעת בדגל (משמש לבדיקת ניצחון מול גוף החייל)."""
    return any_cell_has(cells, consts.FLAG)


def touches_mine(cells):
    """האם אחת מהמשבצות נוגעת במוקש (משמש לבדיקת הפסד מול רגלי החייל)."""
    return any_cell_has(cells, consts.MINE)


# ---------------------------------------------------------------------------
# עזר לבדיקות ידניות: הרצת הקובץ עצמו מדפיסה את הלוח
# ---------------------------------------------------------------------------
def print_matrix():
    symbols = {consts.EMPTY: ".", consts.MINE: "x", consts.FLAG: "f"}
    for row in matrix:
        print(" ".join(symbols[cell] for cell in row))


if __name__ == "__main__":
    build()
    print_matrix()
    print("mines:", mines)
