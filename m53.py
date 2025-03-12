# import time
#
# # Define the decorator
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('start running function')
#         start_time = time.time()  # Record start time
#         result = func(*args, **kwargs)  # Execute the original function
#         end_time = time.time()  # Record end time
#         print('finished ')
#         print(f"Execution time: {end_time - start_time:.4f} seconds")  # Display execution time
#         return result  # Return the result of the original function
#     return wrapper
#
# # Use the decorator
# @timer_decorator
# def sample_function(n):
#     """A sample function that takes some time to complete."""
#     time.sleep(n)  # Sleep for n seconds
#     return "Function completed."
#
# if __name__ == '__main__':
#     result = sample_function(2)  # Execute the function with a 2-second sleep
#     print(result)  # Display the result



# Define a simple user class
# class User:
#     def __init__(self, username, role):
#         self.username = username
#         self.role = role
#
# # Define the authorization decorator
# def requires_role(required_role):
#     def decorator(func):
#         def wrapper(user, *args, **kwargs):
#             if user.role != required_role:
#                 raise PermissionError(f"User '{user.username}' does not have permission to perform this action.")
#             return func(user, *args, **kwargs)  # Execute the original function
#         return wrapper
#     return decorator
#
# # Use the decorator
# @requires_role("admin")
# def delete_user(user, user_id):
#     """Function to delete a user, only accessible to admin users."""
#     print(f"User '{user.username}' deleted user with ID: {user_id}")
#
# if __name__ == '__main__':
#     admin_user = User("Alice", "admin")
#     regular_user = User("Bob", "user")
#
#     # This should work
#     delete_user(admin_user, 42)
#
#     # This should raise a PermissionError
#     try:
#         delete_user(regular_user, 42)
#     except PermissionError as e:
#         print(e)  # Print the permission error message

# List of tuples
# students = [
#     ("Alice", 23),
#     ("Bob", 20),
#     ("Charlie", 22),
#     ("David", 21)
# ]
#
# # Sorting the list of tuples based on the second element (age) using lambda
# sorted_students = sorted(students, key=lambda student: student[1])
#
# # Displaying the sorted list
# print("Students sorted by age:")
# for student in sorted_students:
#     print(student)

# X=lambda  t:t**2
#
# print(X(5))
L=[i**2 for i in range(10)]
print(L)
print('hello')