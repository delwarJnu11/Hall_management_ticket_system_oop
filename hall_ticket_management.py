import time

# create a class for seat initialize


class Seats:
    @classmethod
    def init_seats(self, rows, cols):
        seats = []
        for row in range(1, rows + 1):
            row_of_seats = []
            for col in range(1, cols + 1):
                row_of_seats.append('A')
            seats.append(row_of_seats)
        return seats

# Hall Class


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = Seats.init_seats(self._rows, self._cols)

    def book_seats(self, id, seat_list):
        show_ids = []
        for show in self._show_list:
            show_ids.append(show[0])

        if id not in show_ids:
            print("Invalid show ID. You can't Buy Ticket.")
            return

        for row, col in seat_list:
            if row < 0 or row >= self._rows or col < 0 or col >= self._cols:
                print("Invalid seat selection.")
                return

            if self._seats[id][row][col] == 'X':
                print(
                    f"Seat ({row}, {col}) is already booked.Please Try Another Seat.")
                return

            self._seats[id][row][col] = 'X'
            print('Seat Booking successfully Done!')

    def view_show_list(self):
        for show_info in self._show_list:
            show_id, movie_name, time = show_info
            print(f"Show Id: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, id):
        show_ids = []
        for show in self._show_list:
            show_ids.append(show[0])

        if id not in show_ids:
            print("Invalid show ID. Please provide a valid show ID.")
            return

        idx = show_ids.index(id)

        print(
            f"Available seats for Movie -> {self._show_list[idx][1]}:")
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[id][row][col] == 'A':
                    print(f"Seat ({row}, {col})")
        print("Seats After Booked Ticket In Matrix :")
        for row in range(self._rows):
            for col in range(self._cols):
                print(self._seats[id][row][col], end=" ")
            print()


# star Cinema Class
class Star_Cinema(Hall):
    hall_list = []

    def __init__(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)

    @classmethod
    def entry_hall(self, hall):
        self.hall_list.append(hall)


balaka_hall = Star_Cinema(5, 5, 1111)
balaka_hall.entry_show(1, "Jawan", time.ctime())
balaka_hall.entry_show(2, "Dhaka Attack", time.ctime())
balaka_hall.entry_show(5, "King of kotha", time.ctime())


while True:
    print()
    print('1. View Show List')
    print('2. View Available Seats')
    print('3. Book A Seat')
    print('4. Exit')

    option = int(input('Enter option: '))

    if option == 1:
        balaka_hall.view_show_list()
    elif option == 2:
        show_id = int(input('Enter show ID: '))
        balaka_hall.view_available_seats(show_id)
    elif option == 3:
        show_id = int(input('Enter show ID: '))
        seat_row = int(input('Enter seat row: '))
        seat_col = int(input('Enter seat column: '))
        balaka_hall.book_seats(show_id, [(seat_row, seat_col)])
    elif option == 4:
        break
    else:
        print('Invalid option. Please try again.')
