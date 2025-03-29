import streamlit as st

def on_clk():
    print("click")

st.set_page_config(page_title="filonli|indie game dev",layout="centered")

st.title("filonli")
st.badge("Ніклонський Олексій")
st.write("indie game developer")

st.image("res/dusty.png",caption="приклад рівня створеного мною")

st.header("Про мене")
st.write("Вітаю! Мене звати Олексій, з 2018 року я займаюся розробкою особистих проектів на Unity. За роки досвіду я набув розуміння рушію, та маю легкість в створенні ігрового досвіду. Впевнене розуміння С# в поєднанні з UnityEngine API, дозволяє мені створити любу ігрову механіку. А практичне розуміння ігрового дизайну, дозволяє мені поєднати все в повноцінну гру. Також поглиблене розуміння того як працює сучасна 3D графіка(OpenGL) та ігрові рушії дозволяють мені краще знаходити шляхи до оптимізації.")


st.header("Навички")

st.caption("(оберіть меню для більш детальної інформації)")

tabs = st.tabs(["Програмування","Unity","Blender3D","Gimp","Дизайн рівнів","Ігровий дизайн","Платформи","Софт","Мови"])

with tabs[0]:
#    st.write("Мови")
    col = st.columns(8)
    with col[0]: st.badge("C#")
    with col[1]: st.badge("Lua")
    with col[2]: st.badge("C")
    with col[3]: st.badge("Python")
    with col[4]: st.badge("ООП")
    with col[5]: st.badge("SOLID")
    with col[6]: st.badge("KISS")
    with col[7]: st.badge("Git/Github")

with tabs[1]:
    st.badge("Створення компонентів")
    st.badge("Створення плагінів та інструментів для розробки")
    st.badge("Менеджмент проектів")
    st.badge("Створення імпорт та редагування ігрових ассетів")
    st.badge("Публікація проектів")
    st.badge("Debug та виправлення помилок")
    st.badge("Створення сцен")
    st.badge("Створення префабів")
    st.badge("Створення грабельних ігрових прототипів")

with tabs[2]:
    st.badge("Hardsurface modeling")
    st.badge("Subdivision surface modeling")
    st.badge("Створення LOD")
    st.badge("Оптимізація сіток")
    st.badge("Створення матеріалів")
    st.badge("Розгортка")
    st.badge("Hardsurface modeling")
    st.badge("Накладання текстур")

with tabs[3]:
    st.badge("Створення текстур")
    st.badge("Обрізка зоображеннь")
    st.badge("Видалення фону")
    st.badge("Накладання фільтрів")
    st.badge("Малювання освітлення")

with tabs[4]:
    st.badge("Навігація гравця")
    st.badge("Open World Desigh (POI)")
    st.badge("Dor & Key")
    st.badge("Пейсинг")
    st.badge("Потік")
    st.badge("Грейбоксинг/Вайтбоксинг")
    st.badge("Створення подій")
    st.badge("Розміщення механік")
    st.badge("Gates")
    st.badge("Nonlinear level design")
    st.badge("Environment art")

with tabs[5]:
    st.badge("Написання GDD")
    st.badge("Дизайн ігрових механік")
    st.badge("DMA(dynamics,mechanics,aestetics)")
    st.badge("Винагорода")
    st.badge("Прогрессія")
    st.badge("Ігровий потік")
    st.badge("Баланс ігрових механік")
    st.badge("Емерджентність")
    st.badge("Залучення уваги гравця")

with tabs[6]:
    st.badge("Desktop")
    st.badge("Android")

with tabs[7]:
    st.badge("Стресостійкість")
    st.badge("Швидкий ученик")
    

with tabs[8]:
    st.badge("Українська")
    st.badge("Англійська")


st.title("Мої проекти")

#taijpenj
st.subheader("Project TAIJPENJ")
st.markdown("Жанр: Шутер від першої особи")
st.markdown("Рушій: Godot 4.2")
st.markdown("Особливість: Унікальна система перезарядки зброї")

st.video("res/taijpenj_demo.mp4")

st.write("Taijpenj це класичний шутер від першої особи, з унікальними механіками. Ціль створення данного проекту була в винайдені нової формули шутеру, та ігрових механік. Поміж інших цю гру відрізняє її унікальні механіки перезарядки, котрі предаставлені в вигляді міні гри, та сповільнення часу, при пошкодженнях, що спрямовано створити епічні ігрові моменти, та дати можливість гравцю відчути себе вправним.")

#roguelite
st.subheader("Project Didoid")
st.markdown("Жанр: Шутер від першої особи,Roguelite")
st.markdown("Рушій: Unity 2022")
st.markdown("Особливість: Roguelite від першої особи")

st.video("res/roguelite_demo.mp4")

st.write("Ідея створити Project Didoid, в мене з'вилася після дослідження ігрового ринку: я помітив, що в той час коли ігри в жанрі Roguelite та Boomer Shooter дуже популярні, дуже мало якісних ігор які б це поєднували. Ця гра покращила мій досвід в створенні ігор, з рандомною генерацією рівнів, та покращила навички оптимізації, через те що в іграх такого типу дуже багато активних об'єктів. Також це покращило розуміння того як створювати складні ШІ ворогів, та оптимізацію систем котрі використовують патерн StateMachine.")

rt = st.tabs(["Зворотний зв'язок"])
with rt[0]:
    st.markdown("Номер телефону: +380666330475")
    st.markdown("Електронна почта: squirrelreal@gmail.com")
    st.markdown("Itch.io(https://filonli.itch.io/)")
    st.markdown("GitHub(https://github.com/filonli)")
    st.markdown("Адреса: м.Суми,Україна")