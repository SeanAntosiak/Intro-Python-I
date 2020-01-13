# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon():
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
  def __init__(self, lat, lon, name):
    super().__init__(lat, lon)
    self.name = name

  def __str__(self):
    return(f'{self.name} is located at lat {self.lat} and lon {self.lon}')
    

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
  def __init__(self, lat, lon, name, difficulty, size):
    super().__init__(lat, lon, name)
    self.difficulty = difficulty
    self.size = size

  def __str__(self):
    return(f'Name: {self.name}  |  Lat: {self.lat}  |  Lon: {self.lon}  |  ' +
           f'Size: {self.size}  |  Difficulty: {self.difficulty}')
    

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint1 = Waypoint(41.70505, -121.51521, "Catacombs")
print(waypoint1.name, waypoint1.lat, waypoint1.lon, )

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint1)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache1 = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)

# Print it--also make this print more nicely
print(geocache1)
