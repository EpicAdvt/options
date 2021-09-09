
import options
import datetime

c = options.CallOption(110, datetime.datetime(2021, 10, 15), .75, 100)
p = options.PutOption(110, datetime.datetime(2021, 10, 15), .75, 100)
print(c.BSprice(t=.5, vol=.5))
print(p.BSprice(t=.5, vol=.5))