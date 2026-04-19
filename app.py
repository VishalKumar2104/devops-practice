from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "class movie:
    def __init__(self, name, seats):
        self.name = name
        self.availableSeats = seats


class booking:
    def __init__(self, username, movieName, seats):
        self.username = username
        self.movieName = movieName
        self.seats = seats


# Data storage
movies = []
bookings = []


def showMovies():
    print("\nAvailable Movies:")
    for i in range(len(movies)):
        print(f"{i+1}. {movies[i].name} | Seats: {movies[i].availableSeats}")


def bookTicket():
    name = input("Enter name: ")

    showMovies()
    choice = int(input("Choose movie: "))

    if choice < 1 or choice > len(movies):
        print("Invalid choice!")
        return

    m = movies[choice - 1]
    seats = int(input("Seats: "))

    if seats <= m.availableSeats:
        m.availableSeats -= seats
        bookings.append(booking(name, m.name, seats))
        print("Booked!")
    else:
        print("Not enough seats!")


def cancelTicket():
    name = input("Enter name: ")

    for i in range(len(bookings)):
        b = bookings[i]

        if b.username == name:
            for m in movies:
                if m.name == b.movieName:
                    m.availableSeats += b.seats

            bookings.pop(i)
            print("Cancelled!")
            return

    print("No booking found!")


def viewBookings():
    if not bookings:
        print("No bookings!")
        return

    print("\nAll Bookings:")
    for b in bookings:
        print(f"{b.username} | {b.movieName} | {b.seats}")


# Main program
movies.append(movie("Leo", 50))
movies.append(movie("Jailer", 40))
movies.append(movie("Avengers", 30))

while True:
    print("\nMOVIE TICKET BOOKING SYSTEM")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View Bookings")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        showMovies()
    elif choice == 2:
        bookTicket()
    elif choice == 3:
        cancelTicket()
    elif choice == 4:
        viewBookings()
    elif choice == 5:
        print("Thank You!")
        break
    else:
        print("Invalid choice!")
"
app.run(host="0.0.0.0",port=5001)
