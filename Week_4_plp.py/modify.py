def modify_file(input_file, output_file):
    try:
        # Read from the input file
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        # Modify the content (e.g., convert to lowercase)
        modified_content = content.lower()

        # Write to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
modify_file('input.txt', 'output.txt')
