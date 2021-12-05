"""My Math Calculator"""
__author__ = "Tyler Chazin"

# 10/26/21
# Math is imported.
import math


def main():
    """The beginning of the calculator"""
    print(input("Welcome to my math calculator. Press any button to "
                "begin."))

    # Options of the calculator
    """This loop will continue as long as the inputs are between 1 and 7."""
    for user_input in range(1, 9):
        # Options of the calculator
        print("1.Circumference of a circle", "2.Pythagorean Theorem",
              "3.Square root", "4.Quadratic formula", "5.Area",
              "6.Sum of 5 numbers", "7.Fraction to percentage",
              "8.Division between 2 numbers", sep='\n')
        # Once ran, the options are all on new lines.
        """The try except is used in case the user inputs something other than
        an integer. If so, the program will print an error, and call back to
        main. If the user inputs the number 99, the program will stop."""
        try:
            user_input = str(input("Enter a number 1 - 6. To end the "
                                   "program, type '99'."))
            if user_input == "99":
                print("Thanks for using my calculator! Have a good day!")
                break
        except ValueError:
            print("Error. Only the input of numbers is allowed here.")
        # If the user inputs the number 1, the program asks the user
        # for the radius, and then calls the circumference function.
        # It also has a try and an except in case the input is not a number,
        # reinforcing the notice that only numbers may be inputted.
        if user_input == "1":
            try:
                radius = (int(input("Enter the radius: ")))
                if radius > 0:
                    calculate_circumference(radius)
                elif radius < 0:
                    print("Error. The radius of a circle has to be positive.")
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")
        # If the user inputs the number 2, the program asks the
        # user for one of two options, to find the hypotenuse or a side
        # using the pythagorean theorem.
        elif user_input == "2":
            pythagorean_options = ["1.Find Hypotenuse", "2.Find a Side"]
            pythagorean_options = '\n'.join(pythagorean_options)
            print(pythagorean_options)
            # Again, another try except is used in case the user inputs
            # something other than an integer.
            pythagorean_input = 0
            try:
                pythagorean_input = int(input("Enter the number of your "
                                              "objective: "))
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")
            # If the user inputs 1, the program asks for the value of a and b
            # given from the user. It then calls the hypotenuse function with
            # the arguments of a and b. Another try except in case the user
            # doesn't input an integer.
            if pythagorean_input == 1:
                try:
                    a_input = int(input("Enter a side value: "))
                    b_input = int(input("Enter the other side value: "))
                    hypotenuse(a_input, b_input)
                except ValueError:
                    print("Error. Enter numbers only. The program will "
                          "restart.")
            # If the user inputs 2, the program asks for the side value
            # given and the hypotenuse.
            # It then calls the side function with the arguments of the side
            # and the hypotenuse.
            elif pythagorean_input == 2:
                try:
                    side_input = int(input("Enter the side value given: "))
                    hypo_input = int(input("Enter the value given for the "
                                           "hypotenuse: "))
                    side(side_input, hypo_input)
                except ValueError:
                    print("Error. Enter numbers only. The program will "
                          "restart.")
        # If the user inputs 3, the program asks for a number that the user
        # wants to get the square root of. It then calls the square root
        # function with the argument of the input given. Another try except
        # is used. If the square root is less than 0, the program says that
        # the square root is undefined, because it would be a negative.
        elif user_input == "3":
            try:
                sqrt_input = int(input("Enter the number you want to square "
                                       "root: "))
                if sqrt_input >= 0:
                    calculate_square_root(sqrt_input)
                elif sqrt_input < 0:
                    print("Error. This square root is undefined.")
            except ValueError:
                print("Error. Enter numbers only. The program will restart.")
        # If the user inputs 4, the program asks for the values of a, b, and c.
        # It then calls the quadratic function with the arguments of the three
        # inputs.
        # The quadratic function will give the two values of x from the
        # quadratic formula. Another try except is used.
        elif user_input == "4":
            try:
                a = float(input("Enter the value for a: "))
                b = float(input("Enter the value for b: "))
                c = float(input("Enter the value for c: "))
                quadratic(a, b, c)
            except ValueError:
                print("Error. Enter numbers only. The program will restart.")
            except ZeroDivisionError:
                print("Error. The input for a cannot be 0, because you "
                      "cannot divide by 0.")
        # If the user inputs the number 5, the program prompts
        # the user for one of three options, to see which shape the user
        # wants to find the area of. Another try except is used.

        elif user_input == "5":
            area_options = ["1. Area of triangle", "2. Area of square",
                            "3. Area of circle"]
            area_options = '\n'.join(area_options)
            print(area_options)
            area_input = 0
            try:
                area_input = int(input("Enter the number for which shape "
                                       "would you like to find the area for: ")
                                 )
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")
            # If the user inputs one, the program asks for the base and the
            # height of the triangle, and calls the triangle function with
            # the arguments of the base and height.

            try:
                if area_input == 1:
                    tri_base = int(input("Enter the base of the triangle: "))
                    tri_height = int(input("Enter the height of the "
                                           "triangle: "))
                    triangle(tri_base, tri_height)

                # If the user inputs two, the program asks for the base and the
                # height of the square, and calls the square function with the
                # arguments of the base and height.
                elif area_input == 2:
                    sq_base = int(input("Enter the base of the square: "))
                    sq_height = int(input("Enter the height of the square: "))
                    square(sq_base, sq_height)
                # If the user inputs three, the program asks for the radius
                # of a circle, and calls the circle function with the argument
                # of the radius.
                elif area_input == 3:
                    radius = int(input("Enter the radius of the circle: "))
                    circle(radius)

                else:
                    print("Please input a number associated to a shape. The "
                          "program will restart.")
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")

            """If the user inputs the number 6, the program will prompt
            the user for 5 numbers, and will output the sum of those 5 
            numbers."""
        elif user_input == "6":
            num_amount = 0
            sum_of_numbers = 0
            print("Enter 5 numbers of your choice: ")
            # The while loop continues while the amount of numbers inputted
            # is less than 5, and not greater than 5.
            while num_amount < 5 and not num_amount >= 5:
                try:
                    sum_input = int(input())
                    num_amount += 1
                    sum_of_numbers += sum_input
                except ValueError:
                    print("Error. Only the input of numbers is allowed here.")
                # When 5 numbers are inputted, the while loop stops and outputs
                # the sum.
                if num_amount == 5:
                    print("Your sum is:", sum_of_numbers)
        # If the user inputs the number 7, the program asks for the input
        # of the numerator and denominator, and then calls the percentage
        # function with the arguments of the numerator and denominator.

        elif user_input == "7":
            try:
                numerator = int(input("Enter the number for the numerator:"))
                denominator = int(input("Enter the number for the "
                                        "denominator:"))
                fraction_to_percentage(numerator, denominator)
            except ZeroDivisionError:
                print("Error. You cannot divide by 0.")
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")
        # If the user inputs the number 8, the program outputs a list of
        # three options, depending on what kind of division the user wants
        # to do.

        elif user_input == "8":
            division_options = ["1. Find the exact number",
                                "2. Find the remainder",
                                "3. Find the nearest whole number"]
            division_options = '\n'.join(division_options)
            print(division_options)
            division_input = 0
            try:
                division_input = int(input("Enter the number for which type "
                                           "of division you would like to "
                                           "do: "))
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")

            try:
                # If the user inputs 1, the program will ask for the first
                # number, and then asks for a second number. It will then
                # call the division_exact function with the arguments
                # of division_number_1  and division_number_2.
                if division_input == 1:
                    division_number_1 = int(input("Enter the first number: "))
                    division_number_2 = int(input("Enter the second number: "))
                    division_exact(division_number_1, division_number_2)
                # If the user inputs 2, the program again asks for the first
                # number, and then asks for a second number. It will then
                # call the division_remainder function with the arguments of
                # remainder_number_1 and remainder_number_2.
                elif division_input == 2:
                    remainder_number_1 = int(input("Enter the first number: "))
                    remainder_number_2 = int(input("Enter the second "
                                                   "number: "))
                    division_remainder(remainder_number_1, remainder_number_2)
                # If the user inputs 3, the program asks for the first and
                # second number, and calls the division_whole function with
                # the arguments of whole_number_1 and whole_number_2.
                elif division_input == 3:
                    whole_number_1 = int(input("Enter the first number: "))
                    whole_number_2 = int(input("Enter the second number: "))
                    division_whole(whole_number_1, whole_number_2)
            except ValueError:
                print("Error. Only the input of numbers is allowed here.")
            except ZeroDivisionError:
                print("Error. You cannot divide by 0.")
        # If the user doesn't input a number between 1-6 or 99,
        # the program lets the user know that they inputted an invalid
        # number, and to try again.

        else:
            print(input("You have entered an invalid number, press any "
                        "button to try again."))


