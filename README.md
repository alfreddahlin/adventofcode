# Advent of Code
## Running the setup script
Run the setup script with

```make setup year=$YEAR day=$DAY```

For example to setup the 5th day of 2016 use

```make setup year=2016 day=5```

This setup function uses todays day and year as default so simply running `make setup` will setup the current day.
## Running the solution
To execute the solution, run the solve target with the same parameters as the setup

```make solve year=$YEAR day=$DAY```

For example to solve the 5th day of 2016 use

```make solve year=2016 day=5```

This solve target uses the same default values as the setup; today's year and day.

## Session format
Add an `aoc_session` file to the root directory containing the session cookie on the following format.

```cookie: session=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX```