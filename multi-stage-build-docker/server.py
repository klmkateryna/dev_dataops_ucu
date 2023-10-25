from flask import Flask, render_template
# from datetime import date, datetime

app = Flask(__name__)
# today = date.today()
# tm = datetime.now()


@app.route('/')
def my_route_page_function():
    return render_template('home.html')
# def hello():
#     formatted_dt = today.strftime("%B %d, %Y")
#     formatted_cur_tm = tm.strftime("%H:%M:%S")
#     return (f"Hello, Docker World! \n"
#             f"Today's date: {formatted_dt}. \n"
#             f"Kyiv time : {formatted_cur_tm}"
#             )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
