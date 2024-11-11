import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_customers(customers_dict, min_orders=5, min_order_price=20):
    """
    Analyze customer data and determine eligibility for free pizza
    
    Parameters:
    customers_dict: dict
        Dictionary with customer data where each customer has orders list
    min_orders: int
        Minimum number of orders required for eligibility
    min_order_price: float
        Minimum average order price required for eligibility
    
    Returns:
    tuple: (eligible_customers, customer_stats)
    """
    # Initialize dictionary to store customer statistics
    customer_stats = {}
    eligible_customers = []
    
    # Process each customer's data
    for customer, orders in customers_dict.items():
        total_orders = len(orders)
        total_spent = sum(orders)
        avg_order_price = total_spent / total_orders if total_orders > 0 else 0
        
        # Store statistics
        customer_stats[customer] = {
            'total_orders': total_orders,
            'total_spent': total_spent,
            'average_order': avg_order_price
        }
        
        # Check eligibility
        if total_orders >= min_orders and avg_order_price >= min_order_price:
            eligible_customers.append(customer)
    
    return eligible_customers, customer_stats

def visualize_customer_data(customer_stats):
    """
    Create visualizations of customer data
    
    Parameters:
    customer_stats: dict
        Dictionary containing customer statistics
    """
    # Convert to DataFrame for easier plotting
    df = pd.DataFrame.from_dict(customer_stats, orient='index')
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: Total Orders by Customer
    sns.barplot(data=df, y=df.index, x='total_orders', ax=ax1)
    ax1.set_title('Total Orders by Customer')
    ax1.set_xlabel('Number of Orders')
    ax1.set_ylabel('Customer')
    
    # Plot 2: Total Spent by Customer
    sns.barplot(data=df, y=df.index, x='total_spent', ax=ax2)
    ax2.set_title('Total Spent by Customer')
    ax2.set_xlabel('Amount Spent ($)')
    ax2.set_ylabel('Customer')
    
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Sample data
    customers = {
        'Alice': [25, 30, 15, 40, 35, 28],
        'Bob': [15, 10, 20],
        'Charlie': [50, 45, 60, 55, 48],
        'Diana': [22, 18, 25, 30, 28, 35, 40],
        'Eve': [10, 12, 8, 15]
    }
    
    # Get eligible customers and stats
    eligible, stats = analyze_customers(customers, min_orders=5, min_order_price=25)
    
    # Print results
    print("\nEligible customers for free pizza:")
    for customer in eligible:
        print(f"- {customer}")
        
    print("\nCustomer Statistics:")
    for customer, data in stats.items():
        print(f"\n{customer}:")
        print(f"  Total Orders: {data['total_orders']}")
        print(f"  Total Spent: ${data['total_spent']:.2f}")
        print(f"  Average Order: ${data['average_order']:.2f}")
    
    # Create visualizations
    visualize_customer_data(stats)
