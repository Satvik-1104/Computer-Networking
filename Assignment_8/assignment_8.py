import random


class Station:
    def __init__(self, id):
        self.id = id
        self.is_transmitting = False
        self.collision = False
        self.backoff_time = 0
        self.collision_count = 0

    def attempt_transmission(self, channel_busy):
        return self.backoff_time == 0 and not channel_busy

    def set_backoff(self):
        backoff_limit = min((2 ** self.collision_count) - 1, 1023)
        self.backoff_time = random.randint(0, backoff_limit)

    def tick(self):
        if self.backoff_time > 0:
            self.backoff_time -= 1


def csma_cd_simulation(N, total_slots):
    stations = [Station(i) for i in range(N)]
    transmission_times = {i: None for i in range(N)}
    channel_busy = False
    transmitting_station = None
    frame_transmission_time = 50  # Time to transmit a frame
    current_frame_remaining_time = 0

    for slot in range(total_slots):
        if channel_busy and current_frame_remaining_time == 0:
            print(f"Station {transmitting_station.id} finished transmitting at slot {slot}")
            channel_busy = False
            transmitting_station = None

        if channel_busy:
            current_frame_remaining_time -= 1
        else:
            active_stations = [s for s in stations if s.attempt_transmission(channel_busy)]

            if len(active_stations) > 1:
                print(f"Collision detected at slot {slot} among stations {[s.id for s in active_stations]}")
                for s in active_stations:
                    s.collision = True
                    s.collision_count += 1
                    s.set_backoff()
            elif len(active_stations) == 1:
                transmitting_station = active_stations[0]
                transmission_times[transmitting_station.id] = slot
                channel_busy = True
                current_frame_remaining_time = frame_transmission_time
                print(f"Station {transmitting_station.id} starts transmitting at slot {slot}")

        for s in stations:
            s.tick()

    return transmission_times


# User Input
N = int(input("Enter the number of stations: "))
total_slots = int(input("Enter the total number of time slots: "))

transmission_times = csma_cd_simulation(N, total_slots)

# Summary of Results
for station_id, time in transmission_times.items():
    if time is not None:
        print(f"Station {station_id} successfully began transmission at slot {time}")
    else:
        print(f"Station {station_id} did not transmit")
