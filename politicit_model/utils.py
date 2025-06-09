def print_prediction(outputs):
    gender_probabilities, binary_political_probabilities, multiclass_political_probabilities = outputs

    gender = ["Male", "Female"]
    gender_prob = gender_probabilities[0].item()
    print(f"Gender:")
    print(f"  - {gender[0]}: {gender_prob * 100:.2f}%     [{'=' * int(gender_prob * 10):<10}]")
    print(f"  - {gender[1]}: {(1 - gender_prob) * 100:.2f}%   [{'=' * int((1 - gender_prob) * 10):<10}]")

    binary_political = ["Left", "Right"]
    left_prob = binary_political_probabilities[0].item()
    print(f"\nPolitical ideology (binary):")
    print(f"  - {binary_political[0]}: {left_prob * 100:.2f}%     [{'=' * int(left_prob * 10):<10}]")
    print(f"  - {binary_political[1]}: {(1 - left_prob) * 100:.2f}%   [{'=' * int((1 - left_prob) * 10):<10}]")

    multiclass_political = ["Left", "Right", "Moderate left", "Moderate right"]
    print(f"\nPolitical ideology (multiclass):")

    prob = multiclass_political_probabilities[0][0]
    print(f"  - 'Left': {prob * 100:.2f}%             [{'=' * int(prob * 10):<10}]")

    prob = multiclass_political_probabilities[0][1]
    print(f"  - 'Right': {prob * 100:.2f}%            [{'=' * int(prob * 10):<10}]")

    prob = multiclass_political_probabilities[0][2]
    print(f"  - 'Moderate left': {prob * 100:.2f}%   [{'=' * int(prob * 10):<10}]")

    prob = multiclass_political_probabilities[0][3]
    print(f"  - 'Moderate right': {prob * 100:.2f}%   [{'=' * int(prob * 10):<10}]")