import streamlit as st
import pandas as pd
from PIL import Image
import time 

# st.title('Streamlit 超入門')
# st.write('DataFrame')


# df1 = pd.DataFrame({
#     #辞書型
#     '1列目':[1,2,3,12],
#     '2列目':[5,6,7,4],
#     '3列目':[9,10,11,8]
# })

# st.write(df1)

# st.dataframe(df1.style.highlight_max(axis=0))

# st.table(df1.style.highlight_max(axis=0))

"""
# 章 
## 節
### 項

```python
import streamlit as st
import numpy as nm
import pandas as pd
```

"""

# df2 = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
# )

# st.write(df2)
# st.line_chart(df2)


# df3 = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )

# st.map(df3)


# if st.checkbox('Show img'):
#     img = Image.open('apple.jpg')
#     st.image(img, caption='リンゴ', use_column_width=True)

# option1 = st.selectbox(
#     'あなたの好きな数字を教えてください',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は', option1 , 'です。'

# option2 = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は',option2,'です。'


# conditon = st.slider('あなたの今の調子は？',0,100,50)
# 'あなたの今の調子は',conditon,'です。'

# #サイドバーを使った表示
# option2 = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は',option2,'です。'


# conditon = st.sidebar.slider('あなたの今の調子は？',0,100,50)
# 'あなたの今の調子は',conditon,'です。'

#2カラムレイアウトについて
# left_column,right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('個々は右カラムです')

#エキスパンダーによる問い合わせ内容フォームの作成
# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')


#プログレスバーの表示
latest_iteration  = st.empty()
bar = st.progress(0)

#for文が終了しない限り、下のプログラムは実行されない
for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.05)
    
'Done!!!!'
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

