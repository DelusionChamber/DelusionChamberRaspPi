from threading import Timer

class RepeatedTimer(object):
      def __init__(self,t,hFunction):
          self.t=t
          self.is_running = False
          self.hFunction = hFunction
          self.thread = Timer(self.t,self.handle_function)

      def handle_function(self):
          self.hFunction()
          self.thread = Timer(self.t,self.handle_function)
          self.thread.start()

      def start(self):
          if not self.is_running:
              self.is_running = True
              self.thread.start()

      def stop(self):
          self.thread.cancel()
          self.is_running = False
