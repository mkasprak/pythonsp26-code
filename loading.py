import time

# 1. Start with an empty bar string
empty_bar = "----------"
bar_list = list(empty_bar)  # Breakdown to ["-", "-", ...]

print("Initiating Rocket Launch Sequence...")

for i in range(len(bar_list)):
    # Update the specific index in the LIST
    bar_list[i] = "🚀"

    # JOIN back to a STRING to display
    current_status = "".join(bar_list)
    print(f"Status: [{current_status}]")

    # Pause for 1 second before the next iteration
    time.sleep(1)

print("Liftoff!")
