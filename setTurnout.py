import jmri

class setStartup(jmri.jmrit.automat.AbstractAutomaton) :
   def init(self):
     return
   def handle(self):
     self.waitMsec(1000)         # time is in milliseconds
     print "Startup Script: Setting Turnout 5a"
     turnouts.provideTurnout("Turnout 5a").setState(THROWN)
     self.waitMsec(1000)
     turnouts.provideTurnout("Turnout 5a").setState(CLOSED)
     self.waitMsec(1000)

     print "Startup Script: Setting Turnout 5b"
     turnouts.provideTurnout("Turnout 5b").setState(THROWN)
     self.waitMsec(1000)
     turnouts.provideTurnout("Turnout 5b").setState(CLOSED)
     self.waitMsec(1000)

     print "Startup Script: Setting Turnout 7"
     turnouts.provideTurnout("Turnout 7").setState(THROWN)
     self.waitMsec(1000)
     turnouts.provideTurnout("Turnout 7").setState(CLOSED)
     self.waitMsec(1000)

     print "Startup Script: Setting Turnout 15"
     turnouts.provideTurnout("Turnout 15").setState(THROWN)
     self.waitMsec(1000)
     turnouts.provideTurnout("Turnout 15").setState(CLOSED)
     self.waitMsec(1000)

     print "Startup Script: Setting Turnout 17"
     turnouts.provideTurnout("Turnout 17").setState(THROWN)
     self.waitMsec(1000)
     turnouts.provideTurnout("Turnout 17").setState(CLOSED)
     self.waitMsec(1000)

     return False              # all done, don't repeat again

setStartup().start()          # create one of these, and start it running   
