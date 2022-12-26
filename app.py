import streamlit as st
from book import book
from customers import customer
from publisher import publisher
from author import author
from language import language
from book_author import book_author
from orderss import orders
from book_order import order_book
from city import city
from excecute_query import Excecute_query

def main():
    st.title("Bookstore Management System")
    menu=["book", "customer", "publisher", "author", "language", "book_author", "orders", "order_book", "city", "Excecute_query"]
    choice=st.sidebar.selectbox("Database_Entites",menu)

    if choice=="book":
        book()
    elif choice=="customer":
        customer()
    elif choice == "publisher":
        publisher()
    elif choice=="author":
        author()
    elif choice=="language":
        language()
    elif choice == "book_author":
        book_author()
    elif choice == "orders":
        orders()
    elif choice == "order_book":
        order_book()
    elif choice == "city":
        city()
    elif choice == "Excecute_query":
        Excecute_query()
    
if __name__ == '__main__':
    main()

