from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'guitar'



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/hire/")
def hire():
    return render_template('hire.html')   

@app.route("/playing_styles/")
def playing_styles():
    return render_template('playing_styles.html')

@app.route("/guitar_tut/")
def guitar_tut():
    return render_template('guitar_tut.html')      

# @app.route("/quiz/")
# def quiz():
#     return render_template('quiz.html')

@app.route("/quiz_index/")
def quiz_index():
    return render_template('quiz_index.html')

@app.route("/")
def hello():
    session['question'] = 1
    return render_template('index.html')


correctAnswers = 0

@app.route("/quiz/")
def quiz():
    global correctAnswers 
    q = None
    qa = {
             "1" :{
                "text":"Q.What chord is this?",
                "answer":1,
                "answers":["A-minor", "C-major", "C-sharp-min", "C-Flat"],
                "image": "aminor.png"
                }, 
             "2" :{
                "text":"Q.What chord is this?",
                "answer":3,
                "answers":["D-minor", "D-sharp-minor", "D-major", "D#-minor"],
                "image": "dmajor.png"
                },
             "3" :{
                "text":"Q.What chord is this?",
                "answer":2,
                "answers":["C-minor", "C-major", "C-sharp", "C-Flat"],
                "image": "cmajor.png"
                },
             "4" :{
                "text":"Q.Which chord sounds happy?",
                "answer":1,
                "answers":["F-major",  "A#-minor", "B-Flat", "F-minor"],
                "image": "fmajor.png"
                },
             "5" :{
                "text":"Q.What chord sounds sad?",
                "answer":2,
                "answers":["A-major", "B-minor", "F-sharp", "B-Flat"],
                "image": "sadchord.png"
                },
             "6" :{
                "text":"Q.Which string has the same name twice?",
                "answer":3,
                "answers":["B", "G", "E", "D"],
                "image": "6strings.png"
                },
             "7" :{
                "text":"Q.How many strings regular guitar have?",
                "answer":1,
                "answers":["6", "3", "7", "5"],
                "image": "6strings.png"
                },
             "8" :{
                "text":"Q.Which is the correct pattern of the guitar strings?",
                "answer":2,
                "answers":["EDGCAE", "EBGDAE", "DABGEE", "DGAEBE"],
                "image": "strings.png"
                }

             }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    # print('qa length: ', len(qa))    

    answer = request.args.get('answer', None)

    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        q= q+1
        session['question'] = q
        if str (answer) == str (correct):
            correctAnswers += 1
        if q > len(qa):
           return render_template('success.html', text=str(correctAnswers))
        else:
            return render_template('quiz.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q, imagename=qa[str(q)]["image"])
    else:
        session['question'] = 1
        q = session['question']
        correctAnswers = 0

        return render_template('quiz.html', text=qa[str(q)]["text"], answers=qa[str(q)]["answers"], number=q, imagename=qa[str(q)]["image"]) 

@app.route("/success/")
def success():
    return render_template('success.html')

    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
