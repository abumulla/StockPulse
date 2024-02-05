# import streamlit as st
# import firebase_admin
# from firebase_admin import firestore, credentials, auth
# import yfinance as yf
# import plotly.graph_objects as go
# def app():
#     # Initialize Firebase
#     cred = credentials.Certificate("stockpulse-b1818-afca9e4f09d8.json")
#     #firebase_admin.initialize_app(cred)

#     # Get Firestore database reference
#     db = firestore.client()

#     # Set Streamlit app title
#     st.title('Welcome to :violet[StockPulse] :sunglasses:')

#     # Initialize session state variables
#     if 'username' not in st.session_state:
#         st.session_state.username = ''
#     if 'useremail' not in st.session_state:
#         st.session_state.useremail = ''
#     if 'watchlist' not in st.session_state:
#         st.session_state.watchlist = []


#     # Function to authenticate the user using Firebase
#     def authenticate_user():
#         try:
#             user = auth.get_user_by_email(email)
#             st.write('Login success')
#             st.session_state.username = user.uid
#             st.session_state.useremail = user.email
#             st.session_state.signedout = True
#             st.session_state.signout = True
#             load_watchlist(user.uid)

#         except auth.AuthError:
#             st.warning('Login Failed')


#     # Function to clear session state variables
#     def clear_session_state():
#         st.session_state.signout = False
#         st.session_state.signedout = False
#         st.session_state.username = ''
#         st.session_state.watchlist = []


#     # Function to load user's watchlist from Firestore
#     def load_watchlist(uid):
#         watchlist_ref = db.collection('watchlists').document(uid)
#         watchlist_data = watchlist_ref.get().to_dict()
#         if watchlist_data:
#             st.session_state.watchlist = watchlist_data.get('stocks', [])


#     # Function to save user's watchlist to Firestore
#     def save_watchlist(uid):
#         watchlist_ref = db.collection('watchlists').document(uid)
#         watchlist_ref.set({'stocks': st.session_state.watchlist})


#     # Function to get real-time stock data from Yahoo Finance
#     def get_stock_data(symbol):
#         stock_data = yf.download(symbol, period="1d", interval="1m")
#         return stock_data


#     # Function to plot stock data using Plotly Graph Objects
#     def plot_stock_data(symbol, data):
#         fig = go.Figure()
#         fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=symbol))
#         fig.update_layout(title=f"{symbol} Stock Price",
#                         xaxis_title="Timestamp",
#                         yaxis_title="Price (USD)",
#                         showlegend=True,
#                         )
#         st.plotly_chart(fig)


#     # Function to display graphs for each stock in the watchlist
#     def display_watchlist_graphs():
#         st.header('Watchlist Graphs')
#         for stock_symbol in st.session_state.watchlist:
#             st.subheader(f"Graph for {stock_symbol}")
#             stock_data = get_stock_data(stock_symbol)
#             if not stock_data.empty:
#                 plot_stock_data(stock_symbol, stock_data)
#             else:
#                 st.warning(f"Failed to fetch data for {stock_symbol}. Check the stock symbol or try again later.")


#     # Main Streamlit app
#     choice = st.selectbox('Login/Signup', ['Login', 'Sign'])

#     if not st.session_state['signedout']:
#         if choice == 'Login':
#             email = st.text_input('Email')
#             password = st.text_input('Password', type='password')
#             st.button('Login', on_click=authenticate_user)

#         else:
#             email = st.text_input('Email')
#             password = st.text_input('Password', type='password')
#             username = st.text_input('Enter Unique username')

#             if st.button('Create account'):
#                 user = auth.create_user(email=email, password=password, uid=username)
#                 st.success('Account created')
#                 st.markdown('Please login using username and password')
#                 st.balloons()

#     if st.session_state.signout:
#         st.text('Name' + st.session_state.username)
#         st.text('Email id: ' + st.session_state.useremail)

#         # Display watchlist and add/remove functionality
#         st.header('Watchlist')
#         selected_stock = st.text_input('Add a stock to your watchlist')
#         if st.button('Add to Watchlist') and selected_stock:
#             st.session_state.watchlist.append(selected_stock)
#             save_watchlist(st.session_state.username)
#             st.success(f'Added {selected_stock} to your watchlist!')

#         st.write('Your current watchlist:')
#         for stock in st.session_state.watchlist:
#             st.write(stock)

#         remove_stock = st.text_input('Remove a stock from your watchlist')
#         if st.button('Remove from Watchlist') and remove_stock:
#             if remove_stock in st.session_state.watchlist:
#                 st.session_state.watchlist.remove(remove_stock)
#                 save_watchlist(st.session_state.username)
#                 st.success(f'Removed {remove_stock} from your watchlist!')
#             else:
#                 st.warning(f"{remove_stock} is not in your watchlist.")

