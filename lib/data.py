from dataclasses import dataclass

@dataclass
class Rest:
    value: int
    type: str = "rest" # rest or paddle
    value_type: str = "time" # time, distance, or strokes

@dataclass
class Pace:
    value: int
    type: str = "2k" # Relative to 2k (-1 = 2k pace -1), watts, or split (split is in seconds)
    stroke_rate: int = None # If stroke rate is not specified, it is up to the user to set it


@dataclass
class Interval:
    value: int
    type: str # distance, time, or strokes
    pace: Pace = None
    rest: Rest = None

@dataclass
class Workout:
    title: str
    description: str
    heart_rate_zone: str
    total_time: int
    requires_warmup: bool
    intervals: list[Interval]
    interval_count: int = 1 # If intervals are the same, don't repeat them, just increase the count


# Main
if __name__ == "__main__":
    print("Hello World")

