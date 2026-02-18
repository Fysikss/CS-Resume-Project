"""
    Name: wikipedia_oop.py
    Author: Noel Onate
    Created: 2/18/26
    Purpose: OOP method which can be integrated
    into main JARVIS project
"""
# pip install wikipedia
import wikipedia

class WikipediaApp:
    # ----------------------- GET WIKIPEDIA ---------------------------- #
    def get_wikipedia(self, search_term):
        """Search Wikipedia"""
        try:
            # Return a summary result of 3 sentences
            self._summary = wikipedia.summary(search_term, sentences=3)
            return self._summary
        
        except:
            # If there is an exception, allow the user to try again
            return "Try a different search term."
        
def main():
    # Create a program object
    wikipedia_app = WikipediaApp()

    # Menu loop
    while True:
        search = input("What would you like to search for on Wikipedia? ")
        answer = wikipedia_app.get_wikipedia(search)
        print(answer)

        menu_choice = input("Do you want to search again? (y/n): ")
        if menu_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()