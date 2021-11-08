import streamlit as st
import time
import pandas as pd


st.title('健康チェック!')
st.write('BMIを計算し，あなたの健康度を割り出します')

a = int(st.slider('年齢を入力してください',18,100,30))
s = st.selectbox('性別を選択してください',('男性','女性'))
h = float(st.number_input('身長を入力してください（cm）'))
w = float(st.number_input('体重を入力してください（kg）'))

result = 0
num = 0

if h==0 or w==0:
        st.header('')
elif h>0 and w>0:
    bmi = w / ((h/100)**2)
    
    yase ='「やせ気味」という結果です。'
    hyojun = '「標準」という結果です。'
    himan = '「肥満」という結果です。'
    shiman = '「高度肥満」という結果です。'
    
    st.write('あなたのBMI値は',int(bmi),'で，年齢の',a,'歳では，')   
    if 18 <= a <= 49:
        if bmi < 18.5:
            st.header(yase)
            result = 1
        elif 18.5<= bmi <25:
            st.header(hyojun)
            result = 2
        elif 25 <= bmi <30:
            st.header(himan)
            result = 3
        else:
            st.header(shiman)
            result = 4

    if 50 <= a <= 64:
        if bmi < 20:
            st.header(yase)
            result = 1
        elif 20<= bmi <25:
            st.header(hyojun)
            result = 2
        elif 25 <= bmi <30:
            st.header(himan)
            result = 3
        else:
            st.header(shiman)
            result = 4
    
    if 65 <= a:
        if bmi < 21.5:
            st.header(yase)
            result = 1
        elif 21.5<= bmi <25:
            st.header(hyojun)
            result = 2
        elif 25 <= bmi <30:
            st.header(himan)
            result = 3
        else:
            st.header(shiman)
            result = 4
    
    
    df = pd.read_csv('standard.csv', encoding='shift-jis')
    
    if s == '男性':
        if 1<= a <=25:
            sh = df.loc[a-1]['男性身長平均']
            sw = df.loc[a-1]['男性体重平均']
        elif 26<= a <=29:
            sh = df.loc[25]['男性身長平均']
            sw = df.loc[25]['男性体重平均']
        elif 30<= a <=39:
            sh = df.loc[26]['男性身長平均']
            sw = df.loc[26]['男性体重平均']
        elif  40<= a <=49:
            sh = df.loc[27]['男性身長平均']
            sw = df.loc[27]['男性体重平均']
        elif  50<= a <=59:
            sh = df.loc[28]['男性身長平均']
            sw = df.loc[28]['男性体重平均']
        elif  60<= a <=69:
            sh = df.loc[29]['男性身長平均']
            sw = df.loc[29]['男性体重平均']
        elif  70<= a:
            sh = df.loc[30]['男性身長平均']
            sw = df.loc[30]['男性体重平均']
    elif s == '女性':
        if 1<= a <=25:
            sh = df.loc[a-1]['女性身長平均']
            sw = df.loc[a-1]['女性体重平均']
        elif 26<= a <=29:
            sh = df.loc[25]['女性身長平均']
            sw = df.loc[25]['女性体重平均']
        elif 30<= a <=39:
            sh = df.loc[26]['女性身長平均']
            sw = df.loc[26]['女性体重平均']
        elif  40<= a <=49:
            sh = df.loc[27]['女性身長平均']
            sw = df.loc[27]['女性体重平均']
        elif  50<= a <=59:
            sh = df.loc[28]['女性身長平均']
            sw = df.loc[28]['女性体重平均']
        elif  60<= a <=69:
            sh = df.loc[29]['女性身長平均']
            sw = df.loc[29]['女性体重平均']
        elif  70<= a:
            sh = df.loc[30]['女性身長平均']
            sw = df.loc[30]['女性体重平均']
    st.write('')
    st.write('【プチ情報】',s,a,'歳の平均身長は',sh,'cm，平均体重は',sw,'kg')
    #st.write()

    if result == 1:
        st.write('炭水化物をしっかりとっていきましょう。')
        st.image('gluten.png')
    elif result == 2:
        st.write('継続して健康的な食事を続けていきましょう。')
        st.image('kenko.png')
    elif result == 3:
        st.write('野菜を中心とした低カロリーな食事に切り替えていきましょう。')
        st.image('vegetables.png')


    st.write('')


    st.header('あなたのための健康計画作成ツール')
    proper_w = float(((h/100)**2)*22)  #標準体重
    target_w = float(st.number_input('目標体重を入力してください(kg)'))
    st.write('※ちなみにあなたの身長の適正体重は',proper_w,'kgです。')
    priod = int(st.slider('何ヶ月で目標体重を達成しますか',1,12,1))

    diff_w = float((w - target_w)/priod)
    change_w = [w]
    sum_w = w
    button = st.button('健康計画表の自動作成')

    if button == True:

        latest_iteration = st.empty() #空コンテンツと一緒に変数を作成
        bar = st.progress(0)#プログレスを作る　値は０
        for i in range(100):
            latest_iteration.text('作成中')#空のIterationにテキストを入れていく
            bar.progress(i +1)#barの中身を増やしていく
            time.sleep(0.01)
        time.sleep(0.5)

        st.subheader('ダイエット計画表の作成')
        for i in range(priod-1):
            sum_w = int(sum_w - diff_w)
            change_w.append(sum_w)
        st.dataframe(change_w)
        st.line_chart(change_w)
