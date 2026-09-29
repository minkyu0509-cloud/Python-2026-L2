import curses

def display_results(stdscr, students_list):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== DANH SÁCH SINH VIÊN & GPA ===", curses.A_BOLD)
    
    stdscr.addstr(2, 0, f"{'Mã SV':<10} | {'Họ và tên':<20} | {'GPA':<5}")
    stdscr.addstr(3, 0, "-" * 42)

    for i, s in enumerate(students_list):
        stdscr.addstr(4 + i, 0, f"{s.id:<10} | {s.name:<20} | {s.gpa:<5.1f}")

    stdscr.addstr(6 + len(students_list), 0, "Ấn phím bất kỳ để thoát...")
    stdscr.getch()