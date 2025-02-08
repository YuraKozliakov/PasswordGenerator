def validate_complexity(complexity):
    valid_complexities = ['simple', 'medium', 'high']
    if complexity not in valid_complexities:
        raise ValueError("Invalid complexity level. Choose from 'simple', 'medium', or 'high'.")
