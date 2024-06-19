import sys

X = 10  # Length for overlap comparison

def main():
    filenames = input("Enter filenames separated by spaces (e.g., file1.txt file2.txt):\n").split()

    for filename in filenames:
        sequences = read_file(filename)

        if sequences is not None:
            check_sequence = sequences.pop(0)
            check_sequence, sequences = build_algorithm(check_sequence, sequences, 0)
            check_sequence, sequences = build_algorithm(check_sequence, sequences, 1)
            
            output_filename = f'{filename}_output.txt'
            leftovers_filename = f'{filename}_leftovers.txt'

            with open(output_filename, 'w') as file_check_sequence:
                file_check_sequence.write(check_sequence)
            
            with open(leftovers_filename, 'w') as file_check_list:
                for val in sequences:
                    file_check_list.write(val + "\n")
            
            print(f"Processed {filename}. Results saved to {output_filename} and {leftovers_filename}.")
        else:
            print(f"Skipping file {filename} due to read error.")
    
    sys.exit(0)

def build_algorithm(check_sequence, sequences, flag):
    key_sequence = check_sequence[:X] if flag == 0 else check_sequence[-X:]
    reverse_key = key_sequence[::-1]

    idx = 0

    while idx < len(sequences):
        val = sequences[idx]
        i = X - 1

        while i < len(val):
            if val[i] == reverse_key[0] and compare_two_sequences(val, reverse_key, i):
                if compare_overlap(check_sequence, val, i, flag):
                    check_sequence = overlap_sequences(check_sequence, val, i, flag)
                    key_sequence = check_sequence[:X] if flag == 0 else check_sequence[-X:]
                    reverse_key = key_sequence[::-1]
                    sequences.pop(idx)
                    idx = 0
                    break
            i += 1
        else:
            idx += 1
    return check_sequence, sequences

def compare_two_sequences(val, reverse_key, i):
    return all(val[i - idx] == reverse_key[idx] for idx in range(len(reverse_key)))

def compare_overlap(check_sequence, val_sequence, i, flag):
    if flag == 0:
        return all(val_sequence[j] == check_sequence[X - 1 + j - i] for j in range(i, len(val_sequence)))
    else:
        return all(val_sequence[j] == check_sequence[len(check_sequence) - 1 - (i - j)] for j in range(i, -1, -1))

def overlap_sequences(check_sequence, val, i, flag):
    if flag == 0:
        return val[:i - X + 1] + check_sequence
    else:
        return check_sequence + val[i + 1:]

def read_file(filename):
    try:
        with open(filename, "r") as in_file:
            print(f"File {filename} opened successfully\n")
            sequences = []
            sequence_block = ""

            for line in in_file:
                if line.startswith(">"):
                    if sequence_block:
                        sequences.append(sequence_block)
                        sequence_block = ""
                else:
                    sequence_block += line.strip()

            if sequence_block:
                sequences.append(sequence_block)

        return sequences
    except IOError:
        print(f"Cannot open file {filename}! See example.txt\n")
        return None

if __name__ == "__main__":
    main()
