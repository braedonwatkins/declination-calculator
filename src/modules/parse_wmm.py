import numpy as np


def parse_wmm(file_path: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Read and parse the values from WMM.COF file

    Parameters:
        file_path (string): Absolute path to file

    Returns:
        (g, h, g_dot, h_dot) (tuple(2D numpy array)): coefficients parsed from the file
    """

    # Max degree is 12 so initialize arrays as 13x13
    g_arr = np.zeros((13, 13))
    h_arr = np.zeros((13, 13))
    g_dot_arr = np.zeros((13, 13))
    h_dot_arr = np.zeros((13, 13))

    end_marker = "999999999999999999999999999999999999999999999999"

    # TODO: try except pattern for missing / corrupted file
    with open(file_path, "r") as f:
        # TODO: more gracefully handle the first line
        next(f)

        for line in f:
            if line.startswith("#") or not line.strip():
                continue

            values = line.strip().split()

            # TODO: this is a funny way to mark EOF but we can think of something more clever later
            if values[0] == end_marker:
                print("File parsed successfully")
                break

            # TODO: some validation here is nice, but considering this comes from a relatively small file it wouldn't likely be a problem
            # Instead, I think it would make more sense to just validate the model after a few test calculations after reading
            # since that's a more likely point of failure idk

            n = int(values[0])
            m = int(values[1])
            g = float(values[2])
            h = float(values[3])
            g_dot = float(values[4])
            h_dot = float(values[5])

            g_arr[n, m] = g
            g_dot_arr[n, m] = g_dot
            h_arr[n, m] = h
            h_dot_arr[n, m] = h_dot

    return g_arr, h_arr, g_dot_arr, h_dot_arr
