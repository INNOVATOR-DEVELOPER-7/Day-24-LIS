def lis(sequence):
    n = len(sequence)
    # Create an array to store the length of the LIS ending at each index
    lis_length = [1] * n

    # Compute the LIS for each element
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j] and lis_length[i] < lis_length[j] + 1:
                lis_length[i] = lis_length[j] + 1

    # Find the maximum length of the LIS
    max_lis_length = max(lis_length)

    # Reconstruct the LIS
    lis_sequence = []
    current_length = max_lis_length
    for i in range(n - 1, -1, -1):
        if lis_length[i] == current_length:
            lis_sequence.append(sequence[i])
            current_length -= 1

    lis_sequence.reverse()
    return max_lis_length, lis_sequence

# Get the sequence from the user
user_input = input("Enter the sequence separated by space: ")
sequence = list(map(int, user_input.split()))

# Perform the LIS algorithm
max_lis_length, lis_sequence = lis(sequence)

# Print the LIS length and the sequence
print("The length of the Longest Increasing Subsequence is:", max_lis_length)
print("The Longest Increasing Subsequence is:", lis_sequence)
