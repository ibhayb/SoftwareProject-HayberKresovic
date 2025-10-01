def binary_search(array, element, left, right):
   if right < left:
      return False # not found
   mid = (left+right)//2
   if element == array[mid]:
      return mid
   elif element < array[mid]:
      return binary_search(array, element, left, mid-1)
   else:
      return binary_search(array, element, mid+1, right)