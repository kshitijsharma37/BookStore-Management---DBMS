# Core Pkgs

import streamlit as st
import pandas as pd
import mysql.connector

mydb=mysql.connector.connect(

    host='localhost',
    user='root',
    database='bookstore2'

)



cur=mydb.cursor()


def sql_excecutor(raw_code):
    cur.execute(raw_code)
    data=cur.fetchall()
    return data


def Excecute_query():
    st.title("SQL_query_exec")
    menu=["Home","About"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=="Home":
        st.subheader("HomePage")

        #Columns/layout
        col1,col2=st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code=st.text_area("Sql code here")
                submit_code=st.form_submit_button("Excecute code")


        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                #result 
                query_result=sql_excecutor(raw_code)
                with st.expander("Results"):
                    st.write(query_result)
                with st.expander("Table"):
                    query_df=pd.DataFrame(query_result)
                    st.dataframe(query_df)




    else:
        st.subheader("About")


if __name__=='__main__':
    Excecute_query()


