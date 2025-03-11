from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Ваша база данных имен и IQ (из оригинального кода)
NAME_IQ_RANGES = {
    "Литвин": (80, 100),
    "Сосков": (50, 70),
    "Фомченков": (90, 110),
    "Тюрин": (60, 80),
    "Подолецкая": (120, 150),
}

PODOLETSKAYA_RESPONSES = [
    "Ах ты шалунишка! 😏",
    "Ну что, опять за своё? 😌",
    "Ты меня сегодня совсем завёл! 💋",
    "Давай без глупостей, ладно? 😒",
    "Ох, как же ты меня возбуждаешь! 🥵",
    "Ты сегодня особенно наглый! 😘",
    "Ну и что ты хочешь от меня? 😏",
    "Ах, как же я тебя хочу! 💕",
    "Ты меня сегодня удивляешь! 😳",
    "Ну что, продолжим? 😈",
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate_iq", methods=['POST'])
def calculate_iq():
    iq_value = int(request.form['iq_value'])
    excitement_level = int(request.form['excitement_level'])

    iq_result = ""
    if iq_value < 10:
        iq_result = "Ваш IQ сегодня на уровне долбаеба, поздравляю! "
    elif iq_value == 10:
        iq_result = "Ваш IQ сегодня на уровне Соскова, поздравляю! "
    elif 10 < iq_value < 25:
        iq_result = "Ваш IQ сегодня на уровне Тюрина, поздравляю! "
    elif 25 < iq_value < 50:
        iq_result = "Ваш IQ сегодня на уровне Подолецкой, поздравляю! ✅"
    elif 50 < iq_value < 100:
        iq_result = "Ваш IQ сегодня на уровне Погонышевой, старость ебаная! "
    elif 100 < iq_value < 150:
        iq_result = "Ваш IQ сегодня на уровне Эйнштейна? Ты ебанулся нахуй? "
    elif 150 < iq_value < 1000:
        iq_result = "Ой да не пиздите! "

    excitement_result = ""
    if excitement_level < 10:
        excitement_result = "Вашей возбужденности не хватит чтобы удовлетворить Подолецкую. ❌"
    elif 10 <= excitement_level <= 25:
        excitement_result = "Вашей возбужденности хватит чтобы удовлетворить Подолецкую на 25%, слабовато блять! ❌"
    elif 25 < excitement_level <= 50:
        excitement_result = "Вашей возбужденности хватит чтобы удовлетворить Подолецкую на 55%, можно и лучше блять! ❌ "
    elif 50 < excitement_level <= 100:
        excitement_result = "Вашей возбужденности хватит чтобы удовлетворить Подолецкую на 100%, АХ АХ АХ АХ! ✅"
    elif 100 < excitement_level <= 999999:
        excitement_result = "Вашей возбужденности хватит чтобы удовлетворить Подолецкую на 10000%, ЕБИ ЕЁ БЫСТРЕЕ, БЫСТРЕЕ, АХ АХ, ЕЩЁЁЁЁЁ! ✅"

    C = (iq_value / 10) + (excitement_level * 3)

    result = f"{iq_result}\n{excitement_result}\nВаш коэффициент секс-зависимости от Подолецкой равен {C:.2f} баллов по шкале Колонтитулиума."

    return jsonify({'result': result})

@app.route("/start_quiz", methods=['POST'])
def start_quiz():
    desired_iq = int(request.form['desired_iq'])
    if desired_iq > 100:
        return jsonify({'quiz': True})
    else:
        return jsonify({'quiz': False})

@app.route("/show_random_iq", methods=['GET'])
def show_random_iq():
    name = request.args.get('name', '').strip()
    if name in NAME_IQ_RANGES:
        iq_range = NAME_IQ_RANGES[name]
        iq = random.randint(iq_range[0], iq_range[1])
        return jsonify({'iq': iq, 'name': name})
    else:
        iq = random.randint(50, 150)
        return jsonify({'iq': iq, 'name': 'Unknown'})

@app.route("/write_to_podoletskaya", methods=['GET'])
def write_to_podoletskaya():
    return jsonify({'message': "Вы написали Подолецкой, ожидайте ответа.. 💌"})

@app.route("/chat_with_podoletskaya", methods=['POST'])
def chat_with_podoletskaya():
    user_message = request.form['user_message']
    podoletskaya_response = random.choice(PODOLETSKAYA_RESPONSES)
    return jsonify({'user_message': user_message, 'podoletskaya_response': podoletskaya_response})

if __name__ == "__main__":
    app.run(debug=True)
