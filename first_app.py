# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd 
import streamlit as st

data=pd.read_csv('database.csv')
#st.title('..Drug Review..')
#st.header('..Drug Review..')
#st.subheader('..Drug Review..')
#st.text('This is some text.')
#st.markdown('Streamlit is **_really_ cool**.')


add_selectbox = st.sidebar.selectbox(
    "Enter or select the Drugname",
    (data['drugname'])
)


st.sidebar.success("successfull")

    
#data[data['drugname']==add_selectbox]
for i in range(data.shape[0]):
    data.rating[i]=eval(data.rating[i])
    data.effective[i]=eval(data.effective[i])
    data.ineffective[i]=eval(data.ineffective[i])
    data.condition[i]=eval(data.condition[i])
    data.Top_side_effect[i]=eval(data.Top_side_effect[i])
    data['Side_effect'][i]=eval(data['Side_effect'][i])

g=list(data.loc[data['drugname']==add_selectbox,'condition'])[0]
h=list(data[data['drugname']==add_selectbox]['rating'])[0]
for i in range(len(h)):
    h[i]=int(float(h[i]*10))
g=pd.DataFrame(g,columns=['Condition'])
h=pd.DataFrame(h,columns=['Effectiveness'])
j=pd.concat([g,h],axis=1)#.set_index('Condition')
#st.write(pd.DataFrame({'Condition':g,'Effectiveness':h},index=h.index))
#data.index.name='Condition'
#st.table(j)
#st.text(st.table(data.loc[data['drugname']==add_selectbox,"condition"]))
#st.table(data)
#st.dataframe(j)


# Display Effective condition  

Q=pd.DataFrame(columns=['Condition','Effectiveness'])
if data.loc[data['drugname']==add_selectbox,'effective'].all():
    st.info("EFFECTIVE CONDITION")
    for k in range(j.shape[0]):
        if j['Effectiveness'][k]>50:
            Q=pd.concat([Q,pd.DataFrame({'Condition':[j['Condition'][k]],'Effectiveness':[j['Effectiveness'][k]]})])

    Q=Q.reset_index(drop=True)
    Q.index+=1
    st.table(Q)


# Display Ineffective condition 
  
Q=pd.DataFrame(columns=['Condition','Effectiveness'])
if data.loc[data['drugname']==add_selectbox,'ineffective'].all():
    st.info('INEFFECTIVE CONDITION')
    for k in range(j.shape[0]):
        if j['Effectiveness'][k]<=50:
            Q=pd.concat([Q,pd.DataFrame({'Condition':[j['Condition'][k]],'Effectiveness':[j['Effectiveness'][k]]})])
    Q=Q.reset_index(drop=True)
    Q.index+=1
    st.table(Q)


# Display side-effects  
    
if data.loc[data['drugname']==add_selectbox,'Top_side_effect'].all():
    st.info('TOP SIDE EFFECTS')
    R=pd.DataFrame(list(data.loc[data['drugname']==add_selectbox,'Top_side_effect'])[0],columns=['Top_side_effect'])
    R.index+=1
    st.table(R)