# The circumference function defined.
def calculate_circumference(radius):
    """The circumference is pi x r^2, and because math is imported, math.pi is
    equal to pi. The format of circumference with .2f makes it so that the
    output of the circumference will have only two decimal places."""
    circumference = 2 * math.pi * radius
    print("The circumference of a circle with the radius of", radius, "is",
          format(circumference, ".2f"))


# The hypotenuse function defined, the first option of the pythagorean theorem.
def hypotenuse(a_input, b_input):
    """The pythagorean theorem is a^2 + b^2 = c^2. the math.sqrt lets us find
    out the square root of a^2 + b^2, which in turn tells the the hypotenuse.
    Again, the format .2f outputs the hypotenuse with two decimal places."""
    pythagorean_theorem = math.sqrt(a_input ** 2 + b_input ** 2)
    print("The value of the hypotenuse with the sides of", a_input, "and",
          b_input, "is", format(pythagorean_theorem, ".2f"))


# The side function defined, the second option of the
# pythagorean theorem.
def side(side_input, hypo_input):
    pythagorean_theorem = math.sqrt(hypo_input ** 2 - side_input ** 2)
    print("The value of the side with the side of", side_input, "and the "
                                                                "hypotenuse "
                                                                "of",
          hypo_input, "is", format(pythagorean_theorem,
                                   ".2f"))


