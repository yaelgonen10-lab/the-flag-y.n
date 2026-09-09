"""
soldier.py
==========
דמות השחקן.

החייל מיוצג ע"י position - הפינה השמאלית-עליונה שלו על הלוח, [row, col].
כל השאר מחושב ממנו:
  * body_cells()  - 6 המשבצות העליונות (הגוף), נבדקות מול הדגל.
  * feet_cells()  - 2 המשבצות התחתונות (הרגליים), נבדקות מול המוקשים.

החייל אינו נשמר במטריצה של game_field - כך אין צורך "למחוק ולצייר מחדש"
אותו בכל תזוזה, והלוגיקה נשארת נקייה.
"""

import consts

# תזוזה של משבצת אחת לכל כיוון, בתור (delta_row, delta_col).
# שימו לב: ב-pygame הכיוון החיובי של ציר Y הוא כלפי מטה, לכן
# "מעלה" זו הקטנת השורה ו"מטה" זו הגדלתה.
DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# הפינה השמאלית-עליונה של החייל על הלוח (row, col).
position = [consts.SOLDIER_START_ROW, consts.SOLDIER_START_COL]


def create():
    """מציב את החייל במיקום ההתחלה (הפינה השמאלית-עליונה של הלוח)."""
    global position
    position = [consts.SOLDIER_START_ROW, consts.SOLDIER_START_COL]


def body_cells():
    """רשימת (row, col) של 6 משבצות הגוף (השורות העליונות)."""
    top, left = position
    return [(top + row, left + col)
            for row in range(consts.SOLDIER_BODY_ROWS)
            for col in range(consts.SOLDIER_COLS)]


def feet_cells():
    """רשימת (row, col) של 2 משבצות הרגליים (השורה התחתונה)."""
    top, left = position
    feet_top = top + consts.SOLDIER_BODY_ROWS
    return [(feet_top + row, left + col)
            for row in range(consts.SOLDIER_FEET_ROWS)
            for col in range(consts.SOLDIER_COLS)]


def can_move(direction):
    """האם תזוזה בכיוון הנתון תשאיר את כל החייל בתוך גבולות הלוח."""
    delta_row, delta_col = DIRECTIONS[direction]
    new_top = position[0] + delta_row
    new_left = position[1] + delta_col
    return (0 <= new_top
            and new_top + consts.SOLDIER_ROWS <= consts.BOARD_ROWS
            and 0 <= new_left
            and new_left + consts.SOLDIER_COLS <= consts.BOARD_COLS)


def move(direction):
    """מזיז את החייל משבצת אחת בכיוון הנתון.
    יש לוודא can_move(direction) לפני הקריאה."""
    delta_row, delta_col = DIRECTIONS[direction]
    position[0] += delta_row
    position[1] += delta_col


def pixel_top_left():
    """מיקום הפינה השמאלית-עליונה של החייל בפיקסלים, עבור הציור."""
    return (position[1] * consts.CELL_SIZE, position[0] * consts.CELL_SIZE)


if __name__ == "__main__":
    create()
    print("position :", position)
    print("body     :", body_cells())
    print("feet     :", feet_cells())
    for d in DIRECTIONS:
        print(f"can_move({d:5}) = {can_move(d)}")
