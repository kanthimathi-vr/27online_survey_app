from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

responses = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/survey/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        name = request.form.get('name')
        age_group = request.form.get('age_group')
        feedback = request.form.get('feedback')
        if name and age_group and feedback:
            responses.append({'name': name, 'age_group': age_group, 'feedback': feedback})
            return redirect(url_for('results'))
    return render_template('survey.html')

@app.route('/results/')
def results():
    age_filter = request.args.get('age_group')
    filtered = [r for r in responses if r['age_group'] == age_filter] if age_filter else responses
    age_groups = sorted(set(r['age_group'] for r in responses))
    return render_template('results.html', responses=filtered, age_groups=age_groups, selected_age=age_filter)

if __name__ == '__main__':
    app.run(debug=True)