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
You can now combine intervals into a Workout object, which is just an array of intervals, with metadata.  The Workout object is in the following format:

```
name (optional): (string) (name of the workout)
description (optional): (string) (description of the workout)
author (optional): (string) (author of the workout)
type (optional): (string) (type of workout, e.g. 'steady state', 'intervals', 'test')
intervals (required): (array) (array of Interval objects)
```

Example of a valid Workout object:

```json
{
    "name": "6x500m",
    "description": "6x500m with 2 minutes rest",
    "author": "Row Xpert",
    "type": "intervals",
    "intervals": [
        {
            "type": "repeat",
            "value": 6,
            "interval": {
                "type": "distance",
                "value": 500,
                "rest": {
                    "type": "time_off",
                    "value": 120
                },
                "pace": null,
                "heart_rate": null,
            }
        }
    ]
}
```

## Workout generator

We use a GAN to generate workouts.  The GAN is trained on a dataset of workouts, which are stored in the [workouts](workouts) directory.  The workouts are stored in JSON format, and are validated using the [Workout Schema](workout_schema.json).  You can validate your workout using the [Workout Schema](workout_schema.json) with the following command:

```bash
$ npm run validate -- --workout <path to your workout>
```

### Usage

To generate a workout, run the following command:

```bash
pip install -r requirements.txt
python generate.py
```

This will generate a workout and save it to the [generated_workouts](generated_workouts) directory.  The workout will be saved in JSON format, and will be validated using the [Workout Schema](workout_schema.json).

