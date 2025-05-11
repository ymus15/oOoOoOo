import re
import sys
import os

def compile_oOoOoOo_to_python(input_file):
    if not input_file.endswith(".oOoOoOo"):
        print("❌ Error!")
        return

    with open(input_file, 'r') as f:
        code = f.read()

    # Sprawdzenie końcówki pliku (10 pustych linii)
    if not code.endswith('\n' * 10):
        print("❌ Error!")
        return

    # Dopasowanie składni tworzenia zmiennej
    var_match = re.search(r"~'o (\w) :\+=\+> \{\>\[\^\(.../\"(.+)\"\\\.\.\.\)\^\]\<\}", code)
    if not var_match:
        print("❌ Error!")
        return

    var_name = var_match.group(1)
    var_value = var_match.group(2)

    # Dopasowanie składni wypisania zmiennej
    print_match = re.search(r"~~'oa :\+=\+> ;;;\+=-\{" + re.escape(var_name) + r"\}-=\+;;;", code)
    if not print_match:
        print(f"❌ Error!")
        return

    # Generowanie kodu Python
    python_code = f"{var_name} = '{var_value}'\n"
    python_code += f"oa = {var_name}\n"
    python_code += "print(oa)\n"

    with open('output.py', 'w') as f:
        f.write(python_code)

    print("✅ Compiled")

# Obsługa z terminala
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python compiler.py <file.oOoOoOo>")
    else:
        compile_oOoOoOo_to_python(sys.argv[1])
