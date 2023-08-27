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


def json_to_workout(json_data) -> Workout:
    """This function takes a json object and converts it to a Workout object
    """
    intervals = []
    interval_count = 1

    for interval_data in json_data["intervals"]:
        value = interval_data["value"]
        interval_type = interval_data["type"]
        pace_data = interval_data.get("pace")
        rest_data = interval_data.get("rest")

        pace = None
        rest = None

        if pace_data:
            pace_value = pace_data["value"]
            pace_type = pace_data["pace_unit"]
            pace = Pace(value=pace_value, type=pace_type)

        if rest_data:
            rest_value = rest_data["value"]
            rest_type = rest_data.get("type", "rest")
            rest_value_type = rest_data.get("value_type", "time")
            rest = Rest(value=rest_value, type=rest_type, value_type=rest_value_type)

        intervals.append(Interval(value=value, type=interval_type, pace=pace, rest=rest))

    if "interval_count" in json_data:
        interval_count = json_data["interval_count"]

    return Workout(
        title=json_data["title"],
        description=json_data["description"],
        heart_rate_zone=json_data["heart_rate_zone"],
        total_time=json_data["total_time"],
        requires_warmup=json_data["requires_warmup"],
        intervals=intervals,
        interval_count=interval_count
    )


# Main
if __name__ == "__main__":
    print("Hello World")