#         st.button('Sign out', on_click=clear_session_state)

#     # Display graphs for each stock in the watchlist
#     display_watchlist_graphs()



import streamlit as st
import firebase_admin
from firebase_admin import firestore, credentials, auth
import yfinance as yf
import plotly.graph_objects as go

def app():
    # Initialize Firebase
    cred = credentials.Certificate("stockpulse-b1818-afca9e4f09d8.json")
    #firebase_admin.initialize_app(cred)

    # Get Firestore database reference
    db = firestore.client()

    # Set Streamlit app title
    st.title('Welcome to :violet[StockPulse] :')

    # Initialize session state variables
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'watchlist' not in st.session_state:
        st.session_state.watchlist = []

    # Function to authenticate the user using Firebase
    def authenticate_user():
        try:
            user = auth.get_user_by_email(email)
            st.write('Login success')
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.signedout = True
            st.session_state.signout = True
            load_watchlist(user.uid)
        except auth.AuthError:
            st.warning('Login Failed')

    # Function to clear session state variables
    def clear_session_state():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''
        st.session_state.watchlist = []

    # Function to load user's watchlist from Firestore
    def load_watchlist(uid):
        watchlist_ref = db.collection('watchlists').document(uid)
        watchlist_data = watchlist_ref.get().to_dict()
        if watchlist_data:
            st.session_state.watchlist = watchlist_data.get('stocks', [])

    # Function to save user's watchlist to Firestore
    def save_watchlist(uid):
        watchlist_ref = db.collection('watchlists').document(uid)
        watchlist_ref.set({'stocks': st.session_state.watchlist})

    # Function to get real-time stock data from Yahoo Finance
    def get_stock_data(symbol):
        stock_data = yf.download(symbol, period="1d", interval="1m")
        return stock_data

    # Function to plot stock data using Plotly Graph Objects
    def plot_stock_data(symbol, data):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=symbol))
        fig.update_layout(title=f"{symbol} Stock Price",
                        xaxis_title="Timestamp",
                        yaxis_title="Price (USD)",
                        showlegend=True,
                        )
        st.plotly_chart(fig)

    # Function to display graphs for each stock in the watchlist
    def display_watchlist_graphs():
        st.header('Watchlist Graphs')
        for stock_symbol in st.session_state.watchlist:
            st.subheader(f"Graph for {stock_symbol}")
            stock_data = get_stock_data(stock_symbol)
            if not stock_data.empty:
                plot_stock_data(stock_symbol, stock_data)
            else:
                st.warning(f"Failed to fetch data for {stock_symbol}. Check the stock symbol or try again later.")

    # Main Streamlit app
    choice = st.selectbox('Login/Signup', ['Login', 'Sign'])

    if not st.session_state['signedout']:
        if choice == 'Login':
            email = st.text_input('Email')
            password = st.text_input('Password', type='password')
            st.button('Login', on_click=authenticate_user)

        else:
            email = st.text_input('Email')
            password = st.text_input('Password', type='password')
            username = st.text_input('Enter Unique username')

            if st.button('Create account'):
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account created')
                st.markdown('Please login using username and password')
                st.balloons()

    if st.session_state.signout:
        st.text('Name' + st.session_state.username)
        st.text('Email id: ' + st.session_state.useremail)

        # Display watchlist and add/remove functionality
        st.header('Watchlist')
        selected_stock = st.text_input('Add a stock to your watchlist')
        if st.button('Add to Watchlist') and selected_stock:
            if selected_stock not in st.session_state.watchlist:
                st.session_state.watchlist.append(selected_stock)
                save_watchlist(st.session_state.username)
                st.success(f'Added {selected_stock} to your watchlist!')
            else:
                st.warning(f'{selected_stock} is already in your watchlist.')

        st.write('Your current watchlist:')
        for stock in st.session_state.watchlist:
            st.write(stock)

        remove_stock = st.text_input('Remove a stock from your watchlist')
        if st.button('Remove from Watchlist') and remove_stock:
            if remove_stock in st.session_state.watchlist:
                st.session_state.watchlist.remove(remove_stock)
                save_watchlist(st.session_state.username)
                st.success(f'Removed {remove_stock} from your watchlist!')
            else:
                st.warning(f"{remove_stock} is not in your watchlist.")

        st.button('Sign out', on_click=clear_session_state)

    # Display graphs for each stock in the watchlist
    display_watchlist_graphs()
