import math
from scipy.special import gammainc


class NISTTests:
    def __init__(self, bit_seq: str):
        """
        Class initialisation
        """
        if not all(bit in "01" for bit in bit_seq):
            raise ValueError("Binary sequence must contains only 0 and 1.")
        self.bit_seq = bit_seq


    def frequency_bit_test(self) -> float:
        """
        Frequency bit test
        :return: P_value
        """
        count_0 = self.bit_seq.count("0")
        count_1 = self.bit_seq.count("1")
        S_n = abs(count_1 - count_0) / math.sqrt(len(self.bit_seq))
        return math.erfc(S_n / math.sqrt(2))
    

    def run_same_bits_test(self) -> float:
        """
        Test on same runs bits
        :return: P_value
        """
        n = len(self.bit_seq)
        if n == 0:
            raise ValueError("Binary sequense should not be empty.")

        zeta = self.bit_seq.count("1") / n
        if abs(zeta - 0.5) >= 2 / math.sqrt(n):
            return 0
        
        V_n = sum(self.bit_seq[i] != self.bit_seq[i + 1]
                  for i in range(n - 1))

        return math.erfc(abs(V_n - 2 * n * zeta * (1 - zeta)) / 
                            (2 * math.sqrt(2 * n) * zeta * (1 - zeta)))


    def count_sequences_in_block(self, block: str) -> int:
        """
        Count max sequence of 1 in block
        :param block: Block of binary sequence
        :return: Max length of 1 in block
        """
        max_len = current_len = 0
        for bit in block:
            if bit not in {"0", "1"}:
                raise ValueError(f"Block contains invalid symbols: '{bit}'")
            current_len = current_len + 1 if bit == "1" else 0
            max_len = max(max_len, current_len)
        return max_len
    

    def classify_sequence(self, seq_len: int) -> int:
        """
        Classify sequences by their lengths
        :param seq_len: Length of sequence
        :return: Index of category(0, 1, 2, 3)
        """
        match seq_len:
                case _ if seq_len <= 1:
                    return 0
                case 2:
                    return 1
                case 3:
                    return 2
                case _:
                    return 3
            

    def block_process(self, probabilities: list, size: int = 8) -> tuple[int]:
        """
        Processing blocks of binary sequences and classify they
        "param probabilities: Probability for every category
        :param size: Size of every block
        :return: Tuple of blocks in every category
        """
        v_i = [0] * 4
        for start_index in range(0, len(self.bit_seq), size):
            block = self.bit_seq[start_index:start_index + size]
            max_len = self.count_sequences_in_block(block)
            category = self.classify_sequence(max_len)
            v_i[category] += 1
        return tuple(v_i)


    def calculate_hi_square(self, observed_counts: tuple, expected_probs: list) -> list:
        """
        Calculate Hi_square between observed and waited values
        :param observed_counts: Tuple with blocks of every category
        :param: expected_probs: Probability of every category
        :return: Hi_square 
        """
        hi_square = sum(((observed_counts[i] - 16 * expected_probs[i]) ** 2) / 
                        16 * expected_probs[i] for i in range(len(observed_counts))) 
        return hi_square

    def longest_ones_seq_test(self, probabilities: list[float]) -> float:
        """
        Longest ones sequence test
        :param probabilities: Probability for every category
        :return: P_value for hi_square
        """
        v_i = self.block_process(probabilities)
        hi_square = self.calculate_hi_square(v_i, probabilities)
        return gammainc(3 / 2, hi_square / 2)
    