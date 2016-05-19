from flask import Flask, render_template, request
from foo import print_record_count, filter_func

app = Flask(__name__)

@app.route("/")
def homepage():
  template = 'index.html'
  return render_template(template)

@app.route("/results")
def results():
  reqargs = request.args
  _score =  reqargs.get('score')
  _risk = reqargs.get('risk')
  _name = reqargs.get('name')

  if not _score and not _risk:
        return """
            <h1>Error</h1>
            <p>Must have either a score or risk value</p>
            <p>Go <a href="{url}">back</a></p>
        """.format(url=request.referrer)

  elif request.args.get('score'):
    search_type = 'score'
    search_val = request.args.get('score')
    data = filter_func(score=search_val)

  elif request.args.get('risk'):
    search_type = 'risk'
    search_val = request.args.get('risk')
    data = filter_func(risk=search_val)

  # elif request.args.get('name'): 
  #   search_type = 'name'
  #   search_val = request.args.get('name')
  #   data = filter_func(name=search_val)

  template = 'results.html'
  return render_template(template, data=data,
               search_type=search_type,
               search_val=search_val)     


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)