

# Creating a list of filenames
input_files = [
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/common_end.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/first_last6.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/has23.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/make_ends.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/make_pi.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/max_end3.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/middle_way.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/reverse3.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/rotate_left3.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/same_first_last.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/sum2.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-1/sum3.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-2/big_diff.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-2/centered_average.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-2/count_evens.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-2/has22.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-2/sum13.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/List-2/sum67.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/alarm_clock.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/caught_speeding.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/cigar_party.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/date_fashion.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/in1to10.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/love6.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/near10.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/sorta_sum.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Logic-1/squirrel_play.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/diff21.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/front_3.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/front_back.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/makes10.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/missing_char.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/monkey_trouble.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/near_hundred.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/not_string.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/parrot_trouble.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/pos_neg.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/sleep_in.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-1/sum_double.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/array_count9.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/array_front9.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/array123.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/front_times.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/last2.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/string_bits.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/string_match.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/string_times.py",
"/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/Warmup-2/stringsplosion.py"

]
 # Define the names of the input files and the output file
output_file = '/Users/yiyixu/Documents/First Year/Intro to Computer Programming/CodingBat batch 1/codingbat1.py'

# Open the output file in "append" mode
with open(output_file, "a") as combined_file:
    for input_file in input_files:
        with open(input_file, "r") as file_to_append:
            file_contents = file_to_append.read()
            combined_file.write(file_contents)
            combined_file.write("\n")  # Add a newline to separate the contents of different files
            combined_file.write("\n")  # Add a newline to separate the contents of different files
