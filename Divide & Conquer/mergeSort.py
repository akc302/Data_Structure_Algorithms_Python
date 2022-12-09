def merge_sort(arr):
    # we are splitting the array
    # from first index to middle of the index
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[i]
                j += 1

            k += 1
        # merging
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr_test = [2, 3, 5, 1, 6, 4, 4, 2, 3]

merge_sort(arr_test)

print(arr_test)
