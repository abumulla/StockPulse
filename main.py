# import streamlit as st

# from streamlit_option_menu import option_menu


# import Home, Account, Display, Predict, DeepPrediction, Watchlist




# class MultiApp:

#     def __init__(self):
#         self.apps = []

#     def add_app(self, title, func):

#         self.apps.append({
#             "title": title,
#             "function": func
#         })

#     def run():       
#         app = option_menu(
#             menu_title=None,
#             options=['Home','Account','Display','Predict I','Prediction','Watchlist'],
#             default_index=1,
#             orientation="horizontal",
            
#             )

        
#         if app == "Home":
#             Home.app()
#         if app == "Account":
#             Account.app()    
#         if app == "Display":
#             Display.app()        
#         if app == 'Predict I':
#             Predict.app()
#         if app == 'Prediction':
#             DeepPrediction.app() 
#         if app == 'Watchlist':
#             Watchlist.app()   
             
          
             
#     run()            


# import streamlit as st
# from streamlit_option_menu import option_menu
 
# import Home, Account, Display, Predict, DeepPrediction, Watchlist
 
# class MultiApp:
 
#     def __init__(self):
#         self.apps = []
 
#     def add_app(self, title, func, symbol):
#         self.apps.append({
#             "title": title,
#             "function": func,
#             "symbol": symbol
#         })
 
#     def run(self):      
#         app = option_menu(
#             menu_title="Dashboard",
#             options=['Home', 'Account', 'Display', 'Prediction', 'DeepPrediction', 'Watchlist'],
#             default_index=1,
#             orientation="horizontal",
#         )
 
#         # Get the selected app
#         selected_app = next((a for a in self.apps if a["title"] == app), None)
 
#         # Set background color
#         st.markdown(
#             f"""
#             <style>
#                 .reportview-container {{
#                     background: linear-gradient(to right, #485563, #29323c);
#                     color: white;
#                 }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )
 
#         # Display the selected app with its symbol and title
#         if selected_app:
#             st.sidebar.markdown(f"# {selected_app['symbol']} {selected_app['title']}")
#             selected_app["function"]()
 
# if __name__ == "__main__":
#     # Create an instance of MultiApp
#     multi_app = MultiApp()
 
#     # Add your apps to the MultiApp instance with symbols
#     multi_app.add_app("Home", Home.app, "🏠")
#     multi_app.add_app("Account", Account.app, "👤")
#     multi_app.add_app("Display", Display.app, "🔍")
#     multi_app.add_app('Predict I', Predict.app, "🔮")
#     multi_app.add_app('Prediction', DeepPrediction.app, "📈")
#     multi_app.add_app('Watchlist', Watchlist.app, "📋")
 
#     # Run the selected app
#     multi_app.run()
         
         
         

# import streamlit as st
# from streamlit_option_menu import option_menu
 
# import Home, Account, Display, Predict, DeepPrediction, Watchlist
 
# class MultiApp:
 
#     def __init__(self):
#         self.apps = []
 
#     def add_app(self, title, func, symbol):
#         self.apps.append({
#             "title": title,
#             "function": func,
#             "symbol": symbol
#         })
 
#     def run(self):      
#         app = option_menu(
#             menu_title="Dashboard",
#             options=['Home', 'Account', 'Display', 'Prediction', 'DeepPrediction', 'Watchlist'],
#             default_index=1,
#             orientation="horizontal",
#         )
 
#         # Get the selected app
#         selected_app = next((a for a in self.apps if a["title"] == app), None)
 
#         # Set background color
#         st.markdown(
#             f"""
#             <style>
#                 .reportview-container {{
#                     background: linear-gradient(to right, #485563, #29323c);
#                     color: white;
#                 }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )
 
#         # Display the selected app with its symbol and title
#         if selected_app:
#             st.sidebar.markdown(f"# {selected_app['symbol']} {selected_app['title']}")
#             selected_app["function"]()
 
# if __name__ == "__main__":
#     # Create an instance of MultiApp
#     multi_app = MultiApp()
 
#     # Add your apps to the MultiApp instance with symbols
#     multi_app.add_app("Home", Home.app, "🏠")
#     multi_app.add_app("Account", Account.app, "👤")
#     multi_app.add_app("Display", Display.app, "🔍")
#     multi_app.add_app('Prediction', Predict.app, "🔮")
#     multi_app.add_app('DeepPrediction', DeepPrediction.app, "📈")
#     multi_app.add_app('Watchlist', Watchlist.app, "📋")
 
#     # Run the selected app
#     multi_app.run()





import streamlit as st
from streamlit_option_menu import option_menu

import Home, Account, Display, Predict, DeepPrediction, Watchlist

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func, symbol):
        self.apps.append({
            "title": title,
            "function": func,
            "symbol": symbol
        })

    def run(self):      
        app = option_menu(
            menu_title="Dashboard",
            options=['Home', 'Account', 'Display', 'Prediction', 'DeepPrediction', 'Watchlist'],
            default_index=1,
            orientation="horizontal",
        )

        # Get the selected app
        selected_app = next((a for a in self.apps if a["title"] == app), None)

        # Set background color
        st.markdown(
            f"""
            <style>
                .reportview-container {{
                    background: linear-gradient(to right, #485563, #29323c);
                    color: white;
                }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # Display the selected app with its symbol and title
        if selected_app:
            st.sidebar.markdown(f"# {selected_app['symbol']} {selected_app['title']}")
            selected_app["function"]()

if __name__ == "__main__":
    # Create an instance of MultiApp
    multi_app = MultiApp()

    # Add your apps to the MultiApp instance with symbols
    multi_app.add_app("Home", Home.app, "🏠")
    multi_app.add_app("Account", Account.app, "👤")
    multi_app.add_app("Display", Display.app, "🔍")
    multi_app.add_app('Prediction', Predict.app, "🔮")
    multi_app.add_app('DeepPrediction', DeepPrediction.app, "📈")
    multi_app.add_app('Watchlist', Watchlist.app, "📋")

    # Run the selected app
    multi_app.run()

         