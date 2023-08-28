# row-xpert
## Erg workout generator


### Interval object
- A rowing Interval object is in the following format: 
```
type: 'time', 'distance', 'strokes', 'repeat' (for intervals)
value: (int) (time in seconds, distance in meters, strokes in strokes, repeat in number of times)
interval (optional, required if 'repeat'): if type is 'repeat', this is the interval to repeat
rest (optional): A rest interval to do after the interval
    - type: 'time_off', 'time_paddle', 'distance_paddle', 'strokes_paddle'
    - value: (int) (time in seconds, distance in meters, strokes in strokes)
pace (optional): A pace to hold for the interval
    - split_min (optional): (int) (split in seconds per 500m, relative to 2k pace, minimum)
    - split_max (optional): (int) (split in seconds per 500m, relative to 2k pace, maximum)
    - spm_min (optional): (int) (strokes per minute minimum)
    - spm_max (optional): (int) (strokes per minute maximum)
    - effort (optional): (int) (effort level, 1-10)
heart_rate (optional): A heart rate to hold for the interval
    - min_hr_percent (optional): (int) (minimum heart rate percentage)
    - max_hr_percent (optional): (int) (maximum heart rate percentage)
    - zone (optional): (int) (heart rate zone, 0-5) (0 = UT3, 1 = UT2, 2 = UT1, 3 = AT, 4 = TR, 5 = AN)
```

Note: the only required fields are 'type', 'value', and interval if type is repeat

Rest, pace, heart_rate are not valid if type is 'repeat'.  However, they are still optional if type if not repeat. 

Example of a valid Interval:

```json
{
    "type": "distance",
    "value": 500,
    "rest": {
        "type": "time_off",
        "value": 120
    },
    "pace": null,
    "heart_rate": null,
    "interval": null
}
```
Example of a Interval object using 'repeat'

 ```json 
{
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
```

[The Interval Schema](interval_schema.json) contains all the possible fields for an Interval object.

You can validate your Interval object using the [Interval Schema](workout_schema.json) with the following command:

```bash
$ npm run validate -- --interval <path to your interval object>
```

### Workout object
You can now combine intervals into a Workout object, which is just an array of intervals. Simple!

