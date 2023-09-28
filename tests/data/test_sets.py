import pandas as pd
from my_krml_24625129.data.sets import explore_dataframe

def test_explore_dataframe():
    # Rest of your test code...
    # Create a sample DataFrame for testing
    data = {'A': [1, 2, 3, 4, 5],
            'B': ['foo', 'bar', 'baz', 'qux', 'quux']}
    df = pd.DataFrame(data)

    # Call the function and capture the printed output
    import io
    from contextlib import redirect_stdout

    output = io.StringIO()
    with redirect_stdout(output):
        explore_dataframe(df)

    # Check if the output contains the expected information
    output_str = output.getvalue()
    assert "First 5 rows:" in output_str
    assert "Last 5 rows:" in output_str
    assert "Shape of DataFrame:" in output_str
    assert "Column Names:" in output_str
    assert "DataFrame Info:" in output_str

    # Assuming there are no missing values in the sample DataFrame, check for this line
    assert "Missing Value Counts:" not in output_str

    # Clean up
    output.close()
