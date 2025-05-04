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


    def longest_ones_seq_test(self, PI_I: list[float]) -> float:
        """
        Longest ones sequence test
        :param bit_seq: Binary sequence
        :param PI_I: List of probabilities
        :return: P_value for hi_square
        """
        M = 8
        v_i = [0] * 4
        
        for i in range(0, len(self.bit_seq), M):
            block = self.bit_seq[i:i + M]
            max_len = current_len = 0

            for bit in block:
                if bit not in {"0", "1"}:
                    raise ValueError(f"Block contains invalid symbols: '{bit}'")
                match bit:
                    case "1":
                        current_len += 1
                    case "0":
                        current_len = 0
                max_len = max(max_len, current_len)
            
            match max_len:
                case _ if max_len <= 1:
                    v_i[0] += 1
                case 2:
                    v_i[1] += 1
                case 3:
                    v_i[2] += 1
                case _:
                    v_i[3] += 1
        
        hi_square = 0.0
        for i in range(len(v_i)):
            hi_square += ((v_i[i] - 16 * PI_I[i]) ** 2) / (16 * PI_I[i])
        return gammainc(1.5, hi_square / 2)