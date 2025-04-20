# Streamlitライブラリをインポート
import streamlit as st

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('System')

# テキスト入力ボックスを作成し、ユーザーからの入力を受け取る
user_input = st.time_input('現在の時刻は？')

st.write(user_input)
atr= [1,2,3]
atr_list = st.selectbox("アトラクションを選択",atr)
day=['月','火','水','木','金','土','日']
day_list = st.selectbox('曜日を選択',day)
# ボタンを作成し、クリックされたらメッセージを表示
if st.button('挨拶する'):
    if user_input:  # 名前が入力されているかチェック
        st.success(f'🌟 こんにちは! 🌟')  # メッセージをハイライト
    else:
        st.error('時刻を入力してください。')  # エラーメッセージを表示

# スライダーを作成し、値を選択
number = st.slider('好きな数字（10進数）を選んでください', 0, 100)

# 補足メッセージ
st.caption("十字キー（左右）でも調整できます。")

# 選択した数字を表示
st.write(f'あなたが選んだ数字は「{number}」です。')

# 選択した数値を2進数に変換
binary_representation = bin(number)[2:]  # 'bin'関数で2進数に変換し、先頭の'0b'を取り除く
st.info(f'🔢 10進数の「{number}」を2進数で表現すると「{binary_representation}」になります。 🔢')  # 2進数の表示をハイライト
