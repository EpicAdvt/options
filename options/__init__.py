import datetime


class Option:
  
  def __init__(self, strike: float, expiry: datetime.datetime):
    self._strike = strike
    self._expiry = expiry
    self._iv = None

  def BScalc(self):
    d1 = 


class PutOption(Option):
  pass


class CallOption(Option):
  pass