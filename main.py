from flask import Flask


app = Flask(__name__)


@app.route('/')
def calcAngle(hour,minute):
    if (hour < 0 or minute < 0 or hour > 12 or minute > 60):
        print('Wrong input')
    if (hour == 12):
        hour = 0
    if (minute == 60):
        minute = 0

    # Calculate the angles moved by
    # hour and minute hands with
    # reference to 12:00
    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle of two
    # possible angles
    angle = str(int(min(360 - angle, angle)))

    return angle
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
