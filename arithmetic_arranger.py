def arithmetic_arranger(problems_list, *solve):
    if len(problems_list) > 5:
        return "Error: Too many problems."
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    spaces = "    "

    for i, problem in enumerate(problems_list):  # for each argument like '1 - 2'
        split_problem = problem.split()  # now we will have a list of ['1', '-', '2'] this sort
        #     checking that symbol must be '+' or '-'
        if split_problem[1] not in '-+':
            return "Error: Operator must be '+' or '-'."
        #     checking the length of numbers. Must not be more than four
        if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        #     checking that each number only contains digits.
        try:
            num1 = int(split_problem[0])
            num2 = int(split_problem[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        #     determining which number from the two is larger in length
        max_num = max(len(split_problem[0]), len(split_problem[2]))
        #      adding two to determine no. of dashes to print
        breadth = max_num + 2

        # appending spaces and the 1st number in line1
        for n in range(0, breadth - len(split_problem[0])):
            line1 += " "
        line1 += split_problem[0]

        # appending the operator in line2
        line2 += split_problem[1]
        # appending the 2nd number in line 2
        for l in range(0, breadth - 1 - len(split_problem[2])):
            line2 += ' '
        line2 += split_problem[2]

        # appending the hyphens in line 3
        for m in range(0, breadth):
            line3 += '-'

        if solve:
            if split_problem[1] == '+':
                answer = str(num1 + num2)
            else:
                answer = str(num1 - num2)

            for k in range(0, breadth - len(answer)):
                line4 += " "
            line4 += answer

        if i < len(problems_list) - 1:
            line1 += spaces
            line2 += spaces
            line3 += spaces
            line4 += spaces

    arranged_problems = line1 + '\n' + line2 + '\n' + line3

    if solve:
        arranged_problems += '\n' + line4

    return arranged_problems