# The square root function defined.
def calculate_square_root(sqrt_input):
    """math.sqrt gives the square root of the input. the format .2f outputs it
    with only two decimal places."""
    square_root = math.sqrt(sqrt_input)
    print("The square root of the value", sqrt_input, "is", format(
        square_root, ".2f"))


# The quadratic function defined.
def quadratic(a, b, c):
    """The discriminant is part of the quadratic formula, and the program
    checks if the discriminant is greater than 0 or equal to 0, and then
    plugs it back into the quadratic formula, and outputs the two x values
    with two decimal places. If the discriminant is less than 0 or does not
    equal 0, the program prints that the discriminant is undefined, because
    the  square root of a negative number is undefined."""
    discriminant = (b ** 2.0 - 4.0 * a * c)
    if discriminant > 0 or discriminant == 0:
        sqrt_discriminant = math.sqrt(discriminant)
        quadratic_formula1 = ((-b + sqrt_discriminant) / (2.0 * a))
        quadratic_formula2 = ((-b - sqrt_discriminant) / (2.0 * a))
        print("From the input of", a, b, "and", c, "the x "
                                                   "values are: ",
              format(quadratic_formula1, ".2f"), format(
                quadratic_formula2, ".2f"))

    elif (discriminant < 0) or discriminant != 0:
        print("The discriminant is undefined.")


# The triangle function defined.
def triangle(tri_base, tri_height):
    """Area of a triangle is b x h divided by 2. .2f outputs it with only two
    decimal places."""
    tri_area = tri_base * tri_height / 2.0
    print("The area of a triangle with a base of", tri_base, "and a height "
                                                             "of", tri_height,
          "is", format(tri_area, ".2f"))


# The square function defined.
def square(sq_base, sq_height):
    """Area of a square is b x h. The .2f outputs the area with only two
    decimal places."""
    sq_area = sq_base * sq_height
    print("The area of a square with a base of", sq_base, "and a height of",
          sq_height, "is", format(sq_area, ".2f"))


# The circle function defined.
def circle(radius):
    """The area of a circle is pi x r^2. The .2f outputs the area of the circle
    with only two decimal places."""
    cir_area = math.pi * radius ** 2.0
    print("The area of a circle with a radius of", radius, "is", format(
        cir_area, ".2f"))


# The Percentage function defined.
def fraction_to_percentage(numerator, denominator):
    """To find the percentage of a fraction, you divide the numerator by
    the denominator and multiply it by 100, and add a % sign. The sep
    function adds a colon and a space, and the end function adds a % sign,
    while separating the looped options list from the same line as the
    percentage."""
    percentage = numerator / denominator * 100
    print("The percentage of the fraction given is", percentage, sep=": ",
          end="%\n")




# The exact number given from division function defined.
def division_exact(division_number_1, division_number_2):
    """To get the entire number from dividing two numbers, the program
    divides the first number by the second number, and prints that number
    without any formatting."""
    division = division_number_1 / division_number_2
    print("The exact number given from the division of", division_number_1,
          "and", division_number_2, "is", division)


# The division with remainder function defined.
def division_remainder(remainder_number_1, remainder_number_2):
    """To get the remainder from the division of two numbers, the program
    uses the module operator, which outputs the remainder of the two
    numbers that are divided."""
    remainder = (remainder_number_1 % remainder_number_2)
    print("The remainder given from the division of", remainder_number_1,
          "and", remainder_number_2, "is", remainder)


# The whole number division function defined.
def division_whole(whole_number_1, whole_number_2):
    """In order to get the nearest whole number from the division of two
    numbers, the program uses the floor division operated."""
    whole_number_division = whole_number_1 // whole_number_2
    print("The whole number given from the division of", whole_number_1, "and",
          whole_number_2, "is", whole_number_division)


"""The starting point of the program, outputs a menu of choices. Calls 
back to main."""
main()
