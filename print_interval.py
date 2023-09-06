from datetime import timedelta

def format_time(seconds) -> str:
    if seconds >= 60:
        duration = str(timedelta(seconds=seconds))
        minutes, seconds = duration.split(":")[1:]
        minutes = int(minutes)
        seconds = int(seconds)
        
        formatted_duration = f"{minutes} min"
        if seconds > 0:
            formatted_duration += f", {seconds} sec"
    else:
        formatted_duration = f"{seconds} sec"
        
    return formatted_duration

def print_pace_info(pace_info):
    split_min = pace_info.get("split_min", None)
    split_max = pace_info.get("split_max", None)
    spm_min = pace_info.get("spm_min", None)
    spm_max = pace_info.get("spm_max", None)
    effort = pace_info.get("effort", None)

    if split_min and split_max:
        print(f"Splits: {split_min} to {split_max} above 2k goal pace")

    if spm_min and spm_max:
        print(f"Stroke rate: {spm_min} to {spm_max} spm")

    if effort:
        # Effort is on a scale of 1-10. 1 is easy, 10 is hard.
        print(f"Effort level: {effort}/10")

def print_heart_rate_info(heart_rate_info):
    # Extract heart rate information
    min_hr_percent = heart_rate_info.get("min_hr_percent")
    max_hr_percent = heart_rate_info.get("max_hr_percent")
    heart_rate_zone = heart_rate_info.get("zone")

    # Format heart rate range information
    if min_hr_percent is not None and max_hr_percent is not None:
        print(f"Heart Rate Range: {min_hr_percent}% - {max_hr_percent}%")
    elif min_hr_percent is not None:
        print(f"Minimum Heart Rate Percent: {min_hr_percent}%")
    elif max_hr_percent is not None:
        print(f"Maximum Heart Rate Percent: {max_hr_percent}%")

    # Heart rate zone mappings
    heart_rate_zones = {
        0: "UT3",
        1: "UT2",
        2: "UT1",
        3: "AT",
        4: "TR",
        5: "AN"
    }

    # Format heart rate zone information
    if heart_rate_zone is not None:
        zone_text = heart_rate_zones.get(heart_rate_zone, str(heart_rate_zone))
        print(f"Heart Rate Zone: {zone_text}")

def print_rest_info(rest):
    """ Print rest information from a JSON object in a human-readable format """
    rest_type = rest.get("type", None)
    rest_value = rest.get("value", None)

    rest_type_mapping = {
        "time_off": ("rest", format_time),
        "time_paddle": ("rest", format_time),
        "distance_paddle": ("paddle", lambda x: f"{x} m"),
        "strokes_paddle": ("paddle", lambda x: f"{x} strokes"),
    }

    if rest_type in rest_type_mapping:
        rest_category, format_rest = rest_type_mapping[rest_type]
        formatted_value = format_rest(rest_value)
        print("Rest:", rest_category, formatted_value)


def print_interval(interval_obj):
    """ Print interval information from a JSON object in a human-readable format """

    if not interval_obj:
        return
    
    interval_type = interval_obj.get("type", None)
    value = interval_obj.get("value", None)
    rest = interval_obj.get("rest", None)
    pace = interval_obj.get("pace", None)
    heart_rate = interval_obj.get("heart_rate", None)

    interval_type_mapping = {
        "distance": ("m", None),
        "time": ("", format_time),
        "repeat": ("intervals", None),
        "strokes": ("strokes", None),
    }

    print("Type:", interval_type)

    if interval_type in interval_type_mapping:
        units, format_type = interval_type_mapping[interval_type]
        if format_type:
            value = format_type(value)
    else:
        units = ""

    print("Value:", value, units)

    if interval_type == "repeat":
        repeat = interval_obj.get("interval", None)
        if repeat:
            print("Interval to Repeat:")
            print_interval(repeat)
    
    if rest:
        print_rest_info(rest)

    if pace:
        print_pace_info(pace)

    if heart_rate:
        print_heart_rate_info(heart_rate)




# Example JSON Interval object
interval_json = {
    "type": "repeat",
    "value": 6,
    "interval": {
        "type": "time",
        "value": 120,
        "rest": {
            "type": "time_off",
            "value": 60
        },
        "pace": {
            "split_min": -3,
            "split_max": -2,
            "spm_min": 28,
            "spm_max": 32,
            "effort": 8
        },
        "heart_rate": {
            "min_hr_percent": 60,
            "max_hr_percent": 80,
            "zone": 2
        }
    }
}
# Call the function to print interval values
print_interval(interval_json)
