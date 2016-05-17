from flask import Flask, render_template, request
from foo import print_record_count

app = Flask(__name__)


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)