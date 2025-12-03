from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html', alert=None)
@app.route('/submit',methods=['POST'])
def submit():
    n=request.form.get('username','').strip()
    y=request.form.get('year')
    return render_template('form.html', alert='Enter name') if not n else render_template('result.html', name=n,year=y)
if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)