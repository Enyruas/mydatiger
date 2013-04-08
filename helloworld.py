import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.write('Hello, big tiger!\n My honey!\nBull and Tiger')

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
