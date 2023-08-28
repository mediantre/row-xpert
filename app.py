def print_interval(interval_obj):
    if not interval_obj:
        return
    
    interval_type = interval_obj.get("type", None)
    value = interval_obj.get("value", None)
    rest = interval_obj.get("rest", None)
    pace = interval_obj.get("pace", None)
    heart_rate = interval_obj.get("heart_rate", None)

    
    print("Type:", interval_type)

    if interval_type == "distance":
        units = "m"
    elif interval_type == "time":
        units = "s"
    elif interval_type == "repeat":
        units = "intervals"
    elif interval_type == "strokes":
        units = "strokes"
    else:
        units = ""



    print("Value:", value, units)

    if interval_type == "repeat":
        repeat = interval_obj.get("interval", None)
        if repeat:
            print("Interval to Repeat:")
            print_interval(repeat)
    
    if rest:
        rest_type = rest.get("type", None)
        rest_value = rest.get("value", None)
        print("Rest Type:", rest_type)
        print("Rest Value:", rest_value)
    
    if pace:
        split_min = pace.get("split_min", None)
        split_max = pace.get("split_max", None)
        spm_min = pace.get("spm_min", None)
        spm_max = pace.get("spm_max", None)
        effort = pace.get("effort", None)
        print("Pace Split Min:", split_min)
        print("Pace Split Max:", split_max)
        print("Pace SPM Min:", spm_min)
        print("Pace SPM Max:", spm_max)
        print("Pace Effort:", effort)
    
    if heart_rate:
        min_hr_percent = heart_rate.get("min_hr_percent", None)
        max_hr_percent = heart_rate.get("max_hr_percent", None)
        zone = heart_rate.get("zone", None)
        print("Heart Rate Min Percent:", min_hr_percent)
        print("Heart Rate Max Percent:", max_hr_percent)
        print("Heart Rate Zone:", zone)

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
