nums = [4, 13, 26, 57, 62, 71, 455]
# nums.sort()

def binary_search(nums):
    low = 0
    high = len(nums)-1
    mid = (low+high)//2
    search = int(input("Enter the number you want to search: "))

    while low <= mid:
        if search == nums[mid]:
            print("Number Found at Index Value: ", mid)
            break
        elif search < nums[mid]:
            high = mid-1
        elif search > nums[mid]:
            low = mid+1
        

        mid = (low+high)//2

    if low > mid:
        print("Not Found")

binary_search(nums)