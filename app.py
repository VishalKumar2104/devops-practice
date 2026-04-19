from flask import Flask, request, jsonify

app = Flask(__name__)

# Classes
class movie:
    def __init__(self, name, seats):
        self.name = name
        self.availableSeats = seats


class booking:
    def __init__(self, username, movieName, seats):
        self.username = username
        self.movieName = movieName
        self.seats = seats


# Data
movies = [
    movie("Leo", 50),
    movie("Jailer", 40),
    movie("Avengers", 30)
]

bookings = []


# Show movies
@app.route("/")
def show_movies():
    result = []
    for m in movies:
        result.append({
            "movie": m.name,
            "availableSeats": m.availableSeats
        })
    return jsonify(result)


# Book ticket
@app.route("/book", methods=["POST"])
def book_ticket():
    data = request.get_json()

    name = data["name"]
    movie_name = data["movie"]
    seats = int(data["seats"])

    for m in movies:
        if m.name == movie_name:
            if seats <= m.availableSeats:
                m.availableSeats -= seats
                bookings.append(booking(name, movie_name, seats))
                return jsonify({"message": "Booked successfully"})
            else:
                return jsonify({"message": "Not enough seats"})

    return jsonify({"message": "Movie not found"})


# Cancel ticket
@app.route("/cancel", methods=["POST"])
def cancel_ticket():
    data = request.get_json()
    name = data["name"]

    for i in range(len(bookings)):
        b = bookings[i]
        if b.username == name:
            for m in movies:
                if m.name == b.movieName:
                    m.availableSeats += b.seats

            bookings.pop(i)
            return jsonify({"message": "Cancelled successfully"})

    return jsonify({"message": "No booking found"})


# View bookings
@app.route("/bookings")
def view_bookings():
    result = []
    for b in bookings:
        result.append({
            "name": b.username,
            "movie": b.movieName,
            "seats": b.seats
        })
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
