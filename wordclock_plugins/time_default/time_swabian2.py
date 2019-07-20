class time_swabian2:
    """
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on a german WCA in swabian using the german2 layout
    Based on work from SebVoss, adapted by plotaBot
    """

    def __init__(self):
        self.prefix = range(0,2) +  range(3,7)
        self.minutes=[[], \
            range(29,33) + range(33,37), \
            range(22,26) + range(33,37), \
            range(15,21), \
            range(22,26) + range(41,44) + range(44,48), \
            range(29,33) + range(41,44) + range(44,48), \
            range(44,48), \
            range(29,33) + range(33,37) + range(44,48), \
            range(22,26) + range(33,37), \
            range(11,21), \
            range(22,26) + range(41,44), \
            range(29,33) + range(41,44) ]
        self.hours= [range(82,88), \
            range(55,59), \
            range(66,71), \
            range(77,82), \
            range(105,110), \
            range(49,54), \
            range(57,63), \
            range(99,105), \
            range(71,76), \
            range(91,96), \
            range(88,93), \
            range(62,66), \
            range(82,88)]
       # self.full_hour= range(107,110)

    def get_time(self, time, purist):
        hour=time.hour%12+(1 if time.minute/5 > 2 else 0)
        minute=time.minute/5
        # Assemble indices
        return  \
            (self.prefix if not purist else []) + \
            self.minutes[minute] + \
            self.hours[hour] + \
            ([58] if (hour == 1 and minute != 0) else []) + \
            (self.full_hour if (minute == 0) else [])
