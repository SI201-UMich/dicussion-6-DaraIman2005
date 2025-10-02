def build_data_dict(self):
    """
    Read the CSV into column lists inside self.data_dict.
    Assumes the first line is a header.
    """
    # process rows after the header
    for line in self.raw_data[1:]:
        if not line.strip():
            continue
        parts = [p.strip() for p in line.rstrip("\n").split(",")]
        if len(parts) < 6:
            continue  # skip malformed rows

        # Columns: month, date, sample, sample type, Harris result, Trump result
        self.data_dict['month'].append(parts[0])
        self.data_dict['date'].append(int(parts[1]))
        self.data_dict['sample'].append(int(parts[2]))
        self.data_dict['sample type'].append(parts[3])

        def parse_pct(x):
            # Accept "0.573", "57.3", or "57.3%"
            x = x.strip()
            if x.endswith("%"):
                val = float(x[:-1]) / 100.0
            else:
                val = float(x)
                if val > 1.0:  # looks like a whole percent (e.g., 57.3)
                    val = val / 100.0
            return val

        self.data_dict['Harris result'].append(parse_pct(parts[4]))
        self.data_dict['Trump result'].append(parse_pct(parts[5]))
