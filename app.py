from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    previous_marks = float(request.form["previous_marks"])
    assignment_score = float(request.form["assignment_score"])
    sleep_hours = float(request.form["sleep_hours"])
    internet_hours = float(request.form["internet_hours"])

    input_data = [[
        study_hours,
        attendance,
        previous_marks,
        assignment_score,
        sleep_hours,
        internet_hours
    ]]

    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)