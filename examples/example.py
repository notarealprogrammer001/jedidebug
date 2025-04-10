"""
Example usage of the JediDebug library.
"""

from jedidebug import JediDebug


def demonstrate_basic_usage():
    """Demonstrate basic usage of JediDebug."""
    print("=== Basic Usage ===")
    
    # Activate JediDebug
    JediDebug.activate()
    
    # Try a simple error
    print("\nGenerating a simple error:")
    try:
        1 / 0  # ZeroDivisionError
    except:
        print("Error caught and handled with Jedi wisdom")


def demonstrate_quotes_api():
    """Demonstrate the quotes API."""
    print("\n=== Quotes API ===")
    
    # Get a random motivational quote
    print("\nRandom quote:")
    print(JediDebug.get_motivational_quote())
    
    # Get quotes by category
    print("\nSyntax error quote:")
    try:
        print(JediDebug.get_quote_by_category('syntax'))
    except ValueError as e:
        print(f"Error: {e}")
    
    # List available categories
    print("\nAvailable quote categories:")
    categories = JediDebug.get_available_categories()
    print(", ".join(categories))


def demonstrate_decorator():
    """Demonstrate the Jedi function decorator."""
    print("\n=== Function Decorator ===")
    
    @JediDebug.jedi_function
    def force_error():
        """Function that will raise an error."""
        x = [1, 2, 3]
        return x[10]  # IndexError
    
    print("\nCalling function with decorator:")
    try:
        force_error()
    except:
        print("Error caught from decorated function")


def demonstrate_custom_quotes():
    """Demonstrate adding custom quotes."""
    print("\n=== Custom Quotes ===")
    
    # Add custom general quotes
    custom_quotes = [
        "Your bugs are very impressive. You must be very proud.",
        "Only a Sith deals in unhandled exceptions."
    ]
    num_added = JediDebug.add_quotes(custom_quotes)
    print(f"\nAdded {num_added} custom quotes")
    
    # Add custom categorized quotes
    custom_category_quotes = [
        "The variable is undefined? That's not true. That's impossible!",
        "No. undefined is not a function. That's not true. That's impossible!"
    ]
    num_added = JediDebug.add_categorized_quotes('logic', custom_category_quotes)
    print(f"Added {num_added} custom quotes to 'logic' category")
    
    # Show an example of a custom quote
    print("\nRandom quote (might be custom):")
    print(JediDebug.get_motivational_quote())


def demonstrate_deactivation():
    """Demonstrate deactivating JediDebug."""
    print("\n=== Deactivation ===")
    
    # Check if active
    print(f"\nJediDebug active: {JediDebug.is_active()}")
    
    # Deactivate JediDebug
    JediDebug.deactivate()
    print(f"JediDebug active after deactivation: {JediDebug.is_active()}")
    
    # Generate an error without Jedi wisdom
    print("\nGenerating error after deactivation:")
    try:
        int("not a number")  # ValueError
    except:
        print("Error caught without Jedi wisdom")
    
    # Reactivate for any future demos
    JediDebug.activate()
    print(f"JediDebug active after reactivation: {JediDebug.is_active()}")


def demonstrate_different_errors():
    """Demonstrate different error types with appropriate quotes."""
    print("\n=== Different Error Types ===")
    
    # SyntaxError demonstration
    print("\nSyntaxError demonstration:")
    try:
        exec("if True print('Hello')")  # SyntaxError
    except:
        print("SyntaxError caught with relevant Jedi wisdom")
    
    # TypeError demonstration
    print("\nTypeError demonstration:")
    try:
        len(5)  # TypeError
    except:
        print("TypeError caught with relevant Jedi wisdom")
    
    # FileNotFoundError demonstration
    print("\nFileNotFoundError demonstration:")
    try:
        with open("nonexistent_file.txt", "r") as f:  # FileNotFoundError
            f.read()
    except:
        print("FileNotFoundError caught with relevant Jedi wisdom")


if __name__ == "__main__":
    print("JediDebug Example Program\n")
    
    # Run all demonstrations
    demonstrate_basic_usage()
    demonstrate_quotes_api()
    demonstrate_decorator()
    demonstrate_custom_quotes()
    demonstrate_deactivation()
    demonstrate_different_errors()
    
    print("\nAll examples completed. May the Force be with you!")