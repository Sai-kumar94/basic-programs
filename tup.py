# # t = (1, 2, 3, 1, 2, 3, 1, 2, 3)
# # count_of_3 = t.count(3)
# # last_index_of_3 = len(t) - 1 - t[::-1].index(3)
# # print(f"The number 3 appears {count_of_3} times.")
# # print(f"The last occurrence of 3 is at index {last_index_of_3}.")
#
#
#
# # age=int(input('enter a num'))
# # if age<12:
# #     print('child')
# # elif 12<=age<=18:
# #     print('teenager')
# # else:
# #     print('adult')
#
#
# from collections import Counter
#
# # def find_possible_difference(arr1, arr2):
# #     n, m = len(arr1), len(arr2)
# #     arr2.sort()  # Sort arr2 for easier comparison
# #     smallest_y = float('inf')  # Initialize smallest y as infinity
# #
# #     # Generate all possible values of y
# #     possible_ys = [arr2[i] - arr1[j] for i in range(m) for j in range(n)]
# #
# #     # Check each possible value of y
# #     for y in sorted(possible_ys):
# #         # Adjust arr1 by adding y to all elements
# #         adjusted_arr1 = [x + y for x in arr1]
# #         adjusted_counter = Counter(adjusted_arr1)
# #         arr2_counter = Counter(arr2)
# #
# #         # Find the difference in counters
# #         diff = adjusted_counter - arr2_counter
# #
# #         # If exactly two elements need to be removed
# #         if len(diff) == 2 and sum(diff.values()) == 2:
# #             smallest_y = min(smallest_y, y)
# #
# #     return smallest_y if smallest_y != float('inf') else -1  # Return -1 if no valid y is found
# #
# # # Example Test Cases
# # arr1 = [5, 30, 25, 20, 15]
# # arr2 = [22, 18, 28]
# # print("Output:", find_possible_difference(arr1, arr2))  # Expected Output: -3
#
# # arr1 = [6, 9, 9, 6]
# # arr2 = [3, 6]
# # print("Output:", find_possible_difference(arr1, arr2))  # Expected Output: -3
# #
# # # Additional Test Cases
# # arr1 = [1, 4, 6, 8]
# # arr2 = [3, 5]
# # print("Output:", find_possible_difference(arr1, arr2))  # Expected Output: 2
# #
# # arr1 = [10, 20, 30, 40]
# # arr2 = [15, 35]
# # print("Output:", find_possible_difference(arr1, arr2))  # Expected Output: 5
#
# #
# # from collections import Counter
# #
# #
# # def find_possible_difference(arr1, arr2):
# #     n, m = len(arr1), len(arr2)
# #     arr2.sort()  # Sort arr2 for easier comparison
# #     smallest_y = float('inf')  # Initialize smallest y as infinity
# #
# #     # Generate all possible values of y
# #     possible_ys = [arr2[i] - arr1[j] for i in range(m) for j in range(n)]
# #
# #     # Check each possible value of y
# #     for y in sorted(possible_ys):
# #         # Adjust arr1 by adding y to all elements
# #         adjusted_arr1 = [x + y for x in arr1]
# #
# #         # Count elements in adjusted_arr1 and arr2
# #         adjusted_counter = Counter(adjusted_arr1)
# #         arr2_counter = Counter(arr2)
# #
# #         # Find the difference in counters
# #         diff = adjusted_counter - arr2_counter
# #
# #         # Check if the remaining elements in adjusted_arr1 match arr2 exactly
# #         if len(diff) == 2 and sum(diff.values()) == 2:
# #             # Verify remaining elements after removing these two match arr2
# #             remaining_elements = []
# #             for key, count in adjusted_counter.items():
# #                 if count > arr2_counter[key]:
# #                     remaining_elements.extend([key] * (count - arr2_counter[key]))
# #             if sorted(remaining_elements) == sorted(adjusted_arr1):
# #                 smallest_y = min(smallest_y, y)
# #
# #     return smallest_y if smallest_y != float('inf') else -1  # Return -1 if no valid y is found
# #
# #
# # # Example Test Cases
# # arr1 = [5, 30, 25, 20, 15]
# # arr2 = [22, 18, 28]
# # print("Output:", find_possible_difference(arr1, arr2))  # Expected Output: -3
#
#
# from collections import Counter
#
#
# def find_possible_difference(arr1, arr2):
#     n, m = len(arr1), len(arr2)
#     arr2.sort()  # Sort arr2 for easier comparison
#     smallest_y = float('inf')  # Initialize smallest y as infinity
#
#     # Generate all possible values of y
#     possible_ys = [arr2[i] - arr1[j] for i in range(m) for j in range(n)]
#
#     # Check each possible value of y
#     for y in sorted(possible_ys):
#         # Adjust arr1 by adding y to all elements
#         adjusted_arr1 = [x + y for x in arr1]
#
#         # Count elements in adjusted_arr1 and arr2
#         adjusted_counter = Counter(adjusted_arr1)
#         arr2_counter = Counter(arr2)
#
#         # Find the difference in counters
#         diff = adjusted_counter - arr2_counter
#
#         # Check if the remaining elements in adjusted_arr1 match arr2 exactly
#         if len(diff) == 2 and sum(diff.values()) == 2:
#             # Verify remaining elements after removing these two match arr2
#             remaining_elements = []
#             for key, count in adjusted_counter.items():
#                 if count > arr2_counter[key]:
#                     remaining_elements.extend([key] * (count - arr2_counter[key]))
#             if sorted(remaining_elements) == sorted(arr2):
#                 smallest_y = min(smallest_y, y)
#
#     return smallest_y if smallest_y != float('inf') else -1  # Return -1 if no valid y is found
#
#
# # Example Test Cases
# arr1 = [5, 30, 25, 20, 15]
# arr2 = [22, 18, 28]
# print("Output:", find_possible_difference(arr1, arr2))  # Expected Output: -3
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from collections import Counter
#
#
# def find_possible_difference(arr1, arr2):
#     n, m = len(arr1), len(arr2)
#
#     arr2.sort()
#
#     possible = [arr2[i] - arr1[j] for i in range(m) for j in range(n)]
#
#     for y in sorted(possible):
#         adj = [x + y for x in arr1]
#         diff = Counter(adj) - Counter(arr2)
#
#         if len(diff) == 2 and sum(diff.values()) == 0:
#             return y
#     return -1
# print(find_possible_difference([5, 30, 25, 20, 15], arr2=[22, 18, 28]))

