from googlesearch import search

def get_google_search_results(query, num_results=10):
    # Perform the search
    results = search(query, num_results=num_results)
    
    # Display the results
    for i, result in enumerate(results):
        print(f"{i+1}: {result}")

if __name__ == "__main__":
    query = input("Enter your search query: ")
    get_google_search_results(query)
