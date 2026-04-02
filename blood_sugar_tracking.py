"""
    Writing to files
    Date/time
    calculate average... to come
    Annotated for clarity
"""
import datetime
# Import the datetime module to work with dates and times

# Function to get the user's blood sugar input


def get_sugar():
    # Ask the user for their current blood sugar level
    blood_sugar = input("Enter your current blood sugar level: ")
    # Return the entered value
    return blood_sugar


# Function to save the blood sugar data to a file
def save_to_file(timestamp_str, blood_sugar):
    # Store the data in a dictionary using the timestamp as the key
    health_log = {
        timestamp_str: blood_sugar
    }

    # Open the log file in append mode ('a') so new entries are added to the end
    with open("blood_sugar_log.txt", "a") as file:
        # Write the timestamp and blood sugar value to the file
        file.write(f"{timestamp_str} : {health_log[timestamp_str]},\n")


# Main function to coordinate the workflow
def main():
    # Get the user's blood sugar value
    bs = get_sugar()
    # Get the current date and time
    current_time = datetime.datetime.now()
    # Format the timestamp as a readable string
    timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    # Save the timestamp and blood sugar value to the file
    save_to_file(timestamp_str, bs)
    # Print confirmation to the user
    print(f"{timestamp_str} : {bs}")
    print("Health data successfully logged!")


# Run the main function if this script is executed
main()
