#read file to count number of error, warning and info messages
def count_messages(file_path):
    error =  warning = info = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    error += 1
                elif "WARNING" in line:
                    warning += 1
                elif "INFO" in line:
                    info += 1
        return error, warning, info
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None, None

counts = count_messages("C:\\repos\\AI_Assisted_DevOps\\system_logs1.txt")
print(f"Errors: {counts[0]}, Warnings: {counts[1]}, Info: {counts[2]}")