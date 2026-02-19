#!/bin/bash
# rename_author.sh
# Unify all author attributions to Hiroshi Honma
# Target files: .md, .tex, .py, .txt

echo "Starting author name unification..."

# Define targets
TARGETS=("Mathieu" "Claude" "Gemini" "Grok" "ChatGPT")
AUTHOR="Hiroshi Honma"

for target in "${TARGETS[@]}"; do
    echo "Replacing $target with $AUTHOR..."
    # Linux/macOS compatible sed inplace replacement
    find . -type f \( -name "*.md" -o -name "*.tex" -o -name "*.py" -o -name "*.txt" \) -exec sed -i.bak "s/$target/$AUTHOR/g" {} +
done

# Clean up backup files created by sed
find . -type f -name "*.bak" -delete

echo "Author unification complete."
echo "Note: Please manually verify the Acknowledgements section to ensure AI contributors retain proper credit."
