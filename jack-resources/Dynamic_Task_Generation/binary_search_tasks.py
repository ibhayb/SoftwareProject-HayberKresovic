import random
from formatter_for_copy_paste_export_to_jack3 import *
from formatter_to_xml import format_to_xml, clear_variable_declarations
from append_question_number_to_string import append_question_number_to_string

# Function 1: Binary Search - Second Recursive Call
def generate_task_for_second_recursive_call(question_number, num_calls=5):
    arrays = []
    ks = []

    ls_initial_call = []
    rs_initial_call = []

    ls_first_recursive_call = []
    rs_first_recursive_call = []

    ls_second_recursive_call = []
    rs_second_recursive_call = []

    ls_third_recursive_call = []
    rs_third_recursive_call = []
    
    for _ in range(num_calls):
        size = random.randint(15, 20) 
        array = sorted(random.sample(range(1, 50), size))

        first_mid = (0 + len(array) - 1) // 2
        invalid_k_values = [
            array[first_mid],  # Exclude first found k value
            array[((first_mid - 1) + 0) // 2],  # Exclude second possible k value (lower part)
            array[((first_mid + 1) + len(array) - 1) // 2]  # Exclude second possible k value (upper part)
        ]

        valid_k_values = [x for x in array if x not in invalid_k_values]
        k = random.choice(valid_k_values)  # Randomly pick a value for k that ensures two recursions

        initial_call_left = None
        initial_call_right = None

        first_recursive_call_left = None
        first_recursive_call_right = None

        second_recursive_call_left = None
        second_recursive_call_right = None

        third_recursive_call_left = None
        third_recursive_call_right = None

        def binary_search(array, element, left, right, call_count):
            nonlocal third_recursive_call_left, third_recursive_call_right, second_recursive_call_left, second_recursive_call_right, first_recursive_call_left, first_recursive_call_right, initial_call_left, initial_call_right

            if right < left:
                return False

            mid = (left + right) // 2

            if call_count == 0:
                initial_call_left = left
                initial_call_right = right

            if call_count == 1:
                first_recursive_call_left = left
                first_recursive_call_right = right

            if call_count == 2:
                second_recursive_call_left = left
                second_recursive_call_right = right

            if call_count == 3:
                third_recursive_call_left = left
                third_recursive_call_right = right

            if element == array[mid]:
                return mid
            elif element < array[mid]:
                return binary_search(array, element, left, mid - 1, call_count + 1)
            else:
                return binary_search(array, element, mid + 1, right, call_count + 1)

        binary_search(array, k, 0, len(array) - 1, 0)

        arrays.append(array)
        ks.append(k)
        ls_initial_call.append(initial_call_left)
        rs_initial_call.append(initial_call_right)

        ls_first_recursive_call.append(first_recursive_call_left)
        rs_first_recursive_call.append(first_recursive_call_right)

        ls_second_recursive_call.append(second_recursive_call_left)
        rs_second_recursive_call.append(second_recursive_call_right)

        ls_third_recursive_call.append("" if third_recursive_call_left == None else third_recursive_call_left)
        rs_third_recursive_call.append("" if third_recursive_call_right == None else third_recursive_call_right)

    return [
        (append_question_number_to_string(question_number, 'arrays'), append_question_number_to_string(question_number, 'array'), format_list_of_arrays(arrays)),
        (append_question_number_to_string(question_number, 'ks'), append_question_number_to_string(question_number, 'k'), format_list_of_strings(ks)),
        
        (append_question_number_to_string(question_number, 'ls_initial_call'), append_question_number_to_string(question_number, 'l_initial_call'), format_list_of_integers(ls_initial_call)),
        (append_question_number_to_string(question_number, 'rs_initial_call'), append_question_number_to_string(question_number, 'r_initial_call'), format_list_of_integers(rs_initial_call)),

        (append_question_number_to_string(question_number, 'ls_first_recursive_call'), append_question_number_to_string(question_number, 'l_first_recursive_call'), format_list_of_integers(ls_first_recursive_call)),
        (append_question_number_to_string(question_number, 'rs_first_recursive_call'), append_question_number_to_string(question_number, 'r_first_recursive_call'), format_list_of_integers(rs_first_recursive_call)),

        (append_question_number_to_string(question_number, 'ls_second_recursive_call'), append_question_number_to_string(question_number, 'l_second_recursive_call'), format_list_of_integers(ls_second_recursive_call)),
        (append_question_number_to_string(question_number, 'rs_second_recursive_call'), append_question_number_to_string(question_number, 'r_second_recursive_call'), format_list_of_integers(rs_second_recursive_call)),
        
        (append_question_number_to_string(question_number, 'ls_third_recursive_call'), append_question_number_to_string(question_number, 'l_third_recursive_call'), format_list_of_strings(ls_third_recursive_call)),
        (append_question_number_to_string(question_number, 'rs_third_recursive_call'), append_question_number_to_string(question_number, 'r_third_recursive_call'), format_list_of_strings(rs_third_recursive_call)),
   ]


# Function 2: Binary Search - Interval Tracking
def generate_task_for_interval(question_number, num_calls=5):
    arrays = []
    ks = []

    ls_initial_call = []
    rs_initial_call = []

    ls_first_recursive_call = []
    rs_first_recursive_call = []

    ls_second_recursive_call = []
    rs_second_recursive_call = []

    ls_third_recursive_call = []
    rs_third_recursive_call = []

    initial_solutions = []
    first_solutions = []
    second_solutions = []
    third_solutions = []

    for _ in range(num_calls):
        size = random.randint(10, 15)
        array = sorted(random.sample(range(1, 50), size))

        k = random.choice(array)

        initial_call_left = None
        initial_call_right = None

        first_recursive_call_left = None
        first_recursive_call_right = None

        second_recursive_call_left = None
        second_recursive_call_right = None

        third_recursive_call_left = None
        third_recursive_call_right = None

        def binary_search(array, element, left, right, call_count):
            nonlocal third_recursive_call_left, third_recursive_call_right, second_recursive_call_left, second_recursive_call_right, first_recursive_call_left, first_recursive_call_right, initial_call_left, initial_call_right

            if right < left:
                return False

            mid = (left + right) // 2

            if call_count == 0:
                initial_call_left = left
                initial_call_right = right

            if call_count == 1:
                first_recursive_call_left = left
                first_recursive_call_right = right

            if call_count == 2:
                second_recursive_call_left = left
                second_recursive_call_right = right

            if call_count == 3:
                third_recursive_call_left = left
                third_recursive_call_right = right

            if element == array[mid]:
                return mid
            elif element < array[mid]:
                return binary_search(array, element, left, mid - 1, call_count + 1)
            else:
                return binary_search(array, element, mid + 1, right, call_count + 1)

        binary_search(array, k, 0, len(array) - 1, 0)

        arrays.append(array)
        ks.append(k)

        ls_initial_call.append("" if initial_call_left is None else initial_call_left)
        rs_initial_call.append("" if initial_call_right is None else initial_call_right)

        ls_first_recursive_call.append("" if first_recursive_call_left is None else first_recursive_call_left)
        rs_first_recursive_call.append("" if first_recursive_call_right is None else first_recursive_call_right)

        ls_second_recursive_call.append("" if second_recursive_call_left is None else second_recursive_call_left)
        rs_second_recursive_call.append("" if second_recursive_call_right is None else second_recursive_call_right)

        ls_third_recursive_call.append("" if third_recursive_call_left is None else third_recursive_call_left)
        rs_third_recursive_call.append("" if third_recursive_call_right is None else third_recursive_call_right)

        result = []

        initial_solutions.append(
            f"1. l = {'' if initial_call_left is None else initial_call_left}, r = {'' if initial_call_right is None else initial_call_right}")

        if first_recursive_call_left is not None or first_recursive_call_right is not None:
            first_solutions.append(
                f"2. l = {'' if first_recursive_call_left is None else first_recursive_call_left}, r = {'' if first_recursive_call_right is None else first_recursive_call_right}")
        else:
            first_solutions.append("")

        if second_recursive_call_left is not None or second_recursive_call_right is not None:
            second_solutions.append(
                f"3. l = {'' if second_recursive_call_left is None else second_recursive_call_left}, r = {'' if second_recursive_call_right is None else second_recursive_call_right}")
        else:
            second_solutions.append("")

        if third_recursive_call_left is not None or third_recursive_call_right is not None:
            third_solutions.append(
                f"4. l = {'' if third_recursive_call_left is None else third_recursive_call_left}, r = {'' if third_recursive_call_right is None else third_recursive_call_right}")
        else:
            third_solutions.append("")


    return [
        (append_question_number_to_string(question_number, 'arrays'),
         append_question_number_to_string(question_number, 'array'), format_list_of_arrays(arrays)),
        (
        append_question_number_to_string(question_number, 'ks'), append_question_number_to_string(question_number, 'k'),
        format_list_of_strings(ks)),

        (append_question_number_to_string(question_number, 'ls_initial_call'),
         append_question_number_to_string(question_number, 'l_initial_call'), format_list_of_strings(ls_initial_call)),
        (append_question_number_to_string(question_number, 'rs_initial_call'),
         append_question_number_to_string(question_number, 'r_initial_call'), format_list_of_strings(rs_initial_call)),

        (append_question_number_to_string(question_number, 'ls_first_recursive_call'),
         append_question_number_to_string(question_number, 'l_first_recursive_call'),
         format_list_of_strings(ls_first_recursive_call)),
        (append_question_number_to_string(question_number, 'rs_first_recursive_call'),
         append_question_number_to_string(question_number, 'r_first_recursive_call'),
         format_list_of_strings(rs_first_recursive_call)),

        (append_question_number_to_string(question_number, 'ls_second_recursive_call'),
         append_question_number_to_string(question_number, 'l_second_recursive_call'),
         format_list_of_strings(ls_second_recursive_call)),
        (append_question_number_to_string(question_number, 'rs_second_recursive_call'),
         append_question_number_to_string(question_number, 'r_second_recursive_call'),
         format_list_of_strings(rs_second_recursive_call)),

        (append_question_number_to_string(question_number, 'ls_third_recursive_call'),
         append_question_number_to_string(question_number, 'l_third_recursive_call'),
         format_list_of_strings(ls_third_recursive_call)),
        (append_question_number_to_string(question_number, 'rs_third_recursive_call'),
         append_question_number_to_string(question_number, 'r_third_recursive_call'),
         format_list_of_strings(rs_third_recursive_call)),

        (append_question_number_to_string(question_number, 'initial_solutions'),
         append_question_number_to_string(question_number, 'initial_solution'),
         format_list_of_strings(initial_solutions)),

        (append_question_number_to_string(question_number, 'first_solutions'),
         append_question_number_to_string(question_number, 'first_solution'),
         format_list_of_strings(first_solutions)),

        (append_question_number_to_string(question_number, 'second_solutions'),
         append_question_number_to_string(question_number, 'second_solution'),
         format_list_of_strings(second_solutions)),

        (append_question_number_to_string(question_number, 'third_solutions'),
         append_question_number_to_string(question_number, 'third_solution'),
         format_list_of_strings(third_solutions)),
    ]


# Function 3: Binary Search - Mid Values
def generate_task_for_mid_values(question_number, num_calls=5):
    arrays = []
    ks = []
    
    firstMids = []
    secondMids = []
    thirdMids = []
    fourthMids = []

    firstMidsForDisplayingWithNumeration = []
    secondMidsForDisplayingWithNumeration = []
    thirdMidsForDisplayingWithNumeration = []
    fourthMidsForDisplayingWithNumeration = []

    firstWrongMids = []
    secondWrongMids = []
    thirdWrongMids = []
    fourthWrongMids = []
        
    firstLs = []
    secondLs = []
    thirdLs = []
    fourthLs = []

    firstRs = []
    secondRs = []
    thirdRs = []
    fourthRs = []


    for _ in range(num_calls):
        size = random.randint(7, 9)
        array = sorted(random.sample(range(1, 20), size))

        k = random.choice(array)

        mid_values = []
        wrong_mid_values = []
        l_values = []
        r_values = []

        def binary_search(array, element, left, right):

            if right < left:
                return False

            mid = (left + right) // 2
            mid_values.append(mid)
            wrong_mid_values.append(array[mid])
            l_values.append(left)
            r_values.append(right)

            if element == array[mid]:
                return mid
            elif element < array[mid]:
                return binary_search(array, element, left, mid - 1)
            else:
                return binary_search(array, element, mid + 1, right)

        binary_search(array, k, 0, len(array) - 1)

        while (len(mid_values) < 4):
            mid_values.append("")

        while (len(wrong_mid_values) < 4):
            wrong_mid_values.append("")

        while (len(l_values) < 4):
            l_values.append("")

        while (len(r_values) < 4):
            r_values.append("")

        arrays.append(array)
        ks.append(k)

        firstMids.append(mid_values[0])
        secondMids.append(mid_values[1])
        thirdMids.append(mid_values[2])
        fourthMids.append(mid_values[3])

        firstMidsForDisplayingWithNumeration.append("" if mid_values[0] == "" else "1. " + str(mid_values[0]))
        secondMidsForDisplayingWithNumeration.append("" if mid_values[1] == "" else "2. " + str(mid_values[1]))
        thirdMidsForDisplayingWithNumeration.append("" if mid_values[2] == "" else "3. " + str(mid_values[2]))
        fourthMidsForDisplayingWithNumeration.append("" if mid_values[3] == "" else "4. " + str(mid_values[3]))

        firstWrongMids.append(wrong_mid_values[0])
        secondWrongMids.append(wrong_mid_values[1])
        thirdWrongMids.append(wrong_mid_values[2])
        fourthWrongMids.append(wrong_mid_values[3])

        firstRs.append(r_values[0])
        secondRs.append(r_values[1])
        thirdRs.append(r_values[2])
        fourthRs.append(r_values[3])

        firstLs.append(l_values[0])
        secondLs.append(l_values[1])
        thirdLs.append(l_values[2])
        fourthLs.append(l_values[3])
    
    return [
        (append_question_number_to_string(question_number, 'arrays'), append_question_number_to_string(question_number, 'array'), format_list_of_arrays(arrays)),
        (append_question_number_to_string(question_number, 'ks'), append_question_number_to_string(question_number, 'k'), format_list_of_strings(ks)),
        
        (append_question_number_to_string(question_number, 'first_mids'), append_question_number_to_string(question_number, 'first_mid'), format_list_of_strings(firstMids)),
        (append_question_number_to_string(question_number, 'second_mids'), append_question_number_to_string(question_number, 'second_mid'), format_list_of_strings(secondMids)),
        (append_question_number_to_string(question_number, 'third_mids'), append_question_number_to_string(question_number, 'third_mid'), format_list_of_strings(thirdMids)),
        (append_question_number_to_string(question_number, 'fourth_mids'), append_question_number_to_string(question_number, 'fourth_mid'), format_list_of_strings(fourthMids)),
        
        (append_question_number_to_string(question_number, 'first_mids_for_displaying_with_numeration'), append_question_number_to_string(question_number, 'first_mid_for_displaying_with_numeration'), format_list_of_strings(firstMidsForDisplayingWithNumeration)),
        (append_question_number_to_string(question_number, 'second_mids_for_displaying_with_numeration'), append_question_number_to_string(question_number, 'second_mid_for_displaying_with_numeration'), format_list_of_strings(secondMidsForDisplayingWithNumeration)),
        (append_question_number_to_string(question_number, 'third_mids_for_displaying_with_numeration'), append_question_number_to_string(question_number, 'third_mid_for_displaying_with_numeration'), format_list_of_strings(thirdMidsForDisplayingWithNumeration)),
        (append_question_number_to_string(question_number, 'fourth_mids_for_displaying_with_numeration'), append_question_number_to_string(question_number, 'fourth_mid_for_displaying_with_numeration'), format_list_of_strings(fourthMidsForDisplayingWithNumeration)),

        (append_question_number_to_string(question_number, 'first_wrong_mids'), append_question_number_to_string(question_number, 'first_wrong_mid'), format_list_of_strings(firstWrongMids)),
        (append_question_number_to_string(question_number, 'second_wrong_mids'), append_question_number_to_string(question_number, 'second_wrong_mid'), format_list_of_strings(secondWrongMids)),
        (append_question_number_to_string(question_number, 'third_wrong_mids'), append_question_number_to_string(question_number, 'third_wrong_mid'), format_list_of_strings(thirdWrongMids)),
        (append_question_number_to_string(question_number, 'fourth_wrong_mids'), append_question_number_to_string(question_number, 'fourth_wrong_mid'), format_list_of_strings(fourthWrongMids)),
        
        (append_question_number_to_string(question_number, 'first_ls'), append_question_number_to_string(question_number, 'first_l'), format_list_of_strings(firstLs)),
        (append_question_number_to_string(question_number, 'second_ls'), append_question_number_to_string(question_number, 'second_l'), format_list_of_strings(secondLs)),
        (append_question_number_to_string(question_number, 'third_ls'), append_question_number_to_string(question_number, 'third_l'), format_list_of_strings(thirdLs)),
        (append_question_number_to_string(question_number, 'fourth_ls'), append_question_number_to_string(question_number, 'fourth_l'), format_list_of_strings(fourthLs)),
        
        (append_question_number_to_string(question_number, 'first_rs'), append_question_number_to_string(question_number, 'first_r'), format_list_of_strings(firstRs)),
        (append_question_number_to_string(question_number, 'second_rs'), append_question_number_to_string(question_number, 'second_r'), format_list_of_strings(secondRs)),
        (append_question_number_to_string(question_number, 'third_rs'), append_question_number_to_string(question_number, 'third_r'), format_list_of_strings(thirdRs)),
        (append_question_number_to_string(question_number, 'fourth_rs'), append_question_number_to_string(question_number, 'fourth_r'), format_list_of_strings(fourthRs)),
        ]

# Function 4: Binary Search - Mid Value Comparison Amount
def generate_task_for_mid_value_comparison_amount(question_number, num_calls=100):
    arrays = []
    ks = []
    mid_comps = []

    firstMidsForDisplayingWithNumeration = []
    secondMidsForDisplayingWithNumeration = []
    thirdMidsForDisplayingWithNumeration = []
    fourthMidsForDisplayingWithNumeration = []

    firstAAtMidToKComparison = []
    secondAAtMidToKComparison = []
    thirdAAtMidToKComparison = []
    fourthAAtMidToKComparison = []

    for _ in range(num_calls):
        size = random.randint(7, 9)
        array = sorted(random.sample(range(1, 20), size))

        k = random.choice(array)

        mid_comparisons = 0
        mid_values = []

        def binary_search(array, element, left, right):
            nonlocal mid_comparisons

            if right < left:
                return False

            mid = (left + right) // 2

            mid_values.append(mid)
            mid_comparisons += 1

            if element == array[mid]:
                return mid
            elif element < array[mid]:
                return binary_search(array, element, left, mid - 1)
            else:
                return binary_search(array, element, mid + 1, right)

        binary_search(array, k, 0, len(array) - 1)

        while (len(mid_values) < 4):
            mid_values.append("")

        arrays.append(array)
        ks.append(k)
        mid_comps.append(mid_comparisons)

        firstMidsForDisplayingWithNumeration.append("" if mid_values[0] == "" else "1. " + str(mid_values[0]))
        secondMidsForDisplayingWithNumeration.append("" if mid_values[1] == "" else "2. " + str(mid_values[1]))
        thirdMidsForDisplayingWithNumeration.append("" if mid_values[2] == "" else "3. " + str(mid_values[2]))
        fourthMidsForDisplayingWithNumeration.append("" if mid_values[3] == "" else "4. " + str(mid_values[3]))

        firstAAtMidToKComparison.append("" if mid_values[0] == "" else "1. " + "array[" + str(mid_values[0]) + "]" + (" == " + str(k) if k == array[mid_values[0]] else " != " + str(k)))
        secondAAtMidToKComparison.append("" if mid_values[1] == "" else "2. " + "array[" + str(mid_values[1]) + "]" + (" == " + str(k) if k == array[mid_values[1]] else " != " + str(k)))
        thirdAAtMidToKComparison.append("" if mid_values[2] == "" else "3. " + "array[" + str(mid_values[2]) + "]" + (" == " + str(k) if k == array[mid_values[2]] else " != " + str(k)))
        fourthAAtMidToKComparison.append("" if mid_values[3] == "" else "4. " + "array[" + str(mid_values[3]) + "]" + (" == " + str(k) if k == array[mid_values[3]] else " != " + str(k)))
    
    return [
        (append_question_number_to_string(question_number, 'arrays'), append_question_number_to_string(question_number, 'array'), format_list_of_arrays(arrays)),
        (append_question_number_to_string(question_number, 'ks'), append_question_number_to_string(question_number, 'k'), format_list_of_strings(ks)),
        (append_question_number_to_string(question_number, 'comparisons_of_a_at_position_mid_to_k'), append_question_number_to_string(question_number, 'comparison_of_a_at_position_mid_to_k'), format_list_of_values(mid_comps)),
        
        (append_question_number_to_string(question_number, 'first_mids_for_displaying_with_numeration'), append_question_number_to_string(question_number, 'first_mid_for_displaying_with_numeration'), format_list_of_strings(firstMidsForDisplayingWithNumeration)),
        (append_question_number_to_string(question_number, 'second_mids_for_displaying_with_numeration'), append_question_number_to_string(question_number, 'second_mid_for_displaying_with_numeration'), format_list_of_strings(secondMidsForDisplayingWithNumeration)),
        (append_question_number_to_string(question_number, 'third_mids_for_displaying_with_numeration'), append_question_number_to_string(question_number, 'third_mid_for_displaying_with_numeration'), format_list_of_strings(thirdMidsForDisplayingWithNumeration)),
        (append_question_number_to_string(question_number, 'fourth_mids_for_displaying_with_numeration'), append_question_number_to_string(question_number, 'fourth_mid_for_displaying_with_numeration'), format_list_of_strings(fourthMidsForDisplayingWithNumeration)),
        
        (append_question_number_to_string(question_number, 'first_a_at_mid_to_k_comparisons'), append_question_number_to_string(question_number, 'first_a_at_mid_to_k_comparison'), format_list_of_strings(firstAAtMidToKComparison)),
        (append_question_number_to_string(question_number, 'second_a_at_mid_to_k_comparisons'), append_question_number_to_string(question_number, 'second_a_at_mid_to_k_comparison'), format_list_of_strings(secondAAtMidToKComparison)),
        (append_question_number_to_string(question_number, 'third_a_at_mid_to_k_comparisons'), append_question_number_to_string(question_number, 'third_a_at_mid_to_k_comparison'), format_list_of_strings(thirdAAtMidToKComparison)),
        (append_question_number_to_string(question_number, 'fourth_a_at_mid_to_k_comparisons'), append_question_number_to_string(question_number, 'fourth_a_at_mid_to_k_comparison'), format_list_of_strings(fourthAAtMidToKComparison)),
        ]

folder_path = "/Users/timfinmans/Downloads/Binary Search"

clear_variable_declarations(folder_path)

num_calls = 25

question_number = 1
result = generate_task_for_mid_values(question_number, num_calls)
format_to_xml(folder_path, result, question_number, num_calls)

question_number = 2
result = generate_task_for_mid_value_comparison_amount(question_number, num_calls)
format_to_xml(folder_path, result, question_number, num_calls)

question_number = 3
result = generate_task_for_second_recursive_call(question_number, num_calls)
format_to_xml(folder_path, result, question_number, num_calls)

question_number = 4
result = generate_task_for_interval(question_number, num_calls)
format_to_xml(folder_path, result, question_number, num_calls)

