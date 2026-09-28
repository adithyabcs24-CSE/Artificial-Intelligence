def vacuum_cleaner(position, room_a, room_b):
    if position == "A":
        if room_a == "DIRTY":
            print("SUCK")
            room_a = "CLEAN"
        print("MOVE RIGHT")
        position = "B"
        if room_b == "DIRTY":
            print("SUCK")
            room_b = "CLEAN"
    else:
        if room_b == "DIRTY":
            print("SUCK")
            room_b = "CLEAN"
        print("MOVE LEFT")
        position = "A"
        if room_a == "DIRTY":
            print("SUCK")
            room_a = "CLEAN"

    print("STOP\n\nFinal State:")
    print("Room A:", room_a)
    print("Room B:", room_b)
    print("Final Position:", position)

def get_input(prompt, options):
    while True:
        val = input(prompt).strip().upper()
        if val in options:
            return val
        print(f"Invalid! Choose from {options}")

pos = get_input("Enter starting position (A/B): ", ["A", "B"])
a_stat = get_input("Enter status of Room A (CLEAN/DIRTY): ", ["CLEAN", "DIRTY"])
b_stat = get_input("Enter status of Room B (CLEAN/DIRTY): ", ["CLEAN", "DIRTY"])

print("\n--- Running Simulation ---")
vacuum_cleaner(pos, a_stat, b_stat)
