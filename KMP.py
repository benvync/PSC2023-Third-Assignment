def compute_failure_array(s):
    n = len(s)
    failure = [0] * n
    j = 0

    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = failure[j - 1]

        if s[i] == s[j]:
            j += 1

        failure[i] = j

    return failure

def read_fasta_file(file_path):
    sequence = ''
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence
fasta_file_path = 'KMP_FASTA.txt'

DNA_sequence = read_fasta_file(fasta_file_path)

Sfailure_array = compute_failure_array(DNA_sequence)

print(Sfailure_array)
