import sys
import os
import math

def transform_data(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    output_lines = []
    
    # Append header as it is
    output_lines.append(lines[0].strip())
    
    # Process each data line
    for line in lines[1:]:
        values = line.strip().split(',')
        Ti = values[0]
        A_X = float(values[1]) / 2048 * 9.8
        A_Y = float(values[2]) / 2048 * 9.8
        A_Z = float(values[3]) / 2048 * 9.8
        R_X = float(values[4]) / 16.4
        R_Y = float(values[5]) / 16.4
        R_Z = float(values[6]) / 16.4

        # Calculate ACC_SUM
        ACC_SUM = math.sqrt(A_X**2 + A_Y**2 + A_Z**2)
        
        transformed_line = f"{Ti};{A_X};{A_Y};{A_Z};{R_X};{R_Y};{R_Z};{ACC_SUM}"
        output_lines.append(transformed_line)
    
    # Create the output file name
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}_transform.csv"
    
    # Write the transformed data to the new file
    with open(output_file, 'w') as file:
        for line in output_lines:
            file.write(line + '\n')
    
    print(f"Transformed data has been written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transform_data.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    transform_data(input_file)
