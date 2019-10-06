from datetime import datetime

class DateCreateAccount():
  
  def __init__(self):
    self.date = '{}/{}/{}'.format(datetime.now().day, datetime.now().month, datetime.now().year)
    self.dateCreated()
    
  def dateCreated(self):
    return self.date